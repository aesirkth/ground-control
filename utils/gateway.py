"""
Class to read data from a Gateway device and save it on storage

"""

import csv
import datetime
import threading
from os import mkdir
from os.path import isdir, join

import yaml


class Gateway:
    """ Class to read data received from a Gateway device

    The Gateway device is connected to the computer via a serial connection

    The data read from the Gateway is stored in a CSV file in real time
    The time of reception of each line is stored along the received data
    in ISO format (YYYY-MM-DD HH:MM:SS.ffffff)

    Parameters
    ----------
    serial : Serial instance
        Serial instance used to read data from the Gateway device
    sensors : Sensors instance
        Sensors instance used to process the received data
    path : path-like object
        path to the directory to store received data
    name : str
        name of the Gateway instance. This is used to name the files written on file storage

    Attributes
    ----------
    is_reading : bool
        True if the instance is currently reading data from serial link
    data : list [[datetime.datetime, str, str, ], ]
        data read from Gateway
        each string is the received data, separated by a comma ","
    calibration : dict {key: value, }
        calibration data received from the Gateway
    messages : list [(datetime.datetime, str), ]
        messages received from the Gateway

    Examples
    --------
    >>> serial = SerialWrapper(baudrate=baudrate, bonjour = "TELEMETRY")
    >>> lps = Gateway(serial=serial, path=path, name="telemetry")
    >>> telemetry.start_read() # In another thread (use threading for example)
    >>> data = telemetry.data
    >>> mess = telemetry.messages
    ...
    >>> telemetry.stop_read() # This terminates the above thread

    """
    # This is described in the protocol description
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

    def __init__(self, serial, sensors, path, name):
        self.serial = serial
        self.sensors = sensors
        self.path = path
        self.name = name

        self.is_reading = False

        self.header = ""
        self.data = []
        self.calibration = {}
        self.messages = []

        self.date_created = datetime.datetime.now().replace(microsecond=0).isoformat()

        self.data_file = "{}_{}_data.csv".format(
            self.date_created.replace(":", "-"),
            name)
        self.data_path = join(self.path, self.data_file)

        self.calibration_file = "{}_{}_calibration.yaml".format(
            self.date_created.replace(":", "-"),
            name)
        self.calibration_path = join(self.path, self.calibration_file)

        self.messages_file = "{}_{}_messages.log".format(
            self.date_created.replace(":", "-"),
            name)
        self.messages_path = join(self.path, self.messages_file)

        # Create the folder to store the files if it does not already exist
        if not isdir(self.path):
            mkdir(self.path)

    def __write_data(self, dataArray):
        """ Append a line in the file located at `self.data_path`

        Each element of `dataArray` is written separated by a comma ','
        If the file does not exit, it is created

        Parameters
        ----------
        dataArray: array-like object
            data to write in the file

        """
        with open(self.data_path, 'a+', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(dataArray)

    def __process_header(self, line):
        """ Save header in memory

        The first item is the computer time of reception

        Parameters
        ----------
        line : string
            line received from telemetry, without start and end character

        """
        # Don't write the header twice
        if not self.header:
            self.header = ["Computer Time"] + \
                line.split(self.separators['SEP_DATA'])
            self.__write_data(self.header)
            print("Header : {}".format(self.header))

    def __process_data(self, now, line):
        """ Save data in memory and on file storage

        The first item is the computer time of reception as a datetime.datetime object
        Data cannot be recorded if the header has not been received

        Parameters
        ----------
        now : datetime object
            time of reception of the line
        line : string
            line received from telemetry, without start and end character

        """
        if self.header:
            data = [now] + line.split(self.separators['SEP_DATA'])
            self.data.append(data)
            self.sensors.update_sensors(data)
            self.__write_data(data)

    def __write_calibration(self):
        """ Write the calibration data in the file located at `self.calibration_path`

        """
        with open(self.calibration_path, 'w') as file:
            file.write(yaml.dump(self.calibration))

    def __process_calibration(self, line):
        """ Save calibration data in memory and on file storage

        Parameters
        ----------
        line : string
            line received from telemetry, without start and end character

        """
        # Don't save the calibration twice
        if not self.calibration:
            self.calibration = {value.split(self.separators['SEP_CALI'])[0]: value.split(
                self.separators['SEP_CALI'])[1] for value in line.split(self.separators['SEP_DATA'])}
            self.__write_calibration()
            self.sensors.update_calibration(self.calibration)
            print("Got calibration")

    def __write_message(self, message):
        """ Append a line in the file located at `self.messages_path`

        If the file does not exit, it is created

        Parameters
        ----------
        message: string
            message to write in the file

        """
        with open(self.messages_path, 'a+') as file:
            file.write(message)

    def __process_message(self, now, line):
        """ Save a message line in memory and on file storage

        The message is saved in memory as a list [datetime.datetime, str]

        The datetime.datetime object is stored as a string containing the time
        in ISO format (YYYY-MM-DD HH:MM:SS.ffffff) on files storage
        Use datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f') convert the time back to a 
        datetime.datetime object

        Parameters
        ----------
        now : datetime object
            time of reception of the line
        line : string
            line received from telemetry, without start and end character

        """
        # This is saved in memory
        self.messages.append((now, line))
        # This is written in file
        message = "{}\t{}\n".format(now, line)
        self.__write_message(message)
        # This in printed in the output console
        print("Message : {}".format("{} {}".format(
            now.time().replace(microsecond=0), line)))

    def __process_line(self, line):
        """ Interpret a received line and send it to the right method for further processing

        Parameters
        ----------
        line : str
            line received from the serial link

        """
        if len(line) > 0:
            line_start = line[0]
            line_content = line[1:]
            if line_start in self.separators_reversed:
                line_type = self.separators_reversed[line_start]
                now = datetime.datetime.now()

                if line_type == 'START_DATA':
                    self.__process_data(now, line_content)

                elif line_type == 'START_HEAD':
                    self.__process_header(line_content)

                elif line_type == 'START_CALI':
                    self.__process_calibration(line_content)

                elif line_type == 'START_MESS':
                    self.__process_message(now, line_content)

    def send_command(self, command):
        """ Send a command via serial link

        Parameters
        ----------
        command : str
            data to send as a string

        """
        if self.serial.get_status():
            self.serial.write(command)

    def start_read(self):
        """ Start reading and saving data from Gateway device

        Does not stop until stop_read() is called

        """
        def read_tread():
            while self.is_reading:
                if self.serial.failed:
                    self.is_reading = False
                else:
                    lines = self.serial.readlines()
                    for line in lines:
                        self.__process_line(line)

        self.serial.open_serial()

        self.is_reading = True
        self.data = []

        t = threading.Thread(target=read_tread)
        t.start()

    def stop_read(self):
        """" Call this method to terminate serial reading

        Call start_read() to start the reading again

        """
        self.is_reading = False
        self.serial.close_serial()
