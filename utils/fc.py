################################
#GENERATED FILE DO NOT EDIT
################################

from enum import Enum
import struct

def scaledFloat_to_uint(value, scale):
    return value * scale

def uint_to_scaledFloat(value, scale):
    return value / scale

def packedFloat_to_uint(value, minValue, maxValue, size):
    intMax = (1 << size * 8) - 1
    if(value < minValue):
      return 0
    if(value > maxValue):
      return intMax
    ratio = (value - minValue) / (maxValue - minValue)
    return 1 + ((intMax - 2)) * ratio
  
def uint_to_packedFloat(value, minValue, maxValue, size):
    intMax = (1 << size * 8) - 1
    if(value <= 0):
      return minValue - 1.0
    if(value >= intMax):
      return maxValue + 1.0
    ratio = (value - 1) / (intMax - 2)
    return ratio * (maxValue - minValue) + minValue

class flight_state(Enum):
    sleeping = 0
    idle = 1
    ready = 2
    burning = 3
    ascending = 4
    descending = 5
    drogue = 6
    main_chute = 7
    landed = 8
class fix_status(Enum):
    no_fix = 0
    fix_2D = 1
    fix_3D = 2
class nodes(Enum):
    local = 0
    ground_station = 1
    flight_controller = 2
class fields(Enum):
    timestamp = 0
    system_time = 1
    state = 2
    is_parachute_armed = 3
    is_parachute1_en = 4
    is_parachute2_en = 5
    is_logging_en = 6
    dump_sd = 7
    dump_usb = 8
    is_fpv_en = 9
    is_tm_en = 10
    battery_1 = 11
    battery_2 = 12
    ms_since_boot = 13
    gnss_time = 14
    latitude = 15
    longitude = 16
    altitude = 17
    heading = 18
    horiz_speed = 19
    fix_status = 20
    n_satellites = 21
    h_dop = 22
    pressure = 23
    temperature = 24
    imu_id = 25
    accel_x = 26
    accel_y = 27
    accel_z = 28
    gyro_x = 29
    gyro_y = 30
    gyro_z = 31
    magnet_x = 32
    magnet_y = 33
    magnet_z = 34
    differential_pressure = 35
class messages(Enum):
    local_timestamp = 0
    time_sync = 1
    set_state = 2
    set_parachute_output = 3
    set_data_logging = 4
    dump_flash = 5
    handshake = 6
    return_time_sync = 7
    return_power_mode = 8
    return_radio_equipment = 9
    return_parachute_output = 10
    onboard_battery_voltage = 11
    return_data_logging = 12
    return_dump_flash = 13
    return_handshake = 14
    ms_since_boot = 15
    GNSS_data_1 = 16
    GNSS_data_2 = 17
    ms_raw = 18
    bmp_raw = 19
    imu_raw = 20
    position = 21
    differential_pressure = 22
class categories(Enum):
    none = 0
