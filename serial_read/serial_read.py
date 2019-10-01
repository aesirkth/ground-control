"""
Class to read data sent over serial link and save it on storage

"""

import csv
import datetime
from os import mkdir
from os.path import dirname, isdir

import serial
import serial.tools.list_ports


# See ../dummy_telemetry/dummy_telemetry.ino for the description of the protocol
newline = "N"
newhead = "H"
endline = "E"
sepdata = "\t"
bonjour = "TELEMETRY" # Not used


class Telemetry:
    """ Class to read data received via serial link

    The data read from the serial link is stored in a CSV file in real time
    The system time of receiving each line is stored along the received data
    in ISO format (YYYY-MM-DDTHH:MM:SS.ffffff)

    Parameters
    ----------
    baudrate : int
        Baurate of the serial link
    path : path-like object
        Path to the file to write
        File extension should be '.csv'
    port : string
        Full name/path of the port the instance is set to read data from
    is_reading : bool
        True if the instance is currently reading data from serial link
    
    Examples
    --------
    >>> telemetry = Telemetry(baudrate=115200, path="path/to/file.csv")
    >>> port = telemetry.find_serial(bonjour="TELEMETRY")
    >>> telemetry.start_read()
    ...
    >>> telemetry.stop_read()


    >>> telemetry = Telemetry(baudrate=115200, path="path/to/file.cvs")
    >>> telemetry.start_read(bonjour="TELEMETRY")
    ...
    >>> telemetry.stop_read()

    """
    def __init__(self, baudrate, path):
        self.baudrate = baudrate
        self.path = path
        self.is_reading = False
        self.port = None


    def resetCSV(self):
        """ Empty the file located at `self.path`
        
        If the file does not exist, it is created
        
        """
        base = dirname(self.path)
        
        # This fails if there are two or more levels of directory not yet existing in the path
        if not isdir(base):
            mkdir(base)
        
        with open(self.path, 'w+'):
            print("CVS file flushed")


    def writeCSV(self, dataArray):
        """ Append a line in the file located at `self.path`

        Each element of `dataArray` is written separated by a comma ','

        Parameters
        ----------
        dataArray: array-like object
            data to write in the file

        """
        with open(self.path, 'a', newline='') as csvFile:
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
    
    
    def find_serial(self, bonjour):
        """ Test all connected serial devices to find the one that sends `bonjour` as the first transmitted line

        `self.port` is updated when the device is successfully found. It is set to `None` otherwise

        Parameters
        ----------
        bonjour : string
            string that should be sent by the device we want to find
        
        Returns
        -------
        port : string
            full name/path of the port where the found device is connected
            None is returned if the device is not found

        """
        available_ports = serial.tools.list_ports.comports()

        print("\nSearching for available serial devices...")
        print("Found device(s) : {}".format(", ".join([p.description for p in available_ports])))

        for p in available_ports:
            print("Testing : {}...".format(p.device))
            # The timeout should be long enough to that the telemetry receiver can reset and send BONJOUR before the reading ends
            with serial.Serial(p.device, baudrate=self.baudrate, timeout=2) as ser:
                ser.reset_input_buffer()

                line = self.get_clean_serial_line(ser)

                if line == bonjour:
                    print("Found telemetry device on port : {}".format(p.device))
                    self.port = p.device
                    return p.device

        print("/!\\ Failed to find telemetry device /!\\")
        # Must trigger an exception instead of returning None
        self.port = None
        return None


    def start_read(self, bonjour=None):
        """ Wait to get a valid header via serial link then save all received data to a file

        Does not stop until stop_read() is called

        Parameters
        ----------
        bonjour : string, optional
            string that should be sent by the device we want to find

        """
        self.is_reading = True

        # If `bonjour` is given, search for the device location
        # If not, don't search for the device and assume that `self.port` is already set correctly
        if bonjour != None:
            self.find_serial(bonjour)

        # NB: need to find a way to catch timeouts
        with serial.Serial(self.port, baudrate=self.baudrate, timeout=0.1) as ser:

            self.resetCSV()
            ser.reset_input_buffer() # Reset the buffer

            got_header = False
            print("Waiting for header...")
            # The process might be stuck here...
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
        """" Call this method to terminate serial reading

        Call start_read() to start the reading again

        """
        self.is_reading = False
    