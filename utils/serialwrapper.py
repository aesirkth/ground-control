"""
Class to read and write data from and to a serial connection

"""

import time

import serial
import serial.tools.list_ports


class SerialWrapper:
    """ Class to read and write data through a serial connection

    If `bonjour` is provided, all available serial ports will be tested to find
    the device that sends `bonjour` immediately after connection opening

    If `rfd900` is provided, all available serial ports will be tested to find
    the device that respond to an "AT" command

    If `port` is provided, the serial connection will be opened on port `port`

    The priority order for optional parameters is `bonjour` > `rfd900` > 'port
    If more than one of them is given, the one with the highest priority will be used

    Parameters
    ----------
    baudrate : int
        the baudrate of the connection
    name : str
        name of the instance, used when printing instance status
    bonjour : string, optional
        unique string sent by the targeted gateway when the connection is opened
    rfd900 : bool, optional
        True to automatically find a RFD900 modem among the serial devices
    port : string, optional
        port to open

    Attributes
    ----------
    failed : bool
        True if a fatal error occured
    error : str
        String with the content of the last error
    is_ready : bool
        True if the device is ready to use (ie boot have been completed)

    Examples
    --------
    >>> s = SerialWrapper(baudrate=57600, name="Telemetry", rfd900=True)
    >>> s.open_serial()
    >>> line = s.readline()
    >>> s.close_serial()

    >>> s = SerialWrapper(baudrate=57600, name="Telemetry", port="COM4")
    >>> s.open_serial()
    >>> line = s.readline()
    >>> s.close_serial()

    """
    # Substring to look for in serial device description
    # Serial devices with no subtrings from `serial_desc_substrings` in their description will not
    # be oppened to avoid errors (they might be system devices not intended to be used that way)
    # Use lower case
    serial_desc_substrings = ("usb", "ch340", "arduino")

    def __init__(self, baudrate, name, bonjour="", rfd900=False, port=""):
        self.name = name

        self.failed = False
        self.error = ""
        self.is_ready = False

        if bonjour:
            self.mode = "BONJOUR"
        elif rfd900:
            self.mode = "RFD900"
        elif port:
            self.mode = "PORT"
        else:
            self.__fail_mode(
                "At least one of the optional arguments is needed for SerialWrapper")

        self.bonjour = bonjour
        self.rfd900 = rfd900
        self.port = port

        self.ser = serial.Serial()
        self.ser.baudrate = baudrate
        self.ser.timeout = 0.1
        self.buffer = bytearray()

        self.is_device_found = False

    def __get_safe_devices(self):
        """ Retrieve a list of available devices connected on the computer

        Devices that don't match with the `serial_desc_substrings` are not returned

        Returns
        -------
        safe_devices : list
            a list containing ListPortInfo objects

        """
        safe_devices = []

        devices = serial.tools.list_ports.comports()

        for d in devices:
            flag = False
            for substring in self.serial_desc_substrings:
                if substring in d.description.lower():
                    flag = True
            if flag:
                safe_devices.append(d)

        return safe_devices

    def __auto_find_gateway(self):
        """ Automatically find the right Gateway device among all the serial devices connected to the computer

        `ser.port` is updated when the device is successfully found. It is set to None otherwise

        Returns
        -------
        success : bool
            True if the device is found

        """
        # Change the timeout value to 2 seconds and save the old value
        # The timeout should be long enough to that the Gateway device can reset and send BONJOUR before the reading ends
        timeout = self.ser.timeout
        self.ser.timeout = 2
        self.ser.port = None

        found_device = False

        print("{} : Searching for available serial devices...".format(self.name))

        # Check only devices that are expected to be Arduinos or alike
        safe_devices = self.__get_safe_devices()

        if safe_devices:
            print("These devices will be checked : {}".format(
                ", ".join([p.description for p in safe_devices])))

        else:
            error = "No serial device found"
            self.__fail_mode(error)
            return False

        if self.mode == "RFD900":
            print("Searching for a RFD900 modem")
            # Insert logic to identify RFD900 module here
            for d in safe_devices:
                self.ser.port = d.device
                print("Testing : {}...".format(self.ser.port))

                if self.__open_serial_port():  # If the connection cannot be oppened, no need to read from it
                    # Dirty but the RFD900 needs 1s with no data input before the "+++" to enter AT command mode
                    # In practice the port is unused before we open it so this pause is not really needed
                    # But just to be sure...
                    time.sleep(1)
                    # Try to enter AT command mode
                    self.write('+++', encode=True)
                    # Wait one second and see the "OK" has been sent by the device
                    time.sleep(1)
                    lines = self.readlines()
                    # Exit AT command mode
                    self.write('ATO\r', encode=True)

                    if b'OK' in lines:
                        found_device = True
                        break

                    else:
                        self.close_serial()

        elif self.mode == "BONJOUR":
            print("Searching for a Gateway using the bonjour string : {}".format(
                self.bonjour))

            for d in safe_devices:
                self.ser.port = d.device
                print("Testing : {}...".format(self.ser.port))

                if self.__open_serial_port():  # If the connection cannot be oppened, no need to read from it
                    line = self.readline()

                    if line == self.bonjour:
                        found_device = True
                        break

                    else:
                        self.close_serial()

        self.ser.timeout = timeout  # Restore the previous value

        if found_device:
            self.__safe_mode()
            self.is_ready = True
            self.is_device_found = True
            print("{} : Found device on port : {}".format(
                self.name, self.ser.port))
            
            return True
        
        else:
            error_msg = "Failed to find device"
            self.__fail_mode(error_msg)
            self.is_ready = False
            self.is_device_found = False
            self.port = None
            
            
            return False

    def __fail_mode(self, error):
        """ Set the right value to Instance attributes in case a fatal error occured

        Parameters
        ----------
        error : str
            String with the error text

        """
        self.error = error
        print(self.error)
        self.failed = True
        self.is_ready = False

    def __read_serial_buffer(self):
        """ Read the last received bytes from the serial buffer

        Returns
        -------
        error_code : int
            0 if no error occured
        error_msg : string
            python string describing the error if one occured
        buffer : bytearray
            bytes read from the serial buffer

        """
        error_code = 0
        error_msg = ""
        buffer = bytearray()

        # Get the number of bytes in the buffer
        i = max(1, min(2048, self.ser.in_waiting))

        # Read the buffer
        try:
            buffer = self.ser.read(i)
        # This mostly means that the device is disconnected
        except serial.SerialException as e:
            error_code = 1
            error_msg = "Device disconnected"
        # We get an error "an integer is required (got type NoneType)" when forcing GUI destruction without
        # closing the serial port before (in the thread that reads data)
        except TypeError as e:
            error_code = 2
            error_msg = "Catched program closing"
        # Catch any other exception
        except Exception as e:
            error_code = 3
            error_msg = "{}".format(e)

        return error_code, error_msg, buffer

    def __read_serial_line(self):
        """ Read a line from serial link and return it as a string

        The line is decoded to ascii and the newline character is removed

        Returns
        -------
        error_code : int
            0 if no error occured
        error_msg : string
            python string describing the error if one occured
        line : string
            the processed line read from serial

        """
        error_code = 0
        error_msg = ""
        line = ""

        try:
            line = self.ser.readline()

        # This mostly means that the device is disconnected
        except serial.SerialException as e:
            error_msg = "Device disconnected"
            error_code = 1
        # We get an error "an integer is required (got type NoneType)" when forcing GUI destruction without
        # closing the serial port before (in the thread that reads data)
        except TypeError as e:
            error_code = 2
            error_msg = "Catched program closing"
        # Catch any other exception
        except Exception as e:
            error_code = 3
            error_msg = "{}".format(e)

        return error_code, error_msg, line

    def __safe_mode(self):
        """ Revert the Instance attributes to normal after error recovery

        """
        self.error = ""
        self.failed = False

    def __open_serial_port(self):
        """ Open the serial port

        Relevant variables are cleared

        Returns
        -------
        bool
            True if the port has been successfully openned

        """
        error_msg = ""
        try:
            self.ser.open()
            self.ser.reset_input_buffer()
            self.ser.reset_output_buffer()
            self.failed = False
            self.buffer = bytearray()
            self.__safe_mode()
            if self.mode == "RFD900":
                self.is_ready = True
            print("{} : serial connection opened ({})".format(
                self.name, self.ser.port))
            return True

        except serial.SerialException as e:
            if e.errno == 2:
                error_msg = "Could not open port '{}'".format(self.ser.port)
            else:
                error_msg = e.strerror

        except Exception as e:
            error_msg = "{} : {}".format(
                self.bonjour, e)

        finally:
            if error_msg:
                self.__fail_mode(error_msg)
                self.close_serial()
                return False

    def open_link(self):
        """ Open the link to the Gateway

        Returns
        -------
        bool
            True if the connection is opened
            False if an error occured

        """
        if self.is_device_found:
            if self.mode in ["BONJOUR", "RFD900", "PORT"]:
                return self.__open_serial_port()
            else:
                return True

        else:
            success = False
            if self.mode == "PORT":
                self.ser.port = self.port
                success = self.__open_serial_port()
                if success:
                    self.is_device_found = True

            elif self.mode in ["RFD900", "BONJOUR"]:
                success = self.__auto_find_gateway()  # The port is left open if successful

            return success

    def close_serial(self):
        """ Close the serial connection

        """
        if self.ser.port:
            if self.ser.is_open:
                try:
                    self.ser.reset_input_buffer()
                    self.ser.reset_output_buffer()
                    self.ser.close()
                    print("{} : serial connection closed ({})".format(
                        self.name, self.ser.port))
                except:
                    self.ser.close()
                    print("{} : serial connection closed ({})".format(
                        self.name, self.ser.port))
                self.is_ready = False

    def get_status(self):
        """ Return the state of the serial port

        Returns
        -------
        bool
            True if the serial port is open

        """
        return self.ser.is_open

    def write(self, data, encode=False):
        """ Send data via serial link

        Parameters
        ----------
        data : str
            data to send as a string

        """
        if self.failed:
            return

        if encode:
            self.ser.write(data.encode('utf-8'))
        else:
            self.ser.write(data)

    def readline(self):
        """ Read a line from serial link and return it as a string

        The line is decoded to utf-8 and the newline character is removed

        Returns
        -------
        line : string
            the processed line read from serial. Empty if an error occured

        """
        if self.failed:
            return ""

        error_code, error_msg, line = self.__read_serial_line()

        if error_code:
            error = "{} : {}".format(self.name, error_msg)
            self.__fail_mode(error)
            self.close_serial()
            return ""

        line = line.decode('utf-8', 'backslashreplace')
        line = line.replace('\r\n', "")

        if line == self.bonjour:
            self.is_ready = True

        return line

    def readlines(self, decode=False):
        """ Read the last received lines from the serial buffer

        The lines are decoded to utf-8 and the newline character is removed
        Incomplete lines are saved for later

        Returns
        -------
        lines : [string, ]
            the processed lines read from the serial buffer. Empty if an error occured
        """
        if self.failed:
            return []

        error_code, error_msg, buffer = self.__read_serial_buffer()

        if error_code:
            error = "{} : {}".format(self.name, error_msg)
            self.__fail_mode(error)
            self.close_serial()
            return []

        self.buffer.extend(buffer)

        # Do not run this if no new data has been retrieved
        if self.buffer:
            # Convert the buffer into a list of bytearray (one bytearray for each line)
            r = self.buffer.split(b'\r\n')
            # Data after the last \n is an incomplete line, save for later
            self.buffer = r[-1]
            # This is the complete lines
            lines = r[:-1]
            if decode:
                lines = [l.decode('utf-8', 'backslashreplace') for l in lines]
            if self.bonjour in lines or bytearray(map(ord, self.bonjour)) in lines:
                self.is_ready = True
            return lines
        else:
            return []
