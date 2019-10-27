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

    Attributes
    ----------
    serial_desc_substrings : (str, str, ...)
        substring to look for in serial device description
        Serial devices with no subtrings from `serial_desc_substrings` in their description will not
        be oppened to avoid errors (they might be system devices not intended to be used that way)

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
    serial_desc_substrings = ("usb", "ch340", "arduino")

    def __init__(self, baudrate, bonjour="", port=""):
        self.bonjour = bonjour
        self.port = port
        self.ser = serial.Serial()
        self.ser.baudrate = baudrate
        self.ser.timeout = 0.1
        self.buffer = bytearray()

    def open_serial(self):
        """ Open the serial connection

        Returns
        -------
        bool
            True if the connection is opened
            False if an error occured

        """
        def open_port():
            try:
                self.ser.open()
                self.ser.reset_input_buffer()
                self.ser.reset_output_buffer()
                print("{} : serial connection opened ({})".format(
                    self.bonjour, self.ser.port))
                return True
            except Exception as e:
                print("{} : got serial error : {}".format(self.bonjour, e))
                return False

        # This is true if the device has already been found/openned before
        if self.ser.port:
            if self.ser.is_open:
                print("{} : serial connection is already open, cannot open again ({})".format(
                    self.bonjour, self.ser.port))
                return True
            else:
                return open_port()

        else:
            if self.bonjour:
                print("{} : Serial 'port' is not defined, using 'bonjour' to find device".format(
                    self.bonjour))
                if self.find_device(self.bonjour):
                    return True
            elif self.port:
                print("{} : Using 'port' {}".format(
                    self.bonjour, self.port))
                self.ser.port = self.port
                return open_port()
            else:
                print("{} : Serial 'port' and 'bonjour' are not defined, cannot open port".format(
                    self.bonjour))
                return False

    def close_serial(self):
        """ Close the serial connection

        """
        if self.ser.port:
            if self.ser.is_open:
                self.ser.reset_input_buffer()
                self.ser.reset_output_buffer()
                self.ser.close()
                print("{} : serial connection closed ({})".format(
                    self.bonjour, self.ser.port))
            else:
                print("{} : serial connection already closed ({})".format(
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
        line = line.decode('utf-8', 'backslashreplace')
        line = line.replace('\n', "")
        return line

    def readlines(self):
        """ Read the last received lines from the serial buffer

        The lines are decoded to ascii and the newline character is removed
        Incomplete lines are saved for later

        Parameters
        ----------
        ser : Serial instance
            the Serial instance to read a line from

        Returns
        -------
        lines : [string, ]
            the processed lines read from the serial buffer

        """
        i = max(1, min(2048, self.ser.in_waiting))
        data = self.ser.read(i)
        self.buffer.extend(data)

        if self.buffer:
            r = self.buffer.split(b'\n')
            lines = r[:-1]
            # Data after the last \n is an incomplete line, save for later
            self.buffer = r[-1]
            return [l.decode('utf-8', 'backslashreplace') for l in lines]
        return []

    def write(self, data):
        """ Send data via serial link

        Parameters
        ----------
        data : str
            data to send as a string

        """
        self.ser.write(data.encode('utf-8'))

    def find_device(self, bonjour):
        """ Test all connected serial devices to find the one that sends `bonjour` as the first transmitted line

        `ser.port` is updated when the device is successfully found. It is set to an empty string otherwise

        Parameters
        ----------
        bonjour : string
            string that should be sent by the device we want to find

        Returns
        -------
        success : bool
            True if the device is found

        """
        # Change the timeout value to 2 seconds and save the old value
        # The timeout should be long enough to that the Interface device can reset and send BONJOUR before the reading ends
        timeout = self.ser.timeout
        self.ser.timeout = 2

        # Get all the devices available on the computer
        available_ports = serial.tools.list_ports.comports()

        print("Searching for available serial devices for [{}]...".format(
            self.bonjour))
        if available_ports:
            print("Found available device(s) : {}".format(
                ", ".join([p.description for p in available_ports])))

            possible_interfaces = []
            # Extract devices that are expected to be Arduinos or alike from device list
            for p in available_ports:
                flag = False
                for substring in self.serial_desc_substrings:
                    if substring in p.description.lower():
                        flag = True
                if flag:
                    possible_interfaces.append(p)

            print("These devices will be checked : {}".format(
                ", ".join([p.description for p in possible_interfaces])))

        # Check only devices that are expected to be Arduinos or alike
        for p in possible_interfaces:
            self.ser.port = p.device
            print("Testing : {}...".format(self.ser.port))

            if self.open_serial():  # If the connection cannot be oppened, no need to read from it
                line = self.readline()

                if line == bonjour:
                    print("Found device ({}) on port : {}".format(
                        self.bonjour, self.ser.port))
                    # self.close_serial()
                    self.ser.timeout = timeout  # Restore the previous value
                    return True
                self.close_serial()

        print("/!\\ Failed to find device /!\\\n")
        self.ser.port = ""
        if available_ports:
            self.close_serial()
        self.ser.timeout = timeout  # Restore the previous value
        return False
