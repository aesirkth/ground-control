from utils.serial_wrapper import SerialWrapper
from utils.data_functions import (telemetry_functions, Data,
                                  TimeSeries, RelativeTime)

import time
from threading import Thread

####
#class to handle all telemetry things
####
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
    ser = SerialWrapper("dummy")
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
            print("could not open serial connection")
            print("The microcontroller needs to be reset after every run. Try unplugging it.")
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
        data = telemetry_functions[frameId](ser)
        source = data[0].source
        if data[0].measurement == "ms_since_boot":
            tm.clocks[source].update_time(data[0].value / 1000) # convert to seconds    
            
        else:
            for v in data:
                series = tm.data[v.source][v.measurement]
                series.x.append(tm.clocks[source].get_current_time())
                series.y.append(v.value)
