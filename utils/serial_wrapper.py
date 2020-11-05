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
        self.ser = serial.Serial()
        self.write = self.ser.write #copy pyserial's write function

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
        elif device == "RFD":
            pass #todo
        elif device == "gateway":
            pass #todo

    #tries to find and initialize the correct port
    def open_serial(self, device):
        baudrates = {
            "RFD": 0, #todo
            "gateway": 0,
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