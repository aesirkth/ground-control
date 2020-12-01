from utils.serial_wrapper import SerialReader
from utils.data_handling import *
from utils.definitions import *


#functions to decode data, defined further down
decoding_definitions = {}

####
#class to handle all telemetry things
####
# self.data[*source*] - contains all the decoded data in TimeSeries
# self.clocks[*source*] - contains the ms_since_boot converted to seconds in a RelativeTime class
# source can be "flight" or "engine"
class Telemetry(SerialReader):
    def __init__(self):
        super().__init__("RFD", decoding_definitions)


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
decoding_definitions[ID_FLIGHT_CONTROLLER_STATUS_TM_FC] = [
    BitDecoder("flight", [
        "is_parachute_armed",
        "is_parachute_1_en",
        "is_parachute_2_en",
        "is_fpv_en",
        "is_telemetry_en"
    ]),
    BitDecoder("flight", [
        #todo, software state
    ]),
    BitDecoder("flight", [
        #todo. mission state
    ]),
]


####################### dummy functions
decoding_definitions[0x00] = [Decoder("flight", "<H", "altitude")]
decoding_definitions[0x01] = [Decoder("flight", "<B", "acceleration")]
decoding_definitions[0x02] = [Decoder("flight", "<H", "pressure")]
decoding_definitions[0x03] = [BitDecoder("engine", ["catastrophe"])]
decoding_definitions[0x04] = xyzDecoder("flight", "<B", "gyro")
