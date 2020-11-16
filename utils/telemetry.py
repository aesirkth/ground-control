from utils.serial_wrapper_file import SerialWrapper
from utils.data_handling import (Data, TimeSeries, RelativeTime)

import time
from threading import Thread

#functions to decode data, defined further down
decoding_functions = {}


####
#class to handle all telemetry things
####
#source can be "flight" or "engine"
#
#self.data[*source*] - contains all the decoded data in TimeSeries
#                       the source can be  either "flight" or "engine"
#self.clocks[*source*] - contains the ms_since_boot converted to seconds in a RelativeTime class
#
#stop() - stops the thread completely
#start() - opens or resumes and starts reading serial
#pause() - stops the thread from reading
class Telemetry():
    def __init__(self):
        self.read = False
        self.exit = False
        self.last_packet = 0
        self.ser = SerialWrapper("dummy")

        self.data = {}
        self.data["flight"] = {
            "altitude": TimeSeries(),
            "pressure": TimeSeries(),
            "acceleration": TimeSeries(),
            "gyrox": TimeSeries(),
            "gyroy": TimeSeries(),
            "gyroz": TimeSeries(),
            "ms_since_boot": TimeSeries()
        }
        self.data["engine"] = {
            "catastrophe": TimeSeries()
        }
        self.clocks = {
            "flight": RelativeTime(),
            "engine": RelativeTime() 
        }

        t = Thread(target = telemetry_thread, args = (self,))
        t.start()
    
    #False - not reading, 
    #True - initialized and reading
    def state(self):
        return self.read

    #stops the thread
    def stop(self):
        self.exit = True
    
    #pause the thread
    def pause(self):
        self.read = False
    
    #resume the thread
    def start(self):
        self.read = True


def telemetry_thread(tm):
    SEPARATOR = [0x0A, 0x0D]
    ser = tm.ser
    error= 1 #error variable for ser.openSerial()
    while error:
        #wait for user to start serial
        while not tm.read:
            time.sleep(1)
            if tm.exit:
                return

        #init serial wrapper
        error = ser.open_serial()
        if error:
            tm.read = False

    frameId = 0 #define before the loop so it remains in scope
    while not tm.exit:
        if not tm.read:
            time.sleep(1)
            continue
        
        #test for frame separator, read one byte at a time so it aligns itself
        if not (ser.read_bytes(1) == SEPARATOR[0] and
                ser.read_bytes(1) == SEPARATOR[1]):
            print("Invalid separator or no data. last ID: " + str(frameId))
            continue

        frameId = ser.read_bytes(1)
        data = decoding_functions[frameId](ser)
        source = data[0].source
        if data[0].measurement == "ms_since_boot":
            tm.clocks[source].update_time(data[0].value / 1000) # convert to seconds    
            
        else:
            for v in data:
                series = tm.data[v.source][v.measurement]
                series.x.append(tm.clocks[source].get_current_time())
                series.y.append(v.value)


#ms since boot engine controller
def f0x10(ser):
    value = ser.read_bytes(4)
    return [Data("engine", "ms_since_boot", value)]
decoding_functions[0x10] = f0x10

#μs since boot engine controller
def f0x11(ser):
    value = ser.read_bytes(8)
    return [Data("engine", "us_since_boot", value)]
decoding_functions[0x11] = f0x11

#ms since boot flight controller
def f0x90(ser):
    value = ser.read_bytes(4)
    return [Data("flight", "ms_since_boot", value)]
decoding_functions[0x90] = f0x90

#µs since boot flight controller
def f0x91(ser):
    value = ser.read_bytes(8)
    return [Data("flight", "us_since_boot", value)]
decoding_functions[0x91] = f0x91


####################### made up functions
#altitude
def f0x00(ser):
    value = ser.read_bytes(2)
    return [Data("flight", "altitude", value)]
decoding_functions[0x00] = f0x00

#acceleration
def f0x01(ser):
    value = ser.read_bytes(1)
    return [Data("flight", "acceleration", value)]
decoding_functions[0x01] = f0x01

#pressure
def f0x02(ser):
    value = ser.read_bytes(2)
    return [Data("flight", "pressure", value)]
decoding_functions[0x02] = f0x02

#catastrophe
def f0x03(ser):
    value = ser.read_bytes(1)
    return [Data("engine", "catastrophe", value)]
decoding_functions[0x03] = f0x03

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
decoding_functions[0x04] = f0x04