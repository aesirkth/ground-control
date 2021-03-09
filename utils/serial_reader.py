import serial 
import serial.tools.list_ports
from datetime import datetime
import os
import sys
import time
from threading import Thread
from collections import defaultdict
import json

from utils.definitions import *
from utils.data_handling import (TimeSeries, write_data_db, get_current_time,
    formatted_time_to_sec, get_current_time_sec, NumDecoder, EnumDecoder,
    BitDecoder, EmptyDecoder)

LIVE = 0
BACKUP_TIMESTAMP = 1
FLASH_TIMESTAMP = 2

#contains all the decdoders defined on the bottom
decoding_definitions = {}

####
#a wrapper around the Serial class. It backups all communication to the ./data/ 
#directory. It can also find and open a connection to a device 
###
#init(device)
#   device can be, "gateway", "flight_controller", "RFD"
#
#write(*args) - copy of pyserial's write
#read(*args) - copy of pyserial's read
#open_serial() - open the serial connection
class SerialWrapper():
    def __init__(self, device):
        self.ser = serial.Serial()
        self.device = device
        #get file name
        now = datetime.now()
        time = now.strftime("%Y-%m-%d-%H-%M-%S")
        file_name = device + "-" + time
        #create file and directory
        try:
            dir_name = "data/" 
            os.mkdir(dir_name)
        except:
            pass
        try:
            self.backup = open(dir_name + file_name, "w+b")
        except:
            print("could not create the file: " + dir_name + file_name)
            sys.exit()

    #copy of the pyserial write with added backup
    def write(self, *args):
        self.backup.write(*args)
        self.ser.write(*args)

    #copy of the pyserial read with added backup
    def read(self, *args):
        buf = self.ser.read(*args)
        self.backup.write(buf)
        return buf

    #gets a list with all ports
    def get_safe_devices(self):
        safeStrings = [
            "usb",
            "arduino",
            "ch340"
        ]
        safe_devices = []
        devices = serial.tools.list_ports.comports()
        for d in devices:
            flag = False
            for substring in safeStrings:
                if substring in d.description.lower():
                    flag = True
            if flag:
                safe_devices.append(d)
        return safe_devices

    #returns true or false if a port contatins a device
    def init_device(self):
        if self.device == "RFD":
            # RFD needs 1 seconds of inactivity to eneter AT mode
            time.sleep(1) 
            self.ser.write(b'+++') # enter AT mode
            time.sleep(1) # wait for data 
            buff = self.ser.read_all()
            self.write(b'ATO\r') # exit AT mode
            return b'OK' in buff
        elif self.device == "gateway":
            bonjour = b"LAUNCHPADCONTROLLER" 
            self.ser.write(b'&gB0')
            time.sleep(1)
            buff = self.ser.read_all()
            return bonjour in buff
        elif self.device == "flight_controller":
            handshake = bytes(SEPARATOR + [ID_HANDSHAKE]) 
            response = bytes(SEPARATOR + [ID_RETURN_HANDSHAKE])
            self.ser.write(handshake)
            time.sleep(5)
            buff = self.ser.read_all()
            return response in buff
        else:
            return False
    
    #timestamp the backupfile
    def timestamp(self, time):
        msg = []
        msg += [ID_LOCAL_TIMESTAMP]
        buf = [0 for x in range(4)]
        buf[0] = time & 255
        buf[1] = (time >> 8)  & 255
        buf[2] = (time >> 16) & 255
        buf[3] = (time >> 24) & 255
        msg += buf
        msg += SEPARATOR
        self.backup.write(bytes(msg))

    #start and open serial
    def open_serial(self):
        baudrates ={
            "gateway": 115200,
            "RFD": 57600,
            "flight_controller": 115200
        }
        self.ser.baudrate = baudrates[self.device]

        ports = self.get_safe_devices()
        for v in ports:
            self.ser.port = v.device
            self.ser.open()
            print(self.device + ": Testing " + str(v))
            if self.init_device():
                print(self.device + ": Succesfully connected")
                return True
            print(self.device + ": Did not respond")
            self.ser.close()
        else:
            print(self.device + ": opening serial failed")
            return False    

