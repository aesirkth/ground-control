"""
Read data sent over serial link and save it on storage

"""

import csv
import datetime
import threading
import time
from os import mkdir
from os.path import dirname, isdir

import serial
import serial.tools.list_ports

baudrate = 115200
path = './data/telemetry.csv'

# See ./dummy_telemetry/dummy_telemetry.ino for the description of the protocol
newline = "N"
newhead = "H"
endline = "E"
sepdata = "\t"
bonjour = "TELEMETRY"


class Telemetry:
    def __init__(self, baudrate, path):
        self.baudrate = baudrate
        self.path = path
        # self.is_reading = True
        self.port = self.find_serial(bonjour)

    def resetCSV(self, path=path):
        """ Empty the file located at `path`
        
        If the file does not exist, it is created

        Parameters
        ----------
        path: path-like object
            path to the file to write
        
        """
        base = dirname(path)
        
        if not isdir(base):
            mkdir(base)
        
        with open(path, 'w+'):
            print("CVS file flushed")


    def writeCSV(self, dataArray, path=path):
        """ Append a line in the file located at `path`

        Each element of `dataArray` is written separated by a comma ','

        Parameters
        ----------
        dataArray: array-like object
            data to write in the file

        path: path-like object
            path to the file to write

        """
        with open(path, 'a', newline='') as csvFile:
            writer = csv.writer(csvFile, delimiter=',')
            writer.writerow(dataArray)


    def get_clean_serial_line(self, ser):
        """ Read a line from serial link and return it as a string

        The line is decoded to ascii and the newline character is removed

        NB: The newline character is different on linux systems

        Parameters
        ----------
        ser : Serial instance
            the Serial instance to read a line from
        
        Returns
        -------
        line : string
            the processed line read from serial

        """
        line = ser.readline()
        line = line.decode('ascii')
        line = line.replace("\r\n", "")
        return line


    def find_serial(self, bonjour):
        """ Test all connected serial device to find the one that sends `bonjour` as the first transmitted line

        Parameters
        ----------
        bonjour : string
            string that should be sent by the device we want to find
        
        Returns
        -------
        port : string
            full name/path of the port where the found device is connected 

        """
        available_ports = serial.tools.list_ports.comports()

        print("\nSearching for available serial devices...")
        print("Found device(s) : {}".format(", ".join([p.description for p in available_ports])))

        for p in available_ports:
            print("Testing : {}...".format(p.device))
            # The timeout should be long enough to that the telemetry receiver can reset and send BONJOUR before the reading ends
            with serial.Serial(p.device, baudrate=baudrate, timeout=2) as ser:
                ser.reset_input_buffer()

                line = self.get_clean_serial_line(ser)

                if line == bonjour:
                    print("Found telemetry device on port : {}".format(p.device))
                    return p.device

        print("/!\\ Failed to find telemetry device /!\\")
        # Must trigger an exception instead of returning None
        return None


    def check_header(self, line):
        """ Check if `line` is a valid header

        A valid header :
            - is non empty
            - starts with a `newhead` character ("N")
            - ends with a `endline` character ("E")
        
        Parameters
        ----------
        line: string
            line to verify

        """
        return len(line) > 0 and line[0] == newhead and line[-1] == endline


    def check_line(self, line):
        """ Check if `line` is a valid line

        A valid line :
            - is non empty
            - starts with a `newline` character ("N")
            - ends with a `endline` character ("E")
        
        Parameters
        ----------
        line: string
            line to verify

        """
        return len(line) > 0 and line[0] == newline and line[-1] == endline


    def start_read(self):
        """ Wait to get a valid header via serial link then save all received data to a file

        """
        self.is_reading = True
        # NB: need to find a way to catch timeouts
        with serial.Serial(self.port, baudrate=self.baudrate, timeout=0.1) as ser:

            self.resetCSV()
            ser.reset_input_buffer() #reset the buffer

            got_header = False
            print("Waiting for header...")
            while not got_header:
                line = self.get_clean_serial_line(ser)

                if self.check_header(line):
                    header_data = ["Time"] + line[1:-1].split(sepdata)
                    self.writeCSV(header_data)
                    got_header = True
                    print("Header received : {}".format(",".join(header_data)))

            while self.is_reading:
                line = self.get_clean_serial_line(ser)
                now = datetime.datetime.utcnow().isoformat()
                
                if self.check_line(line):
                    # print(line)
                    line_data = [now] + line[1:-1].split(sepdata)
                    self.writeCSV(line_data)
    

    def stop_read(self):
        self.is_reading = False




if __name__ == "__main__":
    telemetry = Telemetry(baudrate=baudrate, path=path)
    try :
        t = threading.Thread(target=telemetry.start_read)
        t.start()
        while True:
         time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        telemetry.stop_read()
    
    telemetry.stop_read()
