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

class units(Enum):
    local = 0
    test = 1
    ground_station = 2
    flight_controller_tc = 3
    flight_controller = 4
    ground_station_tc = 5
    ground_station_tm = 6
class datatypes(Enum):
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
class altitude_from_test_to_test:
    def __init__(self):
        self._source = units.test
        self._target = units.test
        self._datatype = datatypes.altitude
        self._id = 0
        self._size = 2
        self._altitude = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def set_altitude(self, value):
        self._altitude = value
    def get_buf(self):
        buf = b""
        buf += struct.pack("<H", self._altitude)
        return buf
class acceleration_from_test_to_test:
    def __init__(self):
        self._source = units.test
        self._target = units.test
        self._datatype = datatypes.acceleration
        self._id = 1
        self._size = 1
        self._altitude = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def set_altitude(self, value):
        self._altitude = value
    def get_buf(self):
        buf = b""
        buf += struct.pack("<B", self._altitude)
        return buf
class pressure_from_test_to_test:
    def __init__(self):
        self._source = units.test
        self._target = units.test
        self._datatype = datatypes.pressure
        self._id = 2
        self._size = 2
        self._altitude = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def set_altitude(self, value):
        self._altitude = value
    def get_buf(self):
        buf = b""
        buf += struct.pack("<H", self._altitude)
        return buf
class catastrophe_from_test_to_test:
    def __init__(self):
        self._source = units.test
        self._target = units.test
        self._datatype = datatypes.catastrophe
        self._id = 3
        self._size = 1
        self._bit_field = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def set_catastrophe(self, value):
        self._bit_field =  value * (self._bit_field | (1 << 0)) + (not value) * (self._bit_field & ~(1 << 0))
    def get_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bit_field)
        return buf
class gyro_from_test_to_test:
    def __init__(self):
        self._source = units.test
        self._target = units.test
        self._datatype = datatypes.gyro
        self._id = 4
        self._size = 3
        self._x = 0
        self._y = 0
        self._z = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
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
    def get_buf(self):
        buf = b""
        buf += struct.pack("<B", self._x)
        buf += struct.pack("<B", self._y)
        buf += struct.pack("<B", self._z)
        return buf
class time_sync_from_ground_station_to_flight_controller_tc:
    def __init__(self):
        self._source = units.ground_station
        self._target = units.flight_controller_tc
        self._datatype = datatypes.time_sync
        self._id = 16
        self._size = 4
        self._system_time = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def set_system_time(self, value):
        self._system_time = value
    def get_buf(self):
        buf = b""
        buf += struct.pack("<L", self._system_time)
        return buf
class set_power_mode_from_ground_station_to_flight_controller_tc:
    def __init__(self):
        self._source = units.ground_station
        self._target = units.flight_controller_tc
        self._datatype = datatypes.set_power_mode
        self._id = 17
        self._size = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def get_buf(self):
        buf = b""
        return buf
class set_radio_equipment_from_ground_station_to_flight_controller_tc:
    def __init__(self):
        self._source = units.ground_station
        self._target = units.flight_controller_tc
        self._datatype = datatypes.set_radio_equipment
        self._id = 18
        self._size = 1
        self._bit_field = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def set_is_fpv_en(self, value):
        self._bit_field =  value * (self._bit_field | (1 << 0)) + (not value) * (self._bit_field & ~(1 << 0))
    def set_is_tm_en(self, value):
        self._bit_field =  value * (self._bit_field | (1 << 1)) + (not value) * (self._bit_field & ~(1 << 1))
    def get_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bit_field)
        return buf
class set_parachute_output_from_ground_station_to_flight_controller_tc:
    def __init__(self):
        self._source = units.ground_station
        self._target = units.flight_controller_tc
        self._datatype = datatypes.set_parachute_output
        self._id = 19
        self._size = 1
        self._bit_field = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
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
    def get_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bit_field)
        return buf
class set_data_logging_from_ground_station_to_flight_controller_tc:
    def __init__(self):
        self._source = units.ground_station
        self._target = units.flight_controller_tc
        self._datatype = datatypes.set_data_logging
        self._id = 20
        self._size = 1
        self._bit_field = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def set_is_logging_en(self, value):
        self._bit_field =  value * (self._bit_field | (1 << 0)) + (not value) * (self._bit_field & ~(1 << 0))
    def get_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bit_field)
        return buf
