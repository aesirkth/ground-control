#serialWrapper.py
#
#contains the SerialWrapper which handles serial communication

import serial
import serial.tools.list_ports
import sys
from datetime import datetime
import os

class SerialWrapper:
    def __init__(self):
        self.ser = serial.Serial(timeout = 2)
        self.write = self.ser.write #copy pyserial's write function
        self.initialized = False
        #get file name
        now = datetime.now()
        time = now.strftime("%Y-%m-%d-%H:%M:%S")
        file_name = "tel-" + time
        #create file and directory
        try:
            dir_name = "telemetry_data/" 
            os.mkdir(dir_name)
        except:
            pass
        try:
            self.backup = open(dir_name + file_name, "w")
        except:
            print("could not create the file: " + dir_name + file_name)
            sys.exit()

    #read x bytes as an integer, little endian
    def read_bytes(self, amount):
        bytes = self.ser.read(amount)
        self.backup.write(str(bytes))
        total = 0
        count = 0
        for v in bytes:
            total += v << (count * 8)
            count += 1
        return total

    #read x amount of bytes as a string
    def read_string(self, amount):
        val = str(self.ser.read(amount))
        return val
    
    #tries to initialize a device
    def init_device(self, ser, device):
        if device == "dummy":
            self.ser.write(b'aaa')
            if (ser.read(3) == b'bbb'):
                print("yay")
                return 1
            print("nay")
            return 0
        elif device == "gateway":
            pass #todo

    #tries to find and initialize the correct port
    def open_serial(self, device):
        baudrates = {
            "gateway": 11520, #unsure about this one 
            "dummy": 11520 
        }
        ser = self.ser
        ser.baudrate = baudrates[device]
        ports = self.get_safe_devices()
        for v in ports:
            ser.port = v.device
            ser.open()
            print("Testing" + str(v))
            if self.init_device(ser, device):
                self.initialized = True
                print("Succesfully connected")
                return 0
            ser.close()
        else:
            return 1

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

class GatewayWrapper(SerialWrapper):
    def __init__(self, database):
        super().__init__()
        self.database = database

    #sends the start, target and id byte to the gateway
    #or start, target, separator, id to the launchpad controller
    #target = "c" for controller
    #target = "g" for gateway
    def send_header(self, target, id):
        if not self.initialized:
            return -1

        if target == "c":
            self.write(target)
            self.write(separator)
            self.write(id)
        elif target == "g":
            self.write(target)
            self.write(id)

    def wait_for_data():
        pass

    def time_sync(self,):
        if not self.initialized:
            return -1

    def set_power_mode(self, TBD):
        if not self.initialized:
            return -1

    def set_radio_emitters(self, fpv, tm):
        if not self.initialized:
            return -1

    def set_parachute(self, armed, enable_1, enable_2):
        if not self.initialized:
            return -1