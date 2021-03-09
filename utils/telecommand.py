import datetime
from threading import Thread

from utils.serial_reader import SerialReader
from utils.data_handling import *
from utils.definitions import *
from collections import defaultdict

#used further down
decoding_definitions = {}

####
# class to handle the telecommand link
####
# source can be "flight" or "engine"
#
# self.data[*source*] - contains all the decoded data in TimeSeries
#                       the source can be  either "flight" or "engine"
# self.clocks[*source*] - contains the ms_since_boot converted to seconds in a RelativeTime class
# source can be "engine" or "flight"
# 
##
# none of the functions below will return a value.
# Instead they will get an update pushed to the data dictionary
# see the flight controller documentation for the names and sources
##
# set_engine_power_mode(self, TBD)
# set_engine_state(self, abort, armed, enabled)
# fire_rocket(self)
# time_sync(self)
# set_flight_power_mode(self, TBD)
# set_radio_emitters(self, fpv, tm)
# set_parachute(self, armed, enable_1, enable_2)
class Telecommand(SerialReader):
    def __init__(self, **kwargs):
        super().__init__(device = "flight_controller", **kwargs)

    def __send_header(self, id):
        self.ser.write(bytes(SEPARATOR + [id]))

    def __wait_for_data(self, source, name):
        data = self.data[source][name]
        promise = Promise()
        if self.serial_is_active:
            tries = 50
        else:
            tries = 1
        def thread():
            start_len = len(data.y)
            #wait 5 seconds before failing
            for i in range(tries):
                time.sleep(0.1)
                if start_len != len(data.y):
                    promise.resolve(True)
                    break
            else:
                promise.resolve(False)
        t = Thread(target = thread)
        t.start()
        return promise

    # set the engine power mode
    def set_engine_power_mode(self, TBD):
        if not self.is_serial_open():
            # return a promise that always fails
            return self.__wait_for_data("engine", "nothing :(")
        return self.__wait_for_data("engine", "nothing :(")
        self.__send_header(ID_SET_POWER_MODE_EC)
        return self.__wait_for_data("engine", "TBD")

    # set the engine state
    # abort - abort 
    # armed - set to armed
    # enabled - set to enabled
    def set_engine_state(self, abort, armed, enabled):
        if not self.is_serial_open():
            # return a promise that always fails
            return self.__wait_for_data("engine", "nothing :(")
        return self.__wait_for_data("engine", "nothing :(")
        out = abort > 0
        out += (armed > 0) * 2
        out += (enabled > 0) * 4
        self.__send_header(ID_SET_ENGINE_STATE_EC)
        self.ser.write(bytes([out]))
        return self.__wait_for_data("engine", "TBD")

    # fire rocket
    def fire_rocket(self):
        if not self.is_serial_open():
            # return a promise that always fails
            return self.__wait_for_data("engine", "nothing :(") 
        return self.__wait_for_data("engine", "nothing :(")
        self.__send_header(ID_FIRE_ROCKET_EC)
        self.__wait_for_data("engine", "TBD")
        return self.__wait_for_data("engine", "TBD")
        
    # sends a time sync to the flight controller
    def time_sync(self,):
        if not self.is_serial_open():
            # return a promise that always fails
            return self.__wait_for_data("engine", "nothing :(")
        now = datetime.datetime.now()
        time = now.strftime("%H%M%S%f")[:9]
        time = int(time)
        buf = [0 for x in range(4)]
        buf[0] = time & 255
        buf[1] = (time >> 8)  & 255
        buf[2] = (time >> 16) & 255
        buf[3] = (time >> 24) & 255
        self.__send_header(ID_TIME_SYNC_FC)
        self.ser.write(bytes(buf))
        return self.__wait_for_data("flight", "time_sync")
    
    # send a handshake
    def handshake(self):
        self.__send_header(ID_HANDSHAKE)

    # set the power mode of the flight computer
    def set_flight_power_mode(self, TBD):
        if not self.is_serial_open():
            # return a promise that always fails
            return self.__wait_for_data("engine", "nothing :(")
        return self.__wait_for_data("engine", "nothing :(")
        self.__send_header(ID_SET_POWER_MODE_FC)
        return self.__wait_for_data("flight", "TBD")
        #TBD

    # turn on/off radio transmitters
    # fpv - live video-feed
    # tm - telemetry
    # due to how the protocol is shaped the promise of the result doesn't
    # say if the command succeeded, use it for timing only
    def set_radio_emitters(self, fpv, tm):
        if not self.is_serial_open():
            # return a promise that always fails
            return self.__wait_for_data("engine", "nothing :(")
        self.__send_header(ID_SET_RADIO_EQUIPMENT_FC)
        data = fpv
        data += 2 * (tm > 0)
        self.ser.write(bytes([data]))
        return self.__wait_for_data("flight", "is_fpv_en")

    # set the parachutes
    # armed - arm the parachute
    # enable_1 - if parachute should be armed
    # enable_2 - if parachute should be armed
    # due to how the protocol is shaped the promise of the result doesn't
    # say if the command succeeded, use it for timing only
    def set_parachute(self, armed, enable_1, enable_2):
        if not self.is_serial_open():
            # return a promise that always fails
            return self.__wait_for_data("engine", "nothing :(")
        self.__send_header(ID_SET_PARACHUTE_OUTPUT_FC)
        data = armed
        data += 2 * (enable_1 > 0)
        data += 4 * (enable_2 > 0)
        self.ser.write(bytes([data]))
        return self.__wait_for_data("flight", "is_parachute_armed")

    def set_data_logging(self, logging_enabled):
        if not self.is_serial_open():
            # return a promise that always fails
            return self.__wait_for_data("engine", "nothing :(")
        self.__send_header(ID_SET_DATA_LOGGING)
        self.ser.write(logging_enabled)
        return self.__wait_for_data("flight", "is_logging_en")
    
    def save_data_to_sd(self):
        if not self.is_serial_open():
            # return a promise that always fails
            return self.__wait_for_data("engine", "nothing :(")
        self.__send_header(ID_SET_DUMP_FLASH)
        self.ser.write(bytes([1]))
        return self.__wait_for_data("flight", "dump_sd")