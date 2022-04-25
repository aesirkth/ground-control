import serial 
import serial.tools.list_ports
from datetime import datetime
import os
import sys
import time
from threading import Thread
from collections import defaultdict
import json
import utils.fc as protocol
import utils.EDDA as edda
from utils.definitions import *
from utils.data_handling import (TimeSeries, write_data_db, get_current_time,
    formatted_time_to_sec, get_current_time_sec, NumDecoder, EnumDecoder,
    BitDecoder, EmptyDecoder)
from enum import Enum

LIVE = 0
BACKUP_TIMESTAMP = 1
FLASH_TIMESTAMP = 2

####
#a wrapper around the Serial class. It backups all communication to the ./data/ 
#directory. It can also find and open a connection to a device 
###
#init(device)
#   device can be, "gateway", "flight_controller", "RFD", "telecommand"
#
#write(*args) - copy of pyserial's write
#read(*args) - copy of pyserial's read
#open_serial() - open the serial connection
class SerialWrapper():
    def __init__(self, device):
        self.ser = serial.Serial(timeout=1)
        self.device = device
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

    #copy of the pyserial write with added backup
    def write(self, *args):
        self.backup.write(*args)
        self.ser.write(*args)

    #copy of the pyserial read with added backup
    def read(self, *args):
        buf = self.ser.read(*args)
        self.backup.write(buf)
        return buf

    #gets a list with all ports
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

    #returns true or false if a port contatins a device
    def init_device(self):
        if self.device == "RFD":
            # RFD needs 1 seconds of inactivity to eneter AT mode
            time.sleep(1) 
            self.ser.write(b'+++') # enter AT mode
            time.sleep(1) # wait for data 
            buff = self.ser.read_all()
            self.write(b'ATO\r') # exit AT mode
            return b'OK' in buff
        elif self.device == "gateway":
            bonjour = b"LAUNCHPADCONTROLLER" 
            self.ser.write(b'&gB0')
            time.sleep(1)
            buff = self.ser.read_all()
            return bonjour in buff
        elif self.device == "flight_controller":
            msg = protocol.handshake_from_ground_station_to_flight_controller()
            reply = protocol.return_handshake_from_flight_controller_to_ground_station()
            handshake = bytes(SEPARATOR + [msg.get_id()] + [0]) 
            response = bytes(SEPARATOR + [reply.get_id()] + [0])
            self.ser.read_all()
            self.ser.write(handshake)
            time.sleep(0.5)
            buff = self.ser.read_all()
            return response in buff
        elif self.device == "telecommand":
            msg = protocol.handshake_from_ground_station_to_flight_controller()
            reply = protocol.return_handshake_from_flight_controller_to_ground_station()
            handshake = bytes(SEPARATOR + [msg.get_id()] + [0]) 
            response = bytes(SEPARATOR + [reply.get_id()] + [0])
            self.ser.read_all()
            self.ser.write(handshake)
            time.sleep(0.5)
            buff = self.ser.read_all()
            return response in buff
        else:
            return False
    
    #timestamp the backupfile
    def timestamp(self, time):
        time = int(time)
        msg = protocol.local_timestamp_from_local_to_local()
        msg.set_timestamp(time)
        buf = []
        buf += SEPARATOR
        buf += [msg.get_id()]
        buf += msg.build_buf()
        self.backup.write(bytes(buf))

    #start and open serial
    def open_serial(self):
        baudrates ={
            "gateway": 115200,
            "RFD": 57600,
            "flight_controller": 115200,
            "telecommand": 115200
        }
        self.ser.baudrate = baudrates[self.device]

        ports = self.get_safe_devices()
        for v in ports:
            self.ser.port = v.device
            self.ser.open()
            print(self.device + ": Testing " + str(v))
            if self.init_device():
                print(self.device + ": Succesfully connected")
                return True
            print(self.device + ": Did not respond")
            self.ser.close()
        else:
            print(self.device + ": opening serial failed")
            return False    

