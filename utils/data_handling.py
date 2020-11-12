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
#get_current_time() - interpolates and gets the current time (in seconds)
#update_time() - update the current time (in seconds)
class RelativeTime():
    def __init__(self):
        self.updated = time.time()
        self.time = 0

    def get_current_time(self):
        return time.time() - self.updated + self.time
    
    def update_time(self, new_time):
        self.time = new_time
        self.updated = time.time()