class local_timestamp_from_local_to_local:
    def __init__(self):
        self._sender = nodes.local
        self._receiver = nodes.local
        self._message = messages.local_timestamp
        self._category = categories.none
        self._id = 255
        self._size = 4
        self._timestamp = 0
    def get_sender(self):
        return self._sender
    def get_receiver(self):
        return self._receiver
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def get_category(self):
        return self._category
    def set_timestamp(self, value):
        self._timestamp = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._timestamp)
        return buf
    def get_timestamp(self):
        return self._timestamp
    def get_all_data(self):
        data = []
        data.append((fields.timestamp, self.get_timestamp()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._timestamp = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class time_sync_from_ground_station_to_flight_controller:
    def __init__(self):
        self._sender = nodes.ground_station
        self._receiver = nodes.flight_controller
        self._message = messages.time_sync
        self._category = categories.none
        self._id = 16
        self._size = 4
        self._system_time = 0
    def get_sender(self):
        return self._sender
    def get_receiver(self):
        return self._receiver
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def get_category(self):
        return self._category
    def set_system_time(self, value):
        self._system_time = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._system_time)
        return buf
    def get_system_time(self):
        return self._system_time
    def get_all_data(self):
        data = []
        data.append((fields.system_time, self.get_system_time()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._system_time = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class set_state_from_ground_station_to_flight_controller:
    def __init__(self):
        self._sender = nodes.ground_station
        self._receiver = nodes.flight_controller
        self._message = messages.set_state
        self._category = categories.none
        self._id = 17
        self._size = 1
        self._state = 0
    def get_sender(self):
        return self._sender
    def get_receiver(self):
        return self._receiver
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def get_category(self):
        return self._category
    def set_state(self, value):
        self._state = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._state)
        return buf
    def get_state(self):
        return flight_state(self._state)
    def get_all_data(self):
        data = []
        data.append((fields.state, self.get_state()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._state = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class set_parachute_output_from_ground_station_to_flight_controller:
    def __init__(self):
        self._sender = nodes.ground_station
        self._receiver = nodes.flight_controller
        self._message = messages.set_parachute_output
        self._category = categories.none
        self._id = 18
        self._size = 1
        self._bit_field = 0
    def get_sender(self):
        return self._sender
    def get_receiver(self):
        return self._receiver
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def get_category(self):
        return self._category
    def set_is_parachute_armed(self, value):
        self._bit_field =  value * (self._bit_field | (1 << 0)) + (not value) * (self._bit_field & ~(1 << 0))
    def set_is_parachute1_en(self, value):
        self._bit_field =  value * (self._bit_field | (1 << 1)) + (not value) * (self._bit_field & ~(1 << 1))
    def set_is_parachute2_en(self, value):
        self._bit_field =  value * (self._bit_field | (1 << 2)) + (not value) * (self._bit_field & ~(1 << 2))
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bit_field)
        return buf
    def get_is_parachute_armed(self):
        return self._bit_field & (1 << 0)
    def get_is_parachute1_en(self):
        return self._bit_field & (1 << 1)
    def get_is_parachute2_en(self):
        return self._bit_field & (1 << 2)
    def get_all_data(self):
        data = []
        data.append((fields.is_parachute_armed, self.get_is_parachute_armed()))
        data.append((fields.is_parachute1_en, self.get_is_parachute1_en()))
        data.append((fields.is_parachute2_en, self.get_is_parachute2_en()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bit_field = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class set_data_logging_from_ground_station_to_flight_controller:
    def __init__(self):
        self._sender = nodes.ground_station
        self._receiver = nodes.flight_controller
        self._message = messages.set_data_logging
        self._category = categories.none
        self._id = 19
        self._size = 1
        self._bit_field = 0
    def get_sender(self):
        return self._sender
    def get_receiver(self):
        return self._receiver
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def get_category(self):
        return self._category
    def set_is_logging_en(self, value):
        self._bit_field =  value * (self._bit_field | (1 << 0)) + (not value) * (self._bit_field & ~(1 << 0))
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bit_field)
        return buf
    def get_is_logging_en(self):
        return self._bit_field & (1 << 0)
    def get_all_data(self):
        data = []
        data.append((fields.is_logging_en, self.get_is_logging_en()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bit_field = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class dump_flash_from_ground_station_to_flight_controller:
    def __init__(self):
        self._sender = nodes.ground_station
        self._receiver = nodes.flight_controller
        self._message = messages.dump_flash
        self._category = categories.none
        self._id = 20
        self._size = 1
        self._bit_field = 0
    def get_sender(self):
        return self._sender
    def get_receiver(self):
        return self._receiver
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def get_category(self):
        return self._category
    def set_dump_sd(self, value):
        self._bit_field =  value * (self._bit_field | (1 << 0)) + (not value) * (self._bit_field & ~(1 << 0))
    def set_dump_usb(self, value):
        self._bit_field =  value * (self._bit_field | (1 << 1)) + (not value) * (self._bit_field & ~(1 << 1))
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bit_field)
        return buf
    def get_dump_sd(self):
        return self._bit_field & (1 << 0)
    def get_dump_usb(self):
        return self._bit_field & (1 << 1)
    def get_all_data(self):
        data = []
        data.append((fields.dump_sd, self.get_dump_sd()))
        data.append((fields.dump_usb, self.get_dump_usb()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bit_field = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class handshake_from_ground_station_to_flight_controller:
    def __init__(self):
        self._sender = nodes.ground_station
        self._receiver = nodes.flight_controller
        self._message = messages.handshake
        self._category = categories.none
        self._id = 21
        self._size = 0
    def get_sender(self):
        return self._sender
    def get_receiver(self):
        return self._receiver
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def get_category(self):
        return self._category
    def build_buf(self):
        buf = b""
        return buf
    def get_all_data(self):
        data = []
        return data
    def parse_buf(self, buf):
        index = 0
        return
class return_time_sync_from_flight_controller_to_ground_station:
    def __init__(self):
        self._sender = nodes.flight_controller
        self._receiver = nodes.ground_station
        self._message = messages.return_time_sync
        self._category = categories.none
        self._id = 32
        self._size = 0
    def get_sender(self):
        return self._sender
    def get_receiver(self):
        return self._receiver
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def get_category(self):
        return self._category
    def build_buf(self):
        buf = b""
        return buf
    def get_all_data(self):
        data = []
        return data
    def parse_buf(self, buf):
        index = 0
        return
class return_power_mode_from_flight_controller_to_ground_station:
    def __init__(self):
        self._sender = nodes.flight_controller
        self._receiver = nodes.ground_station
        self._message = messages.return_power_mode
        self._category = categories.none
        self._id = 33
        self._size = 0
    def get_sender(self):
        return self._sender
    def get_receiver(self):
        return self._receiver
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def get_category(self):
        return self._category
    def build_buf(self):
        buf = b""
        return buf
    def get_all_data(self):
        data = []
        return data
    def parse_buf(self, buf):
        index = 0
        return
class return_radio_equipment_from_flight_controller_to_ground_station:
    def __init__(self):
        self._sender = nodes.flight_controller
        self._receiver = nodes.ground_station
        self._message = messages.return_radio_equipment
        self._category = categories.none
        self._id = 34
        self._size = 1
        self._bit_field = 0
    def get_sender(self):
        return self._sender
    def get_receiver(self):
        return self._receiver
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def get_category(self):
        return self._category
    def set_is_fpv_en(self, value):
        self._bit_field =  value * (self._bit_field | (1 << 0)) + (not value) * (self._bit_field & ~(1 << 0))
    def set_is_tm_en(self, value):
        self._bit_field =  value * (self._bit_field | (1 << 1)) + (not value) * (self._bit_field & ~(1 << 1))
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bit_field)
        return buf
    def get_is_fpv_en(self):
        return self._bit_field & (1 << 0)
    def get_is_tm_en(self):
        return self._bit_field & (1 << 1)
    def get_all_data(self):
        data = []
        data.append((fields.is_fpv_en, self.get_is_fpv_en()))
        data.append((fields.is_tm_en, self.get_is_tm_en()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bit_field = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class return_parachute_output_from_flight_controller_to_ground_station:
    def __init__(self):
        self._sender = nodes.flight_controller
        self._receiver = nodes.ground_station
        self._message = messages.return_parachute_output
        self._category = categories.none
        self._id = 35
        self._size = 1
        self._bit_field = 0
    def get_sender(self):
        return self._sender
    def get_receiver(self):
        return self._receiver
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def get_category(self):
        return self._category
    def set_is_parachute_armed(self, value):
        self._bit_field =  value * (self._bit_field | (1 << 0)) + (not value) * (self._bit_field & ~(1 << 0))
    def set_is_parachute1_en(self, value):
        self._bit_field =  value * (self._bit_field | (1 << 1)) + (not value) * (self._bit_field & ~(1 << 1))
    def set_is_parachute2_en(self, value):
        self._bit_field =  value * (self._bit_field | (1 << 2)) + (not value) * (self._bit_field & ~(1 << 2))
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bit_field)
        return buf
    def get_is_parachute_armed(self):
        return self._bit_field & (1 << 0)
    def get_is_parachute1_en(self):
        return self._bit_field & (1 << 1)
    def get_is_parachute2_en(self):
        return self._bit_field & (1 << 2)
    def get_all_data(self):
        data = []
        data.append((fields.is_parachute_armed, self.get_is_parachute_armed()))
        data.append((fields.is_parachute1_en, self.get_is_parachute1_en()))
        data.append((fields.is_parachute2_en, self.get_is_parachute2_en()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bit_field = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class onboard_battery_voltage_from_flight_controller_to_ground_station:
    def __init__(self):
        self._sender = nodes.flight_controller
        self._receiver = nodes.ground_station
        self._message = messages.onboard_battery_voltage
        self._category = categories.none
        self._id = 36
        self._size = 4
        self._battery_1 = 0
        self._battery_2 = 0
    def get_sender(self):
        return self._sender
    def get_receiver(self):
        return self._receiver
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def get_category(self):
        return self._category
    def set_battery_1(self, value):
        self._battery_1 = scaledFloat_to_uint(value, 100)
    def set_battery_2(self, value):
        self._battery_2 = scaledFloat_to_uint(value, 100)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._battery_1)
        buf += struct.pack("<H", self._battery_2)
        return buf
    def get_battery_1(self):
        return uint_to_scaledFloat(self._battery_1, 100)
    def get_battery_2(self):
        return uint_to_scaledFloat(self._battery_2, 100)
    def get_all_data(self):
        data = []
        data.append((fields.battery_1, self.get_battery_1()))
        data.append((fields.battery_2, self.get_battery_2()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._battery_1 = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._battery_2 = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class return_data_logging_from_flight_controller_to_ground_station:
    def __init__(self):
        self._sender = nodes.flight_controller
        self._receiver = nodes.ground_station
        self._message = messages.return_data_logging
        self._category = categories.none
        self._id = 37
        self._size = 1
        self._bit_field = 0
    def get_sender(self):
        return self._sender
    def get_receiver(self):
        return self._receiver
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def get_category(self):
        return self._category
    def set_is_logging_en(self, value):
        self._bit_field =  value * (self._bit_field | (1 << 0)) + (not value) * (self._bit_field & ~(1 << 0))
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bit_field)
        return buf
    def get_is_logging_en(self):
        return self._bit_field & (1 << 0)
    def get_all_data(self):
        data = []
        data.append((fields.is_logging_en, self.get_is_logging_en()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bit_field = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class return_dump_flash_from_flight_controller_to_ground_station:
    def __init__(self):
        self._sender = nodes.flight_controller
        self._receiver = nodes.ground_station
        self._message = messages.return_dump_flash
        self._category = categories.none
        self._id = 38
        self._size = 1
        self._bit_field = 0
    def get_sender(self):
        return self._sender
    def get_receiver(self):
        return self._receiver
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def get_category(self):
        return self._category
    def set_dump_sd(self, value):
        self._bit_field =  value * (self._bit_field | (1 << 0)) + (not value) * (self._bit_field & ~(1 << 0))
    def set_dump_usb(self, value):
        self._bit_field =  value * (self._bit_field | (1 << 1)) + (not value) * (self._bit_field & ~(1 << 1))
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bit_field)
        return buf
    def get_dump_sd(self):
        return self._bit_field & (1 << 0)
    def get_dump_usb(self):
        return self._bit_field & (1 << 1)
    def get_all_data(self):
        data = []
        data.append((fields.dump_sd, self.get_dump_sd()))
        data.append((fields.dump_usb, self.get_dump_usb()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bit_field = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class return_handshake_from_flight_controller_to_ground_station:
    def __init__(self):
        self._sender = nodes.flight_controller
        self._receiver = nodes.ground_station
        self._message = messages.return_handshake
        self._category = categories.none
        self._id = 39
        self._size = 0
    def get_sender(self):
        return self._sender
    def get_receiver(self):
        return self._receiver
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def get_category(self):
        return self._category
    def build_buf(self):
        buf = b""
        return buf
    def get_all_data(self):
        data = []
        return data
    def parse_buf(self, buf):
        index = 0
        return
class ms_since_boot_from_flight_controller_to_ground_station:
    def __init__(self):
        self._sender = nodes.flight_controller
        self._receiver = nodes.ground_station
        self._message = messages.ms_since_boot
        self._category = categories.none
        self._id = 80
        self._size = 4
        self._ms_since_boot = 0
    def get_sender(self):
        return self._sender
    def get_receiver(self):
        return self._receiver
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def get_category(self):
        return self._category
    def set_ms_since_boot(self, value):
        self._ms_since_boot = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._ms_since_boot)
        return buf
    def get_ms_since_boot(self):
        return self._ms_since_boot
    def get_all_data(self):
        data = []
        data.append((fields.ms_since_boot, self.get_ms_since_boot()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._ms_since_boot = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class GNSS_data_1_from_flight_controller_to_ground_station:
    def __init__(self):
        self._sender = nodes.flight_controller
        self._receiver = nodes.ground_station
        self._message = messages.GNSS_data_1
        self._category = categories.none
        self._id = 81
        self._size = 12
        self._gnss_time = 0
        self._latitude = 0
        self._longitude = 0
    def get_sender(self):
        return self._sender
    def get_receiver(self):
        return self._receiver
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def get_category(self):
        return self._category
    def set_gnss_time(self, value):
        self._gnss_time = value
    def set_latitude(self, value):
        self._latitude = value
    def set_longitude(self, value):
        self._longitude = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._gnss_time)
        buf += struct.pack("<l", self._latitude)
        buf += struct.pack("<l", self._longitude)
        return buf
    def get_gnss_time(self):
        return self._gnss_time
    def get_latitude(self):
        return self._latitude
    def get_longitude(self):
        return self._longitude
    def get_all_data(self):
        data = []
        data.append((fields.gnss_time, self.get_gnss_time()))
        data.append((fields.latitude, self.get_latitude()))
        data.append((fields.longitude, self.get_longitude()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._gnss_time = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._latitude = struct.unpack_from("<l", buf, index)[0]
        index += 4
        self._longitude = struct.unpack_from("<l", buf, index)[0]
        index += 4
        return
class GNSS_data_2_from_flight_controller_to_ground_station:
    def __init__(self):
        self._sender = nodes.flight_controller
        self._receiver = nodes.ground_station
        self._message = messages.GNSS_data_2
        self._category = categories.none
        self._id = 82
        self._size = 12
        self._altitude = 0
        self._heading = 0
        self._horiz_speed = 0
        self._fix_status = 0
        self._n_satellites = 0
        self._h_dop = 0
    def get_sender(self):
        return self._sender
    def get_receiver(self):
        return self._receiver
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def get_category(self):
        return self._category
    def set_altitude(self, value):
        self._altitude = scaledFloat_to_uint(value, 10)
    def set_heading(self, value):
        self._heading = value
    def set_horiz_speed(self, value):
        self._horiz_speed = scaledFloat_to_uint(value, 10)
    def set_fix_status(self, value):
        self._fix_status = value.value
    def set_n_satellites(self, value):
        self._n_satellites = value
    def set_h_dop(self, value):
        self._h_dop = scaledFloat_to_uint(value, 10)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<l", self._altitude)
        buf += struct.pack("<h", self._heading)
        buf += struct.pack("<h", self._horiz_speed)
        buf += struct.pack("<B", self._fix_status)
        buf += struct.pack("<B", self._n_satellites)
        buf += struct.pack("<H", self._h_dop)
        return buf
    def get_altitude(self):
        return uint_to_scaledFloat(self._altitude, 10)
    def get_heading(self):
        return self._heading
    def get_horiz_speed(self):
        return uint_to_scaledFloat(self._horiz_speed, 10)
    def get_fix_status(self):
        return fix_status(self._fix_status)
    def get_n_satellites(self):
        return self._n_satellites
    def get_h_dop(self):
        return uint_to_scaledFloat(self._h_dop, 10)
    def get_all_data(self):
        data = []
        data.append((fields.altitude, self.get_altitude()))
        data.append((fields.heading, self.get_heading()))
        data.append((fields.horiz_speed, self.get_horiz_speed()))
        data.append((fields.fix_status, self.get_fix_status()))
        data.append((fields.n_satellites, self.get_n_satellites()))
        data.append((fields.h_dop, self.get_h_dop()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._altitude = struct.unpack_from("<l", buf, index)[0]
        index += 4
        self._heading = struct.unpack_from("<h", buf, index)[0]
        index += 2
        self._horiz_speed = struct.unpack_from("<h", buf, index)[0]
        index += 2
        self._fix_status = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._n_satellites = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._h_dop = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class ms_raw_from_flight_controller_to_ground_station:
    def __init__(self):
        self._sender = nodes.flight_controller
        self._receiver = nodes.ground_station
        self._message = messages.ms_raw
        self._category = categories.none
        self._id = 83
        self._size = 8
        self._pressure = 0
        self._temperature = 0
    def get_sender(self):
        return self._sender
    def get_receiver(self):
        return self._receiver
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def get_category(self):
        return self._category
    def set_pressure(self, value):
        self._pressure = value
    def set_temperature(self, value):
        self._temperature = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<f", self._pressure)
        buf += struct.pack("<f", self._temperature)
        return buf
    def get_pressure(self):
        return self._pressure
    def get_temperature(self):
        return self._temperature
    def get_all_data(self):
        data = []
        data.append((fields.pressure, self.get_pressure()))
        data.append((fields.temperature, self.get_temperature()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._pressure = struct.unpack_from("<f", buf, index)[0]
        index += 4
        self._temperature = struct.unpack_from("<f", buf, index)[0]
        index += 4
        return
class bmp_raw_from_flight_controller_to_ground_station:
    def __init__(self):
        self._sender = nodes.flight_controller
        self._receiver = nodes.ground_station
        self._message = messages.bmp_raw
        self._category = categories.none
        self._id = 84
        self._size = 8
        self._pressure = 0
        self._temperature = 0
    def get_sender(self):
        return self._sender
    def get_receiver(self):
        return self._receiver
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def get_category(self):
        return self._category
    def set_pressure(self, value):
        self._pressure = value
    def set_temperature(self, value):
        self._temperature = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<f", self._pressure)
        buf += struct.pack("<f", self._temperature)
        return buf
    def get_pressure(self):
        return self._pressure
    def get_temperature(self):
        return self._temperature
    def get_all_data(self):
        data = []
        data.append((fields.pressure, self.get_pressure()))
        data.append((fields.temperature, self.get_temperature()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._pressure = struct.unpack_from("<f", buf, index)[0]
        index += 4
        self._temperature = struct.unpack_from("<f", buf, index)[0]
        index += 4
        return
class imu_raw_from_flight_controller_to_ground_station:
    def __init__(self):
        self._sender = nodes.flight_controller
        self._receiver = nodes.ground_station
        self._message = messages.imu_raw
        self._category = categories.none
        self._id = 85
        self._size = 37
        self._imu_id = 0
        self._accel_x = 0
        self._accel_y = 0
        self._accel_z = 0
        self._gyro_x = 0
        self._gyro_y = 0
        self._gyro_z = 0
        self._magnet_x = 0
        self._magnet_y = 0
        self._magnet_z = 0
    def get_sender(self):
        return self._sender
    def get_receiver(self):
        return self._receiver
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def get_category(self):
        return self._category
    def set_imu_id(self, value):
        self._imu_id = value
    def set_accel_x(self, value):
        self._accel_x = value
    def set_accel_y(self, value):
        self._accel_y = value
    def set_accel_z(self, value):
        self._accel_z = value
    def set_gyro_x(self, value):
        self._gyro_x = value
    def set_gyro_y(self, value):
        self._gyro_y = value
    def set_gyro_z(self, value):
        self._gyro_z = value
    def set_magnet_x(self, value):
        self._magnet_x = value
    def set_magnet_y(self, value):
        self._magnet_y = value
    def set_magnet_z(self, value):
        self._magnet_z = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._imu_id)
        buf += struct.pack("<f", self._accel_x)
        buf += struct.pack("<f", self._accel_y)
        buf += struct.pack("<f", self._accel_z)
        buf += struct.pack("<f", self._gyro_x)
        buf += struct.pack("<f", self._gyro_y)
        buf += struct.pack("<f", self._gyro_z)
        buf += struct.pack("<f", self._magnet_x)
        buf += struct.pack("<f", self._magnet_y)
        buf += struct.pack("<f", self._magnet_z)
        return buf
    def get_imu_id(self):
        return self._imu_id
    def get_accel_x(self):
        return self._accel_x
    def get_accel_y(self):
        return self._accel_y
    def get_accel_z(self):
        return self._accel_z
    def get_gyro_x(self):
        return self._gyro_x
    def get_gyro_y(self):
        return self._gyro_y
    def get_gyro_z(self):
        return self._gyro_z
    def get_magnet_x(self):
        return self._magnet_x
    def get_magnet_y(self):
        return self._magnet_y
    def get_magnet_z(self):
        return self._magnet_z
    def get_all_data(self):
        data = []
        data.append((fields.imu_id, self.get_imu_id()))
        data.append((fields.accel_x, self.get_accel_x()))
        data.append((fields.accel_y, self.get_accel_y()))
        data.append((fields.accel_z, self.get_accel_z()))
        data.append((fields.gyro_x, self.get_gyro_x()))
        data.append((fields.gyro_y, self.get_gyro_y()))
        data.append((fields.gyro_z, self.get_gyro_z()))
        data.append((fields.magnet_x, self.get_magnet_x()))
        data.append((fields.magnet_y, self.get_magnet_y()))
        data.append((fields.magnet_z, self.get_magnet_z()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._imu_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._accel_x = struct.unpack_from("<f", buf, index)[0]
        index += 4
        self._accel_y = struct.unpack_from("<f", buf, index)[0]
        index += 4
        self._accel_z = struct.unpack_from("<f", buf, index)[0]
        index += 4
        self._gyro_x = struct.unpack_from("<f", buf, index)[0]
        index += 4
        self._gyro_y = struct.unpack_from("<f", buf, index)[0]
        index += 4
        self._gyro_z = struct.unpack_from("<f", buf, index)[0]
        index += 4
        self._magnet_x = struct.unpack_from("<f", buf, index)[0]
        index += 4
        self._magnet_y = struct.unpack_from("<f", buf, index)[0]
        index += 4
        self._magnet_z = struct.unpack_from("<f", buf, index)[0]
        index += 4
        return
class position_from_flight_controller_to_ground_station:
    def __init__(self):
        self._sender = nodes.flight_controller
        self._receiver = nodes.ground_station
        self._message = messages.position
        self._category = categories.none
        self._id = 86
        self._size = 12
        self._altitude = 0
        self._longitude = 0
        self._latitude = 0
    def get_sender(self):
        return self._sender
    def get_receiver(self):
        return self._receiver
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def get_category(self):
        return self._category
    def set_altitude(self, value):
        self._altitude = value
    def set_longitude(self, value):
        self._longitude = value
    def set_latitude(self, value):
        self._latitude = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<f", self._altitude)
        buf += struct.pack("<f", self._longitude)
        buf += struct.pack("<f", self._latitude)
        return buf
    def get_altitude(self):
        return self._altitude
    def get_longitude(self):
        return self._longitude
    def get_latitude(self):
        return self._latitude
    def get_all_data(self):
        data = []
        data.append((fields.altitude, self.get_altitude()))
        data.append((fields.longitude, self.get_longitude()))
        data.append((fields.latitude, self.get_latitude()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._altitude = struct.unpack_from("<f", buf, index)[0]
        index += 4
        self._longitude = struct.unpack_from("<f", buf, index)[0]
        index += 4
        self._latitude = struct.unpack_from("<f", buf, index)[0]
        index += 4
        return
class differential_pressure_from_flight_controller_to_ground_station:
    def __init__(self):
        self._sender = nodes.flight_controller
        self._receiver = nodes.ground_station
        self._message = messages.differential_pressure
        self._category = categories.none
        self._id = 87
        self._size = 4
        self._differential_pressure = 0
    def get_sender(self):
        return self._sender
    def get_receiver(self):
        return self._receiver
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def get_category(self):
        return self._category
    def set_differential_pressure(self, value):
        self._differential_pressure = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<f", self._differential_pressure)
        return buf
    def get_differential_pressure(self):
        return self._differential_pressure
    def get_all_data(self):
        data = []
        data.append((fields.differential_pressure, self.get_differential_pressure()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._differential_pressure = struct.unpack_from("<f", buf, index)[0]
        index += 4
        return
def id_to_message_class(id):
    if id == 255:
        receiver = local_timestamp_from_local_to_local()
        return receiver
    if id == 16:
        receiver = time_sync_from_ground_station_to_flight_controller()
        return receiver
    if id == 17:
        receiver = set_state_from_ground_station_to_flight_controller()
        return receiver
    if id == 18:
        receiver = set_parachute_output_from_ground_station_to_flight_controller()
        return receiver
    if id == 19:
        receiver = set_data_logging_from_ground_station_to_flight_controller()
        return receiver
    if id == 20:
        receiver = dump_flash_from_ground_station_to_flight_controller()
        return receiver
    if id == 21:
        receiver = handshake_from_ground_station_to_flight_controller()
        return receiver
    if id == 32:
        receiver = return_time_sync_from_flight_controller_to_ground_station()
        return receiver
    if id == 33:
        receiver = return_power_mode_from_flight_controller_to_ground_station()
        return receiver
    if id == 34:
        receiver = return_radio_equipment_from_flight_controller_to_ground_station()
        return receiver
    if id == 35:
        receiver = return_parachute_output_from_flight_controller_to_ground_station()
        return receiver
    if id == 36:
        receiver = onboard_battery_voltage_from_flight_controller_to_ground_station()
        return receiver
    if id == 37:
        receiver = return_data_logging_from_flight_controller_to_ground_station()
        return receiver
    if id == 38:
        receiver = return_dump_flash_from_flight_controller_to_ground_station()
        return receiver
    if id == 39:
        receiver = return_handshake_from_flight_controller_to_ground_station()
        return receiver
    if id == 80:
        receiver = ms_since_boot_from_flight_controller_to_ground_station()
        return receiver
    if id == 81:
        receiver = GNSS_data_1_from_flight_controller_to_ground_station()
        return receiver
    if id == 82:
        receiver = GNSS_data_2_from_flight_controller_to_ground_station()
        return receiver
    if id == 83:
        receiver = ms_raw_from_flight_controller_to_ground_station()
        return receiver
    if id == 84:
        receiver = bmp_raw_from_flight_controller_to_ground_station()
        return receiver
    if id == 85:
        receiver = imu_raw_from_flight_controller_to_ground_station()
        return receiver
    if id == 86:
        receiver = position_from_flight_controller_to_ground_station()
        return receiver
    if id == 87:
        receiver = differential_pressure_from_flight_controller_to_ground_station()
        return receiver
def is_specifier(sender, name, field):
    if (messages.local_timestamp == name and nodes.local == sender):
        if (fields.timestamp == field):
            return False
    if (messages.time_sync == name and nodes.ground_station == sender):
        if (fields.system_time == field):
            return False
    if (messages.set_state == name and nodes.ground_station == sender):
        if (fields.state == field):
            return False
    if (messages.onboard_battery_voltage == name and nodes.flight_controller == sender):
        if (fields.battery_1 == field):
            return False
        if (fields.battery_2 == field):
            return False
    if (messages.ms_since_boot == name and nodes.flight_controller == sender):
        if (fields.ms_since_boot == field):
            return False
    if (messages.GNSS_data_1 == name and nodes.flight_controller == sender):
        if (fields.gnss_time == field):
            return False
        if (fields.latitude == field):
            return False
        if (fields.longitude == field):
            return False
    if (messages.GNSS_data_2 == name and nodes.flight_controller == sender):
        if (fields.altitude == field):
            return False
        if (fields.heading == field):
            return False
        if (fields.horiz_speed == field):
            return False
        if (fields.fix_status == field):
            return False
        if (fields.n_satellites == field):
            return False
        if (fields.h_dop == field):
            return False
    if (messages.ms_raw == name and nodes.flight_controller == sender):
        if (fields.pressure == field):
            return False
        if (fields.temperature == field):
            return False
    if (messages.bmp_raw == name and nodes.flight_controller == sender):
        if (fields.pressure == field):
            return False
        if (fields.temperature == field):
            return False
    if (messages.imu_raw == name and nodes.flight_controller == sender):
        if (fields.imu_id == field):
            return False
        if (fields.accel_x == field):
            return False
        if (fields.accel_y == field):
            return False
        if (fields.accel_z == field):
            return False
        if (fields.gyro_x == field):
            return False
        if (fields.gyro_y == field):
            return False
        if (fields.gyro_z == field):
            return False
        if (fields.magnet_x == field):
            return False
        if (fields.magnet_y == field):
            return False
        if (fields.magnet_z == field):
            return False
    if (messages.position == name and nodes.flight_controller == sender):
        if (fields.altitude == field):
            return False
        if (fields.longitude == field):
            return False
        if (fields.latitude == field):
            return False
    if (messages.differential_pressure == name and nodes.flight_controller == sender):
        if (fields.differential_pressure == field):
            return False
    return False
