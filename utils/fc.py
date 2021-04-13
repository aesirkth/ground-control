################################
#GENERATED FILE DO NOT EDIT
################################

from enum import Enum
import struct

def scaledFloat_to_uint(value, scale):
    return value * scale

def uint_to_scaledFloat(value, scale):
    return value / scale

def packedFloat_to_uint(value, min, max, size):
    max_value = (1 << size * 8) - 1
    difference = max - min
    return (value - min) / difference * max_value

def uint_to_packedFloat(value, min, max, size):
    max_value = (1 << size * 8) - 1
    difference = max - min
    return difference * value / max_value

class fix_status(Enum):
    no_fix = 0
    fix_2D = 1
    fix_3D = 2
class units(Enum):
    local = 0
    test = 1
    ground_station = 2
    flight_controller = 3
class fields(Enum):
    timestamp = 0
    ms_since_boot = 1
    altitude = 2
    catastrophe = 3
    x = 4
    y = 5
    z = 6
    system_time = 7
    is_fpv_en = 8
    is_tm_en = 9
    is_parachute_armed = 10
    is_parachute1_en = 11
    is_parachute2_en = 12
    is_logging_en = 13
    dump_sd = 14
    dump_usb = 15
    battery_1 = 16
    battery_2 = 17
    gnss_time = 18
    latitude = 19
    longitude = 20
    h_dop = 21
    n_satellites = 22
    HW_state = 23
    SW_state = 24
    mission_state = 25
    us_since_boot = 26
    current_time = 27
    heading = 28
    horiz_speed = 29
    fix_status = 30
    temperature_1 = 31
    temperature_2 = 32
    pressure_1 = 33
    pressure_2 = 34
    accel_x = 35
    accel_y = 36
    accel_z = 37
    gyro_x = 38
    gyro_y = 39
    gyro_z = 40
    magnet_x = 41
    magnet_y = 42
    magnet_z = 43
class messages(Enum):
    local_timestamp = 0
    ms_since_boot = 1
    altitude = 2
    acceleration = 3
    pressure = 4
    catastrophe = 5
    gyro = 6
    time_sync = 7
    set_power_mode = 8
    set_radio_equipment = 9
    set_parachute_output = 10
    set_data_logging = 11
    dump_flash = 12
    handshake = 13
    return_time_sync = 14
    return_power_mode = 15
    return_radio_equipment = 16
    return_parachute_output = 17
    onboard_battery_voltage = 18
    gnss_data = 19
    flight_controller_status = 20
    return_data_logging = 21
    return_dump_flash = 22
    return_handshake = 23
    us_since_boot = 24
    current_time = 25
    GNSS_data_1 = 26
    GNSS_data_2 = 27
    inside_static_temperature = 28
    inside_static_pressure = 29
    IMU1 = 30
    IMU2 = 31
