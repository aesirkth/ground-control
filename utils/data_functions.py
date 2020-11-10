#data_functions.py
#contains eveything related to data

import time

telemetry_functions = {}
gateway_functions = {}

#class to store Data
#############
#source - the source of the data e.g. "flight" for flight controller
#         or "engine" for the engine controller
#measurement - What the value means e.g. "pressure" or "altitude"
#value - the value of the measurement e.g. 10 or 3
class Data:
    def __init__(self, source, measurement, value):
        self.source = source #flight or engine
        self.measurement = measurement #name of data
        self.value = value


#class to store time series
###############
#x - list with time values
#y - list with physical values 
class TimeSeries:
    def __init__(self):
        self.x = []
        self.y = []


#class to store and interpolate time
#############
#
class RelativeTime():
    def __init__(self):
        self.updated = time.time()
        self.time = 0

    def get_current_time(self):
        return time.time() - self.updated + self.time
    
    def update_time(self, new_time):
        self.time = new_time
        self.updated = time.time()

#telemetry
#############################################################
#ms since boot engine controller
def f0x10(ser):
    value = ser.read_bytes(4)
    return [Data("engine", "ms_since_boot", value)]
telemetry_functions[0x10] = f0x10

#μs since boot engine controller
def f0x11(ser):
    value = ser.read_bytes(8)
    return [Data("engine", "us_since_boot", value)]
telemetry_functions[0x11] = f0x11

#ms since boot flight controller
def f0x90(ser):
    value = ser.read_bytes(4)
    return [Data("flight", "ms_since_boot", value)]
telemetry_functions[0x90] = f0x90

#µs since boot flight controller
def f0x91(ser):
    value = ser.read_bytes(8)
    return [Data("flight", "us_since_boot", value)]
telemetry_functions[0x91] = f0x91


####################### made up functions
#altitude
def f0x00(ser):
    value = ser.read_bytes(2)
    return [Data("flight", "altitude", value)]
telemetry_functions[0x00] = f0x00

#acceleration
def f0x01(ser):
    value = ser.read_bytes(1)
    return [Data("flight", "acceleration", value)]
telemetry_functions[0x01] = f0x01

#pressure
def f0x02(ser):
    value = ser.read_bytes(2)
    return [Data("flight", "pressure", value)]
telemetry_functions[0x02] = f0x02

#catastrophe
def f0x03(ser):
    value = ser.read_bytes(1)
    return [Data("engine", "catastrophe", value)]
telemetry_functions[0x03] = f0x03

#gyroscope
def f0x04(ser):
    x = ser.read_bytes(1)
    y = ser.read_bytes(1)
    z = ser.read_bytes(1)
    return [
        Data("flight", "gyrox", x),
        Data("flight", "gyroy", y),
        Data("flight", "gyroz", z)
    ]
telemetry_functions[0x04] = f0x04


#gateway
####################################################