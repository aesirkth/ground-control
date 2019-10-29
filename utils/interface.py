"""
Class to read data from an Interface device and save it on storage

"""

import csv
import yaml
import datetime
from os import mkdir
from os.path import isdir, join


class Interface:
    """ Class to read data received from an Interface device

    The Interface device is connected to the computer via a serial connection

    The data read from the Interface is stored in a CSV file in real time
    The time of reception of each line is stored along the received data
    in ISO format (YYYY-MM-DD HH:MM:SS.ffffff)

    Parameters
    ----------
    serial : Serial instance
        Serial instance used to read data from the Interface device
    path : path-like object
        path to the directory to store received data
    name : str
        name of the Interface instance. This is used to name the files written on file storage

    Attributes
    ----------
    is_reading : bool
        True if the instance is currently reading data from serial link
    data : list [[datetime.datetime, str, str, ], ]
        data read from Interface
        each string is the received data, separated by a comma ","
    calibration : dict {key: value, }
        calibration data received from the Interface
    messages : list [(datetime.datetime, str), ]
        messages received from the Interface

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

    def __init__(self, serial, path, name):
        self.path = path

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

        if not isdir(self.path):
            mkdir(self.path)

        self.serial = serial

    def write_data(self, dataArray):
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

    def process_header(self, line):
        """ Save header in memory

        The first item is the computer time of reception

        Parameters
        ----------
        line : string
            line received from telemetry, without start and end character

        """
        # Don't write the header twice
        if not self.header:
            self.header = ["Computer Time"] + line.split(self.separators['SEP_DATA'])
            self.write_data(self.header)
            print("Header : {}".format(self.header))

    def process_data(self, now, line):
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
            self.write_data(data)

    def write_calibration(self):
        """ Write the calibration data in the file located at `self.calibration_path`

        """
        with open(self.calibration_path, 'w') as file:
            file.write(yaml.dump(self.calibration))

    def process_calibration(self, line):
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
            self.write_calibration()
            print("Got calibration")

    def write_message(self, message):
        """ Append a line in the file located at `self.messages_path`

        If the file does not exit, it is created

        Parameters
        ----------
        message: string
            message to write in the file

        """
        with open(self.messages_path, 'a+') as file:
            file.write(message)

    def process_message(self, now, line):
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
        message = "{}\t{}\n".format(now, line)
        self.messages.append((now, line))
        self.write_message(message)
        print("Message : {}".format("{} {}".format(now.time().replace(microsecond=0), line)))

    def process_line(self, line):
        if len(line) > 0:
            line_start = line[0]
            line_content = line[1:]
            if line_start in self.separators_reversed:
                line_type = self.separators_reversed[line_start]
                now = datetime.datetime.now()

                if line_type == 'START_DATA':
                    self.process_data(now, line_content)

                elif line_type == 'START_HEAD':
                    self.process_header(line_content)

                elif line_type == 'START_CALI':
                    self.process_calibration(line_content)

                elif line_type == 'START_MESS':
                    self.process_message(now, line_content)
    
    def send_command(self, command):
        """ Send a command via serial link

        Parameters
        ----------
        command : str
            data to send as a string

        """
        self.serial.write(command)

    def start_read(self):
        """ Start reading and saving data from Interface device

        Does not stop until stop_read() is called

        """

        self.serial.open_serial()

        self.is_reading = True
        self.data = []

        while self.is_reading:
            if self.serial.failed:
                self.is_reading = False
            else:
                lines = self.serial.readlines()
                for line in lines:
                    self.process_line(line)


    def stop_read(self):
        """" Call this method to terminate serial reading

        Call start_read() to start the reading again

        """
        self.is_reading = False
        self.serial.close_serial()

    def get_device_status(self):
        """ Return the state of the Interface

        Ready means that the device is operational ie. completed its boot sequence

        Returns
        -------
        bool
            True if the device is ready

        """
        return self.serial.is_ready
    
    def get_device_error(self):
        """ Return the error status of the serial link

        Returns
        -------
        failed : bool
            True if there was a fatal error
        message : str
            content of the error message

        """
        failed, message = self.serial.get_serial_error()
        return (failed, message)
    
    def get_serial_status(self):
        """ Return the state of the serial link

        Returns
        -------
        bool
            True if the link is open

        """
        return self.serial.get_serial_status()