class altitude_from_test_to_test:
    def __init__(self):
        self._source = units.test
        self._target = units.test
        self._message = messages.altitude
        self._id = 0
        self._size = 2
        self._altitude = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def set_altitude(self, value):
        self._altitude = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._altitude)
        return buf
    def get_altitude(self):
        return self._altitude
    def get_all_data(self):
        data = []
        data.append((fields.altitude, self.get_altitude()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._altitude = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class acceleration_from_test_to_test:
    def __init__(self):
        self._source = units.test
        self._target = units.test
        self._message = messages.acceleration
        self._id = 1
        self._size = 1
        self._altitude = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def set_altitude(self, value):
        self._altitude = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._altitude)
        return buf
    def get_altitude(self):
        return self._altitude
    def get_all_data(self):
        data = []
        data.append((fields.altitude, self.get_altitude()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._altitude = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class pressure_from_test_to_test:
    def __init__(self):
        self._source = units.test
        self._target = units.test
        self._message = messages.pressure
        self._id = 2
        self._size = 2
        self._altitude = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def set_altitude(self, value):
        self._altitude = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._altitude)
        return buf
    def get_altitude(self):
        return self._altitude
    def get_all_data(self):
        data = []
        data.append((fields.altitude, self.get_altitude()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._altitude = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class catastrophe_from_test_to_test:
    def __init__(self):
        self._source = units.test
        self._target = units.test
        self._message = messages.catastrophe
        self._id = 3
        self._size = 1
        self._bit_field = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def set_catastrophe(self, value):
        self._bit_field =  value * (self._bit_field | (1 << 0)) + (not value) * (self._bit_field & ~(1 << 0))
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bit_field)
        return buf
    def get_catastrophe(self):
        return self._bit_field & (1 << 0)
    def get_all_data(self):
        data = []
        data.append((fields.catastrophe, self.get_catastrophe()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bit_field = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class gyro_from_test_to_test:
    def __init__(self):
        self._source = units.test
        self._target = units.test
        self._message = messages.gyro
        self._id = 4
        self._size = 3
        self._x = 0
        self._y = 0
        self._z = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def set_x(self, value):
        self._x = value
    def set_y(self, value):
        self._y = value
    def set_z(self, value):
        self._z = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._x)
        buf += struct.pack("<B", self._y)
        buf += struct.pack("<B", self._z)
        return buf
    def get_x(self):
        return self._x
    def get_y(self):
        return self._y
    def get_z(self):
        return self._z
    def get_all_data(self):
        data = []
        data.append((fields.x, self.get_x()))
        data.append((fields.y, self.get_y()))
        data.append((fields.z, self.get_z()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._x = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._y = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._z = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class time_sync_from_ground_station_to_flight_controller:
    def __init__(self):
        self._source = units.ground_station
        self._target = units.flight_controller
        self._message = messages.time_sync
        self._id = 16
        self._size = 4
        self._system_time = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
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
class set_power_mode_from_ground_station_to_flight_controller:
    def __init__(self):
        self._source = units.ground_station
        self._target = units.flight_controller
        self._message = messages.set_power_mode
        self._id = 17
        self._size = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def build_buf(self):
        buf = b""
        return buf
    def get_all_data(self):
        data = []
        return data
    def parse_buf(self, buf):
        index = 0
        return
class set_radio_equipment_from_ground_station_to_flight_controller:
    def __init__(self):
        self._source = units.ground_station
        self._target = units.flight_controller
        self._message = messages.set_radio_equipment
        self._id = 18
        self._size = 1
        self._bit_field = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
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
class set_parachute_output_from_ground_station_to_flight_controller:
    def __init__(self):
        self._source = units.ground_station
        self._target = units.flight_controller
        self._message = messages.set_parachute_output
        self._id = 19
        self._size = 1
        self._bit_field = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
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
        self._source = units.ground_station
        self._target = units.flight_controller
        self._message = messages.set_data_logging
        self._id = 20
        self._size = 1
        self._bit_field = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
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
        self._source = units.ground_station
        self._target = units.flight_controller
        self._message = messages.dump_flash
        self._id = 21
        self._size = 1
        self._bit_field = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
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
        self._source = units.ground_station
        self._target = units.flight_controller
        self._message = messages.handshake
        self._id = 22
        self._size = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
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
        self._source = units.flight_controller
        self._target = units.ground_station
        self._message = messages.return_time_sync
        self._id = 32
        self._size = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
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
        self._source = units.flight_controller
        self._target = units.ground_station
        self._message = messages.return_power_mode
        self._id = 33
        self._size = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
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
        self._source = units.flight_controller
        self._target = units.ground_station
        self._message = messages.return_radio_equipment
        self._id = 34
        self._size = 1
        self._bit_field = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
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
        self._source = units.flight_controller
        self._target = units.ground_station
        self._message = messages.return_parachute_output
        self._id = 35
        self._size = 1
        self._bit_field = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
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
        self._source = units.flight_controller
        self._target = units.ground_station
        self._message = messages.onboard_battery_voltage
        self._id = 36
        self._size = 4
        self._battery_1 = 0
        self._battery_2 = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
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
class gnss_data_from_flight_controller_to_ground_station:
    def __init__(self):
        self._source = units.flight_controller
        self._target = units.ground_station
        self._message = messages.gnss_data
        self._id = 37
        self._size = 15
        self._gnss_time = 0
        self._latitude = 0
        self._longitude = 0
        self._h_dop = 0
        self._n_satellites = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def set_gnss_time(self, value):
        self._gnss_time = value
    def set_latitude(self, value):
        self._latitude = value
    def set_longitude(self, value):
        self._longitude = value
    def set_h_dop(self, value):
        self._h_dop = scaledFloat_to_uint(value, 100)
    def set_n_satellites(self, value):
        self._n_satellites = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._gnss_time)
        buf += struct.pack("<l", self._latitude)
        buf += struct.pack("<l", self._longitude)
        buf += struct.pack("<H", self._h_dop)
        buf += struct.pack("<B", self._n_satellites)
        return buf
    def get_gnss_time(self):
        return self._gnss_time
    def get_latitude(self):
        return self._latitude
    def get_longitude(self):
        return self._longitude
    def get_h_dop(self):
        return uint_to_scaledFloat(self._h_dop, 100)
    def get_n_satellites(self):
        return self._n_satellites
    def get_all_data(self):
        data = []
        data.append((fields.gnss_time, self.get_gnss_time()))
        data.append((fields.latitude, self.get_latitude()))
        data.append((fields.longitude, self.get_longitude()))
        data.append((fields.h_dop, self.get_h_dop()))
        data.append((fields.n_satellites, self.get_n_satellites()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._gnss_time = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._latitude = struct.unpack_from("<l", buf, index)[0]
        index += 4
        self._longitude = struct.unpack_from("<l", buf, index)[0]
        index += 4
        self._h_dop = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._n_satellites = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class flight_controller_status_from_flight_controller_to_ground_station:
    def __init__(self):
        self._source = units.flight_controller
        self._target = units.ground_station
        self._message = messages.flight_controller_status
        self._id = 38
        self._size = 3
        self._HW_state = 0
        self._SW_state = 0
        self._mission_state = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def set_HW_state(self, value):
        self._HW_state = value
    def set_SW_state(self, value):
        self._SW_state = value
    def set_mission_state(self, value):
        self._mission_state = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._HW_state)
        buf += struct.pack("<B", self._SW_state)
        buf += struct.pack("<B", self._mission_state)
        return buf
    def get_HW_state(self):
        return self._HW_state
    def get_SW_state(self):
        return self._SW_state
    def get_mission_state(self):
        return self._mission_state
    def get_all_data(self):
        data = []
        data.append((fields.HW_state, self.get_HW_state()))
        data.append((fields.SW_state, self.get_SW_state()))
        data.append((fields.mission_state, self.get_mission_state()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._HW_state = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._SW_state = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._mission_state = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class return_data_logging_from_flight_controller_to_ground_station:
    def __init__(self):
        self._source = units.flight_controller
        self._target = units.ground_station
        self._message = messages.return_data_logging
        self._id = 39
        self._size = 1
        self._bit_field = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
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
        self._source = units.flight_controller
        self._target = units.ground_station
        self._message = messages.return_dump_flash
        self._id = 40
        self._size = 1
        self._bit_field = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
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
        self._source = units.flight_controller
        self._target = units.ground_station
        self._message = messages.return_handshake
        self._id = 41
        self._size = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def build_buf(self):
        buf = b""
        return buf
    def get_all_data(self):
        data = []
        return data
    def parse_buf(self, buf):
        index = 0
        return
class ms_since_boot_from_test_to_test:
    def __init__(self):
        self._source = units.test
        self._target = units.test
        self._message = messages.ms_since_boot
        self._id = 64
        self._size = 4
        self._ms_since_boot = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
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
class ms_since_boot_from_flight_controller_to_ground_station:
    def __init__(self):
        self._source = units.flight_controller
        self._target = units.ground_station
        self._message = messages.ms_since_boot
        self._id = 80
        self._size = 4
        self._ms_since_boot = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
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
class us_since_boot_from_flight_controller_to_ground_station:
    def __init__(self):
        self._source = units.flight_controller
        self._target = units.ground_station
        self._message = messages.us_since_boot
        self._id = 81
        self._size = 8
        self._us_since_boot = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def set_us_since_boot(self, value):
        self._us_since_boot = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<Q", self._us_since_boot)
        return buf
    def get_us_since_boot(self):
        return self._us_since_boot
    def get_all_data(self):
        data = []
        data.append((fields.us_since_boot, self.get_us_since_boot()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._us_since_boot = struct.unpack_from("<Q", buf, index)[0]
        index += 8
        return
class current_time_from_flight_controller_to_ground_station:
    def __init__(self):
        self._source = units.flight_controller
        self._target = units.ground_station
        self._message = messages.current_time
        self._id = 82
        self._size = 4
        self._current_time = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def set_current_time(self, value):
        self._current_time = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._current_time)
        return buf
    def get_current_time(self):
        return self._current_time
    def get_all_data(self):
        data = []
        data.append((fields.current_time, self.get_current_time()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._current_time = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class GNSS_data_1_from_flight_controller_to_ground_station:
    def __init__(self):
        self._source = units.flight_controller
        self._target = units.ground_station
        self._message = messages.GNSS_data_1
        self._id = 83
        self._size = 12
        self._gnss_time = 0
        self._latitude = 0
        self._longitude = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
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
        self._source = units.flight_controller
        self._target = units.ground_station
        self._message = messages.GNSS_data_2
        self._id = 84
        self._size = 12
        self._altitude = 0
        self._heading = 0
        self._horiz_speed = 0
        self._fix_status = 0
        self._n_satellites = 0
        self._h_dop = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
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
class inside_static_temperature_from_flight_controller_to_ground_station:
    def __init__(self):
        self._source = units.flight_controller
        self._target = units.ground_station
        self._message = messages.inside_static_temperature
        self._id = 85
        self._size = 8
        self._temperature_1 = 0
        self._temperature_2 = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def set_temperature_1(self, value):
        self._temperature_1 = scaledFloat_to_uint(value, 100)
    def set_temperature_2(self, value):
        self._temperature_2 = scaledFloat_to_uint(value, 100)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<l", self._temperature_1)
        buf += struct.pack("<l", self._temperature_2)
        return buf
    def get_temperature_1(self):
        return uint_to_scaledFloat(self._temperature_1, 100)
    def get_temperature_2(self):
        return uint_to_scaledFloat(self._temperature_2, 100)
    def get_all_data(self):
        data = []
        data.append((fields.temperature_1, self.get_temperature_1()))
        data.append((fields.temperature_2, self.get_temperature_2()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._temperature_1 = struct.unpack_from("<l", buf, index)[0]
        index += 4
        self._temperature_2 = struct.unpack_from("<l", buf, index)[0]
        index += 4
        return
class inside_static_pressure_from_flight_controller_to_ground_station:
    def __init__(self):
        self._source = units.flight_controller
        self._target = units.ground_station
        self._message = messages.inside_static_pressure
        self._id = 86
        self._size = 8
        self._pressure_1 = 0
        self._pressure_2 = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def set_pressure_1(self, value):
        self._pressure_1 = scaledFloat_to_uint(value, 100)
    def set_pressure_2(self, value):
        self._pressure_2 = scaledFloat_to_uint(value, 100)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<l", self._pressure_1)
        buf += struct.pack("<l", self._pressure_2)
        return buf
    def get_pressure_1(self):
        return uint_to_scaledFloat(self._pressure_1, 100)
    def get_pressure_2(self):
        return uint_to_scaledFloat(self._pressure_2, 100)
    def get_all_data(self):
        data = []
        data.append((fields.pressure_1, self.get_pressure_1()))
        data.append((fields.pressure_2, self.get_pressure_2()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._pressure_1 = struct.unpack_from("<l", buf, index)[0]
        index += 4
        self._pressure_2 = struct.unpack_from("<l", buf, index)[0]
        index += 4
        return
class IMU1_from_flight_controller_to_ground_station:
    def __init__(self):
        self._source = units.flight_controller
        self._target = units.ground_station
        self._message = messages.IMU1
        self._id = 87
        self._size = 18
        self._accel_x = 0
        self._accel_y = 0
        self._accel_z = 0
        self._gyro_x = 0
        self._gyro_y = 0
        self._gyro_z = 0
        self._magnet_x = 0
        self._magnet_y = 0
        self._magnet_z = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
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
        buf += struct.pack("<H", self._accel_x)
        buf += struct.pack("<H", self._accel_y)
        buf += struct.pack("<H", self._accel_z)
        buf += struct.pack("<H", self._gyro_x)
        buf += struct.pack("<H", self._gyro_y)
        buf += struct.pack("<H", self._gyro_z)
        buf += struct.pack("<H", self._magnet_x)
        buf += struct.pack("<H", self._magnet_y)
        buf += struct.pack("<H", self._magnet_z)
        return buf
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
        self._accel_x = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._accel_y = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._accel_z = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._gyro_x = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._gyro_y = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._gyro_z = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._magnet_x = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._magnet_y = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._magnet_z = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class IMU2_from_flight_controller_to_ground_station:
    def __init__(self):
        self._source = units.flight_controller
        self._target = units.ground_station
        self._message = messages.IMU2
        self._id = 88
        self._size = 18
        self._accel_x = 0
        self._accel_y = 0
        self._accel_z = 0
        self._gyro_x = 0
        self._gyro_y = 0
        self._gyro_z = 0
        self._magnet_x = 0
        self._magnet_y = 0
        self._magnet_z = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
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
        buf += struct.pack("<H", self._accel_x)
        buf += struct.pack("<H", self._accel_y)
        buf += struct.pack("<H", self._accel_z)
        buf += struct.pack("<H", self._gyro_x)
        buf += struct.pack("<H", self._gyro_y)
        buf += struct.pack("<H", self._gyro_z)
        buf += struct.pack("<H", self._magnet_x)
        buf += struct.pack("<H", self._magnet_y)
        buf += struct.pack("<H", self._magnet_z)
        return buf
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
        self._accel_x = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._accel_y = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._accel_z = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._gyro_x = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._gyro_y = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._gyro_z = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._magnet_x = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._magnet_y = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._magnet_z = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class local_timestamp_from_local_to_local:
    def __init__(self):
        self._source = units.local
        self._target = units.local
        self._message = messages.local_timestamp
        self._id = 255
        self._size = 4
        self._timestamp = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
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
def id_to_receiver(id):
    if id == 0:
        receiver = altitude_from_test_to_test()
        return receiver
    if id == 1:
        receiver = acceleration_from_test_to_test()
        return receiver
    if id == 2:
        receiver = pressure_from_test_to_test()
        return receiver
    if id == 3:
        receiver = catastrophe_from_test_to_test()
        return receiver
    if id == 4:
        receiver = gyro_from_test_to_test()
        return receiver
    if id == 16:
        receiver = time_sync_from_ground_station_to_flight_controller()
        return receiver
    if id == 17:
        receiver = set_power_mode_from_ground_station_to_flight_controller()
        return receiver
    if id == 18:
        receiver = set_radio_equipment_from_ground_station_to_flight_controller()
        return receiver
    if id == 19:
        receiver = set_parachute_output_from_ground_station_to_flight_controller()
        return receiver
    if id == 20:
        receiver = set_data_logging_from_ground_station_to_flight_controller()
        return receiver
    if id == 21:
        receiver = dump_flash_from_ground_station_to_flight_controller()
        return receiver
    if id == 22:
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
        receiver = gnss_data_from_flight_controller_to_ground_station()
        return receiver
    if id == 38:
        receiver = flight_controller_status_from_flight_controller_to_ground_station()
        return receiver
    if id == 39:
        receiver = return_data_logging_from_flight_controller_to_ground_station()
        return receiver
    if id == 40:
        receiver = return_dump_flash_from_flight_controller_to_ground_station()
        return receiver
    if id == 41:
        receiver = return_handshake_from_flight_controller_to_ground_station()
        return receiver
    if id == 64:
        receiver = ms_since_boot_from_test_to_test()
        return receiver
    if id == 80:
        receiver = ms_since_boot_from_flight_controller_to_ground_station()
        return receiver
    if id == 81:
        receiver = us_since_boot_from_flight_controller_to_ground_station()
        return receiver
    if id == 82:
        receiver = current_time_from_flight_controller_to_ground_station()
        return receiver
    if id == 83:
        receiver = GNSS_data_1_from_flight_controller_to_ground_station()
        return receiver
    if id == 84:
        receiver = GNSS_data_2_from_flight_controller_to_ground_station()
        return receiver
    if id == 85:
        receiver = inside_static_temperature_from_flight_controller_to_ground_station()
        return receiver
    if id == 86:
        receiver = inside_static_pressure_from_flight_controller_to_ground_station()
        return receiver
    if id == 87:
        receiver = IMU1_from_flight_controller_to_ground_station()
        return receiver
    if id == 88:
        receiver = IMU2_from_flight_controller_to_ground_station()
        return receiver
    if id == 255:
        receiver = local_timestamp_from_local_to_local()
        return receiver
