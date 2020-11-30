#serialWrapper.py
#
#contains the SerialWrapper which handles serial communication

import serial
import serial.tools.list_ports
import sys
from datetime import datetime
import os
import time

from utils.definitions import *

#Class to read and backup serial communication
#
#read_int(x) -    read x bytes as an integer, little endian
#read_string(x) -   read x bytes as a string
#read_bytes(x) -   read x bytes as a bytes
#init_device() -    tries to initialize the current port
#get_safe_devices() finds devices that are safe to communicate with
#open_serial() -    tests and opens all ports to find a device. returns -1 if it failed
class SerialWrapper:
    def __init__(self, device):
        self.ser = serial.Serial(timeout = 1)
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

    #read x bytes as an integer, little endian
    def read_int(self, amount):
        bytes = self.read_bytes(amount)
        total = 0
        count = 0
        for v in bytes:
            total += v << (count * 8)
            count += 1
        return total

    #read x amount of bytes as a string
    def read_string(self, amount):
        val = self.read_bytes(amount)
        return str(val)

    #read x amount of bytes as bytes
    def read_bytes(self, amount):
        val = self.ser.read(amount)
        self.backup.write(val)
        return val

    
    #tries to initialize a device
    #user self.ser to read and write since it does not need to be saved
    def init_device(self):
        if self.device == "dummy":
            self.ser.write(b'aaa')
            if (self.ser.read(3) == b'bbb'):
                return 1
            else:
                return 0

        elif self.device == "RFD":
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
            "dummy": 11520,
            "gateway": 115200,
            "RFD": 0,
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
        
        #timestamp the backupfile
        def timestamp(self, time):
            pass