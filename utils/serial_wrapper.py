#serialWrapper.py
#
#contains the SerialWrapper which handles serial communication
import serial
import serial.tools.list_ports
import sys
from datetime import datetime
import os
import time
from threading import Thread
from collections import defaultdict

from utils.definitions import *
from utils.data_handling import TimeSeries, RelativeTime, write_data_db, Decoder

#Class to read and backup serial communication
#
#read_int(x) -    read x bytes as an integer, little endian
#read_bytes(x) -   read x bytes as a bytes
#init_device() -    tries to initialize the current port
#get_safe_devices() finds devices that are safe to communicate with
#open_serial() -    tests and opens all ports to find a device. returns -1 if it failed
class SerialWrapper:
    def __init__(self, device, **kwargs):
        self.ser = serial.Serial(timeout = 0.2)
        self.device = device
        self.initialized = False

        #get file name
        now = datetime.now()
        time = now.strftime("%Y-%m-%d-%H-%M-%S")
        file_name = device + "-" + time
        #create file and directory
        try:
            dir_name = "data/" 
            os.mkdir(dir_name)
        except:
            pass
        try:
            self.backup = open(dir_name + file_name, "w+b")
        except:
            print("could not create the file: " + dir_name + file_name)
            sys.exit()

    #basically a copy of pyserials write function
    def write(self, bytes, *args):
        self.backup.write(bytes)
        self.ser.write(bytes, *args)

    #read x amount of bytes as bytes
    def read_bytes(self, amount):
        val = self.ser.read(amount)
        self.backup.write(val)
        return val
        
    #read x bytes as an integer, little endian
    def read_int(self, amount):
        bytes = self.read_bytes(amount)
        if bytes == b"":
            return None
        total = 0
        count = 0
        for v in bytes:
            total += v << (count * 8)
            count += 1
        return total
    
    #tries to initialize a device
    #user self.ser to read and write since it does not need to be saved
    def init_device(self):
        if self.device == "RFD":
            # RFD needs 1 seconds of inactivity to eneter AT mode
            time.sleep(1) 
            self.ser.write(b'+++') #init AT mode
            time.sleep(1) #wait for data 
            buff = self.ser.read_all()
            if b'ok' in buff:
                return 1
            else:
                return 0

        elif self.device == "gateway":
            bonjour = b"LAUNCHPADCONTROLLER" 
            self.ser.write(b'&gB0')
            time.sleep(1)
            buff = self.ser.read_all()
            if bonjour in buff:
                return 1
            else:
                return 0

        elif self.device == "telecommand":
            bonjour = b"LORALINK" 
            self.ser.write(b'&gB0')
            time.sleep(1)
            buff = self.ser.read_all()
            if bonjour in buff:
                return 1
            else:
                return 0

    #finds devices that are safe to communicate with
    def get_safe_devices(self):
        safeStrings = [
            "usb",
            "arduino",
            "ch340"
        ]
        safe_devices = []

        devices = serial.tools.list_ports.comports()

        for d in devices:
            flag = False
            for substring in safeStrings:
                if substring in d.description.lower():
                    flag = True
            if flag:
                safe_devices.append(d)

        return safe_devices
    
    #if the the gateway has been initialized
    def port_is_open(self):
        return self.initialized

    #returns -1 if it fails
    def open_serial(self):
        if self.initialized:
            return 1

        baudrates ={
            "gateway": 115200,
            "RFD": 115200,
            "telecommand": 115200
        }
        self.ser.baudrate = baudrates[self.device]

        ports = self.get_safe_devices()
        for v in ports:
            self.ser.port = v.device
            self.ser.open()
            print(self.device + ": Testing " + str(v))
            if self.init_device():
                self.initialized = True
                print(self.device + ": Succesfully connected")
                return 0
            print(self.device + ": Did not respond")
            self.ser.close()
        else:
            print(self.device + ": opening serial failed")
            return -1
        
    def open_file(self, path):
        self.ser = open(path, "rb")
        self.initialized = True
        return True
    
    #timestamp the backupfile
    #time is in seconds
    #it is then stored in milliseconds
    def timestamp(self, time):
        millis = int(time * 1000)
        msg = []
        msg += SEPARATOR
        msg += [ID_TIMESTAMP]
        buf = [0 for x in range(4)]
        buf[0] = millis & 255
        buf[1] = (millis >> 8)  & 255
        buf[2] = (millis >> 16) & 255
        buf[3] = (millis >> 24) & 255
        msg += buf
        self.backup.write(bytes(msg))


###
#spawns a thread that reads from serial 
#it detects headers defined in definiiotns.py and uses decoders to parse the data
##
#clocks - contains the clock class to keep track of the current time 
#data - contains all the data like data[*source*][*measurement*]
#
#stop() - stops the thread completely
#start() - opens and starts reading serial
#pause() - stops the thread from reading
#resume() - resumes the thread
#state() - if the link is open
class SerialReader():
    def __init__(self, device, decoders, **kwargs):
        self.read = True
        self.exit = False
        self.ser = SerialWrapper(device, **kwargs)
        self.device = device
        self.decoders = decoders
        self.decoders[ID_TIMESTAMP] = [Decoder("flight", "<I", "timestamp")]
        self.client = False
        if "influx" in kwargs: 
            self.client = kwargs["influx"]

        #use defaultdict to let the front-end use uninitialized data
        self.data = defaultdict(lambda: defaultdict(TimeSeries))
        self.clocks = defaultdict(RelativeTime)

        t = Thread(target = reader_thread, args = (self,))
        t.start()

    #stops the thread
    def stop(self):
        self.exit = True

    #if the gateway is currently reading
    def state(self):
        return self.ser.port_is_open()
    
    #pause the thread
    def pause(self):
        self.read = False
    
    def resume(self):
        self.read = True

    #start and open serial
    def open_serial(self):
        return self.ser.open_serial()
    
    def open_file(self, path):
        return self.ser.open_file(path)

def reader_thread(sr):
    ser = sr.ser
    #wait for user to start serial
    while not sr.state():
        time.sleep(0.1)
        if sr.exit:
            return

    frameId = 0 #define before the loop so it remains in scope
    while not sr.exit:
        if not sr.read:
            time.sleep(0.1)
            continue
        
        #test for frame separator, read one byte at a time so it aligns itself
        separator = ser.read_int(1)
        if separator == None:
            continue
        if separator != SEPARATOR[0] or ser.read_int(1) != SEPARATOR[1]:
            print(sr.device + ": Invalid Separator")
            continue

        frame_id_old = frameId
        frame_id = ser.read_int(1)

        if frame_id not in sr.decoders.keys():
            print(sr.device + ": Invalid ID: " + str(frame_id))
            print(sr.device + ": last valid ID: " + str(frame_id_old))
            continue
 
        decoder = sr.decoders[frame_id]
        data = []
        for v in decoder:
            data += v.decode(ser)

        source = data[0].source
        if data[0].measurement == "ms_since_boot":
            sr.clocks[source].update_time(data[0].value / 1000) # convert to seconds   
        elif data[0].measurement == "timestamp":
            sr.clocks[source].update_time(data[0].value / 1000)
            time.sleep(0.010)
        else:
            #write data to database
            if sr.client:
                write_data_db(data, sr.client)
            #push data to local dict
            for v in data:
                series = sr.data[v.source][v.measurement]
                series.x.append(sr.clocks[source].get_current_time())
                series.y.append(v.value)
