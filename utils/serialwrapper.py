"""
Class to read and write data from and to a serial connection

"""

import serial
import serial.tools.list_ports


class SerialWrapper:
    """ Class to read and write data through a serial connection

    If `bonjour` is provided, all available serial ports will be tested to find
    the device that sends `bonjour` immediately after connection opening

    If `port` is provided, the serial connection will be opened on port `port`

    If both `bonjour` and `port` are provided, the the device that sends `bonjour`
    immediately after connection opening will be searched. If it is not found, the
    connection will be opened on the port `port`

    Parameters
    ----------
    baudrate : int
        the baudrate of the connection
    bonjour : string, optional
        unique string sent by the targeted device when the connection is opened
    port : string, optional
        port to open

    Examples
    --------
    >>> s = SerialWrapper(baudrate=112500, bonjour="TELEMETRY")
    >>> s.open_serial()
    >>> line = s.readline()
    >>> s.close_serial()

    >>> s = SerialWrapper(baudrate=112500, port="COM4")
    >>> s.open_serial()
    >>> line = s.readline()
    >>> s.close_serial()

    """

    def __init__(self, baudrate, bonjour="", port=""):
        self.bonjour = bonjour
        self.ser = serial.Serial()
        self.ser.baudrate = baudrate
        self.ser.timeout = 0.1
        if bonjour:
            self.find_device(bonjour)  # This sets ser.port
        elif port or not self.ser.port:
            self.ser.port = port

    def open_serial(self):
        """ Open the serial connection

        """
        if self.ser.port:
            if self.ser.is_open:
                print("{} : serial connection is already open, cannot open again ({})".format(
                    self.bonjour, self.ser.port))
            else:
                self.ser.open()
                print("{} : serial connection opened ({})".format(
                    self.bonjour, self.ser.port))
        else:
            print("{} : cannot open serial connection, 'port' is not defined".format(
                self.bonjour))

    def close_serial(self):
        """ Close the serial connection

        """
        if self.ser.port:
            if self.ser.is_open:
                self.ser.close()
                print("{} : serial connection closed ({})".format(
                    self.bonjour, self.ser.port))
            else:
                print("{} : serial connection is not open, cannot close ({})".format(
                    self.bonjour, self.ser.port))
        else:
            print("{} : cannot close serial connection, 'port' is not defined".format(
                self.bonjour))

    def readline(self):
        """ Read a line from serial link and return it as a string

        The line is decoded to ascii and the newline character is removed

        Parameters
        ----------
        ser : Serial instance
            the Serial instance to read a line from

        Returns
        -------
        line : string
            the processed line read from serial

        """
        line = self.ser.readline()
        line = line.decode('ascii')
        line = line.replace('\n', "")
        return line

    def find_device(self, bonjour):
        """ Test all connected serial devices to find the one that sends `bonjour` as the first transmitted line

        `ser.port` is updated when the device is successfully found. It is set to an empty string otherwise

        Parameters
        ----------
        bonjour : string
            string that should be sent by the device we want to find

        Returns
        -------
        port : string
            full name/path of the port where the found device is connected
            an empty string is returned if the device is not found

        """
        # Change the timeout value to 2 seconds and save the old value
        # The timeout should be long enough to that the Interface device can reset and send BONJOUR before the reading ends
        timeout = self.ser.timeout
        self.ser.timeout = 2

        available_ports = serial.tools.list_ports.comports()

        print("\nSearching for available serial devices for ({})...".format(self.bonjour))
        if available_ports:
            print("Found device(s) : {}".format(
                ", ".join([p.description for p in available_ports])))

        for p in available_ports:
            print("Testing : {}...".format(p.device))
            self.ser.port = p.device
            self.open_serial()
            self.ser.reset_input_buffer()

            line = self.readline()

            if line == bonjour:
                print("Found device ({}) on port : {}\n".format(
                    self.bonjour, self.ser.port))
                self.close_serial()
                self.ser.timeout = timeout  # Restore the previous value
                return p.device

        print("/!\\ Failed to find device /!\\\n")
        # Must trigger an exception instead of returning None
        self.ser.port = ""
        if available_ports:
            self.close_serial()
        self.ser.timeout = timeout  # Restore the previous value
        return None