class dump_flash_from_ground_station_to_flight_controller_tc:
    def __init__(self):
        self._source = units.ground_station
        self._target = units.flight_controller_tc
        self._datatype = datatypes.dump_flash
        self._id = 21
        self._size = 1
        self._bit_field = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def set_dump_sd(self, value):
        self._bit_field =  value * (self._bit_field | (1 << 0)) + (not value) * (self._bit_field & ~(1 << 0))
    def set_dump_usb(self, value):
        self._bit_field =  value * (self._bit_field | (1 << 1)) + (not value) * (self._bit_field & ~(1 << 1))
    def get_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bit_field)
        return buf
class handshake_from_ground_station_to_flight_controller_tc:
    def __init__(self):
        self._source = units.ground_station
        self._target = units.flight_controller_tc
        self._datatype = datatypes.handshake
        self._id = 22
        self._size = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def get_buf(self):
        buf = b""
        return buf
class return_time_sync_from_flight_controller_to_ground_station_tc:
    def __init__(self):
        self._source = units.flight_controller
        self._target = units.ground_station_tc
        self._datatype = datatypes.return_time_sync
        self._id = 32
        self._size = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def get_buf(self):
        buf = b""
        return buf
class return_power_mode_from_flight_controller_to_ground_station_tc:
    def __init__(self):
        self._source = units.flight_controller
        self._target = units.ground_station_tc
        self._datatype = datatypes.return_power_mode
        self._id = 33
        self._size = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def get_buf(self):
        buf = b""
        return buf
class return_radio_equipment_from_flight_controller_to_ground_station_tc:
    def __init__(self):
        self._source = units.flight_controller
        self._target = units.ground_station_tc
        self._datatype = datatypes.return_radio_equipment
        self._id = 34
        self._size = 1
        self._bit_field = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def set_is_fpv_en(self, value):
        self._bit_field =  value * (self._bit_field | (1 << 0)) + (not value) * (self._bit_field & ~(1 << 0))
    def set_is_tm_en(self, value):
        self._bit_field =  value * (self._bit_field | (1 << 1)) + (not value) * (self._bit_field & ~(1 << 1))
    def get_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bit_field)
        return buf
class return_parachute_output_from_flight_controller_to_ground_station_tc:
    def __init__(self):
        self._source = units.flight_controller
        self._target = units.ground_station_tc
        self._datatype = datatypes.return_parachute_output
        self._id = 35
        self._size = 1
        self._bit_field = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
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
    def get_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bit_field)
        return buf
class onboard_battery_voltage_from_flight_controller_to_ground_station_tc:
    def __init__(self):
        self._source = units.flight_controller
        self._target = units.ground_station_tc
        self._datatype = datatypes.onboard_battery_voltage
        self._id = 36
        self._size = 4
        self._battery_1 = 0
        self._battery_2 = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def set_battery_1(self, value):
        self._battery_1 = scaledFloat_to_uint(value, 100)
    def set_battery_2(self, value):
        self._battery_2 = scaledFloat_to_uint(value, 100)
    def get_buf(self):
        buf = b""
        buf += struct.pack("<H", self._battery_1)
        buf += struct.pack("<H", self._battery_2)
        return buf
class gnss_data_from_flight_controller_to_ground_station_tc:
    def __init__(self):
        self._source = units.flight_controller
        self._target = units.ground_station_tc
        self._datatype = datatypes.gnss_data
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
    def get_datatype(self):
        return self._datatype
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
    def get_buf(self):
        buf = b""
        buf += struct.pack("<L", self._gnss_time)
        buf += struct.pack("<l", self._latitude)
        buf += struct.pack("<l", self._longitude)
        buf += struct.pack("<H", self._h_dop)
        buf += struct.pack("<B", self._n_satellites)
        return buf
