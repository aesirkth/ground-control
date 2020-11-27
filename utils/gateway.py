from utils.serial_wrapper import SerialWrapper
from utils.data_handling import (Data, TimeSeries, RelativeTime)

import time
from threading import Thread


#####
# Gateway
#####
class Gateway():
    def __init__(self):
        self.data = {}
        self.read = True
        self.exit = False
        self.ser = SerialWrapper("gateway")

        self.output1 = False
        self.output2 = False
        self.output3 = False
        self.output4 = False

        self.servo1 = 0
        self.servo2 = 0
        self.servo3 = 0
        self.servo4 = 0

        self.bat1 = 0
        self.bat1_raw = 0
        self.bat2 = 0
        self.bat2_raw = 0

    def __send_header(self, target):
        start = 0x26
        target = ord(target)
        self.ser.write([start, target])

    def __read_state(self):
        while not self.ser.ser.in_waiting >= 12:
            time.sleep(0.1)

        state = self.ser.read_int(1)
        self.rfm_success = state & 1 > 0
        self.output1 = state & 2 > 0
        self.output2 = state & 4 > 0
        self.output3 = state & 8 > 0
        self.output4 = state & 16 > 0

        self.servo1 = self.ser.read_int(1)
        self.servo2 = self.ser.read_int(1)
        self.servo3 = self.ser.read_int(1)

        self.bat1_raw = self.ser.read_int(2)
        self.bat2_raw = self.ser.read_int(2)
        # hardcoded calibration
        self.bat1 = 2.555e-5 * self.bat1_raw ** 2 - 0.0835 * self.bat1_raw + 81.83
        self.bat2 = 8.885e-6 * self.bat2_raw ** 2 - 0.0316 * self.bat2_raw + 34.780

        self.rssi_controller = self.ser.read_int(1)
        self.rssi_gateway = self.ser.read_int(1)

        buf = self.ser.read_bytes(2)
        if not buf in b'\r\n':
            print("gateway: invalid separator after state byte")

    # if the gateway is currently open
    def state(self):
        return self.ser.port_is_open()

    # start and open serial
    def start(self):
        return self.ser.open_serial()

    # output can 1, 2, 3 or 4
    # state can be 1 (high) or 0 (low)
    def set_output(self, output, state):
        if not self.state():
            return -1
        outputs = {
            1: 0x61,  # a
            2: 0x62,  # b
            3: 0x63,  # c
            4: 0x64  # d
        }
        self.__send_header("c")

        self.ser.write([outputs[output], state])
        self.__read_state()

    # servo can be 1,2,3
    # angle can be 0-180
    def set_servo(self, servo, angle):
        if not self.state():
            return -1

        servos = {
            1: 0x6A,  # j
            2: 0x6B,  # k
            3: 0x6C  # l
        }
        self.__send_header("c")
        self.ser.write([servos[servo], angle])

        self.__read_state()
