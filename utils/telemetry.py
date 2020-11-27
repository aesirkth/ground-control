from utils.serial_wrapper_file import SerialWrapper
from utils.data_handling import (Data, TimeSeries, RelativeTime, 
                                 Decoder, BitDecoder, CustomDecoder)
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
    SEPARATOR = [0x0A, 0x0D]
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

decoding_definitions[0x10] = [Decoder("engine", "<L", "ms_since_boot")]
decoding_definitions[0x11] = [Decoder("engine", "<Q", "us_since_boot")]
decoding_definitions[0x90] = [Decoder("flight", "<L", "ms_since_boot")]
decoding_definitions[0x91] = [Decoder("flight", "<Q", "us_since_boot")]

####################### made up functions
decoding_definitions[0x00] = [Decoder("flight", "<H", "altitude")]
decoding_definitions[0x01] = [Decoder("flight", "<B", "acceleration")]
decoding_definitions[0x02] = [Decoder("flight", "<H", "pressure")]
decoding_definitions[0x03] = [BitDecoder("engine", ["catastrophe"])]
decoding_definitions[0x04] = [
    Decoder("flight", "<B", "gyrox"),
    Decoder("flight", "<B", "gyroy"),
    Decoder("flight", "<B", "gyroz")
]