class flight_controller_status_from_flight_controller_to_ground_station_tc:
    def __init__(self):
        self._source = units.flight_controller
        self._target = units.ground_station_tc
        self._datatype = datatypes.flight_controller_status
        self._id = 38
        self._size = 3
        self._HW_state = 0
        self._SW_state = 0
        self._mission_state = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
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
    def get_buf(self):
        buf = b""
        buf += struct.pack("<B", self._HW_state)
        buf += struct.pack("<B", self._SW_state)
        buf += struct.pack("<B", self._mission_state)
        return buf
class return_data_logging_from_flight_controller_to_ground_station_tc:
    def __init__(self):
        self._source = units.flight_controller
        self._target = units.ground_station_tc
        self._datatype = datatypes.return_data_logging
        self._id = 39
        self._size = 1
        self._bit_field = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def set_is_logging_en(self, value):
        self._bit_field =  value * (self._bit_field | (1 << 0)) + (not value) * (self._bit_field & ~(1 << 0))
    def get_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bit_field)
        return buf
class return_dump_flash_from_flight_controller_to_ground_station_tc:
    def __init__(self):
        self._source = units.flight_controller
        self._target = units.ground_station_tc
        self._datatype = datatypes.return_dump_flash
        self._id = 40
        self._size = 1
        self._bit_field = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def set_dump_sd(self, value):
        self._bit_field =  value * (self._bit_field | (1 << 0)) + (not value) * (self._bit_field & ~(1 << 0))
    def set_dump_usb(self, value):
        self._bit_field =  value * (self._bit_field | (1 << 1)) + (not value) * (self._bit_field & ~(1 << 1))
    def get_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bit_field)
        return buf
class return_handshake_from_flight_controller_to_ground_station_tc:
    def __init__(self):
        self._source = units.flight_controller
        self._target = units.ground_station_tc
        self._datatype = datatypes.return_handshake
        self._id = 41
        self._size = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def get_buf(self):
        buf = b""
        return buf
class ms_since_boot_from_local_to_local:
    def __init__(self):
        self._source = units.local
        self._target = units.local
        self._datatype = datatypes.ms_since_boot
        self._id = 64
        self._size = 4
        self._ms_since_boot = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def set_ms_since_boot(self, value):
        self._ms_since_boot = value
    def get_buf(self):
        buf = b""
        buf += struct.pack("<L", self._ms_since_boot)
        return buf
class ms_since_boot_from_flight_controller_to_ground_station_tm:
    def __init__(self):
        self._source = units.flight_controller
        self._target = units.ground_station_tm
        self._datatype = datatypes.ms_since_boot
        self._id = 80
        self._size = 4
        self._ms_since_boot = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def set_ms_since_boot(self, value):
        self._ms_since_boot = value
    def get_buf(self):
        buf = b""
        buf += struct.pack("<L", self._ms_since_boot)
        return buf
class us_since_boot_from_flight_controller_to_ground_station_tm:
    def __init__(self):
        self._source = units.flight_controller
        self._target = units.ground_station_tm
        self._datatype = datatypes.us_since_boot
        self._id = 81
        self._size = 4
        self._us_since_boot = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def set_us_since_boot(self, value):
        self._us_since_boot = value
    def get_buf(self):
        buf = b""
        buf += struct.pack("<L", self._us_since_boot)
        return buf
class current_time_from_flight_controller_to_ground_station_tm:
    def __init__(self):
        self._source = units.flight_controller
        self._target = units.ground_station_tm
        self._datatype = datatypes.current_time
        self._id = 82
        self._size = 4
        self._ms_since_boot = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def set_ms_since_boot(self, value):
        self._ms_since_boot = value
    def get_buf(self):
        buf = b""
        buf += struct.pack("<L", self._ms_since_boot)
        return buf
class GNSS_data_1_from_flight_controller_to_ground_station_tm:
    def __init__(self):
        self._source = units.flight_controller
        self._target = units.ground_station_tm
        self._datatype = datatypes.GNSS_data_1
        self._id = 83
        self._size = 12
        self._gnss_time = 0
        self._latitude = 0
        self._longitude = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
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
    def get_buf(self):
        buf = b""
        buf += struct.pack("<L", self._gnss_time)
        buf += struct.pack("<l", self._latitude)
        buf += struct.pack("<l", self._longitude)
        return buf
