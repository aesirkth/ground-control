"""
Class to read data from a Gateway device and save it on storage

"""

import datetime
import threading
from os import mkdir
from os.path import isdir, join


class Gateway:
    """ Class to read data received from a Gateway device

    The Gateway device is connected to the computer via a serial connection

    The data read from the Gateway as bytes is saved in a file

    Parameters
    ----------
    serial : SerialWrapper instance
        SerialWrapper instance used to read data from the Gateway device
    sensors : Sensors instance
        Sensors instance used to process the received data
    path : path-like object
        path to the directory to store received data

    Attributes
    ----------
    is_reading : bool
        True if the instance is currently reading data from serial link

    Examples
    --------
    >>> serial = SerialWrapper(baudrate=57600, name="Telemetry", rfd900=True)
    >>> sensors = Sensors(imu="Test")
    >>> telemetry = Gateway(serial=serial, sensors=sensors, path="./data")
    >>> telemetry.start_read()
    >>> telemetry.send_command('do something')
    ...
    >>> telemetry.stop_read() # This terminates the thread in start_read()

    """

    def __init__(self, serial, sensors, path):
        self.serial = serial
        self.sensors = sensors
        self.path = path
        # This is the same as the serial for consistency
        self.name = self.serial.name

        self.is_reading = False

        self.date_created = datetime.datetime.now().replace(microsecond=0).isoformat()

        self.log_file = "{}_{}.log".format(
            self.date_created.replace(":", "-"),
            self.name)
        self.log_path = join(self.path, self.log_file)

        # Create the folder to store the files if it does not already exist
        if not isdir(self.path):
            mkdir(self.path)

    def __write_frame(self, frame):
        """ Append a line in the file located at `self.log_path`

        Parameters
        ----------
        frame: bytearray()
            frame to write in the file

        """
        with open(self.log_path, 'ab+') as file:
            file.write(frame)

    def send_command(self, command, *args, **kwargs):
        """ Send a command via serial link

        Parameters
        ----------
        command : str
            data to send as a string

        """
        if self.serial.get_status():
            self.serial.write(command, *args, **kwargs)

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
                        self.sensors.update_sensors(line)
                        self.__write_frame(line)

        self.serial.open_serial()

        self.is_reading = True
        self.data = []
        self.sensors.reset()

        t = threading.Thread(target=read_tread)
        t.start()

    def stop_read(self):
        """" Call this method to terminate serial reading

        Call start_read() to start the reading again

        """
        self.is_reading = False
        self.serial.close_serial()
