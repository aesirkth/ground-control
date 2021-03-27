import datetime
from threading import Thread
import time
from utils.serial_reader import SerialReader
from utils.data_handling import *
from utils.definitions import *
from collections import defaultdict
import utils.fc as protocol


####
# class to handle the telecommand link
####
# source can be "flight" or "engine"
#
# self.data[*source*] - contains all the decoded data in TimeSeries
#                       the source can be  either "flight" or "engine"
# 
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

    def __wait_for_data(self, source, datatype, field):
        data = self.data[source][datatype][field]
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

    def __send_message(self, msg):
        self.__send_header(msg.get_id())
        self.ser.write(msg.get_buf())

    # set the engine power mode
    def set_engine_power_mode(self, TBD):
        if not self.is_serial_open():
            # return a promise that always fails
            return self.__wait_for_data("nothing", " ", " ")
        return self.__wait_for_data("engine","TBD", "TBD")

    # set the engine state
    # abort - abort 
    # armed - set to armed
    # enabled - set to enabled
    def set_engine_state(self, abort, armed, enabled):
        if not self.is_serial_open():
            # return a promise that always fails
            return self.__wait_for_data("nothing", " ", " ")
        return self.__wait_for_data("engine", "TBD", "TBD")

    # fire rocket
    def fire_rocket(self):
        if not self.is_serial_open():
            # return a promise that always fails
            return self.__wait_for_data("nothing", " ", " ") 
        return self.__wait_for_data("engine", "TBD", "TBD")
        
    # sends a time sync to the flight controller
    def time_sync(self,):
        if not self.is_serial_open():
            # return a promise that always fails
            return self.__wait_for_data("nothing", " ", " ")
        now = datetime.datetime.now()
        time = now.strftime("%H%M%S%f")[:9]
        time = int(time)
        msg = protocol.time_sync_from_ground_station_to_flight_controller_tc()
        msg.set_system_time(time)
        self.__send_message(msg)
        return self.__wait_for_data("flight", "return_time_sync", "value")

    # set the power mode of the flight computer
    def set_flight_power_mode(self, TBD):
        if not self.is_serial_open():
            # return a promise that always fails
            return self.__wait_for_data("nothing", " ", " ")
        return self.__wait_for_data("flight", "TBD", "TBD")
        #TBD

    # turn on/off radio transmitters
    # fpv - live video-feed
    # tm - telemetry
    # due to how the protocol is shaped the promise of the result doesn't
    # say if the command succeeded, use it for timing only
    def set_radio_emitters(self, fpv, tm):
        if not self.is_serial_open():
            # return a promise that always fails
            return self.__wait_for_data("nothing", " ", " ")
        msg = protocol.set_radio_equipment_from_ground_station_to_flight_controller_tc()
        msg.set_is_fpv_en(fpv)
        msg.set_is_tm_en(tm)
        self.__send_message(msg)
        return self.__wait_for_data("flight", "return_radio_equipment", "is_fpv_en")

    # set the parachutes
    # armed - arm the parachute
    # enable_1 - if parachute should be armed
    # enable_2 - if parachute should be armed
    # due to how the protocol is shaped the promise of the result doesn't
    # say if the command succeeded, use it for timing only
    def set_parachute(self, armed, enable_1, enable_2):
        if not self.is_serial_open():
            # return a promise that always fails
            return self.__wait_for_data("nothing", " ", " ")
        msg = protocol.set_parachute_output_from_ground_station_to_flight_controller_tc()
        msg.set_is_parachute_armed(armed)
        msg.set_is_parachute1_en(enable_1)
        msg.set_is_parachute2_en(enable_2)
        self.__send_message(msg)
        return self.__wait_for_data("flight", "return_parachute_status", "is_parachute_armed")

    def set_data_logging(self, logging_enabled):
        if not self.is_serial_open():
            # return a promise that always fails
            return self.__wait_for_data("nothing", " ", " ")
        msg = protocol.set_data_logging_from_ground_station_to_flight_controller_tc()
        msg.set_is_logging_en(logging_enabled)
        self.__send_message(msg)
        return self.__wait_for_data("flight", "data_logging", "is_logging_en")
    
    def save_data_to_sd(self):
        if not self.is_serial_open():
            # return a promise that always fails
            return self.__wait_for_data("nothing", " ", " ")
        msg = protocol.dump_flash_from_ground_station_to_flight_controller_tc()
        msg.set_dump_sd(True)
        self.__send_message(msg)
        return self.__wait_for_data("flight","return_dump_flash", "dump_sd")