class local_timestamp_from_local_to_local:
    def __init__(self):
        self._source = units.local
        self._target = units.local
        self._datatype = datatypes.local_timestamp
        self._id = 255
        self._size = 4
        self._timestamp = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def set_timestamp(self, value):
        self._timestamp = value
    def get_buf(self):
        buf = b""
        buf += struct.pack("<L", self._timestamp)
        return buf
class altitude:
    def __init__(self):
        self._source = 0
        self._target = 0
        self._datatype = 0
        self._id = 0
        self._size = 2
        self._altitude = 0
    def set_source(self, value):
        self._source = value
    def set_target(self, value):
        self._target = value
    def set_datatype(self, value):
        self._datatype = value
    def set_id(self, value):
        self._id = value
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_size(self):
        return self._size
    def get_id(self):
        return self._id
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
class acceleration:
    def __init__(self):
        self._source = 0
        self._target = 0
        self._datatype = 0
        self._id = 0
        self._size = 1
        self._altitude = 0
    def set_source(self, value):
        self._source = value
    def set_target(self, value):
        self._target = value
    def set_datatype(self, value):
        self._datatype = value
    def set_id(self, value):
        self._id = value
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_size(self):
        return self._size
    def get_id(self):
        return self._id
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
class pressure:
    def __init__(self):
        self._source = 0
        self._target = 0
        self._datatype = 0
        self._id = 0
        self._size = 2
        self._altitude = 0
    def set_source(self, value):
        self._source = value
    def set_target(self, value):
        self._target = value
    def set_datatype(self, value):
        self._datatype = value
    def set_id(self, value):
        self._id = value
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_size(self):
        return self._size
    def get_id(self):
        return self._id
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
class catastrophe:
    def __init__(self):
        self._source = 0
        self._target = 0
        self._datatype = 0
        self._id = 0
        self._size = 1
        self._bit_field = 0
    def set_source(self, value):
        self._source = value
    def set_target(self, value):
        self._target = value
    def set_datatype(self, value):
        self._datatype = value
    def set_id(self, value):
        self._id = value
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_size(self):
        return self._size
    def get_id(self):
        return self._id
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
class gyro:
    def __init__(self):
        self._source = 0
        self._target = 0
        self._datatype = 0
        self._id = 0
        self._size = 3
        self._x = 0
        self._y = 0
        self._z = 0
    def set_source(self, value):
        self._source = value
    def set_target(self, value):
        self._target = value
    def set_datatype(self, value):
        self._datatype = value
    def set_id(self, value):
        self._id = value
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_size(self):
        return self._size
    def get_id(self):
        return self._id
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
class time_sync:
    def __init__(self):
        self._source = 0
        self._target = 0
        self._datatype = 0
        self._id = 0
        self._size = 4
        self._system_time = 0
    def set_source(self, value):
        self._source = value
    def set_target(self, value):
        self._target = value
    def set_datatype(self, value):
        self._datatype = value
    def set_id(self, value):
        self._id = value
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_size(self):
        return self._size
    def get_id(self):
        return self._id
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
class set_power_mode:
    def __init__(self):
        self._source = 0
        self._target = 0
        self._datatype = 0
        self._id = 0
        self._size = 0
    def set_source(self, value):
        self._source = value
    def set_target(self, value):
        self._target = value
    def set_datatype(self, value):
        self._datatype = value
    def set_id(self, value):
        self._id = value
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_size(self):
        return self._size
    def get_id(self):
        return self._id
    def get_all_data(self):
        data = []
        return data
    def parse_buf(self, buf):
        index = 0
        return