#####
#spawns a thread that reads and parses data from a stream.
###
#init(self, *args, influx = False, device = "None")
#   influx is the influx client to write to
#   device is the SerialWrapper device
#
#stop() - stops the reading thread
#pause() - pauses the reader thread
#resume() - resumes the reader thread
#redirect_data() - overwrite the data array to e.g. combine the output from two readers
#serial_is_active() - if the serial connection is open
#serial_is_active() - if a readable connection is open
#open_backup_file(path) - open a file created by this very program
#open_flash_file(path) - open a file dumped from the flash drive
#open_serial() - open a serial connection
#seconds_since_last_message() - get the time since the last message
class SerialReader():
    def __init__(self, *args, influx = False, device = "None"):
        self.influx = influx
        self.device = device
        #stream is for reading
        #serial is for writing
        self.serial_is_active = False
        self.stream_is_active = False
        self.ser = None
        self.stream = None
        self.client = False
        self.last_message_time = LIVE
        self.last_timestamp = 0
        self.time_sync_state = 0
        self.start_time = None
        self.pause = False
        self.exit = False
        self.decoders = decoding_definitions
        #use defaultdict to let the front-end use uninitialized data
        self.data = defaultdict(lambda: defaultdict(TimeSeries))

        t = Thread(target = self.reader_thread)
        t.start()

    #stops the thread
    def stop(self):
        self.exit = True

    #if the serial port is open
    def is_serial_open(self):
        return self.ser_is_active
    
    #if the is reading either from file or serial
    def is_serial_open(self):
        return self.stream_is_active

    #pause the reader thread
    def pause(self):
        self.paused = True
    
    #resume the reader thread
    def resume(self):
        self.paused = False    

    #tell the class to write into another data dict
    def redirect_data(self, data):
        self.data = data

    #opens a file that has been saved from this very program
    def open_backup_file(self, path):
        self.time_sync_state = BACKUP_TIMESTAMP
        self.start_time = None 
        self.stream = open(path, "r+b")
        self.stream_is_active = True

    #opens a file dumped from the flash chip
    def open_flash_file(self, path):
        self.time_sync_state = FLASH_TIMESTAMP
        self.start_time = None
        self.stream = open(path, "r+b")
        self.stream_is_active = True

    #opens the serial connection
    def open_serial(self):
        self.time_sync_state = LIVE
        self.ser = SerialWrapper(self.device)
        result = self.ser.open_serial()
        if result:
            self.serial_is_active = True
            self.stream = self.ser
            self.stream_is_active = True
            return True
        return False

    #gets the seconds since the last message
    def seconds_since_last_message(self):
        return time.time() - self.last_message_time

    #TODO: parse the engine protocol in utils/edda_messages.json
    # The goal is to assign decoders to each ID based on the protocol in the json file
    # each decoder takes care of a single field.
    # self.decoders is a dictionary that contains arrays with decoders corresponding to all data fields for every id.
    # see the bottom of this file for examples 
    #
    # The json object has 3 sub-objects; messages, datatypes and enums
    # "messages" contains IDs and their datatypes
    # "dataypes" contains all the fields for a specific datatype like uint32, enum and packedfloat
    # "enums" contains all the enums
    ##
    # Decoders are defined in data_handling.py
    ##
    # all Decoders take tree_pos as an argument. Tree_pos is an array that specifies
    # where the data will be saved e.g. ["flight", "gyrox"] will be saved in self.data["flight"]["gyrox"]
    # ["Edda Pressure (top)", "PowerInputMeasurement", "current_amperes"] --> self.data["Edda Pressure (top)"]["PowerInputMeasurement"]["current_amperes"]
    #
    # generally it should have this form
    # [*sender name*][*message name*][*field name*]
    # sometimes the message and field name is the same but that's fine, just ignore it and have them repeat
    ###
    # NumDecoder(tree_pos, type, **min, **max, **scale)
    # can decode both integers and packed floats
    # to unpack a float specify "min=" and "max="
    # the type it takes is just the native or packedtype so "uint16" or "int8"
    # "scale=" is not used for the json protocol
    ###
    # EnumDecoder(tree_pos, enum)
    # using the code below; enum would be just be enums[*enum name*] directly
    ###
    # EmptyDecoder(tree_pos)
    # Decodes a data with no fields
    # only useful for fire rocket confirmation
    ###
    # lifehack: open the edda_messages.json in chrome or firefox to get an overview
    # and drop-down menus with everything
    def parse_message_definitions(self, path):
        f = open(path)
        raw = json.load(f)
        f.close()
        messages = {}
        enums = {}
        datatypes = {}
        for message in raw["messages"]:
            if message['receiverNodeName'] == "Flight controller":
                id = message["id"]
                messages[id] = message
        for enum in raw["enums"]:
            name = enum["name"]
            enums[name] = enum["entries"]
        for datatype in raw["datatypes"]:
            name = datatype["name"]
            datatypes[name] = datatype
        
        for id in messages.keys():
            pass
            #do stuff with with the message

    #get the current time using either the computer clock or the last timestamp
    def decide_on_time(self, data):
        self.last_message_time = time.time()
        if self.time_sync_state == LIVE:
            if self.start_time == None:
                    self.start_time = time.time()
            return time.time() - self.start_time

        if self.time_sync_state == BACKUP_TIMESTAMP:
            if data.tree_pos[-1] == "timestamp":
                self.last_timestamp = data.value
            if self.last_timestamp == None:
                return 0 #can't tell a proper value
            else:
                return self.last_timestamp / 1000 #convert to seconds

        if self.time_sync_state == FLASH_TIMESTAMP:
            if data.tree_pos[-1] == "ms_since_boot":
                self.last_timestamp = data.value
            if self.last_timestamp == None:
                return 0 #can't tell a proper time
            else:
                return self.last_timestamp / 1000 #convert to seconds

    #thread that continously reads and extracs data from a stream
    def reader_thread(self):
        while not self.exit:
            if not self.stream_is_active or self.pause:
                continue
            separator = self.stream.read(1)
            #test for frame separator, read one byte at a time so it aligns itself
            if separator == b"":
                continue
            if separator[0] != SEPARATOR[0] or self.stream.read(1)[0] != SEPARATOR[1]:
                print(self.device + ": Invalid Separator: " + str(separator))
                continue
            #timestamp if reading from serial
            if self.stream == self.ser:
                self.ser.timestamp(time.time() - self.start_time)
            frame_id = self.stream.read(1)[0]
            if frame_id not in self.decoders:
                print(self.device + ": Invalid ID: " + str(frame_id))
                continue
            self.last_message_time = time.time()
            decoders = self.decoders[frame_id]
            decoded_data = []
            #run through all decoders
            for decoder in decoders:
                size = decoder.get_size()
                buf = self.stream.read(size)
                decoded_data += decoder.decode(buf)
            sensor_index = None
            for single_data in decoded_data:
                if single_data.tree_pos[-1] == "sensor_index":
                    sensor_index = single_data.value
                    continue
                #add the sensor index to the measurement so e.g. temperature becomes temperature2
                if sensor_index != None:
                    single_data.tree_pos[-1] += str(sensor_index)
                current_time = self.decide_on_time(single_data)
                current_pos = self.data
                #get where to save the data
                for key in single_data.tree_pos:
                    current_pos = current_pos[key]
                current_pos.x.append(current_time)
                current_pos.y.append(single_data.value)


