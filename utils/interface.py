"""
Class to read data from an Interface device and save it on storage

"""

import csv
import datetime
from os import mkdir
from os.path import isdir, join

from .serialwrapper import SerialWrapper


class Interface:
    """ Class to read data received from an Interface device

    The Interface device is connected to the computer via a serial connection

    The data read from the Interface is stored in a CSV file in real time
    The time of reception of each line is stored along the received data
    in ISO format (YYYY-MM-DDTHH:MM:SS.ffffff)

    Parameters
    ----------
    baudrate : int
        baudrate of the serial link
    path : path-like object
        path to the directory to store received data
    bonjour : string
        unique string sent by the targeted Interface when the connection is opened

    Attributes
    ----------
    ser : Serial instance
        Serial instance used to read data from the Interface device
    is_reading : bool
        True if the instance is currently reading data from serial link

    Examples
    --------
    >>> telemetry = Telemetry(baudrate=115200, path="path/to/directory/", bonjour="TELEMETRY")
    >>> telemetry.start_read()
    >>> data = telemetry.data
    >>> mess = telemetry.messages
    ...
    >>> telemetry.stop_read()

    """

    separators = {
        'START_HEAD': '@',
        'START_DATA': '#',
        'START_CALI': '%',
        'START_MESS': '$',
        'SEP_DATA': '&',
        'SEP_CALI': ':',
    }

    # We need to do searches both ways...
    separators_reversed = {value: key for key, value in separators.items()}

    def __init__(self, baudrate, path, bonjour):
        self.path = path

        self.is_reading = False
        self.header = ""
        self.calibration = {}
        self.messages = []
        self.data = [[], [], [], ]
        self.date_created = datetime.datetime.now().replace(microsecond=0).isoformat()
        self.data_file = "{}_data.csv".format(
            self.date_created.replace(":", "-"))
        self.data_path = join(self.path, self.data_file)

        if not isdir(self.path):
            mkdir(self.path)

        with open(self.data_path, 'w'):
            print("Data file created")

        self.serial = SerialWrapper(baudrate=baudrate, bonjour=bonjour)

    def write_data(self, dataArray):
        """ Append a line in the file located at `self.data_path`

        Each element of `dataArray` is written separated by a comma ','

        Parameters
        ----------
        dataArray: array-like object
            data to write in the file

        """
        with open(self.data_path, 'a+', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(dataArray)

    def process_header(self, line):
        # Don't write the header twice
        if not self.header:
            self.header = ["Time"] + line.split(self.separators['SEP_DATA'])
            self.write_data(self.header)
            print("Header : {}".format(self.header))

    def process_data(self, line):
        """ Save data in memory and on file storage

        Parameters
        ----------
        line : string
            line received from telemetry, without start and end character

        """
        if self.header:
            now = datetime.datetime.now().isoformat()
            data = [now] + line.split(self.separators['SEP_DATA'])
            # Need to make this append at the exact same time
            if not self.data[0]:
                self.data[0] = [data[0]]
            else:
                self.data[0].append(data[0])
            if not self.data[1]:
                self.data[1] = [int(data[1])]
            else:
                self.data[1].append(int(data[1]))
            if not self.data[2]:
                self.data[2] = [int(data[2])]
            else:
                self.data[2].append(int(data[2]))
            self.write_data(data)

    def process_calibration(self, line):
        """ Save calibration data in memory

        Parameters
        ----------
        line : string
            line received from telemetry, without start and end character

        """
        # Don't save the calibration twice
        if not self.calibration:
            self.calibration = {value.split(self.separators['SEP_CALI'])[0]: value.split(
                self.separators['SEP_CALI'])[1] for value in line.split(self.separators['SEP_DATA'])}
            print("Got calibration")
            print("Calibration data : {}".format(self.calibration))

    def process_message(self, line):
        """ Save a message line in memory

        Parameters
        ----------
        line : string
            line received from telemetry, without start and end character

        """
        self.messages += line
        print("Message : {}".format(line))

    def process_line(self, line):
        if len(line) > 0:
            line_start = line[0]
            line_content = line[1:]
            if line_start in self.separators_reversed:
                line_type = self.separators_reversed[line_start]

                if line_type == 'START_DATA':
                    self.process_data(line_content)

                elif line_type == 'START_HEAD':
                    self.process_header(line_content)

                elif line_type == 'START_CALI':
                    self.process_calibration(line_content)

                elif line_type == 'START_MESS':
                    self.process_message(line_content)

    def start_read(self):
        """ Start reading and saving data from Interface device

        Does not stop until stop_read() is called

        """
        self.is_reading = True
        self.data = [[], [], [], ]

        self.serial.open_serial()

        while self.is_reading:
            line = self.serial.readline()
            self.process_line(line)

    def stop_read(self):
        """" Call this method to terminate serial reading

        Call start_read() to start the reading again

        """
        self.is_reading = False
        self.serial.close_serial()