class set_radio_equipment:
    def __init__(self):
        self._source = 0
        self._target = 0
        self._datatype = 0
        self._id = 0
        self._size = 1
        self._bit_field = 0
    def set_source(self, value):
        self._source = value
    def set_target(self, value):
        self._target = value
    def set_datatype(self, value):
        self._datatype = value
    def set_id(self, value):
        self._id = value
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_size(self):
        return self._size
    def get_id(self):
        return self._id
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
class set_parachute_output:
    def __init__(self):
        self._source = 0
        self._target = 0
        self._datatype = 0
        self._id = 0
        self._size = 1
        self._bit_field = 0
    def set_source(self, value):
        self._source = value
    def set_target(self, value):
        self._target = value
    def set_datatype(self, value):
        self._datatype = value
    def set_id(self, value):
        self._id = value
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_size(self):
        return self._size
    def get_id(self):
        return self._id
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
class set_data_logging:
    def __init__(self):
        self._source = 0
        self._target = 0
        self._datatype = 0
        self._id = 0
        self._size = 1
        self._bit_field = 0
    def set_source(self, value):
        self._source = value
    def set_target(self, value):
        self._target = value
    def set_datatype(self, value):
        self._datatype = value
    def set_id(self, value):
        self._id = value
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_size(self):
        return self._size
    def get_id(self):
        return self._id
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
class dump_flash:
    def __init__(self):
        self._source = 0
        self._target = 0
        self._datatype = 0
        self._id = 0
        self._size = 1
        self._bit_field = 0
    def set_source(self, value):
        self._source = value
    def set_target(self, value):
        self._target = value
    def set_datatype(self, value):
        self._datatype = value
    def set_id(self, value):
        self._id = value
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_size(self):
        return self._size
    def get_id(self):
        return self._id
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
class handshake:
    def __init__(self):
        self._source = 0
        self._target = 0
        self._datatype = 0
        self._id = 0
        self._size = 0
    def set_source(self, value):
        self._source = value
    def set_target(self, value):
        self._target = value
    def set_datatype(self, value):
        self._datatype = value
    def set_id(self, value):
        self._id = value
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_size(self):
        return self._size
    def get_id(self):
        return self._id
    def get_all_data(self):
        data = []
        return data
    def parse_buf(self, buf):
        index = 0
        return
class return_time_sync:
    def __init__(self):
        self._source = 0
        self._target = 0
        self._datatype = 0
        self._id = 0
        self._size = 0
    def set_source(self, value):
        self._source = value
    def set_target(self, value):
        self._target = value
    def set_datatype(self, value):
        self._datatype = value
    def set_id(self, value):
        self._id = value
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_size(self):
        return self._size
    def get_id(self):
        return self._id
    def get_all_data(self):
        data = []
        return data
    def parse_buf(self, buf):
        index = 0
        return
class return_power_mode:
    def __init__(self):
        self._source = 0
        self._target = 0
        self._datatype = 0
        self._id = 0
        self._size = 0
    def set_source(self, value):
        self._source = value
    def set_target(self, value):
        self._target = value
    def set_datatype(self, value):
        self._datatype = value
    def set_id(self, value):
        self._id = value
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_size(self):
        return self._size
    def get_id(self):
        return self._id
    def get_all_data(self):
        data = []
        return data
    def parse_buf(self, buf):
        index = 0
        return