decoding_definitions[ID_RETURN_RADIO_EQUIPMENT_FC] = [
    BitDecoder(["flight"], ["is_fpv_en", "is_tm_en"])
]

decoding_definitions[ID_RETURN_PARACHUTE_OUTPUT_FC] = [
    BitDecoder(["flight"], ["is_parachute_armed", "is_parachute1_en", "is_parachute2_en"])
]

decoding_definitions[ID_RETURN_TIME_SYNC_FC] = [
    EmptyDecoder(["flight", "time_sync"])
]

decoding_definitions[ID_ONBOARD_BATTERY_VOLTAGE_FC] = [
    NumDecoder(["flight", "battery_1"], "uint16", scale = 100),
    NumDecoder(["flight", "battery_2"], "uint16", scale = 100)
]

decoding_definitions[ID_GNSS_DATA_FC] = [
    NumDecoder(["flight", "gnss_time"], "uint32"),
    NumDecoder(["flight", "latitude"], "int32"),
    NumDecoder(["flight", "longitude"], "int32"),
    NumDecoder(["flight", "h_dop"], "uint16", scale = 100),
    NumDecoder(["flight", "n_satellites"], "uint8"),
]

decoding_definitions[ID_RETURN_SET_DATA_LOGGING_FC] = [
    BitDecoder(["flight"], ["is_logging_en"])
]

decoding_definitions[ID_RETURN_DUMP_FLASH_FC] = [
    BitDecoder(["flight"], ["dump_sd", "dump_flash"])
]

decoding_definitions[ID_CURRENT_TIME] = [
    NumDecoder(["flight", "current_time"], "uint32")
]

decoding_definitions[ID_LOCAL_TIMESTAMP] = [
    NumDecoder(["misc", "timestmp"], "uint32")
]

decoding_definitions[ID_MS_SINCE_BOOT_FC] = [
    NumDecoder(["flight", "ms_since_boot"], "uint32")
]

##
#these are testing decoders
#feel free to remove if they interfere
##
decoding_definitions[0x00] = [NumDecoder(["flight", "altitude"], "uint16")]
decoding_definitions[0x01] = [NumDecoder(["flight", "acceleration"], "int8")]
decoding_definitions[0x02] = [NumDecoder(["flight", "pressure"], "uint16")]
decoding_definitions[0x03] = [BitDecoder(["engine"], ["catastrophe"])]
decoding_definitions[0x04] = [
    NumDecoder(["flight", "gyrox"], "uint8"),
    NumDecoder(["flight", "gyroy"], "uint8"),
    NumDecoder(["flight", "gyroz"], "uint8")
]
decoding_definitions[64] = [
    NumDecoder(["flight", "ms_since_boot"], "uint32")
]