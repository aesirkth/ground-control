from utils.serial_wrapper_file import SerialWrapper
from utils.data_handling import *
from utils.definitions import *

import struct

import time
from threading import Thread

#functions to decode data, defined further down
decoding_definitions = {}

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
#start() - opens and starts reading serial
#pause() - stops the thread from reading
#resume() - resumes the thread
#state() - if the link is open
class Telemetry():
    def __init__(self):
        self.read = True
        self.exit = False
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
    
   #stops the thread
    def stop(self):
        self.exit = True

    #if the gateway is currently reading
    def state(self):
        return self.ser.port_is_open()
    
    #pause the thread
    def pause(self):
        self.read = False
    
    def resume(self):
        self.read = True

    #start and open serial
    def start(self):
        self.ser.open_serial()


def telemetry_thread(tm):
    ser = tm.ser
    
    #wait for user to start serial
    while not tm.state():
        time.sleep(1)
        if tm.exit:
            return

    frameId = 0 #define before the loop so it remains in scope
    while not tm.exit:
        if not tm.read:
            time.sleep(1)
            continue
        
        #test for frame separator, read one byte at a time so it aligns itself
        if not (ser.read_int(1) == SEPARATOR[0] and
                ser.read_int(1) == SEPARATOR[1]):
            print("telemetry: Invalid separator or no data. last ID: " + str(frameId))
            continue
        frame_id_old = frameId
        frame_id = ser.read_int(1)

        if frame_id not in decoding_definitions.keys():
            print("telemetry: Invalid ID: " + str(frame_id))
            print("telemetry: last valid ID: " + str(frame_id_old))
            continue
 
        decoders = decoding_definitions[frame_id]
        data = []
        for v in decoders:
            data += v.decode(ser)

        source = data[0].source
        if data[0].measurement == "ms_since_boot":
            tm.clocks[source].update_time(data[0].value / 1000) # convert to seconds    
        else:
            for v in data:
                series = tm.data[v.source][v.measurement]
                series.x.append(tm.clocks[source].get_current_time())
                series.y.append(v.value)


#all names are taken from the data protocol other than the following
#gyro_x --> IMU1_gyro_x and IMU2_gyro_x e.t.c
#temperature_1 --> temp_inside_1 and temp_outside_1 e.t.c.
#(air_speed) calculated --> air_speed

decoding_definitions[ID_MS_SINCE_BOOT_FC] = [
    Decoder("flight", "<I", "ms_since_boot")]
decoding_definitions[ID_US_SINCE_BOOT_FC] = [
    Decoder("flight", "<Q", "us_since_boot")]
decoding_definitions[ID_GNSS_DATA_1_FC] = [
    Decoder("flight", "<Q", "gnss_time"),
    Decoder("flight", "<I", "latitude"),
    Decoder("flight", "<I", "longitude")
]
decoding_definitions[ID_GNSS_DATA_2_FC] = [
    Decoder("flight", "<I", "altitude", 0.1),
    Decoder("flight", "<S", "heading"),
    Decoder("flight", "<S", "horiz_speed", 0.1),
    Decoder("flight", "<B", "fix_status"),
    Decoder("flight", "<B", "n_satellites"),
    Decoder("flight", "<S", "h_dop", 0.1)
]
decoding_definitions[ID_INSIDE_TEMPERATURE_FC] = (
    MultiDecoder("flight", "<I", "temp_inside_", 1, 2, 0.01))
decoding_definitions[ID_INSIDE_PRESSURE_FC] = (
    MultiDecoder("flight", "<I", "pressure_", 1, 2, 0.01))
decoding_definitions[ID_IMU_1_FC] = (
    xyzDecoder("flight", "<S", "IMU1_accel_") +
    xyzDecoder("flight", "<S", "IMU1_gyro_") +
    xyzDecoder("flight", "<S", "IMU1_magnet_")
)
decoding_definitions[ID_IMU_2_FC] = (
    xyzDecoder("flight", "<S", "IMU2_accel_") +
    xyzDecoder("flight", "<S", "IMU2_gyro_") +
    xyzDecoder("flight", "<S", "IMU2_magnet_")
)
decoding_definitions[ID_EXTERNAL_TEMPERATURE_FC] = (
    MultiDecoder("flight", "<S", "temp_outside_", 1, 2))
decoding_definitions[ID_AIR_SPEED_FC] = [
    Decoder("flight", "<S", "pitot"),
    Decoder("flight", "<S", "air_speed")
]
decoding_definitions[ID_ONBOARD_BATTERY_VOLTAGE_TM_FC] = (
    MultiDecoder("flight", "<S", "battery_", 1, 2, 0.01),
)
decoding_definitions[ID_FLIGHT_CONTROLLER_STATUS_TM_FC] = (
    BitDecoder("flight", [
        "is_parachute_armed",
        "is_parachute_1_en",
        "is_parachute_2_en",
        "is_fpv_en",
        "is_telemetry_en"
    ]) +
    BitDecoder("flight", [
        #todo, software state
    ]) +
    BitDecoder("flight", [
        #todo. mission state
    ])
)

"""
decoding_definitions[0x10] = [Decoder("engine", "<L", "ms_since_boot")]
decoding_definitions[0x11] = [Decoder("engine", "<Q", "us_since_boot")]
decoding_definitions[0x90] = [Decoder("flight", "<L", "ms_since_boot")]
decoding_definitions[0x91] = [Decoder("flight", "<Q", "us_since_boot")]

####################### made up functions
decoding_definitions[0x00] = [Decoder("flight", "<H", "altitude")]
decoding_definitions[0x01] = [Decoder("flight", "<B", "acceleration")]
decoding_definitions[0x02] = [Decoder("flight", "<H", "pressure")]
decoding_definitions[0x03] = [BitDecoder("engine", ["catastrophe"])]
decoding_definitions[0x04] = xyzDecoder("flight", "<B", "gyro")
"""