class return_radio_equipment:
    def __init__(self):
        self._source = 0
        self._target = 0
        self._datatype = 0
        self._id = 0
        self._size = 1
        self._bit_field = 0
    def set_source(self, value):
        self._source = value
    def set_target(self, value):
        self._target = value
    def set_datatype(self, value):
        self._datatype = value
    def set_id(self, value):
        self._id = value
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_size(self):
        return self._size
    def get_id(self):
        return self._id
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
class return_parachute_output:
    def __init__(self):
        self._source = 0
        self._target = 0
        self._datatype = 0
        self._id = 0
        self._size = 1
        self._bit_field = 0
    def set_source(self, value):
        self._source = value
    def set_target(self, value):
        self._target = value
    def set_datatype(self, value):
        self._datatype = value
    def set_id(self, value):
        self._id = value
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_size(self):
        return self._size
    def get_id(self):
        return self._id
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
class onboard_battery_voltage:
    def __init__(self):
        self._source = 0
        self._target = 0
        self._datatype = 0
        self._id = 0
        self._size = 4
        self._battery_1 = 0
        self._battery_2 = 0
    def set_source(self, value):
        self._source = value
    def set_target(self, value):
        self._target = value
    def set_datatype(self, value):
        self._datatype = value
    def set_id(self, value):
        self._id = value
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_size(self):
        return self._size
    def get_id(self):
        return self._id
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
class gnss_data:
    def __init__(self):
        self._source = 0
        self._target = 0
        self._datatype = 0
        self._id = 0
        self._size = 15
        self._gnss_time = 0
        self._latitude = 0
        self._longitude = 0
        self._h_dop = 0
        self._n_satellites = 0
    def set_source(self, value):
        self._source = value
    def set_target(self, value):
        self._target = value
    def set_datatype(self, value):
        self._datatype = value
    def set_id(self, value):
        self._id = value
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_size(self):
        return self._size
    def get_id(self):
        return self._id
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
class flight_controller_status:
    def __init__(self):
        self._source = 0
        self._target = 0
        self._datatype = 0
        self._id = 0
        self._size = 3
        self._HW_state = 0
        self._SW_state = 0
        self._mission_state = 0
    def set_source(self, value):
        self._source = value
    def set_target(self, value):
        self._target = value
    def set_datatype(self, value):
        self._datatype = value
    def set_id(self, value):
        self._id = value
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_size(self):
        return self._size
    def get_id(self):
        return self._id
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
class return_data_logging:
    def __init__(self):
        self._source = 0
        self._target = 0
        self._datatype = 0
        self._id = 0
        self._size = 1
        self._bit_field = 0
    def set_source(self, value):
        self._source = value
    def set_target(self, value):
        self._target = value
    def set_datatype(self, value):
        self._datatype = value
    def set_id(self, value):
        self._id = value
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_size(self):
        return self._size
    def get_id(self):
        return self._id
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
class return_dump_flash:
    def __init__(self):
        self._source = 0
        self._target = 0
        self._datatype = 0
        self._id = 0
        self._size = 1
        self._bit_field = 0
    def set_source(self, value):
        self._source = value
    def set_target(self, value):
        self._target = value
    def set_datatype(self, value):
        self._datatype = value
    def set_id(self, value):
        self._id = value
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_size(self):
        return self._size
    def get_id(self):
        return self._id
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
class return_handshake:
    def __init__(self):
        self._source = 0
        self._target = 0
        self._datatype = 0
        self._id = 0
        self._size = 0
    def set_source(self, value):
        self._source = value
    def set_target(self, value):
        self._target = value
    def set_datatype(self, value):
        self._datatype = value
    def set_id(self, value):
        self._id = value
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_size(self):
        return self._size
    def get_id(self):
        return self._id
    def get_all_data(self):
        data = []
        return data
    def parse_buf(self, buf):
        index = 0
        return