#####
#spawns a thread that reads and parses data from a stream.
###
#init(self, *args, influx = False, device = "None")
#   influx is the influx client to write to
#   device is the SerialWrapper device
#
#stop() - stops the reading thread
#pause() - pauses the reader thread
#resume() - resumes the reader thread
#redirect_data() - overwrite the data array to e.g. combine the output from two readers
#serial_is_active() - if the serial connection is open
#serial_is_active() - if a readable connection is open
#open_backup_file(path) - open a file created by this very program
#open_flash_file(path) - open a file dumped from the flash drive
#open_serial() - open a serial connection
#seconds_since_last_message() - get the time since the last message
class SerialReader():
    def __init__(self, *args, influx = False, device = "None"):
        self.influx = influx
        self.device = device
        #stream is for reading
        #serial is for writing
        self.serial_is_active = False
        self.stream_is_active = False
        self.ser = None
        self.stream = None
        self.client = False
        self.last_message_time = time.time()
        self.last_timestamp = 0
        self.time_sync_state = 0
        self.start_time = None
        self.pause = False
        self.exit = False
        self.decoders = {}
        #use defaultdict to let the front-end use uninitialized data
        self.data = defaultdict(lambda: defaultdict(lambda: defaultdict(TimeSeries)))

        t = Thread(target = self.reader_thread)
        t.start()

    #stops the thread
    def stop(self):
        self.exit = True

    #if the serial port is open
    def is_serial_open(self):
        return self.serial_is_active
    
    #if the is reading either from file or serial
    def is_stream_open(self):
        return self.stream_is_active

    #pause the reader thread
    def pause(self):
        self.paused = True
    
    #resume the reader thread
    def resume(self):
        self.paused = False    

    #tell the class to write into another data dict
    def redirect_data(self, data):
        self.data = data

    #opens a file that has been saved from this very program
    def open_backup_file(self, path):
        self.time_sync_state = BACKUP_TIMESTAMP
        self.start_time = None 
        self.stream = open(path, "r+b")
        self.stream_is_active = True

    #opens a file dumped from the flash chip
    def open_flash_file(self, path):
        self.time_sync_state = FLASH_TIMESTAMP
        self.start_time = None
        self.stream = open(path, "r+b")
        self.stream_is_active = True

    #opens the serial connection
    def open_serial(self):
        self.time_sync_state = LIVE
        self.ser = SerialWrapper(self.device)
        result = self.ser.open_serial()
        if result:
            self.serial_is_active = True
            self.stream = self.ser
            self.stream_is_active = True
            return True
        return False

    def open_simulation(self, sim):
        self.time_sync_state = LIVE
        self.stream = sim
        self.stream_is_active = True

    #gets the seconds since the last message
    def seconds_since_last_message(self):
        return time.time() - self.last_message_time

    #get the current time using either the computer clock or the last timestamp
    def decide_on_time(self, name, value):
        self.last_message_time = time.time()
        if self.time_sync_state == LIVE:
            if self.start_time == None:
                    self.start_time = time.time()
            return time.time() - self.start_time

        if self.time_sync_state == BACKUP_TIMESTAMP:
            if name == "timestamp":
                self.last_timestamp = value
            if self.last_timestamp == None:
                return 0 #can't tell a proper value
            else:
                return self.last_timestamp / 1000 #convert to seconds

        if self.time_sync_state == FLASH_TIMESTAMP:
            if name == "ms_since_boot":
                self.last_timestamp = value
            if self.last_timestamp == None:
                return 0 #can't tell a proper time
            else:
                return self.last_timestamp / 1000 #convert to seconds

    def get_current_time(self):
        return self.decide_on_time("", 0)
    
    def reader_thread(self):
        while not self.exit:
            # Wait for an order
            if not self.stream_is_active or self.pause:
                time.sleep(0.1) # Don't overload the computer
                continue

            # === Looking for the beginning of a sequence
            separator = self.stream.read(1)
            # test for frame separator, read one byte at a time so it aligns itself
            if separator == b"":
                continue
            if separator[0] != SEPARATOR[0]:
                print(self.device + ": Invalid Separator: " + str(separator))
                continue
            #timestamp if reading from serial
            if self.stream == self.ser:
                self.ser.timestamp(self.get_current_time() * 1000)

            # === Checksum + number of data (4 + 4 bits)
            info = self.stream.read(1)[0] # 1 byte
            checksum = (info&240)>>4 # First 4 bits (240 = b"\xf0")
            packet_length = info&15 # Last 4 bits   (15 = b"\x0f")

            # print("Read : separator")
            # print("Read : checksum :", checksum)
            # print("Read : packet_length :", packet_length)

            message_checksum = 0
            messages = []
            for k in range(packet_length):
                # === Reading the id
                frame_id = self.stream.read(1)[0]
                # print("Read : id :", frame_id)

                # we have two different protocol definitions so decide on which one to use
                decoder = protocol.id_to_message_class(frame_id) # fc decoder
                if decoder is None:
                    decoder = edda.id_to_message_class(frame_id) # ec decoder
                if decoder is None:
                    # Error in the transmission
                    print("invalid id: ", frame_id)
                    message_checksum = 16 # This checksum is not valid
                    break

                buf, cs = self.read_data(decoder)
                messages.append((decoder,buf))
                message_checksum += ((frame_id&240)>>4) + (frame_id&15)
                message_checksum = (message_checksum + cs) % 16 # 16 = 2**4

            if checksum != message_checksum:
                print("Checksum doesn't match")
                print("    Given:", checksum, " | Expected:", message_checksum)
                continue
            
            # === Writing data
            for decoder, buf in messages:
                self.decode_and_write(decoder, buf)

    def read_data(self, decoder):
        """Read the data for 1 id and compute its checksum"""
        msg_checksum = 16
        length = decoder.get_size()
        buf = self.stream.read(length)
        if len(buf) != length:
            print("invalid length")
            return b"", msg_checksum
        for byte in buf:
            cs1 = (byte&240)>>4
            cs2 = byte&15
            msg_checksum = (msg_checksum + cs1 +cs2) % 16
        return buf, msg_checksum

    def decode_and_write(self, decoder, buf):
        decoder.parse_buf(buf)
        decoded_data = decoder.get_all_data()
        source = decoder.get_sender()
        message = decoder.get_message()
        suffix = ""
        if len(decoded_data) == 0:
            current_time = self.decide_on_time("", 0)
            self.data[source.name][message.name]["value"].x.append(current_time)
            self.data[source.name][message.name]["value"].y.append(1)
            
        for single_data in decoded_data:
            (field, value) = single_data
            if edda.is_specifier(source, message, field):
                suffix += ":" + (value.name if isinstance(value, Enum) else str(value))

        for single_data in decoded_data:
            (field, value) = single_data
            current_time = self.decide_on_time(field.name, value)
            if self.stream == self.ser:
                print(source.name, message.name, field.name + suffix, value)
            self.data[source.name][message.name][field.name + suffix].x.append(current_time)
            self.data[source.name][message.name][field.name + suffix].y.append(value)
