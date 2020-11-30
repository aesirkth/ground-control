import bitstruct as bs
from datetime import datetime
import time
from threading import Thread

from utils.serial_wrapper import SerialWrapper
from utils.data_handling import *
from utils.definitions import *


#used further down
decoding_definitions = {}

####
#class to handle the telecommand link
####
#source can be "flight" or "engine"
#
#self.data[*source*] - contains all the decoded data in TimeSeries
#                       the source can be  either "flight" or "engine"
#self.clocks[*source*] - contains the ms_since_boot converted to seconds in a RelativeTime class
#
#stop() - stops the thread completely
#start() - opens and starts reading serial
#pause() - stops the thread from reading
#resume() - resumes the thread
#state() - if the link is open
#
##
#none of the functions below will return a value.
#Instead they will get an update pushed to the data dictionary
#see the flight controller documentation for the names and sources
##
#set_engine_power_mode(self, TBD)
#set_engine_state(self, abort, armed, enabled)
#fire_rocket(self)
#time_sync(self)
#set_flight_power_mode(self, TBD)
#set_radio_emitters(self, fpv, tm)
#set_parachute(self, armed, enable_1, enable_2)
class Telecommand():
    def __init__(self):
        self.data = {}
        self.read = True
        self.exit = False
        self.ser = SerialWrapper("telecommand")

        self.data = {}
        self.data["flight"] = {
            "is_parachute_armed": TimeSeries(),
            "is_parachute1_en": TimeSeries(),
            "is_parachute2_en": TimeSeries(),
            "voltage_battery1": TimeSeries(),
            "voltage_battery2": TimeSeries()
        }
        self.data["engine"] = {
            "catastrophe": TimeSeries()
        }
        self.clocks = {
            "flight": RelativeTime(),
            "engine": RelativeTime() 
        }
        t = Thread(target = telecommand_link_thread, args = (self,))
        t.start()

    def __send_header(self, id):
        start = SEPARATOR
        self.ser.write(start.append(id))

    def __wait_for_LoRa_data(self, id):
        pass

    #start and open serial
    def start(self):
        return self.ser.open_serial()

    #stops the thread
    def stop(self):
        self.exit = True

    #if the gateway is currently open
    def state(self):
        return self.ser.port_is_open()
    
    #pause reading
    def pause(self):
        self.read = False
    
    #resume reading
    def resume(self):
        self.read = True
    
    #set the engine power mode
    def set_engine_power_mode(self, TBD):
        if not self.state():
            return -1
        self.__send_header(ID_SET_POWER_MODE_EC)

    #set the engine state
    #abort - abort 
    #armed - set to armed
    #enabled - set to enabled
    def set_engine_state(self, abort, armed, enabled):
        if not self.state():
            return -1
        out = abort > 0
        out += (armed > 0) * 2
        out += (enabled > 0) * 4
        self.__send_header(ID_SET_ENGINE_STATE_EC)
        self.ser.write(out)

    #fire rocket
    def fire_rocket(self):
        if not self.state():
            return -1
        self.__send_header(ID_FIRE_ROCKET_EC)

    #sends a time sync to the flight controller
    def time_sync(self,):
        if not self.state():
            return -1
        now = datetime.now()
        time = now.strftime("%H%M%S%f")[:9]
        time_int = int(time)
        self.__send_header(ID_TIME_SYNC_FC)
        self.ser.write(time_int)

    #set the power mode of the flight computer
    def set_flight_power_mode(self, TBD):
        if not self.state():
            return -1
        self.__send_header(ID_SET_POWER_MODE_FC)
        #TBD

    #turn on/off radio transmitters
    #fpv - live video-feed
    #tm - telemetry
    def set_radio_emitters(self, fpv, tm):
        if not self.state():
            return -1
        self.__send_header(ID_SET_RADIO_EQUIPMENT_FC)
        data = fpv
        data += 2 * (tm > 0)
        self.ser.write(data)

    #set the parachutes
    #armed - arm the parachute
    #enable_1 - if parachute should be armed
    #enable_2 - if parachute should be armed
    def set_parachute(self, armed, enable_1, enable_2):
        if not self.state():
            return -1
        self.__send_header(ID_SET_PARACHUTE_OUTPUT_FC)
        data = armed
        data += 2 * (enable_1 > 0)
        data += 4 * (enable_2 > 0)
        self.ser.write(data)


def telecommand_link_thread(tcl):
    ser = tcl.ser
    
    #wait for user to start serial
    while not tcl.state():
        time.sleep(1)
        if tcl.exit:
            return

    frameId = 0 #define before the loop so it remains in scope
    while not tcl.exit:
        if not tcl.read:
            time.sleep(1)
            continue
        
        #test for frame separator, read one byte at a time so it aligns itself
        if not (ser.read_int(1) == SEPARATOR[0] and
                ser.read_int(1) == SEPARATOR[1]):
            print("telecommand_link: Invalid separator or no data. last ID: " + str(frameId))
            continue

        frameId = ser.read_int(1)

        if frameId not in decoding_definitions.keys():
            print("telecommand_link: Invalid ID: " + str(frameId))
            continue
 
        decoders = decoding_definitions[frameId]
        data = []
        for v in decoders:
            data += v.decode(ser)

        source = data[0].source
        if data[0].measurement == "ms_since_boot":
            tcl.clocks[source].update_time(data[0].value / 1000) # convert to seconds    
        else:
            for v in data:
                series = tcl.data[v.source][v.measurement]
                series.x.append(tcl.clocks[source].get_current_time())
                series.y.append(v.value)



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
    Decoder("flight", "<", "HW_state"),
    Decoder("flight", "<", "SW_state"),
    Decoder("flight", "<", "mission_state")
]