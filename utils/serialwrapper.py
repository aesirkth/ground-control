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

    If `port` is provided, the serial connection will be opened on port `port`

    If both `bonjour` and `port` are provided, the the device that sends `bonjour`
    immediately after connection opening will be searched. If it is not found, the
    connection will be opened on the port `port`

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
        self.bonjour = bonjour
        self.rfd900 = rfd900
        self.port = port

        self.ser = serial.Serial()
        self.ser.baudrate = baudrate
        self.ser.timeout = 0.1
        self.buffer = bytearray()

        self.failed = False
        self.error = ""
        self.is_ready = False

    def __get_available_devices(self):
        """ Retrieve all the available serial device on the computer

        Returns
        -------
        devices : list
            a list containing ListPortInfo objects

        """
        devices = serial.tools.list_ports.comports()
        return devices

    def __filter_safe_devices(self, devices):
        """ Remove all non safe devices from a ListPortInfo list

        Parameters
        ----------
        devices : list
            a list containing ListPortInfo objects

        Returns
        -------
        safe_devices : list
            a list containing ListPortInfo objects

        """
        safe_devices = []

        for d in devices:
            flag = False
            for substring in self.serial_desc_substrings:
                if substring in d.description.lower():
                    flag = True
            if flag:
                safe_devices.append(d)

        return safe_devices

    def __find_gateway(self, bonjour="", rfd900=False):
        """ Test all connected serial devices to find the one that sends `bonjour` as the first transmitted line

        `ser.port` is updated when the device is successfully found. It is set to an empty string otherwise

        If both `bonjour` and `rfd900` are used, `rfd900` is used to find the device

        Parameters
        ----------
        bonjour : string
            string that should be sent by the device we want to find
        rfd900 : bool
            True if a RFD900 modem should be searched for

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

        # Get all the devices available on the computer
        available_devices = self.__get_available_devices()

        print("{} : Searching for available serial devices...".format(self.name))

        if available_devices:
            # Check only devices that are expected to be Arduinos or alike
            safe_devices = self.__filter_safe_devices(available_devices)

            if safe_devices:
                print("These devices will be checked : {}".format(
                    ", ".join([p.description for p in safe_devices])))

            else:
                error = "No serial device found"
                self.__fail_mode(error)
                return False

        else:
            error = "No serial device found"
            self.__fail_mode(error)
            return False

        if rfd900:
            print("Searching for a RFD900 modem")
            # Insert logic to identify RFD900 module here
            for d in safe_devices:
                self.ser.port = d.device
                print("Testing : {}...".format(self.ser.port))

                if self.open_serial():  # If the connection cannot be oppened, no need to read from it
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
                        print("{} : Found device on port : {}".format(
                            self.name, self.ser.port))
                        # self.close_serial()
                        self.ser.timeout = timeout  # Restore the previous value
                        self.__safe_mode()
                        self.is_ready = True
                        return True
                    else:
                        self.close_serial()

        elif bonjour:
            print("Searching for a Gateway using the bonjour string : {}".format(bonjour))

            for d in safe_devices:
                self.ser.port = d.device
                print("Testing : {}...".format(self.ser.port))

                if self.open_serial():  # If the connection cannot be oppened, no need to read from it
                    line = self.readline()

                    if line == bonjour:
                        print("{} : Found device ({}) on port : {}".format(
                            self.name, self.bonjour, self.ser.port))
                        # self.close_serial()
                        self.ser.timeout = timeout  # Restore the previous value
                        self.__safe_mode()
                        self.is_ready = True
                        return True
                    else:
                        self.close_serial()

        error = "Failed to find device"
        self.__fail_mode(error)
        self.ser.port = None
        self.ser.timeout = timeout  # Restore the previous value
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

    def __safe_mode(self):
        """ Revert the Instance attributes to normal after error recovery

        """
        self.error = ""
        self.failed = False

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
                self.failed = False
                self.buffer = bytearray()
                print("{} : serial connection opened ({})".format(
                    self.name, self.ser.port))
                error = ""
                self.__safe_mode()
                if self.rfd900:
                    self.is_ready = True
                return True
            except serial.SerialException as e:
                if e.errno == 2:
                    error = "Could not open port '{}'".format(self.ser.port)
                else:
                    error = e.strerror
            except Exception as e:
                error = "{} : {}".format(
                    self.bonjour, e)
            finally:
                if error:
                    self.__fail_mode(error)
                    self.close_serial()
                    return False

        # This is true if the device has already been found/openned before
        if self.ser.port:
            if self.ser.is_open:
                print("{} : serial connection is already open, cannot open again ({})".format(
                    self.name, self.ser.port))
                return True
            else:
                return open_port()

        else:
            if self.port:
                print("{} : Using 'port' {}".format(
                    self.name, self.port))
                self.ser.port = self.port
                return open_port()
            elif self.rfd900:
                print("{} : Port not defined, looking for device".format(self.name))
                return self.__find_gateway(rfd900=self.rfd900)
            elif self.bonjour:
                print("{} : Port not defined, looking for device".format(self.name))
                return self.__find_gateway(bonjour=self.bonjour)
            else:
                error = "{} : Serial 'port' and 'bonjour' and 'rfd900' are not defined, cannot open port".format(
                    self.name)
                self.__fail_mode(error)
                return False

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
        if self.failed:
            return

        try:
            line = self.ser.readline()
            line = line.decode('utf-8', 'backslashreplace')
            line = line.replace('\r\n', "")
            if line == self.bonjour:
                self.is_ready = True
            error = ""
        # This mostly means that the device is disconnected
        except serial.SerialException as e:
            error = "Device disconnected"
        # We get an error "an integer is required (got type NoneType)" when forcing GUI destruction without
        # closing the serial port before (in the thread that reads data)
        except TypeError as e:
            error = "Catched program closing"
        except Exception as e:
            error = "{} : {}".format(
                self.bonjour, e)
        finally:
            if error:
                self.__fail_mode(error)
                self.close_serial()
                return
            else:
                return line

    def readlines(self, decode=False):
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
        if self.failed:
            return []

        # Get the number of bytes in the buffer
        i = max(1, min(2048, self.ser.in_waiting))
        error = ""
        # Read the buffer
        try:
            data = self.ser.read(i)
            self.buffer.extend(data)
        # This mostly means that the device is disconnected
        except serial.SerialException as e:
            error = "Device disconnected"
        # We get an error "an integer is required (got type NoneType)" when forcing GUI destruction without
        # closing the serial port before (in the thread that reads data)
        except TypeError as e:
            error = "Catched program closing"
        except Exception as e:
            error = "{} : {}".format(
                self.bonjour, e)
        finally:
            if error:
                self.__fail_mode(error)
                self.close_serial()
                return []

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
