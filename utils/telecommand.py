from datetime import datetime
from threading import Thread

from utils.serial_wrapper import SerialReader
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
        super().__init__("telecommand", decoding_definitions, **kwargs)

    def __send_header(self, id):
        start = SEPARATOR
        self.ser.write(start.append(id))

    def __wait_for_data(self, source, name):
        data = self.data[source][name]
        promise = Promise()
        def thread():
            start_len = len(data.y)
            #wait 2 seconds before failing
            for i in range(20):
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
        if not self.state():
            # return a promise that always fails
            return self.__wait_for_data("engine", "nothing :(")
        self.__send_header(ID_SET_POWER_MODE_EC)
        return self.__wait_for_data("engine", "TBD")

    # set the engine state
    # abort - abort 
    # armed - set to armed
    # enabled - set to enabled
    def set_engine_state(self, abort, armed, enabled):
        if not self.state():
            # return a promise that always fails
            return self.__wait_for_data("engine", "nothing :(")
        out = abort > 0
        out += (armed > 0) * 2
        out += (enabled > 0) * 4
        self.__send_header(ID_SET_ENGINE_STATE_EC)
        self.ser.write(out)
        return self.__wait_for_data("engine", "TBD")

    # fire rocket
    def fire_rocket(self):
        if not self.state():
            # return a promise that always fails
            return self.__wait_for_data("engine", "nothing :(") 
        self.__send_header(ID_FIRE_ROCKET_EC)
        self.__wait_for_data("engine", "TBD")
        return self.__wait_for_data("engine", "TBD")
        
    # sends a time sync to the flight controller
    def time_sync(self,):
        if not self.state():
            # return a promise that always fails
            return self.__wait_for_data("engine", "nothing :(")
        now = datetime.now()
        time = now.strftime("%H%M%S%f")[:9]
        time_int = int(time)
        self.__send_header(ID_TIME_SYNC_FC)
        self.ser.write(time_int)
        return self.__wait_for_data("engine", "TBD")

    # set the power mode of the flight computer
    def set_flight_power_mode(self, TBD):
        if not self.state():
            # return a promise that always fails
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
        if not self.state():
            # return a promise that always fails
            return self.__wait_for_data("engine", "nothing :(")
        self.__send_header(ID_SET_RADIO_EQUIPMENT_FC)
        data = fpv
        data += 2 * (tm > 0)
        self.ser.write(data)
        return self.__wait_for_data("flight", "is_fpv_en")

    # set the parachutes
    # armed - arm the parachute
    # enable_1 - if parachute should be armed
    # enable_2 - if parachute should be armed
    # due to how the protocol is shaped the promise of the result doesn't
    # say if the command succeeded, use it for timing only
    def set_parachute(self, armed, enable_1, enable_2):
        if not self.state():
            # return a promise that always fails
            return self.__wait_for_data("engine", "nothing :(")
        self.__send_header(ID_SET_PARACHUTE_OUTPUT_FC)
        data = armed
        data += 2 * (enable_1 > 0)
        data += 4 * (enable_2 > 0)
        self.ser.write(data)
        return self.__wait_for_data("flight", "is_parachute_armed")


#decoding_definitions[ID_SOFTWARE_STATE_EC] = [Decoder("engine",
#decoding_definitions[ID_HARDWARE_STATE_EC] = [Decoder("engine",
#decoding_definitions[ID_RETURN_POWER_MODE_EC] = [Decoder("engine",

decoding_definitions[ID_RETURN_ENGINE_STATE_EC] = [BitDecoder(
    "engine", ["is_launch_aborted","is_engine_armed", "is_engine_en"])]

#decoding_definitions[ID_FIRE_ROCKET_CONFIRMATION_EC] = [Decoder("engine",


#decoding_definitions[ID_RETURN_POWER_MODE_FC] = todo

decoding_definitions[ID_RETURN_RADIO_EQUIPMENT_FC] = [BitDecoder(
    "flight", ["is_fpv_en", "is_tm_en"])]

decoding_definitions[ID_RETURN_PARACHUTE_OUTPUT_FC] = [BitDecoder(
    "flight", ["is_parachute_armed", "is_parachute1_en", "is_parachute2_en"])]

decoding_definitions[ID_ONBOARD_BATTERY_VOLTAGE_FC] = MultiDecoder(
    "flight", "<I", "battery", 1, 2, 0.01)

decoding_definitions[ID_GNSS_DATA_FC] = [
    Decoder("flight", "<I", "gnss_time"),
    Decoder("flight", "<I", "latitude"),
    Decoder("flight", "<I", "longitude"),
    Decoder("flight", "<S", "h_dop", 0.01)
]

decoding_definitions[ID_FLIGHT_CONTROLLER_STATUS_FC] = [
    Decoder("flight", "<c", "HW_state"),
    Decoder("flight", "<c", "SW_state"),
    Decoder("flight", "<c", "mission_state")
]






















tc = Telecommand()
tc.open_serial()

promise = tc.fire_rocket()

#result will be True if it got a response and False if it didn't
def update(result):
    if not result:
        print("got no response")
        return
    
    #to actually get the response you have will have to check under data and get the most recent value
    #on the bottom of utils/telecommand.py you can find the decoders for everything, the last string is always the name it will be saved as
    #i usually try to follow the protocol
    reply = tc.data["engine"]["has_launched"].get_last()
    if reply:
        print("rocket has launched!")
        launch_widget.set_color("green")
    else:
        print("rocket didn't launch for some reason")
        launch_widget.set_color("red")

promise.then(update)




tc.set_parachute(True, True, False).then(update2)

def update2(result):
    if not result:
        print("got no response")
        return

    tm_radio_widget.state = tc.data["flight"]["is_tm_en"].get_last()
    fpv_radio_widget.state = tc.data["flight"]["is_fpv_en"].get_last()