class ms_since_boot:
    def __init__(self):
        self._source = 0
        self._target = 0
        self._datatype = 0
        self._id = 0
        self._size = 4
        self._ms_since_boot = 0
    def set_source(self, value):
        self._source = value
    def set_target(self, value):
        self._target = value
    def set_datatype(self, value):
        self._datatype = value
    def set_id(self, value):
        self._id = value
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_size(self):
        return self._size
    def get_id(self):
        return self._id
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
class ms_since_boot:
    def __init__(self):
        self._source = 0
        self._target = 0
        self._datatype = 0
        self._id = 0
        self._size = 4
        self._ms_since_boot = 0
    def set_source(self, value):
        self._source = value
    def set_target(self, value):
        self._target = value
    def set_datatype(self, value):
        self._datatype = value
    def set_id(self, value):
        self._id = value
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_size(self):
        return self._size
    def get_id(self):
        return self._id
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
class us_since_boot:
    def __init__(self):
        self._source = 0
        self._target = 0
        self._datatype = 0
        self._id = 0
        self._size = 4
        self._us_since_boot = 0
    def set_source(self, value):
        self._source = value
    def set_target(self, value):
        self._target = value
    def set_datatype(self, value):
        self._datatype = value
    def set_id(self, value):
        self._id = value
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_size(self):
        return self._size
    def get_id(self):
        return self._id
    def get_us_since_boot(self):
        return self._us_since_boot
    def get_all_data(self):
        data = []
        data.append((fields.us_since_boot, self.get_us_since_boot()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._us_since_boot = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class current_time:
    def __init__(self):
        self._source = 0
        self._target = 0
        self._datatype = 0
        self._id = 0
        self._size = 4
        self._ms_since_boot = 0
    def set_source(self, value):
        self._source = value
    def set_target(self, value):
        self._target = value
    def set_datatype(self, value):
        self._datatype = value
    def set_id(self, value):
        self._id = value
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_size(self):
        return self._size
    def get_id(self):
        return self._id
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
class GNSS_data_1:
    def __init__(self):
        self._source = 0
        self._target = 0
        self._datatype = 0
        self._id = 0
        self._size = 12
        self._gnss_time = 0
        self._latitude = 0
        self._longitude = 0
    def set_source(self, value):
        self._source = value
    def set_target(self, value):
        self._target = value
    def set_datatype(self, value):
        self._datatype = value
    def set_id(self, value):
        self._id = value
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_size(self):
        return self._size
    def get_id(self):
        return self._id
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
class local_timestamp:
    def __init__(self):
        self._source = 0
        self._target = 0
        self._datatype = 0
        self._id = 0
        self._size = 4
        self._timestamp = 0
    def set_source(self, value):
        self._source = value
    def set_target(self, value):
        self._target = value
    def set_datatype(self, value):
        self._datatype = value
    def set_id(self, value):
        self._id = value
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_datatype(self):
        return self._datatype
    def get_size(self):
        return self._size
    def get_id(self):
        return self._id
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
        receiver = altitude()
        receiver.set_id(0)
        receiver.set_target(units.test)
        receiver.set_source(units.test)
        receiver.set_datatype(datatypes.altitude)
        return receiver
    if id == 1:
        receiver = acceleration()
        receiver.set_id(1)
        receiver.set_target(units.test)
        receiver.set_source(units.test)
        receiver.set_datatype(datatypes.acceleration)
        return receiver
    if id == 2:
        receiver = pressure()
        receiver.set_id(2)
        receiver.set_target(units.test)
        receiver.set_source(units.test)
        receiver.set_datatype(datatypes.pressure)
        return receiver
    if id == 3:
        receiver = catastrophe()
        receiver.set_id(3)
        receiver.set_target(units.test)
        receiver.set_source(units.test)
        receiver.set_datatype(datatypes.catastrophe)
        return receiver
    if id == 4:
        receiver = gyro()
        receiver.set_id(4)
        receiver.set_target(units.test)
        receiver.set_source(units.test)
        receiver.set_datatype(datatypes.gyro)
        return receiver
    if id == 16:
        receiver = time_sync()
        receiver.set_id(16)
        receiver.set_target(units.flight_controller_tc)
        receiver.set_source(units.ground_station)
        receiver.set_datatype(datatypes.time_sync)
        return receiver
    if id == 17:
        receiver = set_power_mode()
        receiver.set_id(17)
        receiver.set_target(units.flight_controller_tc)
        receiver.set_source(units.ground_station)
        receiver.set_datatype(datatypes.set_power_mode)
        return receiver
    if id == 18:
        receiver = set_radio_equipment()
        receiver.set_id(18)
        receiver.set_target(units.flight_controller_tc)
        receiver.set_source(units.ground_station)
        receiver.set_datatype(datatypes.set_radio_equipment)
        return receiver
    if id == 19:
        receiver = set_parachute_output()
        receiver.set_id(19)
        receiver.set_target(units.flight_controller_tc)
        receiver.set_source(units.ground_station)
        receiver.set_datatype(datatypes.set_parachute_output)
        return receiver
    if id == 20:
        receiver = set_data_logging()
        receiver.set_id(20)
        receiver.set_target(units.flight_controller_tc)
        receiver.set_source(units.ground_station)
        receiver.set_datatype(datatypes.set_data_logging)
        return receiver
    if id == 21:
        receiver = dump_flash()
        receiver.set_id(21)
        receiver.set_target(units.flight_controller_tc)
        receiver.set_source(units.ground_station)
        receiver.set_datatype(datatypes.dump_flash)
        return receiver
    if id == 22:
        receiver = handshake()
        receiver.set_id(22)
        receiver.set_target(units.flight_controller_tc)
        receiver.set_source(units.ground_station)
        receiver.set_datatype(datatypes.handshake)
        return receiver
    if id == 32:
        receiver = return_time_sync()
        receiver.set_id(32)
        receiver.set_target(units.ground_station_tc)
        receiver.set_source(units.flight_controller)
        receiver.set_datatype(datatypes.return_time_sync)
        return receiver
    if id == 33:
        receiver = return_power_mode()
        receiver.set_id(33)
        receiver.set_target(units.ground_station_tc)
        receiver.set_source(units.flight_controller)
        receiver.set_datatype(datatypes.return_power_mode)
        return receiver
    if id == 34:
        receiver = return_radio_equipment()
        receiver.set_id(34)
        receiver.set_target(units.ground_station_tc)
        receiver.set_source(units.flight_controller)
        receiver.set_datatype(datatypes.return_radio_equipment)
        return receiver
    if id == 35:
        receiver = return_parachute_output()
        receiver.set_id(35)
        receiver.set_target(units.ground_station_tc)
        receiver.set_source(units.flight_controller)
        receiver.set_datatype(datatypes.return_parachute_output)
        return receiver
    if id == 36:
        receiver = onboard_battery_voltage()
        receiver.set_id(36)
        receiver.set_target(units.ground_station_tc)
        receiver.set_source(units.flight_controller)
        receiver.set_datatype(datatypes.onboard_battery_voltage)
        return receiver
    if id == 37:
        receiver = gnss_data()
        receiver.set_id(37)
        receiver.set_target(units.ground_station_tc)
        receiver.set_source(units.flight_controller)
        receiver.set_datatype(datatypes.gnss_data)
        return receiver
    if id == 38:
        receiver = flight_controller_status()
        receiver.set_id(38)
        receiver.set_target(units.ground_station_tc)
        receiver.set_source(units.flight_controller)
        receiver.set_datatype(datatypes.flight_controller_status)
        return receiver
    if id == 39:
        receiver = return_data_logging()
        receiver.set_id(39)
        receiver.set_target(units.ground_station_tc)
        receiver.set_source(units.flight_controller)
        receiver.set_datatype(datatypes.return_data_logging)
        return receiver
    if id == 40:
        receiver = return_dump_flash()
        receiver.set_id(40)
        receiver.set_target(units.ground_station_tc)
        receiver.set_source(units.flight_controller)
        receiver.set_datatype(datatypes.return_dump_flash)
        return receiver
    if id == 41:
        receiver = return_handshake()
        receiver.set_id(41)
        receiver.set_target(units.ground_station_tc)
        receiver.set_source(units.flight_controller)
        receiver.set_datatype(datatypes.return_handshake)
        return receiver
    if id == 64:
        receiver = ms_since_boot()
        receiver.set_id(64)
        receiver.set_target(units.local)
        receiver.set_source(units.local)
        receiver.set_datatype(datatypes.ms_since_boot)
        return receiver
    if id == 80:
        receiver = ms_since_boot()
        receiver.set_id(80)
        receiver.set_target(units.ground_station_tm)
        receiver.set_source(units.flight_controller)
        receiver.set_datatype(datatypes.ms_since_boot)
        return receiver
    if id == 81:
        receiver = us_since_boot()
        receiver.set_id(81)
        receiver.set_target(units.ground_station_tm)
        receiver.set_source(units.flight_controller)
        receiver.set_datatype(datatypes.us_since_boot)
        return receiver
    if id == 82:
        receiver = current_time()
        receiver.set_id(82)
        receiver.set_target(units.ground_station_tm)
        receiver.set_source(units.flight_controller)
        receiver.set_datatype(datatypes.current_time)
        return receiver
    if id == 83:
        receiver = GNSS_data_1()
        receiver.set_id(83)
        receiver.set_target(units.ground_station_tm)
        receiver.set_source(units.flight_controller)
        receiver.set_datatype(datatypes.GNSS_data_1)
        return receiver
    if id == 255:
        receiver = local_timestamp()
        receiver.set_id(255)
        receiver.set_target(units.local)
        receiver.set_source(units.local)
        receiver.set_datatype(datatypes.local_timestamp)
        return receiver
