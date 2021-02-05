#data_functions.py
#contains classes to parse and store data
#also contains the functions for inluxdb 

import time
import datetime
import struct
from utils.definitions import *
from influxdb import InfluxDBClient

# class to store Data
#############
# source - the source of the data e.g. "flight" for flight controller
#         or "engine" for the engine controller
# measurement - What the value means e.g. "pressure" or "altitude"
# value - the value of the measurement e.g. 10 or 3
class Data:
    def __init__(self, source, measurement, value):
        self.source = source #usually flight or engine
        self.measurement = measurement #name of data
        self.value = value


# class to return data asynchronously
#####################
# resolve(data) - call to "return" data
# then(func) - set the callback function
# wait() - waits and returns the result
class Promise():
    def __init__(self):
        self.function = lambda x: None
        self.result = None
    
    def resolve(self, result):
        self.result = result
        if self.function:
            self.function(result)

    #blocks while waiting for the promise to return
    def wait(self):
        while self.result != None:
            pass
        return self.result

    #set the callback function
    #the callback funtion will take the result as its argument
    def then(self, func):
        self.function = func


#class to store time series
###############
# x - list with time values
# y - list with measurements 
# pack() - returns x and y in a tuple
# get_last() - gets the last y value
class TimeSeries:
    def __init__(self):
        self.x = []
        self.y = []

    def pack(self, *args):
        return (self.x, self.y)

    def get_last(self):
        if len(self.y) == 0:
            return 0
        else: 
            return self.y[-1] 


#class to store and interpolate time
#############
# get_current_time() - interpolates and gets the current time (in seconds)
# update_time() - update the current time (in seconds)
class RelativeTime():
    def __init__(self):
        self.updated = time.time()
        self.time = 0

    def get_current_time(self):
        return time.time() - self.updated + self.time
    
    def update_time(self, new_time):
        self.time = new_time
        self.updated = time.time()


######
#class to decode integers
##
# init(source, packaging, measurement, min = 0, max = 0)
# source - source of the data
# packaging - the python struct field
# measurement - the measurement that is encoded
# min - optional, the min value
# max - optional, the max value
#
# decode(ser) - reads and decodes the data. returns an array with Data classess
class Decoder():
    def __init__(self, source, packaging, measurement, scale = 1, min = 0, max = 0):
        self.source = source
        self.packaging = packaging
        self.source = source
        self.measurement = measurement
        self.scale = scale
        self.min = min
        self.max = max
        
    def decode(self, ser):
        size = struct.calcsize(self.packaging)
        buff = ser.read_bytes(size)
        val = struct.unpack(self.packaging, buff)[0] * self.scale
        if self.max or self.min:
            intmax = 2 << (size * 8) - 1
            if(val <= 0):
                return self.min - 1.0

            if(val >= intmax):
                return self.max + 1.0

            ratio = (val - self.min) / (self.max - self.min)
            val =  1 + ((intmax - 2)) * ratio

        return [Data(self.source, self.measurement, val)]


##
# class to decode boolean values
##
# init(source, bits)
# source - source of the data
# bits - the measurements in order
#
# decode() - returns an array with Data classes
class BitDecoder():
    def __init__(self, source, bits):
        self.source = source
        self.bits = bits

    def decode(self, ser):
        buff = ser.read_int(1)
        out = []
        for i in range(0, len(self.bits)):
            val = (buff & (2 ** i)) > 0
            out.append(Data(self.source, self.bits[i], val))
        return out

    def init(self):
        out = []
        for i in self.bits:
            out.append(Data(self.source, i, 0))
        return out


##
# class to decode anything
##
# init(func)
# func - the function that is used for decoding
# func should return an array with Data classes
#
# decode() - copy of func
class CustomDecoder():
    def __init__(self, func):
        self.decode = func

def get_current_time():
    now = datetime.datetime.now()
    time = now.strftime("%H%M%S%f")[:9]
    return int(time)

def formatted_time_to_sec(time):
    seconds = 0
    formatted = str(time)
    print(formatted)
    formatted = '0' * (9 - len(formatted)) + formatted
    print(formatted)
    seconds += int(formatted[-3:]) / 1000
    seconds += int(formatted[-5:-3])
    seconds += int(formatted[-7:-5]) * 60
    seconds += int(formatted[-9:-7]) * 60 * 60
    return seconds

# returns an array with Decoders with their names concatenated with numbers 
# from start up to and including end 
def MultiDecoder(source, packaging, name, start, end, *args):
    out = []
    for i in range(start, end+1):
        d = Decoder(source, packaging, name + str(i), *args)
        out.append(d)
    return out


# returns 3 decoders with their names concatenaded with x y and z
def xyzDecoder(source, packaging, name, *args):
    out = []
    out.append(Decoder(source, packaging, name + "x", *args))
    out.append(Decoder(source, packaging, name + "y", *args))
    out.append(Decoder(source, packaging, name + "z", *args))
    return out


def init_db(reset = False):
    try:
        client = InfluxDBClient(host='localhost', port='8086')
        client.switch_database(INFLUX_NAME)
        if reset:
            reset_db(client)
        return client
    except:
        print("COULD NOT CONNECT TO INFLUX. NO DATA WILL BE WRITTEN TO THE SERVER")
        return 0

def reset_db(client):
    client.drop_database(INFLUX_NAME)
    client.create_database(INFLUX_NAME)

def write_data_db(data, client, time):
    points = []
    for v in data:
        point = {
            "measurement": v.source,
            "tags": {
                #none
            },
            "time": time,
            "fields": {
                v.measurement: v.value,
            }
        }
        points.append(point)
    try:
        client.write_points(points)
    except:
        print("could not write to the influx server")
    return 0