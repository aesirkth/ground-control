"""
Class to read and write data from and to a serial connection

"""

import time
import datetime

import serial
import serial.tools.list_ports


class DummySerialWrapper:

    def __init__(self, name):
        self.name = name
        self.ser = serial.Serial()
        self.ser.port = 'COM'

        self.start_time = datetime.datetime.now()

        self.failed = False
        self.error = ""
        self.is_ready = False

    def open_serial(self):
        self.is_ready = True
        return True
 
    def close_serial(self):
        self.is_ready = False

    def get_status(self):
        return self.is_ready

    def write(self, data):
        return True

    def readline(self):
        # Frame number
        frame = b'\x01'
        # Status
        frame += b'\x00'
        # Err_msg
        frame += b'\x04\x02'
        # RTC
        now = datetime.datetime.now()
        delay = now - self.start_time
        hour = delay.hour
        minute = delay.minute
        second = delay.second
        millisecond = delay.microsecond/1000
        frame += bytes([hour])
        frame += bytes([minute])
        frame += bytes([second])
        frame += bytes([millisecond])

        # frame += b'\x01\x02\x01\x0B'
        # Timer
        frame += b'\x10\x27\x00\x00' # 5s
        # Battery1
        frame += b'\x00\x00'
        # Battery2
        frame += b'\x00\x00'
        # IMU2
        frame += b'\x07\xAE\x06\xDE\x07\xDE\x07\xDE\x07\xDE\x07\xDE\x07\xDE'
        frame += b'\x07\xDE\x00\xDE\x07\xDE\x07\xDE\x07\xDE\x07\xDE\x07\xDE'
        frame += b'\x07\xAE\x06\xDE\x07\xDE\x07\xDE\x07\xDE\x07\xDE\x07\xDE'
        frame += b'\x07\xDE\x00\xDE\x07\xDE\x07\xDE\x07\xDE\x07\xDE\x07\xDE'
        # BMP2
        frame += b'\xD0\x07\x00\x00\x00\xCD\x8B\x01'
        # BMP3
        frame += b'\x00\x00\x00\x00\x00\x00\x00\x00'
        # MAG
        frame += b'\x00\x00\x00\x00\x00\x00'
        # PITOT
        frame += b'\x00\x00'
        # GPS
        frame += b'\x00\x00\x00\x00'
        frame += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        frame += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        frame += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        frame += b'\x00\x00\xFF'
        # Garbage
        frame += b'\x00\x00\x00\x00\x00\x00\x00'
        return frame

    def readlines(self, decode=False):
        time.sleep(0.1)
        # Frame number
        frame = b'\x02'
        # Status
        frame += b'\x00'
        # Err_msg
        frame += b'\x00\x01'
        # RTC
        now = datetime.datetime.now()
        delay = now - self.start_time
        hour = delay.seconds/3600
        minute = (delay.seconds%3600)/60
        second = delay.seconds%60
        millisecond = delay.microseconds/1000
        frame += bytes([int(hour)])
        frame += bytes([int(minute)])
        frame += bytes([int(second)])
        frame += bytes([int(millisecond*256/1000)])
        # Timer
        frame += b'\x10\x27\x00\x00' # 5s
        # Battery1
        frame += b'\x3C\x0D'
        # Battery2
        frame += b'\x00\x00'
        # IMU2
        frame += b'\x07\xAE\x06\xDE\x07\xDE\x07\xDE\x07\xDE\x07\xDE\x07\xDE'
        frame += b'\x07\xDE\x00\xDE\x07\xDE\x07\xDE\x07\xDE\x07\xDE\x07\xDE'
        frame += b'\x07\xAE\x06\xDE\x07\xDE\x07\xDE\x07\xDE\x07\xDE\x07\xDE'
        frame += b'\x07\xDE\x00\xDE\x07\xDE\x07\xDE\x07\xDE\x07\xDE\x07\xDE'
        # BMP2
        frame += b'\xD0\x07\x00\x00\x00\xCD\x8B\x01'
        # BMP3
        frame += b'\x00\x00\x00\x00\x00\x00\x00\x00'
        # MAG
        frame += b'\x00\x00\x00\x00\x00\x00'
        # PITOT
        frame += b'\x00\x00'
        # GPS
        frame += b'\x00\x00\x00\x00'
        frame += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        frame += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        frame += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        frame += b'\x00\x00\x18'
        # Garbage
        frame += b'\x00\x00\x00\x00\x00\x00\x00'
        return [frame]
