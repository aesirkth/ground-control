#data_handling.py
#contains classes to parse and store data
#also contains the functions for inluxdb 

import time
import datetime
import struct
from utils.definitions import *
from influxdb import InfluxDBClient
import json

# class to store Data
#############
# source - the source of the data e.g. "flight" for flight controller
#         or "engine" for the engine controller
# measurement - What the value means e.g. "pressure" or "altitude"
# value - the value of the measurement e.g. 10 or 3
class Data:
    def __init__(self, tree_pos, value):
        self.tree_pos = tree_pos
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


######
#class to decode numbers
##
# init(tree_pos, type, **min, **max, **scale)
# packaging - the type
# measurement - the measurement that is encoded
# min - optional, the min value
# max - optional, the max value
# scale - multiply the number with this 
#
# get_size() - gets the size of the datatype
# decode(ser) - reads and decodes the data. returns an array with Data classess
class NumDecoder():
    def __init__(self, tree_pos, type, *args, min = 0, max = 0, scale = 1):
        self.tree_pos = tree_pos
        self.max = max
        self.min = min
        self.scale = scale
        type_to_format = {
            "int8": "b",
            "uint8": "B",
            "int16": "h",
            "uint16": "H",
            "int32": "l",
            "uint32": "L",
            "int64": "q",
            "uint64": "Q",
        }
        if len(type) > 1:
            self.packaging = "<" + type_to_format[type]
        else:
            self.packaging = "<" + type
        
    def get_size(self):
        return struct.calcsize(self.packaging)
    
    def decode(self, buf):
        data = struct.unpack(self.packaging, buf)
        val = data[0]
        if self.max or self.min:
            intmax = 2 << (size * 8) - 1
            if(val <= 0):
                return self.min - 1.0
            if(val >= intmax):
                return self.max + 1.0
            ratio = (val - self.min) / (self.max - self.min)
            val =  1 + ((intmax - 2)) * ratio            
        if self.scale:
            val *= self.scale
        return [Data(self.tree_pos, val)]


######
#class to decode enums
######
# init(tree_pos, enum)
# tree_pos - where data should be stored 
# enum - the enum to decode
#
# get_size() - gets the size of the datatype
# decode(buf) - decodes the buffer. returns an array with Data classess
class EnumDecoder():
    def __init__(self, tree_pos, enum):
        self.tree_pos = tree_pos
        self.enum = {}
        #invert the enum
        for key in enum.keys():
            value = enum[key]
            self.enum[value] = key

    def get_size(self):
        return 1 #assume uint8

    def decode(self, buf):
        return [Data(self.tree_pos, self.enum[bytes[0]])]


######
#class to decode empty datatypes
##
# init(tree_pos)
# tree_pos - where the data should be stored 
#
# get_size() - gets the size of the datatype
# decode(buf) - decodes the buffer. returns an array with Data classes
class EmptyDecoder():
    def __init__(self, tree_pos):
        self.tree_pos = tree_pos
    
    def get_size(self):
        return 0
    
    def decode(self, buf):
        return [Data(self.tree_pos, 1)]


######
#class to decode bits
##
# init(tree_pos)
# tree_pos - where the data should be stored 
#
# get_size() - gets the size of the datatype
# decode(buf) - decodes the buffer. returns an array with Data classes
class BitDecoder():
    def __init__(self, tree_path, positions):
        self.tree_path = tree_path
        self.positions = positions

    def get_size(self):
        return 1
    
    def decode(self, buf):
        out = []
        count = 0
        for bit in self.positions:
            value = buf[0] & (1 << count)
            count += 1
            data = Data(self.tree_path + [bit], value)
            out.append(data)
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
    def __init__(self, size, func):
        self.decode = func
        self.size = size

    def get_size(self):
        return self.size


#gets the current time in hhmmss.sss format
def get_current_time():
    now = datetime.datetime.now()
    time = now.strftime("%H%M%S%f")[:9]
    return int(time)

def get_current_time_sec():
    raw = get_current_time()
    return formatted_time_to_sec(raw)

#converts hhmmss.sss to seconds since 00:00
def formatted_time_to_sec(time):
    seconds = 0
    formatted = str(time)
    formatted = '0' * (9 - len(formatted)) + formatted
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

# returns 3 decoders with their names concatenated with x y and z
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