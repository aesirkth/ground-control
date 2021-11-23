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

class fields(Enum):
    current_time_ms = 0
    current_time_us = 1
    debug_messages_mode = 2
    debug_status_leds_mode = 3
    uptime_ms = 4
    max_tx_queue_size = 5
    max_rx_queue_size = 6
    mean_tx_queue_size = 7
    mean_rx_queue_size = 8
    round_trip_time_us = 9
    destination_node = 10
    receiver_node = 11
    debug_mode = 12
    powercan_channel = 13
    edda_signature = 14
    request = 15
    system_state = 16
    gate_state = 17
    response = 18
    result = 19
    checks_failed = 20
    checks_performed = 21
    total_checks = 22
    w = 23
    e = 24
    n = 25
    h = 26
    o = 27
    p = 28
    r = 29
    b = 30
    i = 31
    t = 32
    current_ampere = 33
    voltage_volt = 34
    power_watt = 35
    error = 36
    sensor_index = 37
    temperature_celsius = 38
    measurement_index = 39
    pressure_pascal = 40
    pressure_mbar = 41
    coefficient_number = 42
    coefficient_value = 43
    board_index = 44
    resistance_ohm = 45
    ratio_fraction = 46
    relative_humidity_percentage = 47
    is_heater_on = 48
    acceleration_x_gforce = 49
    acceleration_y_gforce = 50
    acceleration_z_gforce = 51
    sign = 52
    ambient_light_lux = 53
    type = 54
    thread = 55
    task_time_us = 56
    truncated_start_time_us = 57
    loop_time_us = 58
    bus = 59
    position_on_board = 60
    serial_byte0 = 61
    serial_byte1 = 62
    serial_byte2 = 63
    serial_byte3 = 64
    serial_byte4 = 65
    serial_byte5 = 66
    found_family_code = 67
    found_crc = 68
    kind = 69
    channel = 70
    measurement_reference = 71
    failure_reason = 72
    value = 73
    threshold = 74
    validity = 75
    reference_voltage_volt = 76
    differential_voltage_volt = 77
    positive_voltage_volt = 78
    negative_voltage_volt = 79
    frequency_hertz = 80
    found_device_address = 81
    missing_device_address = 82
    devices_successfully_found = 83
    addresses_with_error = 84
    search_time_us = 85
    location = 86
    register_address = 87
    read_data = 88
    write_data = 89
    expected_data = 90
    scanned_address = 91
    warning_count = 92
    error_count = 93
    bus_index = 94
    position_on_bus = 95
    byte0 = 96
    start_time_ms = 97
    byte1 = 98
    searched_family_code = 99
    devices_insuccessfully_found = 100
    search_time_ms = 101
    byte2 = 102
    raw_fault_register = 103
    byte3 = 104
    byte4 = 105
    byte5 = 106
    byte6 = 107
class messages(Enum):
    CurrentTimePing = 0
    CurrentTimePong = 1
    SayHi = 2
    Hello = 3
    CanStatistics = 4
    CanLatency = 5
    SetDebugStatusLedsModeRequest = 6
    SetDebugMessagesModeRequest = 7
    PowerCAN_SetDebugMode = 8
    PowerCAN_GetState = 9
    PowerCAN_TransitionRequest = 10
    PowerCAN_Hello = 11
    PowerCAN_CurrentState = 12
    PowerCAN_TransitionResponse = 13
    PowerCAN_CheckResult = 14
    WenHop = 15
    WenOrbit = 16
    PowerInputMeasurement = 17
    PowerInputMeasurementError = 18
    ColdSideTemperature = 19
    RawTransducerVoltage = 20
    TransducerPressure = 21
    TransducerError = 22
    AmbientPressure = 23
    AmbientPressureCoefficient = 24
    AmbientPressureError = 25
    PlatinumSensorTemperature = 26
    PlatinumSensorResistance = 27
    PlatinumSensorRatio = 28
    ThermocoupleTypeKTemperature = 29
    ThermocoupleColdsideTemperature = 30
    Humidity = 31
    HumidityError = 32
    Acceleration = 33
    AccelerationError = 34
    AccelerationSelfTest = 35
    AmbientLight = 36
    AmbientLightError = 37
    TaskInfo = 38
    LoopInfo = 39
    OneWireDevicePairedWithSensor = 40
    OneWireSearchFamilyMismatch = 41
    OneWireSearchCRCMismatch = 42
    OneWireSearchFoundDevice = 43
    PowerCAN_Temperature = 44
    PowerCAN_Voltage = 45
    PowerCAN_ChannelMeasurementPower = 46
    PowerCAN_ChannelMeasurementVoltage = 47
    PowerCAN_ChannelMeasurementCurrent = 48
    PowerCAN_LoadMeasurementResistance = 49
    PowerCAN_LoadMeasurementVoltage = 50
    PowerCAN_LoadMeasurementPower = 51
    PowerCAN_LoadMeasurementCurrent = 52
    PowerCAN_FailedLoadMeasurementValue = 53
    PowerCAN_FailedLoadMeasurementThreshold = 54
    PowerCAN_ResistanceMeasurementResistance = 55
    PowerCAN_ResistanceMeasurementReferenceVoltage = 56
    PowerCAN_ResistanceMeasurementDifferentialVoltage = 57
    PowerCAN_ResistanceMeasurementPositiveVoltage = 58
    PowerCAN_ResistanceMeasurementNegativeVoltage = 59
    PowerCAN_I2CBusStarted = 60
    PowerCAN_I2CSearchStarted = 61
    PowerCAN_I2CSearchFoundDevice = 62
    PowerCAN_I2CSearchMissingDevice = 63
    PowerCAN_I2CSearchEnded = 64
    PowerCAN_LTC2992Error = 65
    PowerCAN_ADS122C04Error = 66
    PowerCAN_I2CSearchError = 67
    PowerCAN_ErrorStatistics = 68
    DS2482Error = 69
    PartialDebugMessage1 = 70
    OneWireSearchStarted = 71
    I2CBusStarted = 72
    DS28E18QError = 73
    PartialDebugMessage2 = 74
    OneWireSearchEnded = 75
    I2CSearchStarted = 76
    MAX31850KError = 77
    PartialDebugMessage3 = 78
    OneWireDeviceStartupSuccess = 79
    I2CSearchError = 80
    MAX31856Error = 81
    PartialDebugMessage4 = 82
    OneWireDeviceStartupFailure = 83
    I2CSearchFoundDevice = 84
    MAX31865Error = 85
    PartialDebugMessage5 = 86
    I2CSearchEnded = 87
    PartialDebugMessage6 = 88
    PartialDebugMessage7 = 89
class categories(Enum):
    none = 0
class nodes(Enum):
    Flight_Controller = 0
    Edda_Controller = 1
    Edda_Telemetry = 2
    Edda_Pressure_Top = 3
    Edda_Pressure_Bottom = 4
    Edda_Power_Control_Boards = 10
    Ground_Controller = 16
class AccelerationSelfTestDirection(Enum):
    Positive = 0
    Negative = 1
class AccelerationSelfTestResult(Enum):
    Success = 0
    Failure = 1
class ADS122C04Error(Enum):
    LMAONone = 0
    CRCMismatch = 1
    I2CUnknownError = 2
    I2CReceiveBufferEmpty = 3
    I2CAddressNack = 4
    I2CDataNack = 5
    I2CTransmitBufferFull = 6
class DebugMessagesMode(Enum):
    Enabled = 0
    Disabled = 1
class DebugStatusLedsMode(Enum):
    Enabled = 0
    Disabled = 1
class DS2482Error(Enum):
    LMAONone = 0
    CRCMismatch = 1
    I2CUnknownError = 2
    I2CReceiveBufferEmpty = 3
    I2CAddressNack = 4
    I2CDataNack = 5
    I2CTransmitBufferFull = 6
    BusShortDetected = 7
    NoDevicesResponded = 8
    ConfigError = 9
    WaitOnBusyTimeout = 10
    ResetFailure = 11
class DS28E18QError(Enum):
    RequestCRCFailure = 0
    ResponseCRCFailure = 1
    InvalidRequestLength = 2
    InvalidResponseLength = 3
    TransactionFailed = 4
    ExecutionError = 5
    PowerOnResetError = 6
    FailedNackAtCommand = 7
    InvalidInput = 8
    InvalidResult = 9
    InvalidStatusByte = 10
    Unknown = 11
class I2CBus(Enum):
    Wire0 = 0
    Wire1 = 1
    Wire2 = 2
    Unknown = 3
class I2CError(Enum):
    LMAONone = 0
    CRCMismatch = 1
    I2CUnknownError = 2
    I2CReceiveBufferEmpty = 3
    I2CAddressNack = 4
    I2CDataNack = 5
    I2CTransmitBufferFull = 6
class INA260Error(Enum):
    LMAONone = 0
    CRCMismatch = 1
    I2CUnknownError = 2
    I2CReceiveBufferEmpty = 3
    I2CAddressNack = 4
    I2CDataNack = 5
    I2CTransmitBufferFull = 6
    UnexpectedManufacturer = 7
    UnexpectedDie = 8
    UnexpectedConfiguration = 9
    UnexpectedMask = 10
    UnexpectedAlertLimit = 11
class LIS331Error(Enum):
    LMAONone = 0
    CRCMismatch = 1
    I2CUnknownError = 2
    I2CReceiveBufferEmpty = 3
    I2CAddressNack = 4
    I2CDataNack = 5
    I2CTransmitBufferFull = 6
    FailedSelfTestX = 7
    FailedSelfTestY = 8
    FailedSelfTestZ = 9
    InitializationTimeout = 10
class LoopType(Enum):
    MainLoop = 0
    ChitchatLoop = 1
    RGBLoop = 2
    GenericThreadLoop = 3
    EddaLoop = 4
class LTR303Error(Enum):
    LMAONone = 0
    CRCMismatch = 1
    I2CUnknownError = 2
    I2CReceiveBufferEmpty = 3
    I2CAddressNack = 4
    I2CDataNack = 5
    I2CTransmitBufferFull = 6
    UnexpectedManufacturer = 7
    UnexpectedPartNumber = 8
    ReadOldData = 9
    DataIsInvalid = 10
    DataWasReadWithWrongGain = 11
class MAX31850KError(Enum):
    CRCMismatch = 0
    OneWireUnknownError = 1
    SensorShortToVDD = 2
    SensorShortToGND = 3
    SensorOpenCircuit = 4
class MS5803Error(Enum):
    LMAONone = 0
    CRCMismatch = 1
    I2CUnknownError = 2
    I2CReceiveBufferEmpty = 3
    I2CAddressNack = 4
    I2CDataNack = 5
    I2CTransmitBufferFull = 6
    D1BelowBounds = 7
    D1AboveBounds = 8
    D2BelowBounds = 9
    D2AboveBounds = 10
    Value_dT_BelowBounds = 11
    Value_dT_AboveBounds = 12
    Value_TEMP_BelowBounds = 13
    Value_TEMP_AboveBounds = 14
    Value_OFF_BelowBounds = 15
    Value_OFF_AboveBounds = 16
    Value_SENS_BelowBounds = 17
    Value_SENS_AboveBounds = 18
    Value_P_BelowBounds = 19
    Value_P_AboveBounds = 20
class Nodes(Enum):
    EddaController = 1
    EddaTelemetry = 2
    EddaPressureTop = 3
    EddaPressureBottom = 4
    GroundController = 16
    FlightController = 0
    EddaPowerControlBoards = 10
class OneWireBus(Enum):
    Bus0A = 0
    Bus0B = 1
    Bus1A = 2
    Bus1B = 3
    Unknown = 4
class PlatinumSensorIndex(Enum):
    RTD_0 = 0
    RTD_1 = 1
    Unknown = 2
class PowerCAN_ADS122C04Error(Enum):
    I2CArbitration = 0
    I2CBus = 1
    I2CBusy = 2
    I2CNack = 3
    I2CUnknownError = 4
    RegisterWriteFailed = 5
    RegisterResetFailed = 6
class PowerCAN_ADS122C04ErrorLocation(Enum):
    WriteRegister = 0
    ReadRegister = 1
    Reset = 2
    Start = 3
    Stop = 4
    ReadData = 5
    LMAONone = 6
class PowerCAN_CheckResult(Enum):
    SomeFailed = 0
    AllFailed = 1
    AllPassed = 2
    NotYetDone = 3
class PowerCAN_DebugMode(Enum):
    Enabled = 0
    Disabled = 1
class PowerCAN_GateState(Enum):
    Grounded = 0
    ResistanceMeasurement = 1
    High = 2
class PowerCAN_I2CBus(Enum):
    Wire0 = 0
    Wire1 = 1
    Wire2 = 2
    Unknown = 3
class PowerCAN_I2CError(Enum):
    LMAONone = 0
    CRCMismatch = 1
    I2CUnknownError = 2
    I2CReceiveBufferEmpty = 3
    I2CAddressNack = 4
    I2CDataNack = 5
    I2CTransmitBufferFull = 6
class PowerCAN_LoadMeasurementResult(Enum):
    Passed = 0
    Failed = 1
    Invalid = 2
class PowerCAN_LTC2992Error(Enum):
    I2CArbitration = 0
    I2CBus = 1
    I2CBusy = 2
    I2CNack = 3
    I2CUnknownError = 4
    RegisterWriteFailed = 5
    RegisterResetFailed = 6
class PowerCAN_LTC2992ErrorLocation(Enum):
    WriteRegister = 0
    ReadRegister = 1
    Reset = 2
    LoadVoltage = 3
    BoardVoltage = 4
    LoadCurrent = 5
    BoardCurrent = 6
    LoadPower = 7
    BoardPower = 8
    GPIO1 = 9
    GPIO2 = 10
    GPIO3 = 11
    GPIO4 = 12
    LMAONone = 13
class PowerCAN_MeasurementChannel(Enum):
    Load = 0
    Board = 1
class PowerCAN_MeasurementFailureReason(Enum):
    PowerAboveMax = 0
    PowerBelowMin = 1
    CurrentAboveMax = 2
    CurrentBelowMin = 3
    VoltageAboveMax = 4
    VoltageBelowMin = 5
    ResistanceAboveMax = 6
    ResistanceBelowMin = 7
class PowerCAN_MeasurementReference(Enum):
    Internal = 0
    ExternalReference = 1
    Supply = 2
class PowerCAN_ResistanceMeasurementReference(Enum):
    Internal = 0
    ExternalReference = 1
    Supply = 2
class PowerCAN_ResistanceMeasurementValidity(Enum):
    Valid = 0
    Invalid = 1
class PowerCAN_SystemState(Enum):
    Idle = 0
    Arming = 1
    Armed = 2
    Firing = 3
class PowerCAN_TemperatureKind(Enum):
    ADC = 0
    Gates = 1
class PowerCAN_TransitionRequest(Enum):
    Arm = 0
    Disarm = 1
    Fire = 2
    StopFire = 3
class PowerCAN_TransitionResponse(Enum):
    Success = 0
    Failure = 1
class PowerCAN_VoltageKind(Enum):
    Board3V3 = 0
class PowerCANChannel(Enum):
    Channel0_Unknown = 0
    Channel1_Ignition = 1
    Channel2_VentSolenoid = 2
    Channel3_MainValveSolenoid = 3
    Channel4_Unknown = 4
    Channel5_Unknown = 5
    Channel6_Unknown = 6
    Channel7_Unknown = 7
    Channel8_Unknown = 8
    Channel9_Unknown = 9
    Channel10_Unknown = 10
    Channel11_Unknown = 11
    Channel12_Unknown = 12
    Channel13_Unknown = 13
    Channel14_Unknown = 14
    Channel15_Unknown = 15
    Unknown = 16
class PressureSensorIndex(Enum):
    Transducer_0 = 0
    Transducer_1 = 1
    Transducer_2 = 2
    Transducer_3 = 3
class SHT31Error(Enum):
    LMAONone = 0
    CRCMismatch = 1
    I2CUnknownError = 2
    I2CReceiveBufferEmpty = 3
    I2CAddressNack = 4
    I2CDataNack = 5
    I2CTransmitBufferFull = 6
class TaskType(Enum):
    Startup = 0
    CANSetup = 1
    PeripheralSetup = 2
    SensorSetup = 3
    ThreadSetup = 4
    RGBSetup = 5
    MainLoop = 6
    ChitchatLoop = 7
    RGBLoop = 8
    GenericThreadLoop = 9
    EddaLoop = 10
    Wire0Start = 11
    Wire1Start = 12
    Wire2Start = 13
    StartTemperatureBusA = 14
    StartTemperatureBusB = 15
class TemperatureBoardIndex(Enum):
    Board0 = 0
    Board1 = 1
class TemperatureSensorIndex(Enum):
    InternalTemperature = 0
    PowerRegulator = 1
    AmbientPressureSensor = 2
    HumiditySensor = 3
    Unknown = 4
class ThermocoupleIndex(Enum):
    Therm_0 = 0
    Therm_1 = 1
    Therm_2 = 2
    Therm_3 = 3
    Therm_4 = 4
    Therm_5 = 5
    Therm_6 = 6
    Therm_7 = 7
    Therm_8 = 8
    Therm_9 = 9
    Unknown = 10
class Thread(Enum):
    Thread0 = 0
    Thread1 = 1
    Thread2 = 2
    Thread3 = 3
    Thread4 = 4
    Thread5 = 5
    Thread6 = 6
    Thread7 = 7
    Unknown = 8
class TransducerError(Enum):
    LMAONone = 0
    CRCMismatch = 1
    I2CUnknownError = 2
    I2CReceiveBufferEmpty = 3
    I2CAddressNack = 4
    I2CDataNack = 5
    I2CTransmitBufferFull = 6
    Undervoltage = 7
    Overvoltage = 8
class TransducerVoltageMeasurementIndex(Enum):
    Transducer_0 = 0
    Transducer_1 = 1
    Transducer_2 = 2
    Transducer_3 = 3
    Voltage_5V = 4
    Voltage_Ref = 5
    Unknown = 6
class CurrentTimePing_from_Ground_Controller_to_Edda_Controller:
    def __init__(self):
        self._sender = nodes.Ground_Controller
        self._receiver = nodes.Edda_Controller
        self._message = messages.CurrentTimePing
        self._category = categories.none
        self._id = 0
        self._size = 8
        self._current_time_ms = 0
        self._current_time_us = 0
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
    def set_current_time_ms(self, value):
        self._current_time_ms = value
    def set_current_time_us(self, value):
        self._current_time_us = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._current_time_ms)
        buf += struct.pack("<L", self._current_time_us)
        return buf
    def get_current_time_ms(self):
        return self._current_time_ms
    def get_current_time_us(self):
        return self._current_time_us
    def get_all_data(self):
        data = []
        data.append((fields.current_time_ms, self.get_current_time_ms()))
        data.append((fields.current_time_us, self.get_current_time_us()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._current_time_ms = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._current_time_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class CurrentTimePong_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.CurrentTimePong
        self._category = categories.none
        self._id = 1
        self._size = 8
        self._current_time_ms = 0
        self._current_time_us = 0
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
    def set_current_time_ms(self, value):
        self._current_time_ms = value
    def set_current_time_us(self, value):
        self._current_time_us = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._current_time_ms)
        buf += struct.pack("<L", self._current_time_us)
        return buf
    def get_current_time_ms(self):
        return self._current_time_ms
    def get_current_time_us(self):
        return self._current_time_us
    def get_all_data(self):
        data = []
        data.append((fields.current_time_ms, self.get_current_time_ms()))
        data.append((fields.current_time_us, self.get_current_time_us()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._current_time_ms = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._current_time_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class SayHi_from_Ground_Controller_to_Edda_Controller:
    def __init__(self):
        self._sender = nodes.Ground_Controller
        self._receiver = nodes.Edda_Controller
        self._message = messages.SayHi
        self._category = categories.none
        self._id = 2
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
class SayHi_from_Ground_Controller_to_Edda_Telemetry:
    def __init__(self):
        self._sender = nodes.Ground_Controller
        self._receiver = nodes.Edda_Telemetry
        self._message = messages.SayHi
        self._category = categories.none
        self._id = 2
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
class SayHi_from_Ground_Controller_to_Edda_Pressure_Top:
    def __init__(self):
        self._sender = nodes.Ground_Controller
        self._receiver = nodes.Edda_Pressure_Top
        self._message = messages.SayHi
        self._category = categories.none
        self._id = 2
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
class SayHi_from_Ground_Controller_to_Edda_Pressure_Bottom:
    def __init__(self):
        self._sender = nodes.Ground_Controller
        self._receiver = nodes.Edda_Pressure_Bottom
        self._message = messages.SayHi
        self._category = categories.none
        self._id = 2
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
class Hello_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.Hello
        self._category = categories.none
        self._id = 3
        self._size = 6
        self._debug_messages_mode = 0
        self._debug_status_leds_mode = 0
        self._uptime_ms = 0
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
    def set_debug_messages_mode(self, value):
        self._debug_messages_mode = value.value
    def set_debug_status_leds_mode(self, value):
        self._debug_status_leds_mode = value.value
    def set_uptime_ms(self, value):
        self._uptime_ms = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._debug_messages_mode)
        buf += struct.pack("<B", self._debug_status_leds_mode)
        buf += struct.pack("<L", self._uptime_ms)
        return buf
    def get_debug_messages_mode(self):
        return DebugMessagesMode(self._debug_messages_mode)
    def get_debug_status_leds_mode(self):
        return DebugStatusLedsMode(self._debug_status_leds_mode)
    def get_uptime_ms(self):
        return self._uptime_ms
    def get_all_data(self):
        data = []
        data.append((fields.debug_messages_mode, self.get_debug_messages_mode()))
        data.append((fields.debug_status_leds_mode, self.get_debug_status_leds_mode()))
        data.append((fields.uptime_ms, self.get_uptime_ms()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._debug_messages_mode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._debug_status_leds_mode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._uptime_ms = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class Hello_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.Hello
        self._category = categories.none
        self._id = 4
        self._size = 6
        self._debug_messages_mode = 0
        self._debug_status_leds_mode = 0
        self._uptime_ms = 0
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
    def set_debug_messages_mode(self, value):
        self._debug_messages_mode = value.value
    def set_debug_status_leds_mode(self, value):
        self._debug_status_leds_mode = value.value
    def set_uptime_ms(self, value):
        self._uptime_ms = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._debug_messages_mode)
        buf += struct.pack("<B", self._debug_status_leds_mode)
        buf += struct.pack("<L", self._uptime_ms)
        return buf
    def get_debug_messages_mode(self):
        return DebugMessagesMode(self._debug_messages_mode)
    def get_debug_status_leds_mode(self):
        return DebugStatusLedsMode(self._debug_status_leds_mode)
    def get_uptime_ms(self):
        return self._uptime_ms
    def get_all_data(self):
        data = []
        data.append((fields.debug_messages_mode, self.get_debug_messages_mode()))
        data.append((fields.debug_status_leds_mode, self.get_debug_status_leds_mode()))
        data.append((fields.uptime_ms, self.get_uptime_ms()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._debug_messages_mode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._debug_status_leds_mode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._uptime_ms = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class Hello_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.Hello
        self._category = categories.none
        self._id = 5
        self._size = 6
        self._debug_messages_mode = 0
        self._debug_status_leds_mode = 0
        self._uptime_ms = 0
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
    def set_debug_messages_mode(self, value):
        self._debug_messages_mode = value.value
    def set_debug_status_leds_mode(self, value):
        self._debug_status_leds_mode = value.value
    def set_uptime_ms(self, value):
        self._uptime_ms = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._debug_messages_mode)
        buf += struct.pack("<B", self._debug_status_leds_mode)
        buf += struct.pack("<L", self._uptime_ms)
        return buf
    def get_debug_messages_mode(self):
        return DebugMessagesMode(self._debug_messages_mode)
    def get_debug_status_leds_mode(self):
        return DebugStatusLedsMode(self._debug_status_leds_mode)
    def get_uptime_ms(self):
        return self._uptime_ms
    def get_all_data(self):
        data = []
        data.append((fields.debug_messages_mode, self.get_debug_messages_mode()))
        data.append((fields.debug_status_leds_mode, self.get_debug_status_leds_mode()))
        data.append((fields.uptime_ms, self.get_uptime_ms()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._debug_messages_mode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._debug_status_leds_mode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._uptime_ms = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class Hello_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.Hello
        self._category = categories.none
        self._id = 6
        self._size = 6
        self._debug_messages_mode = 0
        self._debug_status_leds_mode = 0
        self._uptime_ms = 0
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
    def set_debug_messages_mode(self, value):
        self._debug_messages_mode = value.value
    def set_debug_status_leds_mode(self, value):
        self._debug_status_leds_mode = value.value
    def set_uptime_ms(self, value):
        self._uptime_ms = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._debug_messages_mode)
        buf += struct.pack("<B", self._debug_status_leds_mode)
        buf += struct.pack("<L", self._uptime_ms)
        return buf
    def get_debug_messages_mode(self):
        return DebugMessagesMode(self._debug_messages_mode)
    def get_debug_status_leds_mode(self):
        return DebugStatusLedsMode(self._debug_status_leds_mode)
    def get_uptime_ms(self):
        return self._uptime_ms
    def get_all_data(self):
        data = []
        data.append((fields.debug_messages_mode, self.get_debug_messages_mode()))
        data.append((fields.debug_status_leds_mode, self.get_debug_status_leds_mode()))
        data.append((fields.uptime_ms, self.get_uptime_ms()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._debug_messages_mode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._debug_status_leds_mode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._uptime_ms = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class CanStatistics_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.CanStatistics
        self._category = categories.none
        self._id = 7
        self._size = 8
        self._max_tx_queue_size = 0
        self._max_rx_queue_size = 0
        self._mean_tx_queue_size = 0
        self._mean_rx_queue_size = 0
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
    def set_max_tx_queue_size(self, value):
        self._max_tx_queue_size = value
    def set_max_rx_queue_size(self, value):
        self._max_rx_queue_size = value
    def set_mean_tx_queue_size(self, value):
        self._mean_tx_queue_size = value
    def set_mean_rx_queue_size(self, value):
        self._mean_rx_queue_size = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._max_tx_queue_size)
        buf += struct.pack("<H", self._max_rx_queue_size)
        buf += struct.pack("<H", self._mean_tx_queue_size)
        buf += struct.pack("<H", self._mean_rx_queue_size)
        return buf
    def get_max_tx_queue_size(self):
        return self._max_tx_queue_size
    def get_max_rx_queue_size(self):
        return self._max_rx_queue_size
    def get_mean_tx_queue_size(self):
        return self._mean_tx_queue_size
    def get_mean_rx_queue_size(self):
        return self._mean_rx_queue_size
    def get_all_data(self):
        data = []
        data.append((fields.max_tx_queue_size, self.get_max_tx_queue_size()))
        data.append((fields.max_rx_queue_size, self.get_max_rx_queue_size()))
        data.append((fields.mean_tx_queue_size, self.get_mean_tx_queue_size()))
        data.append((fields.mean_rx_queue_size, self.get_mean_rx_queue_size()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._max_tx_queue_size = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._max_rx_queue_size = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._mean_tx_queue_size = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._mean_rx_queue_size = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class CanStatistics_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.CanStatistics
        self._category = categories.none
        self._id = 8
        self._size = 8
        self._max_tx_queue_size = 0
        self._max_rx_queue_size = 0
        self._mean_tx_queue_size = 0
        self._mean_rx_queue_size = 0
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
    def set_max_tx_queue_size(self, value):
        self._max_tx_queue_size = value
    def set_max_rx_queue_size(self, value):
        self._max_rx_queue_size = value
    def set_mean_tx_queue_size(self, value):
        self._mean_tx_queue_size = value
    def set_mean_rx_queue_size(self, value):
        self._mean_rx_queue_size = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._max_tx_queue_size)
        buf += struct.pack("<H", self._max_rx_queue_size)
        buf += struct.pack("<H", self._mean_tx_queue_size)
        buf += struct.pack("<H", self._mean_rx_queue_size)
        return buf
    def get_max_tx_queue_size(self):
        return self._max_tx_queue_size
    def get_max_rx_queue_size(self):
        return self._max_rx_queue_size
    def get_mean_tx_queue_size(self):
        return self._mean_tx_queue_size
    def get_mean_rx_queue_size(self):
        return self._mean_rx_queue_size
    def get_all_data(self):
        data = []
        data.append((fields.max_tx_queue_size, self.get_max_tx_queue_size()))
        data.append((fields.max_rx_queue_size, self.get_max_rx_queue_size()))
        data.append((fields.mean_tx_queue_size, self.get_mean_tx_queue_size()))
        data.append((fields.mean_rx_queue_size, self.get_mean_rx_queue_size()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._max_tx_queue_size = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._max_rx_queue_size = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._mean_tx_queue_size = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._mean_rx_queue_size = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class CanStatistics_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.CanStatistics
        self._category = categories.none
        self._id = 9
        self._size = 8
        self._max_tx_queue_size = 0
        self._max_rx_queue_size = 0
        self._mean_tx_queue_size = 0
        self._mean_rx_queue_size = 0
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
    def set_max_tx_queue_size(self, value):
        self._max_tx_queue_size = value
    def set_max_rx_queue_size(self, value):
        self._max_rx_queue_size = value
    def set_mean_tx_queue_size(self, value):
        self._mean_tx_queue_size = value
    def set_mean_rx_queue_size(self, value):
        self._mean_rx_queue_size = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._max_tx_queue_size)
        buf += struct.pack("<H", self._max_rx_queue_size)
        buf += struct.pack("<H", self._mean_tx_queue_size)
        buf += struct.pack("<H", self._mean_rx_queue_size)
        return buf
    def get_max_tx_queue_size(self):
        return self._max_tx_queue_size
    def get_max_rx_queue_size(self):
        return self._max_rx_queue_size
    def get_mean_tx_queue_size(self):
        return self._mean_tx_queue_size
    def get_mean_rx_queue_size(self):
        return self._mean_rx_queue_size
    def get_all_data(self):
        data = []
        data.append((fields.max_tx_queue_size, self.get_max_tx_queue_size()))
        data.append((fields.max_rx_queue_size, self.get_max_rx_queue_size()))
        data.append((fields.mean_tx_queue_size, self.get_mean_tx_queue_size()))
        data.append((fields.mean_rx_queue_size, self.get_mean_rx_queue_size()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._max_tx_queue_size = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._max_rx_queue_size = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._mean_tx_queue_size = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._mean_rx_queue_size = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class CanStatistics_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.CanStatistics
        self._category = categories.none
        self._id = 10
        self._size = 8
        self._max_tx_queue_size = 0
        self._max_rx_queue_size = 0
        self._mean_tx_queue_size = 0
        self._mean_rx_queue_size = 0
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
    def set_max_tx_queue_size(self, value):
        self._max_tx_queue_size = value
    def set_max_rx_queue_size(self, value):
        self._max_rx_queue_size = value
    def set_mean_tx_queue_size(self, value):
        self._mean_tx_queue_size = value
    def set_mean_rx_queue_size(self, value):
        self._mean_rx_queue_size = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._max_tx_queue_size)
        buf += struct.pack("<H", self._max_rx_queue_size)
        buf += struct.pack("<H", self._mean_tx_queue_size)
        buf += struct.pack("<H", self._mean_rx_queue_size)
        return buf
    def get_max_tx_queue_size(self):
        return self._max_tx_queue_size
    def get_max_rx_queue_size(self):
        return self._max_rx_queue_size
    def get_mean_tx_queue_size(self):
        return self._mean_tx_queue_size
    def get_mean_rx_queue_size(self):
        return self._mean_rx_queue_size
    def get_all_data(self):
        data = []
        data.append((fields.max_tx_queue_size, self.get_max_tx_queue_size()))
        data.append((fields.max_rx_queue_size, self.get_max_rx_queue_size()))
        data.append((fields.mean_tx_queue_size, self.get_mean_tx_queue_size()))
        data.append((fields.mean_rx_queue_size, self.get_mean_rx_queue_size()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._max_tx_queue_size = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._max_rx_queue_size = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._mean_tx_queue_size = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._mean_rx_queue_size = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class CanStatistics_from_Ground_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Ground_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.CanStatistics
        self._category = categories.none
        self._id = 11
        self._size = 8
        self._max_tx_queue_size = 0
        self._max_rx_queue_size = 0
        self._mean_tx_queue_size = 0
        self._mean_rx_queue_size = 0
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
    def set_max_tx_queue_size(self, value):
        self._max_tx_queue_size = value
    def set_max_rx_queue_size(self, value):
        self._max_rx_queue_size = value
    def set_mean_tx_queue_size(self, value):
        self._mean_tx_queue_size = value
    def set_mean_rx_queue_size(self, value):
        self._mean_rx_queue_size = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._max_tx_queue_size)
        buf += struct.pack("<H", self._max_rx_queue_size)
        buf += struct.pack("<H", self._mean_tx_queue_size)
        buf += struct.pack("<H", self._mean_rx_queue_size)
        return buf
    def get_max_tx_queue_size(self):
        return self._max_tx_queue_size
    def get_max_rx_queue_size(self):
        return self._max_rx_queue_size
    def get_mean_tx_queue_size(self):
        return self._mean_tx_queue_size
    def get_mean_rx_queue_size(self):
        return self._mean_rx_queue_size
    def get_all_data(self):
        data = []
        data.append((fields.max_tx_queue_size, self.get_max_tx_queue_size()))
        data.append((fields.max_rx_queue_size, self.get_max_rx_queue_size()))
        data.append((fields.mean_tx_queue_size, self.get_mean_tx_queue_size()))
        data.append((fields.mean_rx_queue_size, self.get_mean_rx_queue_size()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._max_tx_queue_size = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._max_rx_queue_size = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._mean_tx_queue_size = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._mean_rx_queue_size = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class CanLatency_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.CanLatency
        self._category = categories.none
        self._id = 12
        self._size = 5
        self._round_trip_time_us = 0
        self._destination_node = 0
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
    def set_round_trip_time_us(self, value):
        self._round_trip_time_us = value
    def set_destination_node(self, value):
        self._destination_node = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._round_trip_time_us)
        buf += struct.pack("<B", self._destination_node)
        return buf
    def get_round_trip_time_us(self):
        return self._round_trip_time_us
    def get_destination_node(self):
        return Nodes(self._destination_node)
    def get_all_data(self):
        data = []
        data.append((fields.round_trip_time_us, self.get_round_trip_time_us()))
        data.append((fields.destination_node, self.get_destination_node()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._round_trip_time_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._destination_node = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class CanLatency_from_Ground_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Ground_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.CanLatency
        self._category = categories.none
        self._id = 13
        self._size = 5
        self._round_trip_time_us = 0
        self._destination_node = 0
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
    def set_round_trip_time_us(self, value):
        self._round_trip_time_us = value
    def set_destination_node(self, value):
        self._destination_node = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._round_trip_time_us)
        buf += struct.pack("<B", self._destination_node)
        return buf
    def get_round_trip_time_us(self):
        return self._round_trip_time_us
    def get_destination_node(self):
        return Nodes(self._destination_node)
    def get_all_data(self):
        data = []
        data.append((fields.round_trip_time_us, self.get_round_trip_time_us()))
        data.append((fields.destination_node, self.get_destination_node()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._round_trip_time_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._destination_node = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class SetDebugStatusLedsModeRequest_from_Ground_Controller_to_Edda_Controller:
    def __init__(self):
        self._sender = nodes.Ground_Controller
        self._receiver = nodes.Edda_Controller
        self._message = messages.SetDebugStatusLedsModeRequest
        self._category = categories.none
        self._id = 48
        self._size = 2
        self._receiver_node = 0
        self._debug_status_leds_mode = 0
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
    def set_receiver_node(self, value):
        self._receiver_node = value.value
    def set_debug_status_leds_mode(self, value):
        self._debug_status_leds_mode = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._receiver_node)
        buf += struct.pack("<B", self._debug_status_leds_mode)
        return buf
    def get_receiver_node(self):
        return Nodes(self._receiver_node)
    def get_debug_status_leds_mode(self):
        return DebugStatusLedsMode(self._debug_status_leds_mode)
    def get_all_data(self):
        data = []
        data.append((fields.receiver_node, self.get_receiver_node()))
        data.append((fields.debug_status_leds_mode, self.get_debug_status_leds_mode()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._receiver_node = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._debug_status_leds_mode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class SetDebugStatusLedsModeRequest_from_Ground_Controller_to_Edda_Telemetry:
    def __init__(self):
        self._sender = nodes.Ground_Controller
        self._receiver = nodes.Edda_Telemetry
        self._message = messages.SetDebugStatusLedsModeRequest
        self._category = categories.none
        self._id = 48
        self._size = 2
        self._receiver_node = 0
        self._debug_status_leds_mode = 0
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
    def set_receiver_node(self, value):
        self._receiver_node = value.value
    def set_debug_status_leds_mode(self, value):
        self._debug_status_leds_mode = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._receiver_node)
        buf += struct.pack("<B", self._debug_status_leds_mode)
        return buf
    def get_receiver_node(self):
        return Nodes(self._receiver_node)
    def get_debug_status_leds_mode(self):
        return DebugStatusLedsMode(self._debug_status_leds_mode)
    def get_all_data(self):
        data = []
        data.append((fields.receiver_node, self.get_receiver_node()))
        data.append((fields.debug_status_leds_mode, self.get_debug_status_leds_mode()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._receiver_node = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._debug_status_leds_mode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class SetDebugStatusLedsModeRequest_from_Ground_Controller_to_Edda_Pressure_Top:
    def __init__(self):
        self._sender = nodes.Ground_Controller
        self._receiver = nodes.Edda_Pressure_Top
        self._message = messages.SetDebugStatusLedsModeRequest
        self._category = categories.none
        self._id = 48
        self._size = 2
        self._receiver_node = 0
        self._debug_status_leds_mode = 0
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
    def set_receiver_node(self, value):
        self._receiver_node = value.value
    def set_debug_status_leds_mode(self, value):
        self._debug_status_leds_mode = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._receiver_node)
        buf += struct.pack("<B", self._debug_status_leds_mode)
        return buf
    def get_receiver_node(self):
        return Nodes(self._receiver_node)
    def get_debug_status_leds_mode(self):
        return DebugStatusLedsMode(self._debug_status_leds_mode)
    def get_all_data(self):
        data = []
        data.append((fields.receiver_node, self.get_receiver_node()))
        data.append((fields.debug_status_leds_mode, self.get_debug_status_leds_mode()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._receiver_node = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._debug_status_leds_mode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class SetDebugStatusLedsModeRequest_from_Ground_Controller_to_Edda_Pressure_Bottom:
    def __init__(self):
        self._sender = nodes.Ground_Controller
        self._receiver = nodes.Edda_Pressure_Bottom
        self._message = messages.SetDebugStatusLedsModeRequest
        self._category = categories.none
        self._id = 48
        self._size = 2
        self._receiver_node = 0
        self._debug_status_leds_mode = 0
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
    def set_receiver_node(self, value):
        self._receiver_node = value.value
    def set_debug_status_leds_mode(self, value):
        self._debug_status_leds_mode = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._receiver_node)
        buf += struct.pack("<B", self._debug_status_leds_mode)
        return buf
    def get_receiver_node(self):
        return Nodes(self._receiver_node)
    def get_debug_status_leds_mode(self):
        return DebugStatusLedsMode(self._debug_status_leds_mode)
    def get_all_data(self):
        data = []
        data.append((fields.receiver_node, self.get_receiver_node()))
        data.append((fields.debug_status_leds_mode, self.get_debug_status_leds_mode()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._receiver_node = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._debug_status_leds_mode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class SetDebugMessagesModeRequest_from_Ground_Controller_to_Edda_Controller:
    def __init__(self):
        self._sender = nodes.Ground_Controller
        self._receiver = nodes.Edda_Controller
        self._message = messages.SetDebugMessagesModeRequest
        self._category = categories.none
        self._id = 49
        self._size = 2
        self._receiver_node = 0
        self._debug_messages_mode = 0
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
    def set_receiver_node(self, value):
        self._receiver_node = value.value
    def set_debug_messages_mode(self, value):
        self._debug_messages_mode = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._receiver_node)
        buf += struct.pack("<B", self._debug_messages_mode)
        return buf
    def get_receiver_node(self):
        return Nodes(self._receiver_node)
    def get_debug_messages_mode(self):
        return DebugMessagesMode(self._debug_messages_mode)
    def get_all_data(self):
        data = []
        data.append((fields.receiver_node, self.get_receiver_node()))
        data.append((fields.debug_messages_mode, self.get_debug_messages_mode()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._receiver_node = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._debug_messages_mode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class SetDebugMessagesModeRequest_from_Ground_Controller_to_Edda_Telemetry:
    def __init__(self):
        self._sender = nodes.Ground_Controller
        self._receiver = nodes.Edda_Telemetry
        self._message = messages.SetDebugMessagesModeRequest
        self._category = categories.none
        self._id = 49
        self._size = 2
        self._receiver_node = 0
        self._debug_messages_mode = 0
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
    def set_receiver_node(self, value):
        self._receiver_node = value.value
    def set_debug_messages_mode(self, value):
        self._debug_messages_mode = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._receiver_node)
        buf += struct.pack("<B", self._debug_messages_mode)
        return buf
    def get_receiver_node(self):
        return Nodes(self._receiver_node)
    def get_debug_messages_mode(self):
        return DebugMessagesMode(self._debug_messages_mode)
    def get_all_data(self):
        data = []
        data.append((fields.receiver_node, self.get_receiver_node()))
        data.append((fields.debug_messages_mode, self.get_debug_messages_mode()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._receiver_node = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._debug_messages_mode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class SetDebugMessagesModeRequest_from_Ground_Controller_to_Edda_Pressure_Top:
    def __init__(self):
        self._sender = nodes.Ground_Controller
        self._receiver = nodes.Edda_Pressure_Top
        self._message = messages.SetDebugMessagesModeRequest
        self._category = categories.none
        self._id = 49
        self._size = 2
        self._receiver_node = 0
        self._debug_messages_mode = 0
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
    def set_receiver_node(self, value):
        self._receiver_node = value.value
    def set_debug_messages_mode(self, value):
        self._debug_messages_mode = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._receiver_node)
        buf += struct.pack("<B", self._debug_messages_mode)
        return buf
    def get_receiver_node(self):
        return Nodes(self._receiver_node)
    def get_debug_messages_mode(self):
        return DebugMessagesMode(self._debug_messages_mode)
    def get_all_data(self):
        data = []
        data.append((fields.receiver_node, self.get_receiver_node()))
        data.append((fields.debug_messages_mode, self.get_debug_messages_mode()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._receiver_node = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._debug_messages_mode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class SetDebugMessagesModeRequest_from_Ground_Controller_to_Edda_Pressure_Bottom:
    def __init__(self):
        self._sender = nodes.Ground_Controller
        self._receiver = nodes.Edda_Pressure_Bottom
        self._message = messages.SetDebugMessagesModeRequest
        self._category = categories.none
        self._id = 49
        self._size = 2
        self._receiver_node = 0
        self._debug_messages_mode = 0
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
    def set_receiver_node(self, value):
        self._receiver_node = value.value
    def set_debug_messages_mode(self, value):
        self._debug_messages_mode = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._receiver_node)
        buf += struct.pack("<B", self._debug_messages_mode)
        return buf
    def get_receiver_node(self):
        return Nodes(self._receiver_node)
    def get_debug_messages_mode(self):
        return DebugMessagesMode(self._debug_messages_mode)
    def get_all_data(self):
        data = []
        data.append((fields.receiver_node, self.get_receiver_node()))
        data.append((fields.debug_messages_mode, self.get_debug_messages_mode()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._receiver_node = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._debug_messages_mode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_SetDebugMode_from_Ground_Controller_to_Edda_Controller:
    def __init__(self):
        self._sender = nodes.Ground_Controller
        self._receiver = nodes.Edda_Controller
        self._message = messages.PowerCAN_SetDebugMode
        self._category = categories.none
        self._id = 50
        self._size = 2
        self._debug_mode = 0
        self._powercan_channel = 0
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
    def set_debug_mode(self, value):
        self._debug_mode = value.value
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._debug_mode)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_debug_mode(self):
        return PowerCAN_DebugMode(self._debug_mode)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.debug_mode, self.get_debug_mode()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._debug_mode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_SetDebugMode_from_Ground_Controller_to_Edda_Power_Control_Boards:
    def __init__(self):
        self._sender = nodes.Ground_Controller
        self._receiver = nodes.Edda_Power_Control_Boards
        self._message = messages.PowerCAN_SetDebugMode
        self._category = categories.none
        self._id = 50
        self._size = 2
        self._debug_mode = 0
        self._powercan_channel = 0
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
    def set_debug_mode(self, value):
        self._debug_mode = value.value
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._debug_mode)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_debug_mode(self):
        return PowerCAN_DebugMode(self._debug_mode)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.debug_mode, self.get_debug_mode()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._debug_mode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_GetState_from_Ground_Controller_to_Edda_Controller:
    def __init__(self):
        self._sender = nodes.Ground_Controller
        self._receiver = nodes.Edda_Controller
        self._message = messages.PowerCAN_GetState
        self._category = categories.none
        self._id = 51
        self._size = 1
        self._powercan_channel = 0
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
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_GetState_from_Ground_Controller_to_Edda_Power_Control_Boards:
    def __init__(self):
        self._sender = nodes.Ground_Controller
        self._receiver = nodes.Edda_Power_Control_Boards
        self._message = messages.PowerCAN_GetState
        self._category = categories.none
        self._id = 51
        self._size = 1
        self._powercan_channel = 0
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
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_TransitionRequest_from_Ground_Controller_to_Edda_Controller:
    def __init__(self):
        self._sender = nodes.Ground_Controller
        self._receiver = nodes.Edda_Controller
        self._message = messages.PowerCAN_TransitionRequest
        self._category = categories.none
        self._id = 52
        self._size = 4
        self._edda_signature = 0
        self._request = 0
        self._powercan_channel = 0
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
    def set_edda_signature(self, value):
        self._edda_signature = value
    def set_request(self, value):
        self._request = value.value
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._edda_signature)
        buf += struct.pack("<B", self._request)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_edda_signature(self):
        return self._edda_signature
    def get_request(self):
        return PowerCAN_TransitionRequest(self._request)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.edda_signature, self.get_edda_signature()))
        data.append((fields.request, self.get_request()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._edda_signature = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._request = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_TransitionRequest_from_Ground_Controller_to_Edda_Power_Control_Boards:
    def __init__(self):
        self._sender = nodes.Ground_Controller
        self._receiver = nodes.Edda_Power_Control_Boards
        self._message = messages.PowerCAN_TransitionRequest
        self._category = categories.none
        self._id = 52
        self._size = 4
        self._edda_signature = 0
        self._request = 0
        self._powercan_channel = 0
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
    def set_edda_signature(self, value):
        self._edda_signature = value
    def set_request(self, value):
        self._request = value.value
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._edda_signature)
        buf += struct.pack("<B", self._request)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_edda_signature(self):
        return self._edda_signature
    def get_request(self):
        return PowerCAN_TransitionRequest(self._request)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.edda_signature, self.get_edda_signature()))
        data.append((fields.request, self.get_request()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._edda_signature = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._request = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_SetDebugMode_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_SetDebugMode
        self._category = categories.none
        self._id = 64
        self._size = 2
        self._debug_mode = 0
        self._powercan_channel = 0
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
    def set_debug_mode(self, value):
        self._debug_mode = value.value
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._debug_mode)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_debug_mode(self):
        return PowerCAN_DebugMode(self._debug_mode)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.debug_mode, self.get_debug_mode()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._debug_mode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_SetDebugMode_from_Edda_Controller_to_Edda_Power_Control_Boards:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Edda_Power_Control_Boards
        self._message = messages.PowerCAN_SetDebugMode
        self._category = categories.none
        self._id = 64
        self._size = 2
        self._debug_mode = 0
        self._powercan_channel = 0
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
    def set_debug_mode(self, value):
        self._debug_mode = value.value
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._debug_mode)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_debug_mode(self):
        return PowerCAN_DebugMode(self._debug_mode)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.debug_mode, self.get_debug_mode()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._debug_mode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_GetState_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_GetState
        self._category = categories.none
        self._id = 65
        self._size = 1
        self._powercan_channel = 0
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
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_GetState_from_Edda_Controller_to_Edda_Power_Control_Boards:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Edda_Power_Control_Boards
        self._message = messages.PowerCAN_GetState
        self._category = categories.none
        self._id = 65
        self._size = 1
        self._powercan_channel = 0
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
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_TransitionRequest_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_TransitionRequest
        self._category = categories.none
        self._id = 66
        self._size = 4
        self._edda_signature = 0
        self._request = 0
        self._powercan_channel = 0
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
    def set_edda_signature(self, value):
        self._edda_signature = value
    def set_request(self, value):
        self._request = value.value
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._edda_signature)
        buf += struct.pack("<B", self._request)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_edda_signature(self):
        return self._edda_signature
    def get_request(self):
        return PowerCAN_TransitionRequest(self._request)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.edda_signature, self.get_edda_signature()))
        data.append((fields.request, self.get_request()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._edda_signature = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._request = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_TransitionRequest_from_Edda_Controller_to_Edda_Power_Control_Boards:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Edda_Power_Control_Boards
        self._message = messages.PowerCAN_TransitionRequest
        self._category = categories.none
        self._id = 66
        self._size = 4
        self._edda_signature = 0
        self._request = 0
        self._powercan_channel = 0
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
    def set_edda_signature(self, value):
        self._edda_signature = value
    def set_request(self, value):
        self._request = value.value
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._edda_signature)
        buf += struct.pack("<B", self._request)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_edda_signature(self):
        return self._edda_signature
    def get_request(self):
        return PowerCAN_TransitionRequest(self._request)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.edda_signature, self.get_edda_signature()))
        data.append((fields.request, self.get_request()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._edda_signature = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._request = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_Hello_from_Edda_Power_Control_Boards_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Power_Control_Boards
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_Hello
        self._category = categories.none
        self._id = 67
        self._size = 2
        self._debug_mode = 0
        self._powercan_channel = 0
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
    def set_debug_mode(self, value):
        self._debug_mode = value.value
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._debug_mode)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_debug_mode(self):
        return PowerCAN_DebugMode(self._debug_mode)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.debug_mode, self.get_debug_mode()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._debug_mode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_CurrentState_from_Edda_Power_Control_Boards_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Power_Control_Boards
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_CurrentState
        self._category = categories.none
        self._id = 68
        self._size = 3
        self._system_state = 0
        self._gate_state = 0
        self._powercan_channel = 0
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
    def set_system_state(self, value):
        self._system_state = value.value
    def set_gate_state(self, value):
        self._gate_state = value.value
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._system_state)
        buf += struct.pack("<B", self._gate_state)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_system_state(self):
        return PowerCAN_SystemState(self._system_state)
    def get_gate_state(self):
        return PowerCAN_GateState(self._gate_state)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.system_state, self.get_system_state()))
        data.append((fields.gate_state, self.get_gate_state()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._system_state = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._gate_state = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_TransitionResponse_from_Edda_Power_Control_Boards_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Power_Control_Boards
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_TransitionResponse
        self._category = categories.none
        self._id = 69
        self._size = 3
        self._request = 0
        self._response = 0
        self._powercan_channel = 0
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
    def set_request(self, value):
        self._request = value.value
    def set_response(self, value):
        self._response = value.value
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._request)
        buf += struct.pack("<B", self._response)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_request(self):
        return PowerCAN_TransitionRequest(self._request)
    def get_response(self):
        return PowerCAN_TransitionResponse(self._response)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.request, self.get_request()))
        data.append((fields.response, self.get_response()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._request = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._response = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_CheckResult_from_Edda_Power_Control_Boards_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Power_Control_Boards
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_CheckResult
        self._category = categories.none
        self._id = 70
        self._size = 5
        self._result = 0
        self._checks_failed = 0
        self._checks_performed = 0
        self._total_checks = 0
        self._powercan_channel = 0
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
    def set_result(self, value):
        self._result = value.value
    def set_checks_failed(self, value):
        self._checks_failed = value
    def set_checks_performed(self, value):
        self._checks_performed = value
    def set_total_checks(self, value):
        self._total_checks = value
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._result)
        buf += struct.pack("<B", self._checks_failed)
        buf += struct.pack("<B", self._checks_performed)
        buf += struct.pack("<B", self._total_checks)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_result(self):
        return PowerCAN_CheckResult(self._result)
    def get_checks_failed(self):
        return self._checks_failed
    def get_checks_performed(self):
        return self._checks_performed
    def get_total_checks(self):
        return self._total_checks
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.result, self.get_result()))
        data.append((fields.checks_failed, self.get_checks_failed()))
        data.append((fields.checks_performed, self.get_checks_performed()))
        data.append((fields.total_checks, self.get_total_checks()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._result = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._checks_failed = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._checks_performed = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._total_checks = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class CurrentTimePing_from_Edda_Controller_to_Edda_Telemetry:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Edda_Telemetry
        self._message = messages.CurrentTimePing
        self._category = categories.none
        self._id = 144
        self._size = 8
        self._current_time_ms = 0
        self._current_time_us = 0
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
    def set_current_time_ms(self, value):
        self._current_time_ms = value
    def set_current_time_us(self, value):
        self._current_time_us = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._current_time_ms)
        buf += struct.pack("<L", self._current_time_us)
        return buf
    def get_current_time_ms(self):
        return self._current_time_ms
    def get_current_time_us(self):
        return self._current_time_us
    def get_all_data(self):
        data = []
        data.append((fields.current_time_ms, self.get_current_time_ms()))
        data.append((fields.current_time_us, self.get_current_time_us()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._current_time_ms = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._current_time_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class CurrentTimePing_from_Edda_Controller_to_Edda_Pressure_Top:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Edda_Pressure_Top
        self._message = messages.CurrentTimePing
        self._category = categories.none
        self._id = 144
        self._size = 8
        self._current_time_ms = 0
        self._current_time_us = 0
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
    def set_current_time_ms(self, value):
        self._current_time_ms = value
    def set_current_time_us(self, value):
        self._current_time_us = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._current_time_ms)
        buf += struct.pack("<L", self._current_time_us)
        return buf
    def get_current_time_ms(self):
        return self._current_time_ms
    def get_current_time_us(self):
        return self._current_time_us
    def get_all_data(self):
        data = []
        data.append((fields.current_time_ms, self.get_current_time_ms()))
        data.append((fields.current_time_us, self.get_current_time_us()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._current_time_ms = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._current_time_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class CurrentTimePing_from_Edda_Controller_to_Edda_Pressure_Bottom:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Edda_Pressure_Bottom
        self._message = messages.CurrentTimePing
        self._category = categories.none
        self._id = 144
        self._size = 8
        self._current_time_ms = 0
        self._current_time_us = 0
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
    def set_current_time_ms(self, value):
        self._current_time_ms = value
    def set_current_time_us(self, value):
        self._current_time_us = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._current_time_ms)
        buf += struct.pack("<L", self._current_time_us)
        return buf
    def get_current_time_ms(self):
        return self._current_time_ms
    def get_current_time_us(self):
        return self._current_time_us
    def get_all_data(self):
        data = []
        data.append((fields.current_time_ms, self.get_current_time_ms()))
        data.append((fields.current_time_us, self.get_current_time_us()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._current_time_ms = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._current_time_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class CurrentTimePong_from_Edda_Telemetry_to_Edda_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Edda_Controller
        self._message = messages.CurrentTimePong
        self._category = categories.none
        self._id = 145
        self._size = 8
        self._current_time_ms = 0
        self._current_time_us = 0
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
    def set_current_time_ms(self, value):
        self._current_time_ms = value
    def set_current_time_us(self, value):
        self._current_time_us = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._current_time_ms)
        buf += struct.pack("<L", self._current_time_us)
        return buf
    def get_current_time_ms(self):
        return self._current_time_ms
    def get_current_time_us(self):
        return self._current_time_us
    def get_all_data(self):
        data = []
        data.append((fields.current_time_ms, self.get_current_time_ms()))
        data.append((fields.current_time_us, self.get_current_time_us()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._current_time_ms = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._current_time_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class CurrentTimePong_from_Edda_Pressure_Top_to_Edda_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Edda_Controller
        self._message = messages.CurrentTimePong
        self._category = categories.none
        self._id = 146
        self._size = 8
        self._current_time_ms = 0
        self._current_time_us = 0
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
    def set_current_time_ms(self, value):
        self._current_time_ms = value
    def set_current_time_us(self, value):
        self._current_time_us = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._current_time_ms)
        buf += struct.pack("<L", self._current_time_us)
        return buf
    def get_current_time_ms(self):
        return self._current_time_ms
    def get_current_time_us(self):
        return self._current_time_us
    def get_all_data(self):
        data = []
        data.append((fields.current_time_ms, self.get_current_time_ms()))
        data.append((fields.current_time_us, self.get_current_time_us()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._current_time_ms = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._current_time_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class CurrentTimePong_from_Edda_Pressure_Bottom_to_Edda_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Edda_Controller
        self._message = messages.CurrentTimePong
        self._category = categories.none
        self._id = 147
        self._size = 8
        self._current_time_ms = 0
        self._current_time_us = 0
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
    def set_current_time_ms(self, value):
        self._current_time_ms = value
    def set_current_time_us(self, value):
        self._current_time_us = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._current_time_ms)
        buf += struct.pack("<L", self._current_time_us)
        return buf
    def get_current_time_ms(self):
        return self._current_time_ms
    def get_current_time_us(self):
        return self._current_time_us
    def get_all_data(self):
        data = []
        data.append((fields.current_time_ms, self.get_current_time_ms()))
        data.append((fields.current_time_us, self.get_current_time_us()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._current_time_ms = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._current_time_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class SayHi_from_Edda_Controller_to_Edda_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Edda_Controller
        self._message = messages.SayHi
        self._category = categories.none
        self._id = 148
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
class SayHi_from_Edda_Controller_to_Edda_Telemetry:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Edda_Telemetry
        self._message = messages.SayHi
        self._category = categories.none
        self._id = 148
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
class SayHi_from_Edda_Controller_to_Edda_Pressure_Top:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Edda_Pressure_Top
        self._message = messages.SayHi
        self._category = categories.none
        self._id = 148
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
class SayHi_from_Edda_Controller_to_Edda_Pressure_Bottom:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Edda_Pressure_Bottom
        self._message = messages.SayHi
        self._category = categories.none
        self._id = 148
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
class WenHop_from_Edda_Controller_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Flight_Controller
        self._message = messages.WenHop
        self._category = categories.none
        self._id = 149
        self._size = 6
        self._w = 0
        self._e = 0
        self._n = 0
        self._h = 0
        self._o = 0
        self._p = 0
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
    def set_w(self, value):
        self._w = value
    def set_e(self, value):
        self._e = value
    def set_n(self, value):
        self._n = value
    def set_h(self, value):
        self._h = value
    def set_o(self, value):
        self._o = value
    def set_p(self, value):
        self._p = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._w)
        buf += struct.pack("<B", self._e)
        buf += struct.pack("<B", self._n)
        buf += struct.pack("<B", self._h)
        buf += struct.pack("<B", self._o)
        buf += struct.pack("<B", self._p)
        return buf
    def get_w(self):
        return self._w
    def get_e(self):
        return self._e
    def get_n(self):
        return self._n
    def get_h(self):
        return self._h
    def get_o(self):
        return self._o
    def get_p(self):
        return self._p
    def get_all_data(self):
        data = []
        data.append((fields.w, self.get_w()))
        data.append((fields.e, self.get_e()))
        data.append((fields.n, self.get_n()))
        data.append((fields.h, self.get_h()))
        data.append((fields.o, self.get_o()))
        data.append((fields.p, self.get_p()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._w = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._e = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._n = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._h = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._o = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._p = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class WenHop_from_Edda_Telemetry_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Flight_Controller
        self._message = messages.WenHop
        self._category = categories.none
        self._id = 150
        self._size = 6
        self._w = 0
        self._e = 0
        self._n = 0
        self._h = 0
        self._o = 0
        self._p = 0
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
    def set_w(self, value):
        self._w = value
    def set_e(self, value):
        self._e = value
    def set_n(self, value):
        self._n = value
    def set_h(self, value):
        self._h = value
    def set_o(self, value):
        self._o = value
    def set_p(self, value):
        self._p = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._w)
        buf += struct.pack("<B", self._e)
        buf += struct.pack("<B", self._n)
        buf += struct.pack("<B", self._h)
        buf += struct.pack("<B", self._o)
        buf += struct.pack("<B", self._p)
        return buf
    def get_w(self):
        return self._w
    def get_e(self):
        return self._e
    def get_n(self):
        return self._n
    def get_h(self):
        return self._h
    def get_o(self):
        return self._o
    def get_p(self):
        return self._p
    def get_all_data(self):
        data = []
        data.append((fields.w, self.get_w()))
        data.append((fields.e, self.get_e()))
        data.append((fields.n, self.get_n()))
        data.append((fields.h, self.get_h()))
        data.append((fields.o, self.get_o()))
        data.append((fields.p, self.get_p()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._w = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._e = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._n = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._h = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._o = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._p = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class WenHop_from_Edda_Pressure_Top_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Flight_Controller
        self._message = messages.WenHop
        self._category = categories.none
        self._id = 151
        self._size = 6
        self._w = 0
        self._e = 0
        self._n = 0
        self._h = 0
        self._o = 0
        self._p = 0
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
    def set_w(self, value):
        self._w = value
    def set_e(self, value):
        self._e = value
    def set_n(self, value):
        self._n = value
    def set_h(self, value):
        self._h = value
    def set_o(self, value):
        self._o = value
    def set_p(self, value):
        self._p = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._w)
        buf += struct.pack("<B", self._e)
        buf += struct.pack("<B", self._n)
        buf += struct.pack("<B", self._h)
        buf += struct.pack("<B", self._o)
        buf += struct.pack("<B", self._p)
        return buf
    def get_w(self):
        return self._w
    def get_e(self):
        return self._e
    def get_n(self):
        return self._n
    def get_h(self):
        return self._h
    def get_o(self):
        return self._o
    def get_p(self):
        return self._p
    def get_all_data(self):
        data = []
        data.append((fields.w, self.get_w()))
        data.append((fields.e, self.get_e()))
        data.append((fields.n, self.get_n()))
        data.append((fields.h, self.get_h()))
        data.append((fields.o, self.get_o()))
        data.append((fields.p, self.get_p()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._w = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._e = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._n = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._h = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._o = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._p = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class WenHop_from_Edda_Pressure_Bottom_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Flight_Controller
        self._message = messages.WenHop
        self._category = categories.none
        self._id = 152
        self._size = 6
        self._w = 0
        self._e = 0
        self._n = 0
        self._h = 0
        self._o = 0
        self._p = 0
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
    def set_w(self, value):
        self._w = value
    def set_e(self, value):
        self._e = value
    def set_n(self, value):
        self._n = value
    def set_h(self, value):
        self._h = value
    def set_o(self, value):
        self._o = value
    def set_p(self, value):
        self._p = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._w)
        buf += struct.pack("<B", self._e)
        buf += struct.pack("<B", self._n)
        buf += struct.pack("<B", self._h)
        buf += struct.pack("<B", self._o)
        buf += struct.pack("<B", self._p)
        return buf
    def get_w(self):
        return self._w
    def get_e(self):
        return self._e
    def get_n(self):
        return self._n
    def get_h(self):
        return self._h
    def get_o(self):
        return self._o
    def get_p(self):
        return self._p
    def get_all_data(self):
        data = []
        data.append((fields.w, self.get_w()))
        data.append((fields.e, self.get_e()))
        data.append((fields.n, self.get_n()))
        data.append((fields.h, self.get_h()))
        data.append((fields.o, self.get_o()))
        data.append((fields.p, self.get_p()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._w = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._e = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._n = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._h = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._o = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._p = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class WenOrbit_from_Edda_Controller_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Flight_Controller
        self._message = messages.WenOrbit
        self._category = categories.none
        self._id = 153
        self._size = 8
        self._w = 0
        self._e = 0
        self._n = 0
        self._o = 0
        self._r = 0
        self._b = 0
        self._i = 0
        self._t = 0
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
    def set_w(self, value):
        self._w = value
    def set_e(self, value):
        self._e = value
    def set_n(self, value):
        self._n = value
    def set_o(self, value):
        self._o = value
    def set_r(self, value):
        self._r = value
    def set_b(self, value):
        self._b = value
    def set_i(self, value):
        self._i = value
    def set_t(self, value):
        self._t = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._w)
        buf += struct.pack("<B", self._e)
        buf += struct.pack("<B", self._n)
        buf += struct.pack("<B", self._o)
        buf += struct.pack("<B", self._r)
        buf += struct.pack("<B", self._b)
        buf += struct.pack("<B", self._i)
        buf += struct.pack("<B", self._t)
        return buf
    def get_w(self):
        return self._w
    def get_e(self):
        return self._e
    def get_n(self):
        return self._n
    def get_o(self):
        return self._o
    def get_r(self):
        return self._r
    def get_b(self):
        return self._b
    def get_i(self):
        return self._i
    def get_t(self):
        return self._t
    def get_all_data(self):
        data = []
        data.append((fields.w, self.get_w()))
        data.append((fields.e, self.get_e()))
        data.append((fields.n, self.get_n()))
        data.append((fields.o, self.get_o()))
        data.append((fields.r, self.get_r()))
        data.append((fields.b, self.get_b()))
        data.append((fields.i, self.get_i()))
        data.append((fields.t, self.get_t()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._w = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._e = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._n = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._o = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._r = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._b = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._i = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._t = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class WenOrbit_from_Edda_Telemetry_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Flight_Controller
        self._message = messages.WenOrbit
        self._category = categories.none
        self._id = 154
        self._size = 8
        self._w = 0
        self._e = 0
        self._n = 0
        self._o = 0
        self._r = 0
        self._b = 0
        self._i = 0
        self._t = 0
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
    def set_w(self, value):
        self._w = value
    def set_e(self, value):
        self._e = value
    def set_n(self, value):
        self._n = value
    def set_o(self, value):
        self._o = value
    def set_r(self, value):
        self._r = value
    def set_b(self, value):
        self._b = value
    def set_i(self, value):
        self._i = value
    def set_t(self, value):
        self._t = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._w)
        buf += struct.pack("<B", self._e)
        buf += struct.pack("<B", self._n)
        buf += struct.pack("<B", self._o)
        buf += struct.pack("<B", self._r)
        buf += struct.pack("<B", self._b)
        buf += struct.pack("<B", self._i)
        buf += struct.pack("<B", self._t)
        return buf
    def get_w(self):
        return self._w
    def get_e(self):
        return self._e
    def get_n(self):
        return self._n
    def get_o(self):
        return self._o
    def get_r(self):
        return self._r
    def get_b(self):
        return self._b
    def get_i(self):
        return self._i
    def get_t(self):
        return self._t
    def get_all_data(self):
        data = []
        data.append((fields.w, self.get_w()))
        data.append((fields.e, self.get_e()))
        data.append((fields.n, self.get_n()))
        data.append((fields.o, self.get_o()))
        data.append((fields.r, self.get_r()))
        data.append((fields.b, self.get_b()))
        data.append((fields.i, self.get_i()))
        data.append((fields.t, self.get_t()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._w = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._e = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._n = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._o = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._r = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._b = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._i = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._t = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class WenOrbit_from_Edda_Pressure_Top_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Flight_Controller
        self._message = messages.WenOrbit
        self._category = categories.none
        self._id = 155
        self._size = 8
        self._w = 0
        self._e = 0
        self._n = 0
        self._o = 0
        self._r = 0
        self._b = 0
        self._i = 0
        self._t = 0
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
    def set_w(self, value):
        self._w = value
    def set_e(self, value):
        self._e = value
    def set_n(self, value):
        self._n = value
    def set_o(self, value):
        self._o = value
    def set_r(self, value):
        self._r = value
    def set_b(self, value):
        self._b = value
    def set_i(self, value):
        self._i = value
    def set_t(self, value):
        self._t = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._w)
        buf += struct.pack("<B", self._e)
        buf += struct.pack("<B", self._n)
        buf += struct.pack("<B", self._o)
        buf += struct.pack("<B", self._r)
        buf += struct.pack("<B", self._b)
        buf += struct.pack("<B", self._i)
        buf += struct.pack("<B", self._t)
        return buf
    def get_w(self):
        return self._w
    def get_e(self):
        return self._e
    def get_n(self):
        return self._n
    def get_o(self):
        return self._o
    def get_r(self):
        return self._r
    def get_b(self):
        return self._b
    def get_i(self):
        return self._i
    def get_t(self):
        return self._t
    def get_all_data(self):
        data = []
        data.append((fields.w, self.get_w()))
        data.append((fields.e, self.get_e()))
        data.append((fields.n, self.get_n()))
        data.append((fields.o, self.get_o()))
        data.append((fields.r, self.get_r()))
        data.append((fields.b, self.get_b()))
        data.append((fields.i, self.get_i()))
        data.append((fields.t, self.get_t()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._w = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._e = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._n = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._o = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._r = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._b = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._i = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._t = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class WenOrbit_from_Edda_Pressure_Bottom_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Flight_Controller
        self._message = messages.WenOrbit
        self._category = categories.none
        self._id = 156
        self._size = 8
        self._w = 0
        self._e = 0
        self._n = 0
        self._o = 0
        self._r = 0
        self._b = 0
        self._i = 0
        self._t = 0
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
    def set_w(self, value):
        self._w = value
    def set_e(self, value):
        self._e = value
    def set_n(self, value):
        self._n = value
    def set_o(self, value):
        self._o = value
    def set_r(self, value):
        self._r = value
    def set_b(self, value):
        self._b = value
    def set_i(self, value):
        self._i = value
    def set_t(self, value):
        self._t = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._w)
        buf += struct.pack("<B", self._e)
        buf += struct.pack("<B", self._n)
        buf += struct.pack("<B", self._o)
        buf += struct.pack("<B", self._r)
        buf += struct.pack("<B", self._b)
        buf += struct.pack("<B", self._i)
        buf += struct.pack("<B", self._t)
        return buf
    def get_w(self):
        return self._w
    def get_e(self):
        return self._e
    def get_n(self):
        return self._n
    def get_o(self):
        return self._o
    def get_r(self):
        return self._r
    def get_b(self):
        return self._b
    def get_i(self):
        return self._i
    def get_t(self):
        return self._t
    def get_all_data(self):
        data = []
        data.append((fields.w, self.get_w()))
        data.append((fields.e, self.get_e()))
        data.append((fields.n, self.get_n()))
        data.append((fields.o, self.get_o()))
        data.append((fields.r, self.get_r()))
        data.append((fields.b, self.get_b()))
        data.append((fields.i, self.get_i()))
        data.append((fields.t, self.get_t()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._w = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._e = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._n = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._o = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._r = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._b = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._i = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._t = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerInputMeasurement_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerInputMeasurement
        self._category = categories.none
        self._id = 157
        self._size = 6
        self._current_ampere = 0
        self._voltage_volt = 0
        self._power_watt = 0
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
    def set_current_ampere(self, value):
        self._current_ampere = packedFloat_to_uint(value, -15, 15, 2)
    def set_voltage_volt(self, value):
        self._voltage_volt = packedFloat_to_uint(value, 0, 36, 2)
    def set_power_watt(self, value):
        self._power_watt = packedFloat_to_uint(value, -540, 540, 2)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._current_ampere)
        buf += struct.pack("<H", self._voltage_volt)
        buf += struct.pack("<H", self._power_watt)
        return buf
    def get_current_ampere(self):
        return uint_to_packedFloat(self._current_ampere, -15, 15, 2)
    def get_voltage_volt(self):
        return uint_to_packedFloat(self._voltage_volt, 0, 36, 2)
    def get_power_watt(self):
        return uint_to_packedFloat(self._power_watt, -540, 540, 2)
    def get_all_data(self):
        data = []
        data.append((fields.current_ampere, self.get_current_ampere()))
        data.append((fields.voltage_volt, self.get_voltage_volt()))
        data.append((fields.power_watt, self.get_power_watt()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._current_ampere = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._voltage_volt = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._power_watt = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class PowerInputMeasurement_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerInputMeasurement
        self._category = categories.none
        self._id = 158
        self._size = 6
        self._current_ampere = 0
        self._voltage_volt = 0
        self._power_watt = 0
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
    def set_current_ampere(self, value):
        self._current_ampere = packedFloat_to_uint(value, -15, 15, 2)
    def set_voltage_volt(self, value):
        self._voltage_volt = packedFloat_to_uint(value, 0, 36, 2)
    def set_power_watt(self, value):
        self._power_watt = packedFloat_to_uint(value, -540, 540, 2)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._current_ampere)
        buf += struct.pack("<H", self._voltage_volt)
        buf += struct.pack("<H", self._power_watt)
        return buf
    def get_current_ampere(self):
        return uint_to_packedFloat(self._current_ampere, -15, 15, 2)
    def get_voltage_volt(self):
        return uint_to_packedFloat(self._voltage_volt, 0, 36, 2)
    def get_power_watt(self):
        return uint_to_packedFloat(self._power_watt, -540, 540, 2)
    def get_all_data(self):
        data = []
        data.append((fields.current_ampere, self.get_current_ampere()))
        data.append((fields.voltage_volt, self.get_voltage_volt()))
        data.append((fields.power_watt, self.get_power_watt()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._current_ampere = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._voltage_volt = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._power_watt = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class PowerInputMeasurement_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerInputMeasurement
        self._category = categories.none
        self._id = 159
        self._size = 6
        self._current_ampere = 0
        self._voltage_volt = 0
        self._power_watt = 0
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
    def set_current_ampere(self, value):
        self._current_ampere = packedFloat_to_uint(value, -15, 15, 2)
    def set_voltage_volt(self, value):
        self._voltage_volt = packedFloat_to_uint(value, 0, 36, 2)
    def set_power_watt(self, value):
        self._power_watt = packedFloat_to_uint(value, -540, 540, 2)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._current_ampere)
        buf += struct.pack("<H", self._voltage_volt)
        buf += struct.pack("<H", self._power_watt)
        return buf
    def get_current_ampere(self):
        return uint_to_packedFloat(self._current_ampere, -15, 15, 2)
    def get_voltage_volt(self):
        return uint_to_packedFloat(self._voltage_volt, 0, 36, 2)
    def get_power_watt(self):
        return uint_to_packedFloat(self._power_watt, -540, 540, 2)
    def get_all_data(self):
        data = []
        data.append((fields.current_ampere, self.get_current_ampere()))
        data.append((fields.voltage_volt, self.get_voltage_volt()))
        data.append((fields.power_watt, self.get_power_watt()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._current_ampere = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._voltage_volt = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._power_watt = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class PowerInputMeasurement_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerInputMeasurement
        self._category = categories.none
        self._id = 160
        self._size = 6
        self._current_ampere = 0
        self._voltage_volt = 0
        self._power_watt = 0
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
    def set_current_ampere(self, value):
        self._current_ampere = packedFloat_to_uint(value, -15, 15, 2)
    def set_voltage_volt(self, value):
        self._voltage_volt = packedFloat_to_uint(value, 0, 36, 2)
    def set_power_watt(self, value):
        self._power_watt = packedFloat_to_uint(value, -540, 540, 2)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._current_ampere)
        buf += struct.pack("<H", self._voltage_volt)
        buf += struct.pack("<H", self._power_watt)
        return buf
    def get_current_ampere(self):
        return uint_to_packedFloat(self._current_ampere, -15, 15, 2)
    def get_voltage_volt(self):
        return uint_to_packedFloat(self._voltage_volt, 0, 36, 2)
    def get_power_watt(self):
        return uint_to_packedFloat(self._power_watt, -540, 540, 2)
    def get_all_data(self):
        data = []
        data.append((fields.current_ampere, self.get_current_ampere()))
        data.append((fields.voltage_volt, self.get_voltage_volt()))
        data.append((fields.power_watt, self.get_power_watt()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._current_ampere = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._voltage_volt = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._power_watt = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class PowerInputMeasurementError_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerInputMeasurementError
        self._category = categories.none
        self._id = 161
        self._size = 1
        self._error = 0
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
    def set_error(self, value):
        self._error = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._error)
        return buf
    def get_error(self):
        return INA260Error(self._error)
    def get_all_data(self):
        data = []
        data.append((fields.error, self.get_error()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerInputMeasurementError_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerInputMeasurementError
        self._category = categories.none
        self._id = 162
        self._size = 1
        self._error = 0
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
    def set_error(self, value):
        self._error = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._error)
        return buf
    def get_error(self):
        return INA260Error(self._error)
    def get_all_data(self):
        data = []
        data.append((fields.error, self.get_error()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerInputMeasurementError_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerInputMeasurementError
        self._category = categories.none
        self._id = 163
        self._size = 1
        self._error = 0
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
    def set_error(self, value):
        self._error = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._error)
        return buf
    def get_error(self):
        return INA260Error(self._error)
    def get_all_data(self):
        data = []
        data.append((fields.error, self.get_error()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerInputMeasurementError_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerInputMeasurementError
        self._category = categories.none
        self._id = 164
        self._size = 1
        self._error = 0
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
    def set_error(self, value):
        self._error = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._error)
        return buf
    def get_error(self):
        return INA260Error(self._error)
    def get_all_data(self):
        data = []
        data.append((fields.error, self.get_error()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class ColdSideTemperature_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.ColdSideTemperature
        self._category = categories.none
        self._id = 165
        self._size = 3
        self._sensor_index = 0
        self._temperature_celsius = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value.value
    def set_temperature_celsius(self, value):
        self._temperature_celsius = packedFloat_to_uint(value, -55, 125, 2)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<H", self._temperature_celsius)
        return buf
    def get_sensor_index(self):
        return TemperatureSensorIndex(self._sensor_index)
    def get_temperature_celsius(self):
        return uint_to_packedFloat(self._temperature_celsius, -55, 125, 2)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.temperature_celsius, self.get_temperature_celsius()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._temperature_celsius = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class ColdSideTemperature_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.ColdSideTemperature
        self._category = categories.none
        self._id = 166
        self._size = 3
        self._sensor_index = 0
        self._temperature_celsius = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value.value
    def set_temperature_celsius(self, value):
        self._temperature_celsius = packedFloat_to_uint(value, -55, 125, 2)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<H", self._temperature_celsius)
        return buf
    def get_sensor_index(self):
        return TemperatureSensorIndex(self._sensor_index)
    def get_temperature_celsius(self):
        return uint_to_packedFloat(self._temperature_celsius, -55, 125, 2)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.temperature_celsius, self.get_temperature_celsius()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._temperature_celsius = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class ColdSideTemperature_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.ColdSideTemperature
        self._category = categories.none
        self._id = 167
        self._size = 3
        self._sensor_index = 0
        self._temperature_celsius = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value.value
    def set_temperature_celsius(self, value):
        self._temperature_celsius = packedFloat_to_uint(value, -55, 125, 2)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<H", self._temperature_celsius)
        return buf
    def get_sensor_index(self):
        return TemperatureSensorIndex(self._sensor_index)
    def get_temperature_celsius(self):
        return uint_to_packedFloat(self._temperature_celsius, -55, 125, 2)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.temperature_celsius, self.get_temperature_celsius()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._temperature_celsius = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class ColdSideTemperature_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.ColdSideTemperature
        self._category = categories.none
        self._id = 168
        self._size = 3
        self._sensor_index = 0
        self._temperature_celsius = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value.value
    def set_temperature_celsius(self, value):
        self._temperature_celsius = packedFloat_to_uint(value, -55, 125, 2)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<H", self._temperature_celsius)
        return buf
    def get_sensor_index(self):
        return TemperatureSensorIndex(self._sensor_index)
    def get_temperature_celsius(self):
        return uint_to_packedFloat(self._temperature_celsius, -55, 125, 2)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.temperature_celsius, self.get_temperature_celsius()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._temperature_celsius = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class RawTransducerVoltage_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.RawTransducerVoltage
        self._category = categories.none
        self._id = 169
        self._size = 5
        self._measurement_index = 0
        self._voltage_volt = 0
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
    def set_measurement_index(self, value):
        self._measurement_index = value.value
    def set_voltage_volt(self, value):
        self._voltage_volt = packedFloat_to_uint(value, -0.2, 5.2, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._measurement_index)
        buf += struct.pack("<L", self._voltage_volt)
        return buf
    def get_measurement_index(self):
        return TransducerVoltageMeasurementIndex(self._measurement_index)
    def get_voltage_volt(self):
        return uint_to_packedFloat(self._voltage_volt, -0.2, 5.2, 4)
    def get_all_data(self):
        data = []
        data.append((fields.measurement_index, self.get_measurement_index()))
        data.append((fields.voltage_volt, self.get_voltage_volt()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._measurement_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._voltage_volt = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class RawTransducerVoltage_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.RawTransducerVoltage
        self._category = categories.none
        self._id = 170
        self._size = 5
        self._measurement_index = 0
        self._voltage_volt = 0
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
    def set_measurement_index(self, value):
        self._measurement_index = value.value
    def set_voltage_volt(self, value):
        self._voltage_volt = packedFloat_to_uint(value, -0.2, 5.2, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._measurement_index)
        buf += struct.pack("<L", self._voltage_volt)
        return buf
    def get_measurement_index(self):
        return TransducerVoltageMeasurementIndex(self._measurement_index)
    def get_voltage_volt(self):
        return uint_to_packedFloat(self._voltage_volt, -0.2, 5.2, 4)
    def get_all_data(self):
        data = []
        data.append((fields.measurement_index, self.get_measurement_index()))
        data.append((fields.voltage_volt, self.get_voltage_volt()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._measurement_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._voltage_volt = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class TransducerPressure_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.TransducerPressure
        self._category = categories.none
        self._id = 171
        self._size = 5
        self._sensor_index = 0
        self._pressure_pascal = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value.value
    def set_pressure_pascal(self, value):
        self._pressure_pascal = packedFloat_to_uint(value, -1000000, 10000000, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._pressure_pascal)
        return buf
    def get_sensor_index(self):
        return PressureSensorIndex(self._sensor_index)
    def get_pressure_pascal(self):
        return uint_to_packedFloat(self._pressure_pascal, -1000000, 10000000, 4)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.pressure_pascal, self.get_pressure_pascal()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._pressure_pascal = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class TransducerPressure_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.TransducerPressure
        self._category = categories.none
        self._id = 172
        self._size = 5
        self._sensor_index = 0
        self._pressure_pascal = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value.value
    def set_pressure_pascal(self, value):
        self._pressure_pascal = packedFloat_to_uint(value, -1000000, 10000000, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._pressure_pascal)
        return buf
    def get_sensor_index(self):
        return PressureSensorIndex(self._sensor_index)
    def get_pressure_pascal(self):
        return uint_to_packedFloat(self._pressure_pascal, -1000000, 10000000, 4)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.pressure_pascal, self.get_pressure_pascal()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._pressure_pascal = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class TransducerError_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.TransducerError
        self._category = categories.none
        self._id = 173
        self._size = 2
        self._measurement_index = 0
        self._error = 0
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
    def set_measurement_index(self, value):
        self._measurement_index = value.value
    def set_error(self, value):
        self._error = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._measurement_index)
        buf += struct.pack("<B", self._error)
        return buf
    def get_measurement_index(self):
        return TransducerVoltageMeasurementIndex(self._measurement_index)
    def get_error(self):
        return TransducerError(self._error)
    def get_all_data(self):
        data = []
        data.append((fields.measurement_index, self.get_measurement_index()))
        data.append((fields.error, self.get_error()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._measurement_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class TransducerError_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.TransducerError
        self._category = categories.none
        self._id = 174
        self._size = 2
        self._measurement_index = 0
        self._error = 0
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
    def set_measurement_index(self, value):
        self._measurement_index = value.value
    def set_error(self, value):
        self._error = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._measurement_index)
        buf += struct.pack("<B", self._error)
        return buf
    def get_measurement_index(self):
        return TransducerVoltageMeasurementIndex(self._measurement_index)
    def get_error(self):
        return TransducerError(self._error)
    def get_all_data(self):
        data = []
        data.append((fields.measurement_index, self.get_measurement_index()))
        data.append((fields.error, self.get_error()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._measurement_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class AmbientPressure_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.AmbientPressure
        self._category = categories.none
        self._id = 175
        self._size = 4
        self._pressure_mbar = 0
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
    def set_pressure_mbar(self, value):
        self._pressure_mbar = packedFloat_to_uint(value, 0, 10000, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._pressure_mbar)
        return buf
    def get_pressure_mbar(self):
        return uint_to_packedFloat(self._pressure_mbar, 0, 10000, 4)
    def get_all_data(self):
        data = []
        data.append((fields.pressure_mbar, self.get_pressure_mbar()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._pressure_mbar = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class AmbientPressure_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.AmbientPressure
        self._category = categories.none
        self._id = 176
        self._size = 4
        self._pressure_mbar = 0
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
    def set_pressure_mbar(self, value):
        self._pressure_mbar = packedFloat_to_uint(value, 0, 10000, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._pressure_mbar)
        return buf
    def get_pressure_mbar(self):
        return uint_to_packedFloat(self._pressure_mbar, 0, 10000, 4)
    def get_all_data(self):
        data = []
        data.append((fields.pressure_mbar, self.get_pressure_mbar()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._pressure_mbar = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class AmbientPressureCoefficient_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.AmbientPressureCoefficient
        self._category = categories.none
        self._id = 177
        self._size = 3
        self._coefficient_number = 0
        self._coefficient_value = 0
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
    def set_coefficient_number(self, value):
        self._coefficient_number = value
    def set_coefficient_value(self, value):
        self._coefficient_value = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._coefficient_number)
        buf += struct.pack("<H", self._coefficient_value)
        return buf
    def get_coefficient_number(self):
        return self._coefficient_number
    def get_coefficient_value(self):
        return self._coefficient_value
    def get_all_data(self):
        data = []
        data.append((fields.coefficient_number, self.get_coefficient_number()))
        data.append((fields.coefficient_value, self.get_coefficient_value()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._coefficient_number = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._coefficient_value = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class AmbientPressureCoefficient_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.AmbientPressureCoefficient
        self._category = categories.none
        self._id = 178
        self._size = 3
        self._coefficient_number = 0
        self._coefficient_value = 0
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
    def set_coefficient_number(self, value):
        self._coefficient_number = value
    def set_coefficient_value(self, value):
        self._coefficient_value = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._coefficient_number)
        buf += struct.pack("<H", self._coefficient_value)
        return buf
    def get_coefficient_number(self):
        return self._coefficient_number
    def get_coefficient_value(self):
        return self._coefficient_value
    def get_all_data(self):
        data = []
        data.append((fields.coefficient_number, self.get_coefficient_number()))
        data.append((fields.coefficient_value, self.get_coefficient_value()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._coefficient_number = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._coefficient_value = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class AmbientPressureError_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.AmbientPressureError
        self._category = categories.none
        self._id = 179
        self._size = 1
        self._error = 0
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
    def set_error(self, value):
        self._error = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._error)
        return buf
    def get_error(self):
        return MS5803Error(self._error)
    def get_all_data(self):
        data = []
        data.append((fields.error, self.get_error()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class AmbientPressureError_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.AmbientPressureError
        self._category = categories.none
        self._id = 180
        self._size = 1
        self._error = 0
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
    def set_error(self, value):
        self._error = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._error)
        return buf
    def get_error(self):
        return MS5803Error(self._error)
    def get_all_data(self):
        data = []
        data.append((fields.error, self.get_error()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PlatinumSensorTemperature_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.PlatinumSensorTemperature
        self._category = categories.none
        self._id = 181
        self._size = 6
        self._board_index = 0
        self._sensor_index = 0
        self._temperature_celsius = 0
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
    def set_board_index(self, value):
        self._board_index = value.value
    def set_sensor_index(self, value):
        self._sensor_index = value.value
    def set_temperature_celsius(self, value):
        self._temperature_celsius = packedFloat_to_uint(value, -200, 850, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._board_index)
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._temperature_celsius)
        return buf
    def get_board_index(self):
        return TemperatureBoardIndex(self._board_index)
    def get_sensor_index(self):
        return PlatinumSensorIndex(self._sensor_index)
    def get_temperature_celsius(self):
        return uint_to_packedFloat(self._temperature_celsius, -200, 850, 4)
    def get_all_data(self):
        data = []
        data.append((fields.board_index, self.get_board_index()))
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.temperature_celsius, self.get_temperature_celsius()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._board_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._temperature_celsius = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class PlatinumSensorResistance_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.PlatinumSensorResistance
        self._category = categories.none
        self._id = 182
        self._size = 6
        self._board_index = 0
        self._sensor_index = 0
        self._resistance_ohm = 0
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
    def set_board_index(self, value):
        self._board_index = value.value
    def set_sensor_index(self, value):
        self._sensor_index = value.value
    def set_resistance_ohm(self, value):
        self._resistance_ohm = packedFloat_to_uint(value, 0, 5000, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._board_index)
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._resistance_ohm)
        return buf
    def get_board_index(self):
        return TemperatureBoardIndex(self._board_index)
    def get_sensor_index(self):
        return PlatinumSensorIndex(self._sensor_index)
    def get_resistance_ohm(self):
        return uint_to_packedFloat(self._resistance_ohm, 0, 5000, 4)
    def get_all_data(self):
        data = []
        data.append((fields.board_index, self.get_board_index()))
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.resistance_ohm, self.get_resistance_ohm()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._board_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._resistance_ohm = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class PlatinumSensorRatio_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.PlatinumSensorRatio
        self._category = categories.none
        self._id = 183
        self._size = 6
        self._board_index = 0
        self._sensor_index = 0
        self._ratio_fraction = 0
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
    def set_board_index(self, value):
        self._board_index = value.value
    def set_sensor_index(self, value):
        self._sensor_index = value.value
    def set_ratio_fraction(self, value):
        self._ratio_fraction = packedFloat_to_uint(value, 0, 1, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._board_index)
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._ratio_fraction)
        return buf
    def get_board_index(self):
        return TemperatureBoardIndex(self._board_index)
    def get_sensor_index(self):
        return PlatinumSensorIndex(self._sensor_index)
    def get_ratio_fraction(self):
        return uint_to_packedFloat(self._ratio_fraction, 0, 1, 4)
    def get_all_data(self):
        data = []
        data.append((fields.board_index, self.get_board_index()))
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.ratio_fraction, self.get_ratio_fraction()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._board_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._ratio_fraction = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class ThermocoupleTypeKTemperature_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.ThermocoupleTypeKTemperature
        self._category = categories.none
        self._id = 184
        self._size = 6
        self._board_index = 0
        self._sensor_index = 0
        self._temperature_celsius = 0
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
    def set_board_index(self, value):
        self._board_index = value.value
    def set_sensor_index(self, value):
        self._sensor_index = value.value
    def set_temperature_celsius(self, value):
        self._temperature_celsius = packedFloat_to_uint(value, -200, 1350, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._board_index)
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._temperature_celsius)
        return buf
    def get_board_index(self):
        return TemperatureBoardIndex(self._board_index)
    def get_sensor_index(self):
        return ThermocoupleIndex(self._sensor_index)
    def get_temperature_celsius(self):
        return uint_to_packedFloat(self._temperature_celsius, -200, 1350, 4)
    def get_all_data(self):
        data = []
        data.append((fields.board_index, self.get_board_index()))
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.temperature_celsius, self.get_temperature_celsius()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._board_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._temperature_celsius = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class ThermocoupleColdsideTemperature_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.ThermocoupleColdsideTemperature
        self._category = categories.none
        self._id = 185
        self._size = 4
        self._board_index = 0
        self._sensor_index = 0
        self._temperature_celsius = 0
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
    def set_board_index(self, value):
        self._board_index = value.value
    def set_sensor_index(self, value):
        self._sensor_index = value.value
    def set_temperature_celsius(self, value):
        self._temperature_celsius = packedFloat_to_uint(value, -55, 125, 2)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._board_index)
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<H", self._temperature_celsius)
        return buf
    def get_board_index(self):
        return TemperatureBoardIndex(self._board_index)
    def get_sensor_index(self):
        return ThermocoupleIndex(self._sensor_index)
    def get_temperature_celsius(self):
        return uint_to_packedFloat(self._temperature_celsius, -55, 125, 2)
    def get_all_data(self):
        data = []
        data.append((fields.board_index, self.get_board_index()))
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.temperature_celsius, self.get_temperature_celsius()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._board_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._temperature_celsius = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class Humidity_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.Humidity
        self._category = categories.none
        self._id = 187
        self._size = 3
        self._relative_humidity_percentage = 0
        self._is_heater_on = 0
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
    def set_relative_humidity_percentage(self, value):
        self._relative_humidity_percentage = packedFloat_to_uint(value, 0, 100, 2)
    def set_is_heater_on(self, value):
        self._is_heater_on = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._relative_humidity_percentage)
        buf += struct.pack("<B", self._is_heater_on)
        return buf
    def get_relative_humidity_percentage(self):
        return uint_to_packedFloat(self._relative_humidity_percentage, 0, 100, 2)
    def get_is_heater_on(self):
        return self._is_heater_on
    def get_all_data(self):
        data = []
        data.append((fields.relative_humidity_percentage, self.get_relative_humidity_percentage()))
        data.append((fields.is_heater_on, self.get_is_heater_on()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._relative_humidity_percentage = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._is_heater_on = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class HumidityError_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.HumidityError
        self._category = categories.none
        self._id = 188
        self._size = 1
        self._error = 0
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
    def set_error(self, value):
        self._error = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._error)
        return buf
    def get_error(self):
        return SHT31Error(self._error)
    def get_all_data(self):
        data = []
        data.append((fields.error, self.get_error()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class Acceleration_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.Acceleration
        self._category = categories.none
        self._id = 189
        self._size = 8
        self._acceleration_x_gforce = 0
        self._acceleration_y_gforce = 0
        self._acceleration_z_gforce = 0
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
    def set_acceleration_x_gforce(self, value):
        self._acceleration_x_gforce = packedFloat_to_uint(value, -20, 20, 2)
    def set_acceleration_y_gforce(self, value):
        self._acceleration_y_gforce = packedFloat_to_uint(value, -20, 20, 2)
    def set_acceleration_z_gforce(self, value):
        self._acceleration_z_gforce = packedFloat_to_uint(value, -20, 20, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._acceleration_x_gforce)
        buf += struct.pack("<H", self._acceleration_y_gforce)
        buf += struct.pack("<L", self._acceleration_z_gforce)
        return buf
    def get_acceleration_x_gforce(self):
        return uint_to_packedFloat(self._acceleration_x_gforce, -20, 20, 2)
    def get_acceleration_y_gforce(self):
        return uint_to_packedFloat(self._acceleration_y_gforce, -20, 20, 2)
    def get_acceleration_z_gforce(self):
        return uint_to_packedFloat(self._acceleration_z_gforce, -20, 20, 4)
    def get_all_data(self):
        data = []
        data.append((fields.acceleration_x_gforce, self.get_acceleration_x_gforce()))
        data.append((fields.acceleration_y_gforce, self.get_acceleration_y_gforce()))
        data.append((fields.acceleration_z_gforce, self.get_acceleration_z_gforce()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._acceleration_x_gforce = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._acceleration_y_gforce = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._acceleration_z_gforce = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class AccelerationError_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.AccelerationError
        self._category = categories.none
        self._id = 190
        self._size = 1
        self._error = 0
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
    def set_error(self, value):
        self._error = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._error)
        return buf
    def get_error(self):
        return LIS331Error(self._error)
    def get_all_data(self):
        data = []
        data.append((fields.error, self.get_error()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class AccelerationSelfTest_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.AccelerationSelfTest
        self._category = categories.none
        self._id = 191
        self._size = 8
        self._sign = 0
        self._result = 0
        self._acceleration_x_gforce = 0
        self._acceleration_y_gforce = 0
        self._acceleration_z_gforce = 0
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
    def set_sign(self, value):
        self._sign = value.value
    def set_result(self, value):
        self._result = value.value
    def set_acceleration_x_gforce(self, value):
        self._acceleration_x_gforce = packedFloat_to_uint(value, -20, 20, 2)
    def set_acceleration_y_gforce(self, value):
        self._acceleration_y_gforce = packedFloat_to_uint(value, -20, 20, 2)
    def set_acceleration_z_gforce(self, value):
        self._acceleration_z_gforce = packedFloat_to_uint(value, -20, 20, 2)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sign)
        buf += struct.pack("<B", self._result)
        buf += struct.pack("<H", self._acceleration_x_gforce)
        buf += struct.pack("<H", self._acceleration_y_gforce)
        buf += struct.pack("<H", self._acceleration_z_gforce)
        return buf
    def get_sign(self):
        return AccelerationSelfTestDirection(self._sign)
    def get_result(self):
        return AccelerationSelfTestResult(self._result)
    def get_acceleration_x_gforce(self):
        return uint_to_packedFloat(self._acceleration_x_gforce, -20, 20, 2)
    def get_acceleration_y_gforce(self):
        return uint_to_packedFloat(self._acceleration_y_gforce, -20, 20, 2)
    def get_acceleration_z_gforce(self):
        return uint_to_packedFloat(self._acceleration_z_gforce, -20, 20, 2)
    def get_all_data(self):
        data = []
        data.append((fields.sign, self.get_sign()))
        data.append((fields.result, self.get_result()))
        data.append((fields.acceleration_x_gforce, self.get_acceleration_x_gforce()))
        data.append((fields.acceleration_y_gforce, self.get_acceleration_y_gforce()))
        data.append((fields.acceleration_z_gforce, self.get_acceleration_z_gforce()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sign = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._result = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._acceleration_x_gforce = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._acceleration_y_gforce = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._acceleration_z_gforce = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class AmbientLight_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.AmbientLight
        self._category = categories.none
        self._id = 192
        self._size = 4
        self._ambient_light_lux = 0
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
    def set_ambient_light_lux(self, value):
        self._ambient_light_lux = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<f", self._ambient_light_lux)
        return buf
    def get_ambient_light_lux(self):
        return self._ambient_light_lux
    def get_all_data(self):
        data = []
        data.append((fields.ambient_light_lux, self.get_ambient_light_lux()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._ambient_light_lux = struct.unpack_from("<f", buf, index)[0]
        index += 4
        return
class AmbientLightError_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.AmbientLightError
        self._category = categories.none
        self._id = 193
        self._size = 1
        self._error = 0
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
    def set_error(self, value):
        self._error = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._error)
        return buf
    def get_error(self):
        return LTR303Error(self._error)
    def get_all_data(self):
        data = []
        data.append((fields.error, self.get_error()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class TaskInfo_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.TaskInfo
        self._category = categories.none
        self._id = 198
        self._size = 8
        self._type = 0
        self._thread = 0
        self._task_time_us = 0
        self._truncated_start_time_us = 0
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
    def set_type(self, value):
        self._type = value.value
    def set_thread(self, value):
        self._thread = value.value
    def set_task_time_us(self, value):
        self._task_time_us = value
    def set_truncated_start_time_us(self, value):
        self._truncated_start_time_us = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._type)
        buf += struct.pack("<B", self._thread)
        buf += struct.pack("<L", self._task_time_us)
        buf += struct.pack("<H", self._truncated_start_time_us)
        return buf
    def get_type(self):
        return TaskType(self._type)
    def get_thread(self):
        return Thread(self._thread)
    def get_task_time_us(self):
        return self._task_time_us
    def get_truncated_start_time_us(self):
        return self._truncated_start_time_us
    def get_all_data(self):
        data = []
        data.append((fields.type, self.get_type()))
        data.append((fields.thread, self.get_thread()))
        data.append((fields.task_time_us, self.get_task_time_us()))
        data.append((fields.truncated_start_time_us, self.get_truncated_start_time_us()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._type = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._thread = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._task_time_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._truncated_start_time_us = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class TaskInfo_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.TaskInfo
        self._category = categories.none
        self._id = 199
        self._size = 8
        self._type = 0
        self._thread = 0
        self._task_time_us = 0
        self._truncated_start_time_us = 0
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
    def set_type(self, value):
        self._type = value.value
    def set_thread(self, value):
        self._thread = value.value
    def set_task_time_us(self, value):
        self._task_time_us = value
    def set_truncated_start_time_us(self, value):
        self._truncated_start_time_us = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._type)
        buf += struct.pack("<B", self._thread)
        buf += struct.pack("<L", self._task_time_us)
        buf += struct.pack("<H", self._truncated_start_time_us)
        return buf
    def get_type(self):
        return TaskType(self._type)
    def get_thread(self):
        return Thread(self._thread)
    def get_task_time_us(self):
        return self._task_time_us
    def get_truncated_start_time_us(self):
        return self._truncated_start_time_us
    def get_all_data(self):
        data = []
        data.append((fields.type, self.get_type()))
        data.append((fields.thread, self.get_thread()))
        data.append((fields.task_time_us, self.get_task_time_us()))
        data.append((fields.truncated_start_time_us, self.get_truncated_start_time_us()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._type = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._thread = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._task_time_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._truncated_start_time_us = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class TaskInfo_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.TaskInfo
        self._category = categories.none
        self._id = 200
        self._size = 8
        self._type = 0
        self._thread = 0
        self._task_time_us = 0
        self._truncated_start_time_us = 0
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
    def set_type(self, value):
        self._type = value.value
    def set_thread(self, value):
        self._thread = value.value
    def set_task_time_us(self, value):
        self._task_time_us = value
    def set_truncated_start_time_us(self, value):
        self._truncated_start_time_us = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._type)
        buf += struct.pack("<B", self._thread)
        buf += struct.pack("<L", self._task_time_us)
        buf += struct.pack("<H", self._truncated_start_time_us)
        return buf
    def get_type(self):
        return TaskType(self._type)
    def get_thread(self):
        return Thread(self._thread)
    def get_task_time_us(self):
        return self._task_time_us
    def get_truncated_start_time_us(self):
        return self._truncated_start_time_us
    def get_all_data(self):
        data = []
        data.append((fields.type, self.get_type()))
        data.append((fields.thread, self.get_thread()))
        data.append((fields.task_time_us, self.get_task_time_us()))
        data.append((fields.truncated_start_time_us, self.get_truncated_start_time_us()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._type = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._thread = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._task_time_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._truncated_start_time_us = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class TaskInfo_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.TaskInfo
        self._category = categories.none
        self._id = 201
        self._size = 8
        self._type = 0
        self._thread = 0
        self._task_time_us = 0
        self._truncated_start_time_us = 0
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
    def set_type(self, value):
        self._type = value.value
    def set_thread(self, value):
        self._thread = value.value
    def set_task_time_us(self, value):
        self._task_time_us = value
    def set_truncated_start_time_us(self, value):
        self._truncated_start_time_us = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._type)
        buf += struct.pack("<B", self._thread)
        buf += struct.pack("<L", self._task_time_us)
        buf += struct.pack("<H", self._truncated_start_time_us)
        return buf
    def get_type(self):
        return TaskType(self._type)
    def get_thread(self):
        return Thread(self._thread)
    def get_task_time_us(self):
        return self._task_time_us
    def get_truncated_start_time_us(self):
        return self._truncated_start_time_us
    def get_all_data(self):
        data = []
        data.append((fields.type, self.get_type()))
        data.append((fields.thread, self.get_thread()))
        data.append((fields.task_time_us, self.get_task_time_us()))
        data.append((fields.truncated_start_time_us, self.get_truncated_start_time_us()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._type = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._thread = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._task_time_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._truncated_start_time_us = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class LoopInfo_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.LoopInfo
        self._category = categories.none
        self._id = 202
        self._size = 8
        self._type = 0
        self._thread = 0
        self._loop_time_us = 0
        self._truncated_start_time_us = 0
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
    def set_type(self, value):
        self._type = value.value
    def set_thread(self, value):
        self._thread = value.value
    def set_loop_time_us(self, value):
        self._loop_time_us = value
    def set_truncated_start_time_us(self, value):
        self._truncated_start_time_us = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._type)
        buf += struct.pack("<B", self._thread)
        buf += struct.pack("<L", self._loop_time_us)
        buf += struct.pack("<H", self._truncated_start_time_us)
        return buf
    def get_type(self):
        return LoopType(self._type)
    def get_thread(self):
        return Thread(self._thread)
    def get_loop_time_us(self):
        return self._loop_time_us
    def get_truncated_start_time_us(self):
        return self._truncated_start_time_us
    def get_all_data(self):
        data = []
        data.append((fields.type, self.get_type()))
        data.append((fields.thread, self.get_thread()))
        data.append((fields.loop_time_us, self.get_loop_time_us()))
        data.append((fields.truncated_start_time_us, self.get_truncated_start_time_us()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._type = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._thread = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._loop_time_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._truncated_start_time_us = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class LoopInfo_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.LoopInfo
        self._category = categories.none
        self._id = 203
        self._size = 8
        self._type = 0
        self._thread = 0
        self._loop_time_us = 0
        self._truncated_start_time_us = 0
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
    def set_type(self, value):
        self._type = value.value
    def set_thread(self, value):
        self._thread = value.value
    def set_loop_time_us(self, value):
        self._loop_time_us = value
    def set_truncated_start_time_us(self, value):
        self._truncated_start_time_us = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._type)
        buf += struct.pack("<B", self._thread)
        buf += struct.pack("<L", self._loop_time_us)
        buf += struct.pack("<H", self._truncated_start_time_us)
        return buf
    def get_type(self):
        return LoopType(self._type)
    def get_thread(self):
        return Thread(self._thread)
    def get_loop_time_us(self):
        return self._loop_time_us
    def get_truncated_start_time_us(self):
        return self._truncated_start_time_us
    def get_all_data(self):
        data = []
        data.append((fields.type, self.get_type()))
        data.append((fields.thread, self.get_thread()))
        data.append((fields.loop_time_us, self.get_loop_time_us()))
        data.append((fields.truncated_start_time_us, self.get_truncated_start_time_us()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._type = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._thread = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._loop_time_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._truncated_start_time_us = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class LoopInfo_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.LoopInfo
        self._category = categories.none
        self._id = 204
        self._size = 8
        self._type = 0
        self._thread = 0
        self._loop_time_us = 0
        self._truncated_start_time_us = 0
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
    def set_type(self, value):
        self._type = value.value
    def set_thread(self, value):
        self._thread = value.value
    def set_loop_time_us(self, value):
        self._loop_time_us = value
    def set_truncated_start_time_us(self, value):
        self._truncated_start_time_us = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._type)
        buf += struct.pack("<B", self._thread)
        buf += struct.pack("<L", self._loop_time_us)
        buf += struct.pack("<H", self._truncated_start_time_us)
        return buf
    def get_type(self):
        return LoopType(self._type)
    def get_thread(self):
        return Thread(self._thread)
    def get_loop_time_us(self):
        return self._loop_time_us
    def get_truncated_start_time_us(self):
        return self._truncated_start_time_us
    def get_all_data(self):
        data = []
        data.append((fields.type, self.get_type()))
        data.append((fields.thread, self.get_thread()))
        data.append((fields.loop_time_us, self.get_loop_time_us()))
        data.append((fields.truncated_start_time_us, self.get_truncated_start_time_us()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._type = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._thread = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._loop_time_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._truncated_start_time_us = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class LoopInfo_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.LoopInfo
        self._category = categories.none
        self._id = 205
        self._size = 8
        self._type = 0
        self._thread = 0
        self._loop_time_us = 0
        self._truncated_start_time_us = 0
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
    def set_type(self, value):
        self._type = value.value
    def set_thread(self, value):
        self._thread = value.value
    def set_loop_time_us(self, value):
        self._loop_time_us = value
    def set_truncated_start_time_us(self, value):
        self._truncated_start_time_us = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._type)
        buf += struct.pack("<B", self._thread)
        buf += struct.pack("<L", self._loop_time_us)
        buf += struct.pack("<H", self._truncated_start_time_us)
        return buf
    def get_type(self):
        return LoopType(self._type)
    def get_thread(self):
        return Thread(self._thread)
    def get_loop_time_us(self):
        return self._loop_time_us
    def get_truncated_start_time_us(self):
        return self._truncated_start_time_us
    def get_all_data(self):
        data = []
        data.append((fields.type, self.get_type()))
        data.append((fields.thread, self.get_thread()))
        data.append((fields.loop_time_us, self.get_loop_time_us()))
        data.append((fields.truncated_start_time_us, self.get_truncated_start_time_us()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._type = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._thread = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._loop_time_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._truncated_start_time_us = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class OneWireDevicePairedWithSensor_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.OneWireDevicePairedWithSensor
        self._category = categories.none
        self._id = 207
        self._size = 8
        self._bus = 0
        self._position_on_board = 0
        self._serial_byte0 = 0
        self._serial_byte1 = 0
        self._serial_byte2 = 0
        self._serial_byte3 = 0
        self._serial_byte4 = 0
        self._serial_byte5 = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_position_on_board(self, value):
        self._position_on_board = value
    def set_serial_byte0(self, value):
        self._serial_byte0 = value
    def set_serial_byte1(self, value):
        self._serial_byte1 = value
    def set_serial_byte2(self, value):
        self._serial_byte2 = value
    def set_serial_byte3(self, value):
        self._serial_byte3 = value
    def set_serial_byte4(self, value):
        self._serial_byte4 = value
    def set_serial_byte5(self, value):
        self._serial_byte5 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._position_on_board)
        buf += struct.pack("<B", self._serial_byte0)
        buf += struct.pack("<B", self._serial_byte1)
        buf += struct.pack("<B", self._serial_byte2)
        buf += struct.pack("<B", self._serial_byte3)
        buf += struct.pack("<B", self._serial_byte4)
        buf += struct.pack("<B", self._serial_byte5)
        return buf
    def get_bus(self):
        return OneWireBus(self._bus)
    def get_position_on_board(self):
        return self._position_on_board
    def get_serial_byte0(self):
        return self._serial_byte0
    def get_serial_byte1(self):
        return self._serial_byte1
    def get_serial_byte2(self):
        return self._serial_byte2
    def get_serial_byte3(self):
        return self._serial_byte3
    def get_serial_byte4(self):
        return self._serial_byte4
    def get_serial_byte5(self):
        return self._serial_byte5
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.position_on_board, self.get_position_on_board()))
        data.append((fields.serial_byte0, self.get_serial_byte0()))
        data.append((fields.serial_byte1, self.get_serial_byte1()))
        data.append((fields.serial_byte2, self.get_serial_byte2()))
        data.append((fields.serial_byte3, self.get_serial_byte3()))
        data.append((fields.serial_byte4, self.get_serial_byte4()))
        data.append((fields.serial_byte5, self.get_serial_byte5()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._position_on_board = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte5 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class OneWireSearchFamilyMismatch_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.OneWireSearchFamilyMismatch
        self._category = categories.none
        self._id = 208
        self._size = 8
        self._bus = 0
        self._serial_byte0 = 0
        self._serial_byte1 = 0
        self._serial_byte2 = 0
        self._serial_byte3 = 0
        self._serial_byte4 = 0
        self._serial_byte5 = 0
        self._found_family_code = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_serial_byte0(self, value):
        self._serial_byte0 = value
    def set_serial_byte1(self, value):
        self._serial_byte1 = value
    def set_serial_byte2(self, value):
        self._serial_byte2 = value
    def set_serial_byte3(self, value):
        self._serial_byte3 = value
    def set_serial_byte4(self, value):
        self._serial_byte4 = value
    def set_serial_byte5(self, value):
        self._serial_byte5 = value
    def set_found_family_code(self, value):
        self._found_family_code = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._serial_byte0)
        buf += struct.pack("<B", self._serial_byte1)
        buf += struct.pack("<B", self._serial_byte2)
        buf += struct.pack("<B", self._serial_byte3)
        buf += struct.pack("<B", self._serial_byte4)
        buf += struct.pack("<B", self._serial_byte5)
        buf += struct.pack("<B", self._found_family_code)
        return buf
    def get_bus(self):
        return OneWireBus(self._bus)
    def get_serial_byte0(self):
        return self._serial_byte0
    def get_serial_byte1(self):
        return self._serial_byte1
    def get_serial_byte2(self):
        return self._serial_byte2
    def get_serial_byte3(self):
        return self._serial_byte3
    def get_serial_byte4(self):
        return self._serial_byte4
    def get_serial_byte5(self):
        return self._serial_byte5
    def get_found_family_code(self):
        return self._found_family_code
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.serial_byte0, self.get_serial_byte0()))
        data.append((fields.serial_byte1, self.get_serial_byte1()))
        data.append((fields.serial_byte2, self.get_serial_byte2()))
        data.append((fields.serial_byte3, self.get_serial_byte3()))
        data.append((fields.serial_byte4, self.get_serial_byte4()))
        data.append((fields.serial_byte5, self.get_serial_byte5()))
        data.append((fields.found_family_code, self.get_found_family_code()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte5 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._found_family_code = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class OneWireSearchCRCMismatch_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.OneWireSearchCRCMismatch
        self._category = categories.none
        self._id = 209
        self._size = 8
        self._bus = 0
        self._serial_byte0 = 0
        self._serial_byte1 = 0
        self._serial_byte2 = 0
        self._serial_byte3 = 0
        self._serial_byte4 = 0
        self._serial_byte5 = 0
        self._found_crc = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_serial_byte0(self, value):
        self._serial_byte0 = value
    def set_serial_byte1(self, value):
        self._serial_byte1 = value
    def set_serial_byte2(self, value):
        self._serial_byte2 = value
    def set_serial_byte3(self, value):
        self._serial_byte3 = value
    def set_serial_byte4(self, value):
        self._serial_byte4 = value
    def set_serial_byte5(self, value):
        self._serial_byte5 = value
    def set_found_crc(self, value):
        self._found_crc = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._serial_byte0)
        buf += struct.pack("<B", self._serial_byte1)
        buf += struct.pack("<B", self._serial_byte2)
        buf += struct.pack("<B", self._serial_byte3)
        buf += struct.pack("<B", self._serial_byte4)
        buf += struct.pack("<B", self._serial_byte5)
        buf += struct.pack("<B", self._found_crc)
        return buf
    def get_bus(self):
        return OneWireBus(self._bus)
    def get_serial_byte0(self):
        return self._serial_byte0
    def get_serial_byte1(self):
        return self._serial_byte1
    def get_serial_byte2(self):
        return self._serial_byte2
    def get_serial_byte3(self):
        return self._serial_byte3
    def get_serial_byte4(self):
        return self._serial_byte4
    def get_serial_byte5(self):
        return self._serial_byte5
    def get_found_crc(self):
        return self._found_crc
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.serial_byte0, self.get_serial_byte0()))
        data.append((fields.serial_byte1, self.get_serial_byte1()))
        data.append((fields.serial_byte2, self.get_serial_byte2()))
        data.append((fields.serial_byte3, self.get_serial_byte3()))
        data.append((fields.serial_byte4, self.get_serial_byte4()))
        data.append((fields.serial_byte5, self.get_serial_byte5()))
        data.append((fields.found_crc, self.get_found_crc()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte5 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._found_crc = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class OneWireSearchFoundDevice_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.OneWireSearchFoundDevice
        self._category = categories.none
        self._id = 210
        self._size = 7
        self._bus = 0
        self._serial_byte0 = 0
        self._serial_byte1 = 0
        self._serial_byte2 = 0
        self._serial_byte3 = 0
        self._serial_byte4 = 0
        self._serial_byte5 = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_serial_byte0(self, value):
        self._serial_byte0 = value
    def set_serial_byte1(self, value):
        self._serial_byte1 = value
    def set_serial_byte2(self, value):
        self._serial_byte2 = value
    def set_serial_byte3(self, value):
        self._serial_byte3 = value
    def set_serial_byte4(self, value):
        self._serial_byte4 = value
    def set_serial_byte5(self, value):
        self._serial_byte5 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._serial_byte0)
        buf += struct.pack("<B", self._serial_byte1)
        buf += struct.pack("<B", self._serial_byte2)
        buf += struct.pack("<B", self._serial_byte3)
        buf += struct.pack("<B", self._serial_byte4)
        buf += struct.pack("<B", self._serial_byte5)
        return buf
    def get_bus(self):
        return OneWireBus(self._bus)
    def get_serial_byte0(self):
        return self._serial_byte0
    def get_serial_byte1(self):
        return self._serial_byte1
    def get_serial_byte2(self):
        return self._serial_byte2
    def get_serial_byte3(self):
        return self._serial_byte3
    def get_serial_byte4(self):
        return self._serial_byte4
    def get_serial_byte5(self):
        return self._serial_byte5
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.serial_byte0, self.get_serial_byte0()))
        data.append((fields.serial_byte1, self.get_serial_byte1()))
        data.append((fields.serial_byte2, self.get_serial_byte2()))
        data.append((fields.serial_byte3, self.get_serial_byte3()))
        data.append((fields.serial_byte4, self.get_serial_byte4()))
        data.append((fields.serial_byte5, self.get_serial_byte5()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte5 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_Temperature_from_Edda_Power_Control_Boards_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Power_Control_Boards
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_Temperature
        self._category = categories.none
        self._id = 215
        self._size = 6
        self._kind = 0
        self._temperature_celsius = 0
        self._powercan_channel = 0
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
    def set_kind(self, value):
        self._kind = value.value
    def set_temperature_celsius(self, value):
        self._temperature_celsius = packedFloat_to_uint(value, -100, 300, 4)
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._kind)
        buf += struct.pack("<L", self._temperature_celsius)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_kind(self):
        return PowerCAN_TemperatureKind(self._kind)
    def get_temperature_celsius(self):
        return uint_to_packedFloat(self._temperature_celsius, -100, 300, 4)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.kind, self.get_kind()))
        data.append((fields.temperature_celsius, self.get_temperature_celsius()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._kind = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._temperature_celsius = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_Voltage_from_Edda_Power_Control_Boards_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Power_Control_Boards
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_Voltage
        self._category = categories.none
        self._id = 216
        self._size = 6
        self._kind = 0
        self._voltage_volt = 0
        self._powercan_channel = 0
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
    def set_kind(self, value):
        self._kind = value.value
    def set_voltage_volt(self, value):
        self._voltage_volt = packedFloat_to_uint(value, -30, 30, 4)
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._kind)
        buf += struct.pack("<L", self._voltage_volt)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_kind(self):
        return PowerCAN_VoltageKind(self._kind)
    def get_voltage_volt(self):
        return uint_to_packedFloat(self._voltage_volt, -30, 30, 4)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.kind, self.get_kind()))
        data.append((fields.voltage_volt, self.get_voltage_volt()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._kind = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._voltage_volt = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_ChannelMeasurementPower_from_Edda_Power_Control_Boards_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Power_Control_Boards
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_ChannelMeasurementPower
        self._category = categories.none
        self._id = 217
        self._size = 6
        self._channel = 0
        self._power_watt = 0
        self._powercan_channel = 0
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
    def set_channel(self, value):
        self._channel = value.value
    def set_power_watt(self, value):
        self._power_watt = packedFloat_to_uint(value, 0, 1000, 4)
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._channel)
        buf += struct.pack("<L", self._power_watt)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_channel(self):
        return PowerCAN_MeasurementChannel(self._channel)
    def get_power_watt(self):
        return uint_to_packedFloat(self._power_watt, 0, 1000, 4)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.channel, self.get_channel()))
        data.append((fields.power_watt, self.get_power_watt()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._power_watt = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_ChannelMeasurementVoltage_from_Edda_Power_Control_Boards_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Power_Control_Boards
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_ChannelMeasurementVoltage
        self._category = categories.none
        self._id = 218
        self._size = 6
        self._channel = 0
        self._voltage_volt = 0
        self._powercan_channel = 0
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
    def set_channel(self, value):
        self._channel = value.value
    def set_voltage_volt(self, value):
        self._voltage_volt = packedFloat_to_uint(value, -30, 30, 4)
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._channel)
        buf += struct.pack("<L", self._voltage_volt)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_channel(self):
        return PowerCAN_MeasurementChannel(self._channel)
    def get_voltage_volt(self):
        return uint_to_packedFloat(self._voltage_volt, -30, 30, 4)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.channel, self.get_channel()))
        data.append((fields.voltage_volt, self.get_voltage_volt()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._voltage_volt = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_ChannelMeasurementCurrent_from_Edda_Power_Control_Boards_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Power_Control_Boards
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_ChannelMeasurementCurrent
        self._category = categories.none
        self._id = 219
        self._size = 6
        self._channel = 0
        self._current_ampere = 0
        self._powercan_channel = 0
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
    def set_channel(self, value):
        self._channel = value.value
    def set_current_ampere(self, value):
        self._current_ampere = packedFloat_to_uint(value, 0, 30, 4)
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._channel)
        buf += struct.pack("<L", self._current_ampere)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_channel(self):
        return PowerCAN_MeasurementChannel(self._channel)
    def get_current_ampere(self):
        return uint_to_packedFloat(self._current_ampere, 0, 30, 4)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.channel, self.get_channel()))
        data.append((fields.current_ampere, self.get_current_ampere()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._current_ampere = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_LoadMeasurementResistance_from_Edda_Power_Control_Boards_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Power_Control_Boards
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_LoadMeasurementResistance
        self._category = categories.none
        self._id = 220
        self._size = 7
        self._measurement_reference = 0
        self._result = 0
        self._resistance_ohm = 0
        self._powercan_channel = 0
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
    def set_measurement_reference(self, value):
        self._measurement_reference = value.value
    def set_result(self, value):
        self._result = value.value
    def set_resistance_ohm(self, value):
        self._resistance_ohm = packedFloat_to_uint(value, 0, 100000, 4)
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._measurement_reference)
        buf += struct.pack("<B", self._result)
        buf += struct.pack("<L", self._resistance_ohm)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_measurement_reference(self):
        return PowerCAN_MeasurementReference(self._measurement_reference)
    def get_result(self):
        return PowerCAN_LoadMeasurementResult(self._result)
    def get_resistance_ohm(self):
        return uint_to_packedFloat(self._resistance_ohm, 0, 100000, 4)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.measurement_reference, self.get_measurement_reference()))
        data.append((fields.result, self.get_result()))
        data.append((fields.resistance_ohm, self.get_resistance_ohm()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._measurement_reference = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._result = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._resistance_ohm = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_LoadMeasurementVoltage_from_Edda_Power_Control_Boards_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Power_Control_Boards
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_LoadMeasurementVoltage
        self._category = categories.none
        self._id = 221
        self._size = 7
        self._measurement_reference = 0
        self._result = 0
        self._voltage_volt = 0
        self._powercan_channel = 0
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
    def set_measurement_reference(self, value):
        self._measurement_reference = value.value
    def set_result(self, value):
        self._result = value.value
    def set_voltage_volt(self, value):
        self._voltage_volt = packedFloat_to_uint(value, -30, 30, 4)
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._measurement_reference)
        buf += struct.pack("<B", self._result)
        buf += struct.pack("<L", self._voltage_volt)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_measurement_reference(self):
        return PowerCAN_MeasurementReference(self._measurement_reference)
    def get_result(self):
        return PowerCAN_LoadMeasurementResult(self._result)
    def get_voltage_volt(self):
        return uint_to_packedFloat(self._voltage_volt, -30, 30, 4)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.measurement_reference, self.get_measurement_reference()))
        data.append((fields.result, self.get_result()))
        data.append((fields.voltage_volt, self.get_voltage_volt()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._measurement_reference = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._result = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._voltage_volt = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_LoadMeasurementPower_from_Edda_Power_Control_Boards_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Power_Control_Boards
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_LoadMeasurementPower
        self._category = categories.none
        self._id = 222
        self._size = 7
        self._measurement_reference = 0
        self._result = 0
        self._power_watt = 0
        self._powercan_channel = 0
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
    def set_measurement_reference(self, value):
        self._measurement_reference = value.value
    def set_result(self, value):
        self._result = value.value
    def set_power_watt(self, value):
        self._power_watt = packedFloat_to_uint(value, 0, 1000, 4)
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._measurement_reference)
        buf += struct.pack("<B", self._result)
        buf += struct.pack("<L", self._power_watt)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_measurement_reference(self):
        return PowerCAN_MeasurementReference(self._measurement_reference)
    def get_result(self):
        return PowerCAN_LoadMeasurementResult(self._result)
    def get_power_watt(self):
        return uint_to_packedFloat(self._power_watt, 0, 1000, 4)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.measurement_reference, self.get_measurement_reference()))
        data.append((fields.result, self.get_result()))
        data.append((fields.power_watt, self.get_power_watt()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._measurement_reference = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._result = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._power_watt = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_LoadMeasurementCurrent_from_Edda_Power_Control_Boards_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Power_Control_Boards
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_LoadMeasurementCurrent
        self._category = categories.none
        self._id = 223
        self._size = 7
        self._measurement_reference = 0
        self._result = 0
        self._current_ampere = 0
        self._powercan_channel = 0
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
    def set_measurement_reference(self, value):
        self._measurement_reference = value.value
    def set_result(self, value):
        self._result = value.value
    def set_current_ampere(self, value):
        self._current_ampere = packedFloat_to_uint(value, 0, 30, 4)
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._measurement_reference)
        buf += struct.pack("<B", self._result)
        buf += struct.pack("<L", self._current_ampere)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_measurement_reference(self):
        return PowerCAN_MeasurementReference(self._measurement_reference)
    def get_result(self):
        return PowerCAN_LoadMeasurementResult(self._result)
    def get_current_ampere(self):
        return uint_to_packedFloat(self._current_ampere, 0, 30, 4)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.measurement_reference, self.get_measurement_reference()))
        data.append((fields.result, self.get_result()))
        data.append((fields.current_ampere, self.get_current_ampere()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._measurement_reference = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._result = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._current_ampere = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_FailedLoadMeasurementValue_from_Edda_Power_Control_Boards_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Power_Control_Boards
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_FailedLoadMeasurementValue
        self._category = categories.none
        self._id = 224
        self._size = 7
        self._measurement_reference = 0
        self._failure_reason = 0
        self._value = 0
        self._powercan_channel = 0
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
    def set_measurement_reference(self, value):
        self._measurement_reference = value.value
    def set_failure_reason(self, value):
        self._failure_reason = value.value
    def set_value(self, value):
        self._value = packedFloat_to_uint(value, 0, 1000000, 4)
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._measurement_reference)
        buf += struct.pack("<B", self._failure_reason)
        buf += struct.pack("<L", self._value)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_measurement_reference(self):
        return PowerCAN_MeasurementReference(self._measurement_reference)
    def get_failure_reason(self):
        return PowerCAN_MeasurementFailureReason(self._failure_reason)
    def get_value(self):
        return uint_to_packedFloat(self._value, 0, 1000000, 4)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.measurement_reference, self.get_measurement_reference()))
        data.append((fields.failure_reason, self.get_failure_reason()))
        data.append((fields.value, self.get_value()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._measurement_reference = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._failure_reason = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._value = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_FailedLoadMeasurementThreshold_from_Edda_Power_Control_Boards_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Power_Control_Boards
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_FailedLoadMeasurementThreshold
        self._category = categories.none
        self._id = 225
        self._size = 7
        self._measurement_reference = 0
        self._failure_reason = 0
        self._threshold = 0
        self._powercan_channel = 0
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
    def set_measurement_reference(self, value):
        self._measurement_reference = value.value
    def set_failure_reason(self, value):
        self._failure_reason = value.value
    def set_threshold(self, value):
        self._threshold = packedFloat_to_uint(value, 0, 1000000, 4)
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._measurement_reference)
        buf += struct.pack("<B", self._failure_reason)
        buf += struct.pack("<L", self._threshold)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_measurement_reference(self):
        return PowerCAN_MeasurementReference(self._measurement_reference)
    def get_failure_reason(self):
        return PowerCAN_MeasurementFailureReason(self._failure_reason)
    def get_threshold(self):
        return uint_to_packedFloat(self._threshold, 0, 1000000, 4)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.measurement_reference, self.get_measurement_reference()))
        data.append((fields.failure_reason, self.get_failure_reason()))
        data.append((fields.threshold, self.get_threshold()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._measurement_reference = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._failure_reason = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._threshold = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_ResistanceMeasurementResistance_from_Edda_Power_Control_Boards_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Power_Control_Boards
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_ResistanceMeasurementResistance
        self._category = categories.none
        self._id = 226
        self._size = 7
        self._measurement_reference = 0
        self._validity = 0
        self._resistance_ohm = 0
        self._powercan_channel = 0
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
    def set_measurement_reference(self, value):
        self._measurement_reference = value.value
    def set_validity(self, value):
        self._validity = value.value
    def set_resistance_ohm(self, value):
        self._resistance_ohm = packedFloat_to_uint(value, 0, 100000, 4)
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._measurement_reference)
        buf += struct.pack("<B", self._validity)
        buf += struct.pack("<L", self._resistance_ohm)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_measurement_reference(self):
        return PowerCAN_ResistanceMeasurementReference(self._measurement_reference)
    def get_validity(self):
        return PowerCAN_ResistanceMeasurementValidity(self._validity)
    def get_resistance_ohm(self):
        return uint_to_packedFloat(self._resistance_ohm, 0, 100000, 4)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.measurement_reference, self.get_measurement_reference()))
        data.append((fields.validity, self.get_validity()))
        data.append((fields.resistance_ohm, self.get_resistance_ohm()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._measurement_reference = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._validity = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._resistance_ohm = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_ResistanceMeasurementReferenceVoltage_from_Edda_Power_Control_Boards_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Power_Control_Boards
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_ResistanceMeasurementReferenceVoltage
        self._category = categories.none
        self._id = 227
        self._size = 7
        self._measurement_reference = 0
        self._validity = 0
        self._reference_voltage_volt = 0
        self._powercan_channel = 0
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
    def set_measurement_reference(self, value):
        self._measurement_reference = value.value
    def set_validity(self, value):
        self._validity = value.value
    def set_reference_voltage_volt(self, value):
        self._reference_voltage_volt = packedFloat_to_uint(value, 0, 5, 4)
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._measurement_reference)
        buf += struct.pack("<B", self._validity)
        buf += struct.pack("<L", self._reference_voltage_volt)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_measurement_reference(self):
        return PowerCAN_ResistanceMeasurementReference(self._measurement_reference)
    def get_validity(self):
        return PowerCAN_ResistanceMeasurementValidity(self._validity)
    def get_reference_voltage_volt(self):
        return uint_to_packedFloat(self._reference_voltage_volt, 0, 5, 4)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.measurement_reference, self.get_measurement_reference()))
        data.append((fields.validity, self.get_validity()))
        data.append((fields.reference_voltage_volt, self.get_reference_voltage_volt()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._measurement_reference = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._validity = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._reference_voltage_volt = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_ResistanceMeasurementDifferentialVoltage_from_Edda_Power_Control_Boards_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Power_Control_Boards
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_ResistanceMeasurementDifferentialVoltage
        self._category = categories.none
        self._id = 228
        self._size = 7
        self._measurement_reference = 0
        self._validity = 0
        self._differential_voltage_volt = 0
        self._powercan_channel = 0
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
    def set_measurement_reference(self, value):
        self._measurement_reference = value.value
    def set_validity(self, value):
        self._validity = value.value
    def set_differential_voltage_volt(self, value):
        self._differential_voltage_volt = packedFloat_to_uint(value, 0, 5, 4)
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._measurement_reference)
        buf += struct.pack("<B", self._validity)
        buf += struct.pack("<L", self._differential_voltage_volt)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_measurement_reference(self):
        return PowerCAN_ResistanceMeasurementReference(self._measurement_reference)
    def get_validity(self):
        return PowerCAN_ResistanceMeasurementValidity(self._validity)
    def get_differential_voltage_volt(self):
        return uint_to_packedFloat(self._differential_voltage_volt, 0, 5, 4)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.measurement_reference, self.get_measurement_reference()))
        data.append((fields.validity, self.get_validity()))
        data.append((fields.differential_voltage_volt, self.get_differential_voltage_volt()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._measurement_reference = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._validity = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._differential_voltage_volt = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_ResistanceMeasurementPositiveVoltage_from_Edda_Power_Control_Boards_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Power_Control_Boards
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_ResistanceMeasurementPositiveVoltage
        self._category = categories.none
        self._id = 229
        self._size = 7
        self._measurement_reference = 0
        self._validity = 0
        self._positive_voltage_volt = 0
        self._powercan_channel = 0
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
    def set_measurement_reference(self, value):
        self._measurement_reference = value.value
    def set_validity(self, value):
        self._validity = value.value
    def set_positive_voltage_volt(self, value):
        self._positive_voltage_volt = packedFloat_to_uint(value, 0, 5, 4)
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._measurement_reference)
        buf += struct.pack("<B", self._validity)
        buf += struct.pack("<L", self._positive_voltage_volt)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_measurement_reference(self):
        return PowerCAN_ResistanceMeasurementReference(self._measurement_reference)
    def get_validity(self):
        return PowerCAN_ResistanceMeasurementValidity(self._validity)
    def get_positive_voltage_volt(self):
        return uint_to_packedFloat(self._positive_voltage_volt, 0, 5, 4)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.measurement_reference, self.get_measurement_reference()))
        data.append((fields.validity, self.get_validity()))
        data.append((fields.positive_voltage_volt, self.get_positive_voltage_volt()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._measurement_reference = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._validity = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._positive_voltage_volt = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_ResistanceMeasurementNegativeVoltage_from_Edda_Power_Control_Boards_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Power_Control_Boards
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_ResistanceMeasurementNegativeVoltage
        self._category = categories.none
        self._id = 230
        self._size = 7
        self._measurement_reference = 0
        self._validity = 0
        self._negative_voltage_volt = 0
        self._powercan_channel = 0
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
    def set_measurement_reference(self, value):
        self._measurement_reference = value.value
    def set_validity(self, value):
        self._validity = value.value
    def set_negative_voltage_volt(self, value):
        self._negative_voltage_volt = packedFloat_to_uint(value, 0, 5, 4)
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._measurement_reference)
        buf += struct.pack("<B", self._validity)
        buf += struct.pack("<L", self._negative_voltage_volt)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_measurement_reference(self):
        return PowerCAN_ResistanceMeasurementReference(self._measurement_reference)
    def get_validity(self):
        return PowerCAN_ResistanceMeasurementValidity(self._validity)
    def get_negative_voltage_volt(self):
        return uint_to_packedFloat(self._negative_voltage_volt, 0, 5, 4)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.measurement_reference, self.get_measurement_reference()))
        data.append((fields.validity, self.get_validity()))
        data.append((fields.negative_voltage_volt, self.get_negative_voltage_volt()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._measurement_reference = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._validity = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._negative_voltage_volt = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_I2CBusStarted_from_Edda_Power_Control_Boards_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Power_Control_Boards
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_I2CBusStarted
        self._category = categories.none
        self._id = 231
        self._size = 6
        self._bus = 0
        self._frequency_hertz = 0
        self._powercan_channel = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_frequency_hertz(self, value):
        self._frequency_hertz = value
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<L", self._frequency_hertz)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_bus(self):
        return PowerCAN_I2CBus(self._bus)
    def get_frequency_hertz(self):
        return self._frequency_hertz
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.frequency_hertz, self.get_frequency_hertz()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._frequency_hertz = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_I2CSearchStarted_from_Edda_Power_Control_Boards_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Power_Control_Boards
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_I2CSearchStarted
        self._category = categories.none
        self._id = 232
        self._size = 2
        self._bus = 0
        self._powercan_channel = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_bus(self):
        return PowerCAN_I2CBus(self._bus)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_I2CSearchFoundDevice_from_Edda_Power_Control_Boards_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Power_Control_Boards
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_I2CSearchFoundDevice
        self._category = categories.none
        self._id = 233
        self._size = 3
        self._bus = 0
        self._found_device_address = 0
        self._powercan_channel = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_found_device_address(self, value):
        self._found_device_address = value
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._found_device_address)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_bus(self):
        return PowerCAN_I2CBus(self._bus)
    def get_found_device_address(self):
        return self._found_device_address
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.found_device_address, self.get_found_device_address()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._found_device_address = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_I2CSearchMissingDevice_from_Edda_Power_Control_Boards_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Power_Control_Boards
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_I2CSearchMissingDevice
        self._category = categories.none
        self._id = 234
        self._size = 3
        self._bus = 0
        self._missing_device_address = 0
        self._powercan_channel = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_missing_device_address(self, value):
        self._missing_device_address = value
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._missing_device_address)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_bus(self):
        return PowerCAN_I2CBus(self._bus)
    def get_missing_device_address(self):
        return self._missing_device_address
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.missing_device_address, self.get_missing_device_address()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._missing_device_address = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_I2CSearchEnded_from_Edda_Power_Control_Boards_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Power_Control_Boards
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_I2CSearchEnded
        self._category = categories.none
        self._id = 235
        self._size = 8
        self._bus = 0
        self._devices_successfully_found = 0
        self._addresses_with_error = 0
        self._search_time_us = 0
        self._powercan_channel = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_devices_successfully_found(self, value):
        self._devices_successfully_found = value
    def set_addresses_with_error(self, value):
        self._addresses_with_error = value
    def set_search_time_us(self, value):
        self._search_time_us = value
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._devices_successfully_found)
        buf += struct.pack("<B", self._addresses_with_error)
        buf += struct.pack("<L", self._search_time_us)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_bus(self):
        return PowerCAN_I2CBus(self._bus)
    def get_devices_successfully_found(self):
        return self._devices_successfully_found
    def get_addresses_with_error(self):
        return self._addresses_with_error
    def get_search_time_us(self):
        return self._search_time_us
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.devices_successfully_found, self.get_devices_successfully_found()))
        data.append((fields.addresses_with_error, self.get_addresses_with_error()))
        data.append((fields.search_time_us, self.get_search_time_us()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._devices_successfully_found = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._addresses_with_error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._search_time_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_LTC2992Error_from_Edda_Power_Control_Boards_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Power_Control_Boards
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_LTC2992Error
        self._category = categories.none
        self._id = 236
        self._size = 7
        self._error = 0
        self._location = 0
        self._register_address = 0
        self._read_data = 0
        self._write_data = 0
        self._expected_data = 0
        self._powercan_channel = 0
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
    def set_error(self, value):
        self._error = value.value
    def set_location(self, value):
        self._location = value.value
    def set_register_address(self, value):
        self._register_address = value
    def set_read_data(self, value):
        self._read_data = value
    def set_write_data(self, value):
        self._write_data = value
    def set_expected_data(self, value):
        self._expected_data = value
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._error)
        buf += struct.pack("<B", self._location)
        buf += struct.pack("<B", self._register_address)
        buf += struct.pack("<B", self._read_data)
        buf += struct.pack("<B", self._write_data)
        buf += struct.pack("<B", self._expected_data)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_error(self):
        return PowerCAN_LTC2992Error(self._error)
    def get_location(self):
        return PowerCAN_LTC2992ErrorLocation(self._location)
    def get_register_address(self):
        return self._register_address
    def get_read_data(self):
        return self._read_data
    def get_write_data(self):
        return self._write_data
    def get_expected_data(self):
        return self._expected_data
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.error, self.get_error()))
        data.append((fields.location, self.get_location()))
        data.append((fields.register_address, self.get_register_address()))
        data.append((fields.read_data, self.get_read_data()))
        data.append((fields.write_data, self.get_write_data()))
        data.append((fields.expected_data, self.get_expected_data()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._location = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._register_address = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._read_data = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._write_data = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._expected_data = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_ADS122C04Error_from_Edda_Power_Control_Boards_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Power_Control_Boards
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_ADS122C04Error
        self._category = categories.none
        self._id = 237
        self._size = 7
        self._error = 0
        self._location = 0
        self._register_address = 0
        self._read_data = 0
        self._write_data = 0
        self._expected_data = 0
        self._powercan_channel = 0
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
    def set_error(self, value):
        self._error = value.value
    def set_location(self, value):
        self._location = value.value
    def set_register_address(self, value):
        self._register_address = value
    def set_read_data(self, value):
        self._read_data = value
    def set_write_data(self, value):
        self._write_data = value
    def set_expected_data(self, value):
        self._expected_data = value
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._error)
        buf += struct.pack("<B", self._location)
        buf += struct.pack("<B", self._register_address)
        buf += struct.pack("<B", self._read_data)
        buf += struct.pack("<B", self._write_data)
        buf += struct.pack("<B", self._expected_data)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_error(self):
        return PowerCAN_ADS122C04Error(self._error)
    def get_location(self):
        return PowerCAN_ADS122C04ErrorLocation(self._location)
    def get_register_address(self):
        return self._register_address
    def get_read_data(self):
        return self._read_data
    def get_write_data(self):
        return self._write_data
    def get_expected_data(self):
        return self._expected_data
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.error, self.get_error()))
        data.append((fields.location, self.get_location()))
        data.append((fields.register_address, self.get_register_address()))
        data.append((fields.read_data, self.get_read_data()))
        data.append((fields.write_data, self.get_write_data()))
        data.append((fields.expected_data, self.get_expected_data()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._location = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._register_address = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._read_data = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._write_data = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._expected_data = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_I2CSearchError_from_Edda_Power_Control_Boards_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Power_Control_Boards
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_I2CSearchError
        self._category = categories.none
        self._id = 238
        self._size = 4
        self._bus = 0
        self._error = 0
        self._scanned_address = 0
        self._powercan_channel = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_error(self, value):
        self._error = value.value
    def set_scanned_address(self, value):
        self._scanned_address = value
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._error)
        buf += struct.pack("<B", self._scanned_address)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_bus(self):
        return PowerCAN_I2CBus(self._bus)
    def get_error(self):
        return PowerCAN_I2CError(self._error)
    def get_scanned_address(self):
        return self._scanned_address
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.error, self.get_error()))
        data.append((fields.scanned_address, self.get_scanned_address()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._scanned_address = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_ErrorStatistics_from_Edda_Power_Control_Boards_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Power_Control_Boards
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_ErrorStatistics
        self._category = categories.none
        self._id = 239
        self._size = 5
        self._warning_count = 0
        self._error_count = 0
        self._powercan_channel = 0
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
    def set_warning_count(self, value):
        self._warning_count = value
    def set_error_count(self, value):
        self._error_count = value
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._warning_count)
        buf += struct.pack("<H", self._error_count)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_warning_count(self):
        return self._warning_count
    def get_error_count(self):
        return self._error_count
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.warning_count, self.get_warning_count()))
        data.append((fields.error_count, self.get_error_count()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._warning_count = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._error_count = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class DS2482Error_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.DS2482Error
        self._category = categories.none
        self._id = 442
        self._size = 5
        self._error = 0
        self._board_index = 0
        self._bus_index = 0
        self._position_on_bus = 0
        self._position_on_board = 0
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
    def set_error(self, value):
        self._error = value.value
    def set_board_index(self, value):
        self._board_index = value.value
    def set_bus_index(self, value):
        self._bus_index = value.value
    def set_position_on_bus(self, value):
        self._position_on_bus = value
    def set_position_on_board(self, value):
        self._position_on_board = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._error)
        buf += struct.pack("<B", self._board_index)
        buf += struct.pack("<B", self._bus_index)
        buf += struct.pack("<B", self._position_on_bus)
        buf += struct.pack("<B", self._position_on_board)
        return buf
    def get_error(self):
        return DS2482Error(self._error)
    def get_board_index(self):
        return TemperatureBoardIndex(self._board_index)
    def get_bus_index(self):
        return OneWireBus(self._bus_index)
    def get_position_on_bus(self):
        return self._position_on_bus
    def get_position_on_board(self):
        return self._position_on_board
    def get_all_data(self):
        data = []
        data.append((fields.error, self.get_error()))
        data.append((fields.board_index, self.get_board_index()))
        data.append((fields.bus_index, self.get_bus_index()))
        data.append((fields.position_on_bus, self.get_position_on_bus()))
        data.append((fields.position_on_board, self.get_position_on_board()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._board_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._bus_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._position_on_bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._position_on_board = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage1_from_Edda_Controller_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage1
        self._category = categories.none
        self._id = 450
        self._size = 1
        self._byte0 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage1_from_Edda_Telemetry_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage1
        self._category = categories.none
        self._id = 451
        self._size = 1
        self._byte0 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage1_from_Edda_Pressure_Top_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage1
        self._category = categories.none
        self._id = 452
        self._size = 1
        self._byte0 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage1_from_Edda_Pressure_Bottom_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage1
        self._category = categories.none
        self._id = 453
        self._size = 1
        self._byte0 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class OneWireSearchStarted_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.OneWireSearchStarted
        self._category = categories.none
        self._id = 462
        self._size = 5
        self._bus = 0
        self._start_time_ms = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_start_time_ms(self, value):
        self._start_time_ms = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<L", self._start_time_ms)
        return buf
    def get_bus(self):
        return OneWireBus(self._bus)
    def get_start_time_ms(self):
        return self._start_time_ms
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.start_time_ms, self.get_start_time_ms()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._start_time_ms = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class I2CBusStarted_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CBusStarted
        self._category = categories.none
        self._id = 467
        self._size = 5
        self._bus = 0
        self._frequency_hertz = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_frequency_hertz(self, value):
        self._frequency_hertz = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<L", self._frequency_hertz)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_frequency_hertz(self):
        return self._frequency_hertz
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.frequency_hertz, self.get_frequency_hertz()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._frequency_hertz = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class I2CBusStarted_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CBusStarted
        self._category = categories.none
        self._id = 468
        self._size = 5
        self._bus = 0
        self._frequency_hertz = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_frequency_hertz(self, value):
        self._frequency_hertz = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<L", self._frequency_hertz)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_frequency_hertz(self):
        return self._frequency_hertz
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.frequency_hertz, self.get_frequency_hertz()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._frequency_hertz = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class I2CBusStarted_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CBusStarted
        self._category = categories.none
        self._id = 469
        self._size = 5
        self._bus = 0
        self._frequency_hertz = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_frequency_hertz(self, value):
        self._frequency_hertz = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<L", self._frequency_hertz)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_frequency_hertz(self):
        return self._frequency_hertz
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.frequency_hertz, self.get_frequency_hertz()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._frequency_hertz = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class I2CBusStarted_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CBusStarted
        self._category = categories.none
        self._id = 470
        self._size = 5
        self._bus = 0
        self._frequency_hertz = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_frequency_hertz(self, value):
        self._frequency_hertz = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<L", self._frequency_hertz)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_frequency_hertz(self):
        return self._frequency_hertz
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.frequency_hertz, self.get_frequency_hertz()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._frequency_hertz = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class DS28E18QError_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.DS28E18QError
        self._category = categories.none
        self._id = 698
        self._size = 5
        self._error = 0
        self._board_index = 0
        self._bus_index = 0
        self._position_on_bus = 0
        self._position_on_board = 0
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
    def set_error(self, value):
        self._error = value.value
    def set_board_index(self, value):
        self._board_index = value.value
    def set_bus_index(self, value):
        self._bus_index = value.value
    def set_position_on_bus(self, value):
        self._position_on_bus = value
    def set_position_on_board(self, value):
        self._position_on_board = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._error)
        buf += struct.pack("<B", self._board_index)
        buf += struct.pack("<B", self._bus_index)
        buf += struct.pack("<B", self._position_on_bus)
        buf += struct.pack("<B", self._position_on_board)
        return buf
    def get_error(self):
        return DS28E18QError(self._error)
    def get_board_index(self):
        return TemperatureBoardIndex(self._board_index)
    def get_bus_index(self):
        return OneWireBus(self._bus_index)
    def get_position_on_bus(self):
        return self._position_on_bus
    def get_position_on_board(self):
        return self._position_on_board
    def get_all_data(self):
        data = []
        data.append((fields.error, self.get_error()))
        data.append((fields.board_index, self.get_board_index()))
        data.append((fields.bus_index, self.get_bus_index()))
        data.append((fields.position_on_bus, self.get_position_on_bus()))
        data.append((fields.position_on_board, self.get_position_on_board()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._board_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._bus_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._position_on_bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._position_on_board = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage2_from_Edda_Controller_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage2
        self._category = categories.none
        self._id = 706
        self._size = 2
        self._byte0 = 0
        self._byte1 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage2_from_Edda_Telemetry_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage2
        self._category = categories.none
        self._id = 707
        self._size = 2
        self._byte0 = 0
        self._byte1 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage2_from_Edda_Pressure_Top_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage2
        self._category = categories.none
        self._id = 708
        self._size = 2
        self._byte0 = 0
        self._byte1 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage2_from_Edda_Pressure_Bottom_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage2
        self._category = categories.none
        self._id = 709
        self._size = 2
        self._byte0 = 0
        self._byte1 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class OneWireSearchEnded_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.OneWireSearchEnded
        self._category = categories.none
        self._id = 718
        self._size = 6
        self._bus = 0
        self._searched_family_code = 0
        self._devices_successfully_found = 0
        self._devices_insuccessfully_found = 0
        self._search_time_ms = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_searched_family_code(self, value):
        self._searched_family_code = value
    def set_devices_successfully_found(self, value):
        self._devices_successfully_found = value
    def set_devices_insuccessfully_found(self, value):
        self._devices_insuccessfully_found = value
    def set_search_time_ms(self, value):
        self._search_time_ms = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._searched_family_code)
        buf += struct.pack("<B", self._devices_successfully_found)
        buf += struct.pack("<B", self._devices_insuccessfully_found)
        buf += struct.pack("<H", self._search_time_ms)
        return buf
    def get_bus(self):
        return OneWireBus(self._bus)
    def get_searched_family_code(self):
        return self._searched_family_code
    def get_devices_successfully_found(self):
        return self._devices_successfully_found
    def get_devices_insuccessfully_found(self):
        return self._devices_insuccessfully_found
    def get_search_time_ms(self):
        return self._search_time_ms
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.searched_family_code, self.get_searched_family_code()))
        data.append((fields.devices_successfully_found, self.get_devices_successfully_found()))
        data.append((fields.devices_insuccessfully_found, self.get_devices_insuccessfully_found()))
        data.append((fields.search_time_ms, self.get_search_time_ms()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._searched_family_code = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._devices_successfully_found = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._devices_insuccessfully_found = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._search_time_ms = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class I2CSearchStarted_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CSearchStarted
        self._category = categories.none
        self._id = 723
        self._size = 1
        self._bus = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class I2CSearchStarted_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CSearchStarted
        self._category = categories.none
        self._id = 724
        self._size = 1
        self._bus = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class I2CSearchStarted_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CSearchStarted
        self._category = categories.none
        self._id = 725
        self._size = 1
        self._bus = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class I2CSearchStarted_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CSearchStarted
        self._category = categories.none
        self._id = 726
        self._size = 1
        self._bus = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class MAX31850KError_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.MAX31850KError
        self._category = categories.none
        self._id = 954
        self._size = 3
        self._error = 0
        self._board_index = 0
        self._sensor_index = 0
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
    def set_error(self, value):
        self._error = value.value
    def set_board_index(self, value):
        self._board_index = value.value
    def set_sensor_index(self, value):
        self._sensor_index = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._error)
        buf += struct.pack("<B", self._board_index)
        buf += struct.pack("<B", self._sensor_index)
        return buf
    def get_error(self):
        return MAX31850KError(self._error)
    def get_board_index(self):
        return TemperatureBoardIndex(self._board_index)
    def get_sensor_index(self):
        return ThermocoupleIndex(self._sensor_index)
    def get_all_data(self):
        data = []
        data.append((fields.error, self.get_error()))
        data.append((fields.board_index, self.get_board_index()))
        data.append((fields.sensor_index, self.get_sensor_index()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._board_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage3_from_Edda_Controller_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage3
        self._category = categories.none
        self._id = 962
        self._size = 3
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage3_from_Edda_Telemetry_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage3
        self._category = categories.none
        self._id = 963
        self._size = 3
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage3_from_Edda_Pressure_Top_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage3
        self._category = categories.none
        self._id = 964
        self._size = 3
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage3_from_Edda_Pressure_Bottom_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage3
        self._category = categories.none
        self._id = 965
        self._size = 3
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class OneWireDeviceStartupSuccess_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.OneWireDeviceStartupSuccess
        self._category = categories.none
        self._id = 974
        self._size = 7
        self._bus = 0
        self._serial_byte0 = 0
        self._serial_byte1 = 0
        self._serial_byte2 = 0
        self._serial_byte3 = 0
        self._serial_byte4 = 0
        self._serial_byte5 = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_serial_byte0(self, value):
        self._serial_byte0 = value
    def set_serial_byte1(self, value):
        self._serial_byte1 = value
    def set_serial_byte2(self, value):
        self._serial_byte2 = value
    def set_serial_byte3(self, value):
        self._serial_byte3 = value
    def set_serial_byte4(self, value):
        self._serial_byte4 = value
    def set_serial_byte5(self, value):
        self._serial_byte5 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._serial_byte0)
        buf += struct.pack("<B", self._serial_byte1)
        buf += struct.pack("<B", self._serial_byte2)
        buf += struct.pack("<B", self._serial_byte3)
        buf += struct.pack("<B", self._serial_byte4)
        buf += struct.pack("<B", self._serial_byte5)
        return buf
    def get_bus(self):
        return OneWireBus(self._bus)
    def get_serial_byte0(self):
        return self._serial_byte0
    def get_serial_byte1(self):
        return self._serial_byte1
    def get_serial_byte2(self):
        return self._serial_byte2
    def get_serial_byte3(self):
        return self._serial_byte3
    def get_serial_byte4(self):
        return self._serial_byte4
    def get_serial_byte5(self):
        return self._serial_byte5
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.serial_byte0, self.get_serial_byte0()))
        data.append((fields.serial_byte1, self.get_serial_byte1()))
        data.append((fields.serial_byte2, self.get_serial_byte2()))
        data.append((fields.serial_byte3, self.get_serial_byte3()))
        data.append((fields.serial_byte4, self.get_serial_byte4()))
        data.append((fields.serial_byte5, self.get_serial_byte5()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte5 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class I2CSearchError_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CSearchError
        self._category = categories.none
        self._id = 979
        self._size = 3
        self._bus = 0
        self._error = 0
        self._scanned_address = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_error(self, value):
        self._error = value.value
    def set_scanned_address(self, value):
        self._scanned_address = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._error)
        buf += struct.pack("<B", self._scanned_address)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_error(self):
        return I2CError(self._error)
    def get_scanned_address(self):
        return self._scanned_address
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.error, self.get_error()))
        data.append((fields.scanned_address, self.get_scanned_address()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._scanned_address = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class I2CSearchError_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CSearchError
        self._category = categories.none
        self._id = 980
        self._size = 3
        self._bus = 0
        self._error = 0
        self._scanned_address = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_error(self, value):
        self._error = value.value
    def set_scanned_address(self, value):
        self._scanned_address = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._error)
        buf += struct.pack("<B", self._scanned_address)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_error(self):
        return I2CError(self._error)
    def get_scanned_address(self):
        return self._scanned_address
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.error, self.get_error()))
        data.append((fields.scanned_address, self.get_scanned_address()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._scanned_address = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class I2CSearchError_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CSearchError
        self._category = categories.none
        self._id = 981
        self._size = 3
        self._bus = 0
        self._error = 0
        self._scanned_address = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_error(self, value):
        self._error = value.value
    def set_scanned_address(self, value):
        self._scanned_address = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._error)
        buf += struct.pack("<B", self._scanned_address)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_error(self):
        return I2CError(self._error)
    def get_scanned_address(self):
        return self._scanned_address
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.error, self.get_error()))
        data.append((fields.scanned_address, self.get_scanned_address()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._scanned_address = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class I2CSearchError_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CSearchError
        self._category = categories.none
        self._id = 982
        self._size = 3
        self._bus = 0
        self._error = 0
        self._scanned_address = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_error(self, value):
        self._error = value.value
    def set_scanned_address(self, value):
        self._scanned_address = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._error)
        buf += struct.pack("<B", self._scanned_address)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_error(self):
        return I2CError(self._error)
    def get_scanned_address(self):
        return self._scanned_address
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.error, self.get_error()))
        data.append((fields.scanned_address, self.get_scanned_address()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._scanned_address = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class MAX31856Error_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.MAX31856Error
        self._category = categories.none
        self._id = 1210
        self._size = 3
        self._board_index = 0
        self._sensor_index = 0
        self._raw_fault_register = 0
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
    def set_board_index(self, value):
        self._board_index = value.value
    def set_sensor_index(self, value):
        self._sensor_index = value.value
    def set_raw_fault_register(self, value):
        self._raw_fault_register = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._board_index)
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<B", self._raw_fault_register)
        return buf
    def get_board_index(self):
        return TemperatureBoardIndex(self._board_index)
    def get_sensor_index(self):
        return ThermocoupleIndex(self._sensor_index)
    def get_raw_fault_register(self):
        return self._raw_fault_register
    def get_all_data(self):
        data = []
        data.append((fields.board_index, self.get_board_index()))
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.raw_fault_register, self.get_raw_fault_register()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._board_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._raw_fault_register = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage4_from_Edda_Controller_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage4
        self._category = categories.none
        self._id = 1218
        self._size = 4
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage4_from_Edda_Telemetry_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage4
        self._category = categories.none
        self._id = 1219
        self._size = 4
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage4_from_Edda_Pressure_Top_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage4
        self._category = categories.none
        self._id = 1220
        self._size = 4
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage4_from_Edda_Pressure_Bottom_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage4
        self._category = categories.none
        self._id = 1221
        self._size = 4
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class OneWireDeviceStartupFailure_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.OneWireDeviceStartupFailure
        self._category = categories.none
        self._id = 1230
        self._size = 7
        self._bus = 0
        self._serial_byte0 = 0
        self._serial_byte1 = 0
        self._serial_byte2 = 0
        self._serial_byte3 = 0
        self._serial_byte4 = 0
        self._serial_byte5 = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_serial_byte0(self, value):
        self._serial_byte0 = value
    def set_serial_byte1(self, value):
        self._serial_byte1 = value
    def set_serial_byte2(self, value):
        self._serial_byte2 = value
    def set_serial_byte3(self, value):
        self._serial_byte3 = value
    def set_serial_byte4(self, value):
        self._serial_byte4 = value
    def set_serial_byte5(self, value):
        self._serial_byte5 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._serial_byte0)
        buf += struct.pack("<B", self._serial_byte1)
        buf += struct.pack("<B", self._serial_byte2)
        buf += struct.pack("<B", self._serial_byte3)
        buf += struct.pack("<B", self._serial_byte4)
        buf += struct.pack("<B", self._serial_byte5)
        return buf
    def get_bus(self):
        return OneWireBus(self._bus)
    def get_serial_byte0(self):
        return self._serial_byte0
    def get_serial_byte1(self):
        return self._serial_byte1
    def get_serial_byte2(self):
        return self._serial_byte2
    def get_serial_byte3(self):
        return self._serial_byte3
    def get_serial_byte4(self):
        return self._serial_byte4
    def get_serial_byte5(self):
        return self._serial_byte5
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.serial_byte0, self.get_serial_byte0()))
        data.append((fields.serial_byte1, self.get_serial_byte1()))
        data.append((fields.serial_byte2, self.get_serial_byte2()))
        data.append((fields.serial_byte3, self.get_serial_byte3()))
        data.append((fields.serial_byte4, self.get_serial_byte4()))
        data.append((fields.serial_byte5, self.get_serial_byte5()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte5 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class I2CSearchFoundDevice_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CSearchFoundDevice
        self._category = categories.none
        self._id = 1235
        self._size = 2
        self._bus = 0
        self._found_device_address = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_found_device_address(self, value):
        self._found_device_address = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._found_device_address)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_found_device_address(self):
        return self._found_device_address
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.found_device_address, self.get_found_device_address()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._found_device_address = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class I2CSearchFoundDevice_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CSearchFoundDevice
        self._category = categories.none
        self._id = 1236
        self._size = 2
        self._bus = 0
        self._found_device_address = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_found_device_address(self, value):
        self._found_device_address = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._found_device_address)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_found_device_address(self):
        return self._found_device_address
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.found_device_address, self.get_found_device_address()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._found_device_address = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class I2CSearchFoundDevice_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CSearchFoundDevice
        self._category = categories.none
        self._id = 1237
        self._size = 2
        self._bus = 0
        self._found_device_address = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_found_device_address(self, value):
        self._found_device_address = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._found_device_address)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_found_device_address(self):
        return self._found_device_address
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.found_device_address, self.get_found_device_address()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._found_device_address = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class I2CSearchFoundDevice_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CSearchFoundDevice
        self._category = categories.none
        self._id = 1238
        self._size = 2
        self._bus = 0
        self._found_device_address = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_found_device_address(self, value):
        self._found_device_address = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._found_device_address)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_found_device_address(self):
        return self._found_device_address
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.found_device_address, self.get_found_device_address()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._found_device_address = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class MAX31865Error_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.MAX31865Error
        self._category = categories.none
        self._id = 1466
        self._size = 3
        self._board_index = 0
        self._sensor_index = 0
        self._raw_fault_register = 0
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
    def set_board_index(self, value):
        self._board_index = value.value
    def set_sensor_index(self, value):
        self._sensor_index = value.value
    def set_raw_fault_register(self, value):
        self._raw_fault_register = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._board_index)
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<B", self._raw_fault_register)
        return buf
    def get_board_index(self):
        return TemperatureBoardIndex(self._board_index)
    def get_sensor_index(self):
        return PlatinumSensorIndex(self._sensor_index)
    def get_raw_fault_register(self):
        return self._raw_fault_register
    def get_all_data(self):
        data = []
        data.append((fields.board_index, self.get_board_index()))
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.raw_fault_register, self.get_raw_fault_register()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._board_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._raw_fault_register = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage5_from_Edda_Controller_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage5
        self._category = categories.none
        self._id = 1474
        self._size = 5
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
        self._byte4 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def set_byte4(self, value):
        self._byte4 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_byte4(self):
        return self._byte4
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        data.append((fields.byte4, self.get_byte4()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage5_from_Edda_Telemetry_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage5
        self._category = categories.none
        self._id = 1475
        self._size = 5
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
        self._byte4 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def set_byte4(self, value):
        self._byte4 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_byte4(self):
        return self._byte4
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        data.append((fields.byte4, self.get_byte4()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage5_from_Edda_Pressure_Top_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage5
        self._category = categories.none
        self._id = 1476
        self._size = 5
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
        self._byte4 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def set_byte4(self, value):
        self._byte4 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_byte4(self):
        return self._byte4
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        data.append((fields.byte4, self.get_byte4()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage5_from_Edda_Pressure_Bottom_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage5
        self._category = categories.none
        self._id = 1477
        self._size = 5
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
        self._byte4 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def set_byte4(self, value):
        self._byte4 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_byte4(self):
        return self._byte4
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        data.append((fields.byte4, self.get_byte4()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class I2CSearchEnded_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CSearchEnded
        self._category = categories.none
        self._id = 1491
        self._size = 7
        self._bus = 0
        self._devices_successfully_found = 0
        self._addresses_with_error = 0
        self._search_time_us = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_devices_successfully_found(self, value):
        self._devices_successfully_found = value
    def set_addresses_with_error(self, value):
        self._addresses_with_error = value
    def set_search_time_us(self, value):
        self._search_time_us = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._devices_successfully_found)
        buf += struct.pack("<B", self._addresses_with_error)
        buf += struct.pack("<L", self._search_time_us)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_devices_successfully_found(self):
        return self._devices_successfully_found
    def get_addresses_with_error(self):
        return self._addresses_with_error
    def get_search_time_us(self):
        return self._search_time_us
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.devices_successfully_found, self.get_devices_successfully_found()))
        data.append((fields.addresses_with_error, self.get_addresses_with_error()))
        data.append((fields.search_time_us, self.get_search_time_us()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._devices_successfully_found = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._addresses_with_error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._search_time_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class I2CSearchEnded_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CSearchEnded
        self._category = categories.none
        self._id = 1492
        self._size = 7
        self._bus = 0
        self._devices_successfully_found = 0
        self._addresses_with_error = 0
        self._search_time_us = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_devices_successfully_found(self, value):
        self._devices_successfully_found = value
    def set_addresses_with_error(self, value):
        self._addresses_with_error = value
    def set_search_time_us(self, value):
        self._search_time_us = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._devices_successfully_found)
        buf += struct.pack("<B", self._addresses_with_error)
        buf += struct.pack("<L", self._search_time_us)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_devices_successfully_found(self):
        return self._devices_successfully_found
    def get_addresses_with_error(self):
        return self._addresses_with_error
    def get_search_time_us(self):
        return self._search_time_us
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.devices_successfully_found, self.get_devices_successfully_found()))
        data.append((fields.addresses_with_error, self.get_addresses_with_error()))
        data.append((fields.search_time_us, self.get_search_time_us()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._devices_successfully_found = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._addresses_with_error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._search_time_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class I2CSearchEnded_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CSearchEnded
        self._category = categories.none
        self._id = 1493
        self._size = 7
        self._bus = 0
        self._devices_successfully_found = 0
        self._addresses_with_error = 0
        self._search_time_us = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_devices_successfully_found(self, value):
        self._devices_successfully_found = value
    def set_addresses_with_error(self, value):
        self._addresses_with_error = value
    def set_search_time_us(self, value):
        self._search_time_us = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._devices_successfully_found)
        buf += struct.pack("<B", self._addresses_with_error)
        buf += struct.pack("<L", self._search_time_us)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_devices_successfully_found(self):
        return self._devices_successfully_found
    def get_addresses_with_error(self):
        return self._addresses_with_error
    def get_search_time_us(self):
        return self._search_time_us
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.devices_successfully_found, self.get_devices_successfully_found()))
        data.append((fields.addresses_with_error, self.get_addresses_with_error()))
        data.append((fields.search_time_us, self.get_search_time_us()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._devices_successfully_found = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._addresses_with_error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._search_time_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class I2CSearchEnded_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CSearchEnded
        self._category = categories.none
        self._id = 1494
        self._size = 7
        self._bus = 0
        self._devices_successfully_found = 0
        self._addresses_with_error = 0
        self._search_time_us = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_devices_successfully_found(self, value):
        self._devices_successfully_found = value
    def set_addresses_with_error(self, value):
        self._addresses_with_error = value
    def set_search_time_us(self, value):
        self._search_time_us = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._devices_successfully_found)
        buf += struct.pack("<B", self._addresses_with_error)
        buf += struct.pack("<L", self._search_time_us)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_devices_successfully_found(self):
        return self._devices_successfully_found
    def get_addresses_with_error(self):
        return self._addresses_with_error
    def get_search_time_us(self):
        return self._search_time_us
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.devices_successfully_found, self.get_devices_successfully_found()))
        data.append((fields.addresses_with_error, self.get_addresses_with_error()))
        data.append((fields.search_time_us, self.get_search_time_us()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._devices_successfully_found = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._addresses_with_error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._search_time_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class PartialDebugMessage6_from_Edda_Controller_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage6
        self._category = categories.none
        self._id = 1730
        self._size = 6
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
        self._byte4 = 0
        self._byte5 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def set_byte4(self, value):
        self._byte4 = value
    def set_byte5(self, value):
        self._byte5 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        buf += struct.pack("<B", self._byte5)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_byte4(self):
        return self._byte4
    def get_byte5(self):
        return self._byte5
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        data.append((fields.byte4, self.get_byte4()))
        data.append((fields.byte5, self.get_byte5()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte5 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage6_from_Edda_Telemetry_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage6
        self._category = categories.none
        self._id = 1731
        self._size = 6
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
        self._byte4 = 0
        self._byte5 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def set_byte4(self, value):
        self._byte4 = value
    def set_byte5(self, value):
        self._byte5 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        buf += struct.pack("<B", self._byte5)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_byte4(self):
        return self._byte4
    def get_byte5(self):
        return self._byte5
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        data.append((fields.byte4, self.get_byte4()))
        data.append((fields.byte5, self.get_byte5()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte5 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage6_from_Edda_Pressure_Top_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage6
        self._category = categories.none
        self._id = 1732
        self._size = 6
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
        self._byte4 = 0
        self._byte5 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def set_byte4(self, value):
        self._byte4 = value
    def set_byte5(self, value):
        self._byte5 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        buf += struct.pack("<B", self._byte5)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_byte4(self):
        return self._byte4
    def get_byte5(self):
        return self._byte5
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        data.append((fields.byte4, self.get_byte4()))
        data.append((fields.byte5, self.get_byte5()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte5 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage6_from_Edda_Pressure_Bottom_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage6
        self._category = categories.none
        self._id = 1733
        self._size = 6
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
        self._byte4 = 0
        self._byte5 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def set_byte4(self, value):
        self._byte4 = value
    def set_byte5(self, value):
        self._byte5 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        buf += struct.pack("<B", self._byte5)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_byte4(self):
        return self._byte4
    def get_byte5(self):
        return self._byte5
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        data.append((fields.byte4, self.get_byte4()))
        data.append((fields.byte5, self.get_byte5()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte5 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage7_from_Edda_Controller_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage7
        self._category = categories.none
        self._id = 1986
        self._size = 7
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
        self._byte4 = 0
        self._byte5 = 0
        self._byte6 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def set_byte4(self, value):
        self._byte4 = value
    def set_byte5(self, value):
        self._byte5 = value
    def set_byte6(self, value):
        self._byte6 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        buf += struct.pack("<B", self._byte5)
        buf += struct.pack("<B", self._byte6)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_byte4(self):
        return self._byte4
    def get_byte5(self):
        return self._byte5
    def get_byte6(self):
        return self._byte6
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        data.append((fields.byte4, self.get_byte4()))
        data.append((fields.byte5, self.get_byte5()))
        data.append((fields.byte6, self.get_byte6()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte5 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte6 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage7_from_Edda_Telemetry_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage7
        self._category = categories.none
        self._id = 1987
        self._size = 7
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
        self._byte4 = 0
        self._byte5 = 0
        self._byte6 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def set_byte4(self, value):
        self._byte4 = value
    def set_byte5(self, value):
        self._byte5 = value
    def set_byte6(self, value):
        self._byte6 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        buf += struct.pack("<B", self._byte5)
        buf += struct.pack("<B", self._byte6)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_byte4(self):
        return self._byte4
    def get_byte5(self):
        return self._byte5
    def get_byte6(self):
        return self._byte6
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        data.append((fields.byte4, self.get_byte4()))
        data.append((fields.byte5, self.get_byte5()))
        data.append((fields.byte6, self.get_byte6()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte5 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte6 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage7_from_Edda_Pressure_Top_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage7
        self._category = categories.none
        self._id = 1988
        self._size = 7
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
        self._byte4 = 0
        self._byte5 = 0
        self._byte6 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def set_byte4(self, value):
        self._byte4 = value
    def set_byte5(self, value):
        self._byte5 = value
    def set_byte6(self, value):
        self._byte6 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        buf += struct.pack("<B", self._byte5)
        buf += struct.pack("<B", self._byte6)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_byte4(self):
        return self._byte4
    def get_byte5(self):
        return self._byte5
    def get_byte6(self):
        return self._byte6
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        data.append((fields.byte4, self.get_byte4()))
        data.append((fields.byte5, self.get_byte5()))
        data.append((fields.byte6, self.get_byte6()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte5 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte6 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage7_from_Edda_Pressure_Bottom_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage7
        self._category = categories.none
        self._id = 1989
        self._size = 7
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
        self._byte4 = 0
        self._byte5 = 0
        self._byte6 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def set_byte4(self, value):
        self._byte4 = value
    def set_byte5(self, value):
        self._byte5 = value
    def set_byte6(self, value):
        self._byte6 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        buf += struct.pack("<B", self._byte5)
        buf += struct.pack("<B", self._byte6)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_byte4(self):
        return self._byte4
    def get_byte5(self):
        return self._byte5
    def get_byte6(self):
        return self._byte6
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        data.append((fields.byte4, self.get_byte4()))
        data.append((fields.byte5, self.get_byte5()))
        data.append((fields.byte6, self.get_byte6()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte5 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte6 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
def id_to_message_class(id):
    if id == 0:
        receiver = CurrentTimePing_from_Ground_Controller_to_Edda_Controller()
        return receiver
    if id == 1:
        receiver = CurrentTimePong_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 2:
        receiver = SayHi_from_Ground_Controller_to_Edda_Controller()
        return receiver
    if id == 2:
        receiver = SayHi_from_Ground_Controller_to_Edda_Telemetry()
        return receiver
    if id == 2:
        receiver = SayHi_from_Ground_Controller_to_Edda_Pressure_Top()
        return receiver
    if id == 2:
        receiver = SayHi_from_Ground_Controller_to_Edda_Pressure_Bottom()
        return receiver
    if id == 3:
        receiver = Hello_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 4:
        receiver = Hello_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 5:
        receiver = Hello_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 6:
        receiver = Hello_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 7:
        receiver = CanStatistics_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 8:
        receiver = CanStatistics_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 9:
        receiver = CanStatistics_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 10:
        receiver = CanStatistics_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 11:
        receiver = CanStatistics_from_Ground_Controller_to_Ground_Controller()
        return receiver
    if id == 12:
        receiver = CanLatency_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 13:
        receiver = CanLatency_from_Ground_Controller_to_Ground_Controller()
        return receiver
    if id == 48:
        receiver = SetDebugStatusLedsModeRequest_from_Ground_Controller_to_Edda_Controller()
        return receiver
    if id == 48:
        receiver = SetDebugStatusLedsModeRequest_from_Ground_Controller_to_Edda_Telemetry()
        return receiver
    if id == 48:
        receiver = SetDebugStatusLedsModeRequest_from_Ground_Controller_to_Edda_Pressure_Top()
        return receiver
    if id == 48:
        receiver = SetDebugStatusLedsModeRequest_from_Ground_Controller_to_Edda_Pressure_Bottom()
        return receiver
    if id == 49:
        receiver = SetDebugMessagesModeRequest_from_Ground_Controller_to_Edda_Controller()
        return receiver
    if id == 49:
        receiver = SetDebugMessagesModeRequest_from_Ground_Controller_to_Edda_Telemetry()
        return receiver
    if id == 49:
        receiver = SetDebugMessagesModeRequest_from_Ground_Controller_to_Edda_Pressure_Top()
        return receiver
    if id == 49:
        receiver = SetDebugMessagesModeRequest_from_Ground_Controller_to_Edda_Pressure_Bottom()
        return receiver
    if id == 50:
        receiver = PowerCAN_SetDebugMode_from_Ground_Controller_to_Edda_Controller()
        return receiver
    if id == 50:
        receiver = PowerCAN_SetDebugMode_from_Ground_Controller_to_Edda_Power_Control_Boards()
        return receiver
    if id == 51:
        receiver = PowerCAN_GetState_from_Ground_Controller_to_Edda_Controller()
        return receiver
    if id == 51:
        receiver = PowerCAN_GetState_from_Ground_Controller_to_Edda_Power_Control_Boards()
        return receiver
    if id == 52:
        receiver = PowerCAN_TransitionRequest_from_Ground_Controller_to_Edda_Controller()
        return receiver
    if id == 52:
        receiver = PowerCAN_TransitionRequest_from_Ground_Controller_to_Edda_Power_Control_Boards()
        return receiver
    if id == 64:
        receiver = PowerCAN_SetDebugMode_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 64:
        receiver = PowerCAN_SetDebugMode_from_Edda_Controller_to_Edda_Power_Control_Boards()
        return receiver
    if id == 65:
        receiver = PowerCAN_GetState_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 65:
        receiver = PowerCAN_GetState_from_Edda_Controller_to_Edda_Power_Control_Boards()
        return receiver
    if id == 66:
        receiver = PowerCAN_TransitionRequest_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 66:
        receiver = PowerCAN_TransitionRequest_from_Edda_Controller_to_Edda_Power_Control_Boards()
        return receiver
    if id == 67:
        receiver = PowerCAN_Hello_from_Edda_Power_Control_Boards_to_Ground_Controller()
        return receiver
    if id == 68:
        receiver = PowerCAN_CurrentState_from_Edda_Power_Control_Boards_to_Ground_Controller()
        return receiver
    if id == 69:
        receiver = PowerCAN_TransitionResponse_from_Edda_Power_Control_Boards_to_Ground_Controller()
        return receiver
    if id == 70:
        receiver = PowerCAN_CheckResult_from_Edda_Power_Control_Boards_to_Ground_Controller()
        return receiver
    if id == 144:
        receiver = CurrentTimePing_from_Edda_Controller_to_Edda_Telemetry()
        return receiver
    if id == 144:
        receiver = CurrentTimePing_from_Edda_Controller_to_Edda_Pressure_Top()
        return receiver
    if id == 144:
        receiver = CurrentTimePing_from_Edda_Controller_to_Edda_Pressure_Bottom()
        return receiver
    if id == 145:
        receiver = CurrentTimePong_from_Edda_Telemetry_to_Edda_Controller()
        return receiver
    if id == 146:
        receiver = CurrentTimePong_from_Edda_Pressure_Top_to_Edda_Controller()
        return receiver
    if id == 147:
        receiver = CurrentTimePong_from_Edda_Pressure_Bottom_to_Edda_Controller()
        return receiver
    if id == 148:
        receiver = SayHi_from_Edda_Controller_to_Edda_Controller()
        return receiver
    if id == 148:
        receiver = SayHi_from_Edda_Controller_to_Edda_Telemetry()
        return receiver
    if id == 148:
        receiver = SayHi_from_Edda_Controller_to_Edda_Pressure_Top()
        return receiver
    if id == 148:
        receiver = SayHi_from_Edda_Controller_to_Edda_Pressure_Bottom()
        return receiver
    if id == 149:
        receiver = WenHop_from_Edda_Controller_to_Flight_Controller()
        return receiver
    if id == 150:
        receiver = WenHop_from_Edda_Telemetry_to_Flight_Controller()
        return receiver
    if id == 151:
        receiver = WenHop_from_Edda_Pressure_Top_to_Flight_Controller()
        return receiver
    if id == 152:
        receiver = WenHop_from_Edda_Pressure_Bottom_to_Flight_Controller()
        return receiver
    if id == 153:
        receiver = WenOrbit_from_Edda_Controller_to_Flight_Controller()
        return receiver
    if id == 154:
        receiver = WenOrbit_from_Edda_Telemetry_to_Flight_Controller()
        return receiver
    if id == 155:
        receiver = WenOrbit_from_Edda_Pressure_Top_to_Flight_Controller()
        return receiver
    if id == 156:
        receiver = WenOrbit_from_Edda_Pressure_Bottom_to_Flight_Controller()
        return receiver
    if id == 157:
        receiver = PowerInputMeasurement_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 158:
        receiver = PowerInputMeasurement_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 159:
        receiver = PowerInputMeasurement_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 160:
        receiver = PowerInputMeasurement_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 161:
        receiver = PowerInputMeasurementError_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 162:
        receiver = PowerInputMeasurementError_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 163:
        receiver = PowerInputMeasurementError_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 164:
        receiver = PowerInputMeasurementError_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 165:
        receiver = ColdSideTemperature_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 166:
        receiver = ColdSideTemperature_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 167:
        receiver = ColdSideTemperature_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 168:
        receiver = ColdSideTemperature_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 169:
        receiver = RawTransducerVoltage_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 170:
        receiver = RawTransducerVoltage_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 171:
        receiver = TransducerPressure_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 172:
        receiver = TransducerPressure_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 173:
        receiver = TransducerError_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 174:
        receiver = TransducerError_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 175:
        receiver = AmbientPressure_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 176:
        receiver = AmbientPressure_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 177:
        receiver = AmbientPressureCoefficient_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 178:
        receiver = AmbientPressureCoefficient_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 179:
        receiver = AmbientPressureError_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 180:
        receiver = AmbientPressureError_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 181:
        receiver = PlatinumSensorTemperature_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 182:
        receiver = PlatinumSensorResistance_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 183:
        receiver = PlatinumSensorRatio_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 184:
        receiver = ThermocoupleTypeKTemperature_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 185:
        receiver = ThermocoupleColdsideTemperature_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 187:
        receiver = Humidity_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 188:
        receiver = HumidityError_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 189:
        receiver = Acceleration_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 190:
        receiver = AccelerationError_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 191:
        receiver = AccelerationSelfTest_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 192:
        receiver = AmbientLight_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 193:
        receiver = AmbientLightError_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 198:
        receiver = TaskInfo_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 199:
        receiver = TaskInfo_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 200:
        receiver = TaskInfo_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 201:
        receiver = TaskInfo_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 202:
        receiver = LoopInfo_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 203:
        receiver = LoopInfo_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 204:
        receiver = LoopInfo_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 205:
        receiver = LoopInfo_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 207:
        receiver = OneWireDevicePairedWithSensor_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 208:
        receiver = OneWireSearchFamilyMismatch_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 209:
        receiver = OneWireSearchCRCMismatch_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 210:
        receiver = OneWireSearchFoundDevice_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 215:
        receiver = PowerCAN_Temperature_from_Edda_Power_Control_Boards_to_Ground_Controller()
        return receiver
    if id == 216:
        receiver = PowerCAN_Voltage_from_Edda_Power_Control_Boards_to_Ground_Controller()
        return receiver
    if id == 217:
        receiver = PowerCAN_ChannelMeasurementPower_from_Edda_Power_Control_Boards_to_Ground_Controller()
        return receiver
    if id == 218:
        receiver = PowerCAN_ChannelMeasurementVoltage_from_Edda_Power_Control_Boards_to_Ground_Controller()
        return receiver
    if id == 219:
        receiver = PowerCAN_ChannelMeasurementCurrent_from_Edda_Power_Control_Boards_to_Ground_Controller()
        return receiver
    if id == 220:
        receiver = PowerCAN_LoadMeasurementResistance_from_Edda_Power_Control_Boards_to_Ground_Controller()
        return receiver
    if id == 221:
        receiver = PowerCAN_LoadMeasurementVoltage_from_Edda_Power_Control_Boards_to_Ground_Controller()
        return receiver
    if id == 222:
        receiver = PowerCAN_LoadMeasurementPower_from_Edda_Power_Control_Boards_to_Ground_Controller()
        return receiver
    if id == 223:
        receiver = PowerCAN_LoadMeasurementCurrent_from_Edda_Power_Control_Boards_to_Ground_Controller()
        return receiver
    if id == 224:
        receiver = PowerCAN_FailedLoadMeasurementValue_from_Edda_Power_Control_Boards_to_Ground_Controller()
        return receiver
    if id == 225:
        receiver = PowerCAN_FailedLoadMeasurementThreshold_from_Edda_Power_Control_Boards_to_Ground_Controller()
        return receiver
    if id == 226:
        receiver = PowerCAN_ResistanceMeasurementResistance_from_Edda_Power_Control_Boards_to_Ground_Controller()
        return receiver
    if id == 227:
        receiver = PowerCAN_ResistanceMeasurementReferenceVoltage_from_Edda_Power_Control_Boards_to_Ground_Controller()
        return receiver
    if id == 228:
        receiver = PowerCAN_ResistanceMeasurementDifferentialVoltage_from_Edda_Power_Control_Boards_to_Ground_Controller()
        return receiver
    if id == 229:
        receiver = PowerCAN_ResistanceMeasurementPositiveVoltage_from_Edda_Power_Control_Boards_to_Ground_Controller()
        return receiver
    if id == 230:
        receiver = PowerCAN_ResistanceMeasurementNegativeVoltage_from_Edda_Power_Control_Boards_to_Ground_Controller()
        return receiver
    if id == 231:
        receiver = PowerCAN_I2CBusStarted_from_Edda_Power_Control_Boards_to_Ground_Controller()
        return receiver
    if id == 232:
        receiver = PowerCAN_I2CSearchStarted_from_Edda_Power_Control_Boards_to_Ground_Controller()
        return receiver
    if id == 233:
        receiver = PowerCAN_I2CSearchFoundDevice_from_Edda_Power_Control_Boards_to_Ground_Controller()
        return receiver
    if id == 234:
        receiver = PowerCAN_I2CSearchMissingDevice_from_Edda_Power_Control_Boards_to_Ground_Controller()
        return receiver
    if id == 235:
        receiver = PowerCAN_I2CSearchEnded_from_Edda_Power_Control_Boards_to_Ground_Controller()
        return receiver
    if id == 236:
        receiver = PowerCAN_LTC2992Error_from_Edda_Power_Control_Boards_to_Ground_Controller()
        return receiver
    if id == 237:
        receiver = PowerCAN_ADS122C04Error_from_Edda_Power_Control_Boards_to_Ground_Controller()
        return receiver
    if id == 238:
        receiver = PowerCAN_I2CSearchError_from_Edda_Power_Control_Boards_to_Ground_Controller()
        return receiver
    if id == 239:
        receiver = PowerCAN_ErrorStatistics_from_Edda_Power_Control_Boards_to_Ground_Controller()
        return receiver
    if id == 442:
        receiver = DS2482Error_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 450:
        receiver = PartialDebugMessage1_from_Edda_Controller_to_Flight_Controller()
        return receiver
    if id == 451:
        receiver = PartialDebugMessage1_from_Edda_Telemetry_to_Flight_Controller()
        return receiver
    if id == 452:
        receiver = PartialDebugMessage1_from_Edda_Pressure_Top_to_Flight_Controller()
        return receiver
    if id == 453:
        receiver = PartialDebugMessage1_from_Edda_Pressure_Bottom_to_Flight_Controller()
        return receiver
    if id == 462:
        receiver = OneWireSearchStarted_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 467:
        receiver = I2CBusStarted_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 468:
        receiver = I2CBusStarted_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 469:
        receiver = I2CBusStarted_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 470:
        receiver = I2CBusStarted_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 698:
        receiver = DS28E18QError_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 706:
        receiver = PartialDebugMessage2_from_Edda_Controller_to_Flight_Controller()
        return receiver
    if id == 707:
        receiver = PartialDebugMessage2_from_Edda_Telemetry_to_Flight_Controller()
        return receiver
    if id == 708:
        receiver = PartialDebugMessage2_from_Edda_Pressure_Top_to_Flight_Controller()
        return receiver
    if id == 709:
        receiver = PartialDebugMessage2_from_Edda_Pressure_Bottom_to_Flight_Controller()
        return receiver
    if id == 718:
        receiver = OneWireSearchEnded_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 723:
        receiver = I2CSearchStarted_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 724:
        receiver = I2CSearchStarted_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 725:
        receiver = I2CSearchStarted_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 726:
        receiver = I2CSearchStarted_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 954:
        receiver = MAX31850KError_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 962:
        receiver = PartialDebugMessage3_from_Edda_Controller_to_Flight_Controller()
        return receiver
    if id == 963:
        receiver = PartialDebugMessage3_from_Edda_Telemetry_to_Flight_Controller()
        return receiver
    if id == 964:
        receiver = PartialDebugMessage3_from_Edda_Pressure_Top_to_Flight_Controller()
        return receiver
    if id == 965:
        receiver = PartialDebugMessage3_from_Edda_Pressure_Bottom_to_Flight_Controller()
        return receiver
    if id == 974:
        receiver = OneWireDeviceStartupSuccess_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 979:
        receiver = I2CSearchError_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 980:
        receiver = I2CSearchError_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 981:
        receiver = I2CSearchError_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 982:
        receiver = I2CSearchError_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 1210:
        receiver = MAX31856Error_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 1218:
        receiver = PartialDebugMessage4_from_Edda_Controller_to_Flight_Controller()
        return receiver
    if id == 1219:
        receiver = PartialDebugMessage4_from_Edda_Telemetry_to_Flight_Controller()
        return receiver
    if id == 1220:
        receiver = PartialDebugMessage4_from_Edda_Pressure_Top_to_Flight_Controller()
        return receiver
    if id == 1221:
        receiver = PartialDebugMessage4_from_Edda_Pressure_Bottom_to_Flight_Controller()
        return receiver
    if id == 1230:
        receiver = OneWireDeviceStartupFailure_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 1235:
        receiver = I2CSearchFoundDevice_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 1236:
        receiver = I2CSearchFoundDevice_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 1237:
        receiver = I2CSearchFoundDevice_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 1238:
        receiver = I2CSearchFoundDevice_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 1466:
        receiver = MAX31865Error_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 1474:
        receiver = PartialDebugMessage5_from_Edda_Controller_to_Flight_Controller()
        return receiver
    if id == 1475:
        receiver = PartialDebugMessage5_from_Edda_Telemetry_to_Flight_Controller()
        return receiver
    if id == 1476:
        receiver = PartialDebugMessage5_from_Edda_Pressure_Top_to_Flight_Controller()
        return receiver
    if id == 1477:
        receiver = PartialDebugMessage5_from_Edda_Pressure_Bottom_to_Flight_Controller()
        return receiver
    if id == 1491:
        receiver = I2CSearchEnded_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 1492:
        receiver = I2CSearchEnded_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 1493:
        receiver = I2CSearchEnded_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 1494:
        receiver = I2CSearchEnded_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 1730:
        receiver = PartialDebugMessage6_from_Edda_Controller_to_Flight_Controller()
        return receiver
    if id == 1731:
        receiver = PartialDebugMessage6_from_Edda_Telemetry_to_Flight_Controller()
        return receiver
    if id == 1732:
        receiver = PartialDebugMessage6_from_Edda_Pressure_Top_to_Flight_Controller()
        return receiver
    if id == 1733:
        receiver = PartialDebugMessage6_from_Edda_Pressure_Bottom_to_Flight_Controller()
        return receiver
    if id == 1986:
        receiver = PartialDebugMessage7_from_Edda_Controller_to_Flight_Controller()
        return receiver
    if id == 1987:
        receiver = PartialDebugMessage7_from_Edda_Telemetry_to_Flight_Controller()
        return receiver
    if id == 1988:
        receiver = PartialDebugMessage7_from_Edda_Pressure_Top_to_Flight_Controller()
        return receiver
    if id == 1989:
        receiver = PartialDebugMessage7_from_Edda_Pressure_Bottom_to_Flight_Controller()
        return receiver
def is_specifier(sender, name, field):
    if (messages.CurrentTimePing == name and nodes.Ground_Controller == sender):
        if (fields.current_time_ms == field):
            return False
        if (fields.current_time_us == field):
            return False
    if (messages.CurrentTimePong == name and nodes.Edda_Controller == sender):
        if (fields.current_time_ms == field):
            return False
        if (fields.current_time_us == field):
            return False
    if (messages.Hello == name and nodes.Edda_Controller == sender):
        if (fields.debug_messages_mode == field):
            return False
        if (fields.debug_status_leds_mode == field):
            return False
        if (fields.uptime_ms == field):
            return False
    if (messages.Hello == name and nodes.Edda_Telemetry == sender):
        if (fields.debug_messages_mode == field):
            return False
        if (fields.debug_status_leds_mode == field):
            return False
        if (fields.uptime_ms == field):
            return False
    if (messages.Hello == name and nodes.Edda_Pressure_Top == sender):
        if (fields.debug_messages_mode == field):
            return False
        if (fields.debug_status_leds_mode == field):
            return False
        if (fields.uptime_ms == field):
            return False
    if (messages.Hello == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.debug_messages_mode == field):
            return False
        if (fields.debug_status_leds_mode == field):
            return False
        if (fields.uptime_ms == field):
            return False
    if (messages.CanStatistics == name and nodes.Edda_Controller == sender):
        if (fields.max_tx_queue_size == field):
            return False
        if (fields.max_rx_queue_size == field):
            return False
        if (fields.mean_tx_queue_size == field):
            return False
        if (fields.mean_rx_queue_size == field):
            return False
    if (messages.CanStatistics == name and nodes.Edda_Telemetry == sender):
        if (fields.max_tx_queue_size == field):
            return False
        if (fields.max_rx_queue_size == field):
            return False
        if (fields.mean_tx_queue_size == field):
            return False
        if (fields.mean_rx_queue_size == field):
            return False
    if (messages.CanStatistics == name and nodes.Edda_Pressure_Top == sender):
        if (fields.max_tx_queue_size == field):
            return False
        if (fields.max_rx_queue_size == field):
            return False
        if (fields.mean_tx_queue_size == field):
            return False
        if (fields.mean_rx_queue_size == field):
            return False
    if (messages.CanStatistics == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.max_tx_queue_size == field):
            return False
        if (fields.max_rx_queue_size == field):
            return False
        if (fields.mean_tx_queue_size == field):
            return False
        if (fields.mean_rx_queue_size == field):
            return False
    if (messages.CanStatistics == name and nodes.Ground_Controller == sender):
        if (fields.max_tx_queue_size == field):
            return False
        if (fields.max_rx_queue_size == field):
            return False
        if (fields.mean_tx_queue_size == field):
            return False
        if (fields.mean_rx_queue_size == field):
            return False
    if (messages.CanLatency == name and nodes.Edda_Controller == sender):
        if (fields.round_trip_time_us == field):
            return False
        if (fields.destination_node == field):
            return True
    if (messages.CanLatency == name and nodes.Ground_Controller == sender):
        if (fields.round_trip_time_us == field):
            return False
        if (fields.destination_node == field):
            return True
    if (messages.SetDebugStatusLedsModeRequest == name and nodes.Ground_Controller == sender):
        if (fields.receiver_node == field):
            return True
        if (fields.debug_status_leds_mode == field):
            return False
    if (messages.SetDebugStatusLedsModeRequest == name and nodes.Ground_Controller == sender):
        if (fields.receiver_node == field):
            return True
        if (fields.debug_status_leds_mode == field):
            return False
    if (messages.SetDebugStatusLedsModeRequest == name and nodes.Ground_Controller == sender):
        if (fields.receiver_node == field):
            return True
        if (fields.debug_status_leds_mode == field):
            return False
    if (messages.SetDebugStatusLedsModeRequest == name and nodes.Ground_Controller == sender):
        if (fields.receiver_node == field):
            return True
        if (fields.debug_status_leds_mode == field):
            return False
    if (messages.SetDebugMessagesModeRequest == name and nodes.Ground_Controller == sender):
        if (fields.receiver_node == field):
            return True
        if (fields.debug_messages_mode == field):
            return False
    if (messages.SetDebugMessagesModeRequest == name and nodes.Ground_Controller == sender):
        if (fields.receiver_node == field):
            return True
        if (fields.debug_messages_mode == field):
            return False
    if (messages.SetDebugMessagesModeRequest == name and nodes.Ground_Controller == sender):
        if (fields.receiver_node == field):
            return True
        if (fields.debug_messages_mode == field):
            return False
    if (messages.SetDebugMessagesModeRequest == name and nodes.Ground_Controller == sender):
        if (fields.receiver_node == field):
            return True
        if (fields.debug_messages_mode == field):
            return False
    if (messages.PowerCAN_SetDebugMode == name and nodes.Ground_Controller == sender):
        if (fields.debug_mode == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_SetDebugMode == name and nodes.Ground_Controller == sender):
        if (fields.debug_mode == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_GetState == name and nodes.Ground_Controller == sender):
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_GetState == name and nodes.Ground_Controller == sender):
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_TransitionRequest == name and nodes.Ground_Controller == sender):
        if (fields.edda_signature == field):
            return False
        if (fields.request == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_TransitionRequest == name and nodes.Ground_Controller == sender):
        if (fields.edda_signature == field):
            return False
        if (fields.request == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_SetDebugMode == name and nodes.Edda_Controller == sender):
        if (fields.debug_mode == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_SetDebugMode == name and nodes.Edda_Controller == sender):
        if (fields.debug_mode == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_GetState == name and nodes.Edda_Controller == sender):
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_GetState == name and nodes.Edda_Controller == sender):
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_TransitionRequest == name and nodes.Edda_Controller == sender):
        if (fields.edda_signature == field):
            return False
        if (fields.request == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_TransitionRequest == name and nodes.Edda_Controller == sender):
        if (fields.edda_signature == field):
            return False
        if (fields.request == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_Hello == name and nodes.Edda_Power_Control_Boards == sender):
        if (fields.debug_mode == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_CurrentState == name and nodes.Edda_Power_Control_Boards == sender):
        if (fields.system_state == field):
            return False
        if (fields.gate_state == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_TransitionResponse == name and nodes.Edda_Power_Control_Boards == sender):
        if (fields.request == field):
            return False
        if (fields.response == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_CheckResult == name and nodes.Edda_Power_Control_Boards == sender):
        if (fields.result == field):
            return False
        if (fields.checks_failed == field):
            return False
        if (fields.checks_performed == field):
            return False
        if (fields.total_checks == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.CurrentTimePing == name and nodes.Edda_Controller == sender):
        if (fields.current_time_ms == field):
            return False
        if (fields.current_time_us == field):
            return False
    if (messages.CurrentTimePing == name and nodes.Edda_Controller == sender):
        if (fields.current_time_ms == field):
            return False
        if (fields.current_time_us == field):
            return False
    if (messages.CurrentTimePing == name and nodes.Edda_Controller == sender):
        if (fields.current_time_ms == field):
            return False
        if (fields.current_time_us == field):
            return False
    if (messages.CurrentTimePong == name and nodes.Edda_Telemetry == sender):
        if (fields.current_time_ms == field):
            return False
        if (fields.current_time_us == field):
            return False
    if (messages.CurrentTimePong == name and nodes.Edda_Pressure_Top == sender):
        if (fields.current_time_ms == field):
            return False
        if (fields.current_time_us == field):
            return False
    if (messages.CurrentTimePong == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.current_time_ms == field):
            return False
        if (fields.current_time_us == field):
            return False
    if (messages.WenHop == name and nodes.Edda_Controller == sender):
        if (fields.w == field):
            return False
        if (fields.e == field):
            return False
        if (fields.n == field):
            return False
        if (fields.h == field):
            return False
        if (fields.o == field):
            return False
        if (fields.p == field):
            return False
    if (messages.WenHop == name and nodes.Edda_Telemetry == sender):
        if (fields.w == field):
            return False
        if (fields.e == field):
            return False
        if (fields.n == field):
            return False
        if (fields.h == field):
            return False
        if (fields.o == field):
            return False
        if (fields.p == field):
            return False
    if (messages.WenHop == name and nodes.Edda_Pressure_Top == sender):
        if (fields.w == field):
            return False
        if (fields.e == field):
            return False
        if (fields.n == field):
            return False
        if (fields.h == field):
            return False
        if (fields.o == field):
            return False
        if (fields.p == field):
            return False
    if (messages.WenHop == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.w == field):
            return False
        if (fields.e == field):
            return False
        if (fields.n == field):
            return False
        if (fields.h == field):
            return False
        if (fields.o == field):
            return False
        if (fields.p == field):
            return False
    if (messages.WenOrbit == name and nodes.Edda_Controller == sender):
        if (fields.w == field):
            return False
        if (fields.e == field):
            return False
        if (fields.n == field):
            return False
        if (fields.o == field):
            return False
        if (fields.r == field):
            return False
        if (fields.b == field):
            return False
        if (fields.i == field):
            return False
        if (fields.t == field):
            return False
    if (messages.WenOrbit == name and nodes.Edda_Telemetry == sender):
        if (fields.w == field):
            return False
        if (fields.e == field):
            return False
        if (fields.n == field):
            return False
        if (fields.o == field):
            return False
        if (fields.r == field):
            return False
        if (fields.b == field):
            return False
        if (fields.i == field):
            return False
        if (fields.t == field):
            return False
    if (messages.WenOrbit == name and nodes.Edda_Pressure_Top == sender):
        if (fields.w == field):
            return False
        if (fields.e == field):
            return False
        if (fields.n == field):
            return False
        if (fields.o == field):
            return False
        if (fields.r == field):
            return False
        if (fields.b == field):
            return False
        if (fields.i == field):
            return False
        if (fields.t == field):
            return False
    if (messages.WenOrbit == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.w == field):
            return False
        if (fields.e == field):
            return False
        if (fields.n == field):
            return False
        if (fields.o == field):
            return False
        if (fields.r == field):
            return False
        if (fields.b == field):
            return False
        if (fields.i == field):
            return False
        if (fields.t == field):
            return False
    if (messages.PowerInputMeasurement == name and nodes.Edda_Controller == sender):
        if (fields.current_ampere == field):
            return False
        if (fields.voltage_volt == field):
            return False
        if (fields.power_watt == field):
            return False
    if (messages.PowerInputMeasurement == name and nodes.Edda_Telemetry == sender):
        if (fields.current_ampere == field):
            return False
        if (fields.voltage_volt == field):
            return False
        if (fields.power_watt == field):
            return False
    if (messages.PowerInputMeasurement == name and nodes.Edda_Pressure_Top == sender):
        if (fields.current_ampere == field):
            return False
        if (fields.voltage_volt == field):
            return False
        if (fields.power_watt == field):
            return False
    if (messages.PowerInputMeasurement == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.current_ampere == field):
            return False
        if (fields.voltage_volt == field):
            return False
        if (fields.power_watt == field):
            return False
    if (messages.PowerInputMeasurementError == name and nodes.Edda_Controller == sender):
        if (fields.error == field):
            return False
    if (messages.PowerInputMeasurementError == name and nodes.Edda_Telemetry == sender):
        if (fields.error == field):
            return False
    if (messages.PowerInputMeasurementError == name and nodes.Edda_Pressure_Top == sender):
        if (fields.error == field):
            return False
    if (messages.PowerInputMeasurementError == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.error == field):
            return False
    if (messages.ColdSideTemperature == name and nodes.Edda_Controller == sender):
        if (fields.sensor_index == field):
            return True
        if (fields.temperature_celsius == field):
            return False
    if (messages.ColdSideTemperature == name and nodes.Edda_Telemetry == sender):
        if (fields.sensor_index == field):
            return True
        if (fields.temperature_celsius == field):
            return False
    if (messages.ColdSideTemperature == name and nodes.Edda_Pressure_Top == sender):
        if (fields.sensor_index == field):
            return True
        if (fields.temperature_celsius == field):
            return False
    if (messages.ColdSideTemperature == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.sensor_index == field):
            return True
        if (fields.temperature_celsius == field):
            return False
    if (messages.RawTransducerVoltage == name and nodes.Edda_Pressure_Top == sender):
        if (fields.measurement_index == field):
            return True
        if (fields.voltage_volt == field):
            return False
    if (messages.RawTransducerVoltage == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.measurement_index == field):
            return True
        if (fields.voltage_volt == field):
            return False
    if (messages.TransducerPressure == name and nodes.Edda_Pressure_Top == sender):
        if (fields.sensor_index == field):
            return True
        if (fields.pressure_pascal == field):
            return False
    if (messages.TransducerPressure == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.sensor_index == field):
            return True
        if (fields.pressure_pascal == field):
            return False
    if (messages.TransducerError == name and nodes.Edda_Pressure_Top == sender):
        if (fields.measurement_index == field):
            return True
        if (fields.error == field):
            return False
    if (messages.TransducerError == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.measurement_index == field):
            return True
        if (fields.error == field):
            return False
    if (messages.AmbientPressure == name and nodes.Edda_Pressure_Top == sender):
        if (fields.pressure_mbar == field):
            return False
    if (messages.AmbientPressure == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.pressure_mbar == field):
            return False
    if (messages.AmbientPressureCoefficient == name and nodes.Edda_Pressure_Top == sender):
        if (fields.coefficient_number == field):
            return False
        if (fields.coefficient_value == field):
            return False
    if (messages.AmbientPressureCoefficient == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.coefficient_number == field):
            return False
        if (fields.coefficient_value == field):
            return False
    if (messages.AmbientPressureError == name and nodes.Edda_Pressure_Top == sender):
        if (fields.error == field):
            return False
    if (messages.AmbientPressureError == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.error == field):
            return False
    if (messages.PlatinumSensorTemperature == name and nodes.Edda_Telemetry == sender):
        if (fields.board_index == field):
            return True
        if (fields.sensor_index == field):
            return True
        if (fields.temperature_celsius == field):
            return False
    if (messages.PlatinumSensorResistance == name and nodes.Edda_Telemetry == sender):
        if (fields.board_index == field):
            return True
        if (fields.sensor_index == field):
            return True
        if (fields.resistance_ohm == field):
            return False
    if (messages.PlatinumSensorRatio == name and nodes.Edda_Telemetry == sender):
        if (fields.board_index == field):
            return True
        if (fields.sensor_index == field):
            return True
        if (fields.ratio_fraction == field):
            return False
    if (messages.ThermocoupleTypeKTemperature == name and nodes.Edda_Telemetry == sender):
        if (fields.board_index == field):
            return True
        if (fields.sensor_index == field):
            return True
        if (fields.temperature_celsius == field):
            return False
    if (messages.ThermocoupleColdsideTemperature == name and nodes.Edda_Telemetry == sender):
        if (fields.board_index == field):
            return True
        if (fields.sensor_index == field):
            return True
        if (fields.temperature_celsius == field):
            return False
    if (messages.Humidity == name and nodes.Edda_Controller == sender):
        if (fields.relative_humidity_percentage == field):
            return False
        if (fields.is_heater_on == field):
            return False
    if (messages.HumidityError == name and nodes.Edda_Controller == sender):
        if (fields.error == field):
            return False
    if (messages.Acceleration == name and nodes.Edda_Controller == sender):
        if (fields.acceleration_x_gforce == field):
            return False
        if (fields.acceleration_y_gforce == field):
            return False
        if (fields.acceleration_z_gforce == field):
            return False
    if (messages.AccelerationError == name and nodes.Edda_Controller == sender):
        if (fields.error == field):
            return False
    if (messages.AccelerationSelfTest == name and nodes.Edda_Controller == sender):
        if (fields.sign == field):
            return True
        if (fields.result == field):
            return False
        if (fields.acceleration_x_gforce == field):
            return False
        if (fields.acceleration_y_gforce == field):
            return False
        if (fields.acceleration_z_gforce == field):
            return False
    if (messages.AmbientLight == name and nodes.Edda_Controller == sender):
        if (fields.ambient_light_lux == field):
            return False
    if (messages.AmbientLightError == name and nodes.Edda_Controller == sender):
        if (fields.error == field):
            return False
    if (messages.TaskInfo == name and nodes.Edda_Controller == sender):
        if (fields.type == field):
            return True
        if (fields.thread == field):
            return True
        if (fields.task_time_us == field):
            return False
        if (fields.truncated_start_time_us == field):
            return False
    if (messages.TaskInfo == name and nodes.Edda_Telemetry == sender):
        if (fields.type == field):
            return True
        if (fields.thread == field):
            return True
        if (fields.task_time_us == field):
            return False
        if (fields.truncated_start_time_us == field):
            return False
    if (messages.TaskInfo == name and nodes.Edda_Pressure_Top == sender):
        if (fields.type == field):
            return True
        if (fields.thread == field):
            return True
        if (fields.task_time_us == field):
            return False
        if (fields.truncated_start_time_us == field):
            return False
    if (messages.TaskInfo == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.type == field):
            return True
        if (fields.thread == field):
            return True
        if (fields.task_time_us == field):
            return False
        if (fields.truncated_start_time_us == field):
            return False
    if (messages.LoopInfo == name and nodes.Edda_Controller == sender):
        if (fields.type == field):
            return True
        if (fields.thread == field):
            return True
        if (fields.loop_time_us == field):
            return False
        if (fields.truncated_start_time_us == field):
            return False
    if (messages.LoopInfo == name and nodes.Edda_Telemetry == sender):
        if (fields.type == field):
            return True
        if (fields.thread == field):
            return True
        if (fields.loop_time_us == field):
            return False
        if (fields.truncated_start_time_us == field):
            return False
    if (messages.LoopInfo == name and nodes.Edda_Pressure_Top == sender):
        if (fields.type == field):
            return True
        if (fields.thread == field):
            return True
        if (fields.loop_time_us == field):
            return False
        if (fields.truncated_start_time_us == field):
            return False
    if (messages.LoopInfo == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.type == field):
            return True
        if (fields.thread == field):
            return True
        if (fields.loop_time_us == field):
            return False
        if (fields.truncated_start_time_us == field):
            return False
    if (messages.OneWireDevicePairedWithSensor == name and nodes.Edda_Telemetry == sender):
        if (fields.bus == field):
            return True
        if (fields.position_on_board == field):
            return False
        if (fields.serial_byte0 == field):
            return False
        if (fields.serial_byte1 == field):
            return False
        if (fields.serial_byte2 == field):
            return False
        if (fields.serial_byte3 == field):
            return False
        if (fields.serial_byte4 == field):
            return False
        if (fields.serial_byte5 == field):
            return False
    if (messages.OneWireSearchFamilyMismatch == name and nodes.Edda_Telemetry == sender):
        if (fields.bus == field):
            return True
        if (fields.serial_byte0 == field):
            return False
        if (fields.serial_byte1 == field):
            return False
        if (fields.serial_byte2 == field):
            return False
        if (fields.serial_byte3 == field):
            return False
        if (fields.serial_byte4 == field):
            return False
        if (fields.serial_byte5 == field):
            return False
        if (fields.found_family_code == field):
            return False
    if (messages.OneWireSearchCRCMismatch == name and nodes.Edda_Telemetry == sender):
        if (fields.bus == field):
            return True
        if (fields.serial_byte0 == field):
            return False
        if (fields.serial_byte1 == field):
            return False
        if (fields.serial_byte2 == field):
            return False
        if (fields.serial_byte3 == field):
            return False
        if (fields.serial_byte4 == field):
            return False
        if (fields.serial_byte5 == field):
            return False
        if (fields.found_crc == field):
            return False
    if (messages.OneWireSearchFoundDevice == name and nodes.Edda_Telemetry == sender):
        if (fields.bus == field):
            return True
        if (fields.serial_byte0 == field):
            return False
        if (fields.serial_byte1 == field):
            return False
        if (fields.serial_byte2 == field):
            return False
        if (fields.serial_byte3 == field):
            return False
        if (fields.serial_byte4 == field):
            return False
        if (fields.serial_byte5 == field):
            return False
    if (messages.PowerCAN_Temperature == name and nodes.Edda_Power_Control_Boards == sender):
        if (fields.kind == field):
            return True
        if (fields.temperature_celsius == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_Voltage == name and nodes.Edda_Power_Control_Boards == sender):
        if (fields.kind == field):
            return True
        if (fields.voltage_volt == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_ChannelMeasurementPower == name and nodes.Edda_Power_Control_Boards == sender):
        if (fields.channel == field):
            return True
        if (fields.power_watt == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_ChannelMeasurementVoltage == name and nodes.Edda_Power_Control_Boards == sender):
        if (fields.channel == field):
            return True
        if (fields.voltage_volt == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_ChannelMeasurementCurrent == name and nodes.Edda_Power_Control_Boards == sender):
        if (fields.channel == field):
            return True
        if (fields.current_ampere == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_LoadMeasurementResistance == name and nodes.Edda_Power_Control_Boards == sender):
        if (fields.measurement_reference == field):
            return False
        if (fields.result == field):
            return False
        if (fields.resistance_ohm == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_LoadMeasurementVoltage == name and nodes.Edda_Power_Control_Boards == sender):
        if (fields.measurement_reference == field):
            return False
        if (fields.result == field):
            return False
        if (fields.voltage_volt == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_LoadMeasurementPower == name and nodes.Edda_Power_Control_Boards == sender):
        if (fields.measurement_reference == field):
            return False
        if (fields.result == field):
            return False
        if (fields.power_watt == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_LoadMeasurementCurrent == name and nodes.Edda_Power_Control_Boards == sender):
        if (fields.measurement_reference == field):
            return False
        if (fields.result == field):
            return False
        if (fields.current_ampere == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_FailedLoadMeasurementValue == name and nodes.Edda_Power_Control_Boards == sender):
        if (fields.measurement_reference == field):
            return False
        if (fields.failure_reason == field):
            return False
        if (fields.value == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_FailedLoadMeasurementThreshold == name and nodes.Edda_Power_Control_Boards == sender):
        if (fields.measurement_reference == field):
            return False
        if (fields.failure_reason == field):
            return False
        if (fields.threshold == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_ResistanceMeasurementResistance == name and nodes.Edda_Power_Control_Boards == sender):
        if (fields.measurement_reference == field):
            return True
        if (fields.validity == field):
            return False
        if (fields.resistance_ohm == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_ResistanceMeasurementReferenceVoltage == name and nodes.Edda_Power_Control_Boards == sender):
        if (fields.measurement_reference == field):
            return True
        if (fields.validity == field):
            return False
        if (fields.reference_voltage_volt == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_ResistanceMeasurementDifferentialVoltage == name and nodes.Edda_Power_Control_Boards == sender):
        if (fields.measurement_reference == field):
            return True
        if (fields.validity == field):
            return False
        if (fields.differential_voltage_volt == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_ResistanceMeasurementPositiveVoltage == name and nodes.Edda_Power_Control_Boards == sender):
        if (fields.measurement_reference == field):
            return True
        if (fields.validity == field):
            return False
        if (fields.positive_voltage_volt == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_ResistanceMeasurementNegativeVoltage == name and nodes.Edda_Power_Control_Boards == sender):
        if (fields.measurement_reference == field):
            return True
        if (fields.validity == field):
            return False
        if (fields.negative_voltage_volt == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_I2CBusStarted == name and nodes.Edda_Power_Control_Boards == sender):
        if (fields.bus == field):
            return True
        if (fields.frequency_hertz == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_I2CSearchStarted == name and nodes.Edda_Power_Control_Boards == sender):
        if (fields.bus == field):
            return True
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_I2CSearchFoundDevice == name and nodes.Edda_Power_Control_Boards == sender):
        if (fields.bus == field):
            return True
        if (fields.found_device_address == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_I2CSearchMissingDevice == name and nodes.Edda_Power_Control_Boards == sender):
        if (fields.bus == field):
            return True
        if (fields.missing_device_address == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_I2CSearchEnded == name and nodes.Edda_Power_Control_Boards == sender):
        if (fields.bus == field):
            return True
        if (fields.devices_successfully_found == field):
            return False
        if (fields.addresses_with_error == field):
            return False
        if (fields.search_time_us == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_LTC2992Error == name and nodes.Edda_Power_Control_Boards == sender):
        if (fields.error == field):
            return False
        if (fields.location == field):
            return False
        if (fields.register_address == field):
            return False
        if (fields.read_data == field):
            return False
        if (fields.write_data == field):
            return False
        if (fields.expected_data == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_ADS122C04Error == name and nodes.Edda_Power_Control_Boards == sender):
        if (fields.error == field):
            return False
        if (fields.location == field):
            return False
        if (fields.register_address == field):
            return False
        if (fields.read_data == field):
            return False
        if (fields.write_data == field):
            return False
        if (fields.expected_data == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_I2CSearchError == name and nodes.Edda_Power_Control_Boards == sender):
        if (fields.bus == field):
            return True
        if (fields.error == field):
            return False
        if (fields.scanned_address == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_ErrorStatistics == name and nodes.Edda_Power_Control_Boards == sender):
        if (fields.warning_count == field):
            return False
        if (fields.error_count == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.DS2482Error == name and nodes.Edda_Telemetry == sender):
        if (fields.error == field):
            return False
        if (fields.board_index == field):
            return True
        if (fields.bus_index == field):
            return True
        if (fields.position_on_bus == field):
            return False
        if (fields.position_on_board == field):
            return False
    if (messages.PartialDebugMessage1 == name and nodes.Edda_Controller == sender):
        if (fields.byte0 == field):
            return False
    if (messages.PartialDebugMessage1 == name and nodes.Edda_Telemetry == sender):
        if (fields.byte0 == field):
            return False
    if (messages.PartialDebugMessage1 == name and nodes.Edda_Pressure_Top == sender):
        if (fields.byte0 == field):
            return False
    if (messages.PartialDebugMessage1 == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.byte0 == field):
            return False
    if (messages.OneWireSearchStarted == name and nodes.Edda_Telemetry == sender):
        if (fields.bus == field):
            return True
        if (fields.start_time_ms == field):
            return False
    if (messages.I2CBusStarted == name and nodes.Edda_Controller == sender):
        if (fields.bus == field):
            return True
        if (fields.frequency_hertz == field):
            return False
    if (messages.I2CBusStarted == name and nodes.Edda_Telemetry == sender):
        if (fields.bus == field):
            return True
        if (fields.frequency_hertz == field):
            return False
    if (messages.I2CBusStarted == name and nodes.Edda_Pressure_Top == sender):
        if (fields.bus == field):
            return True
        if (fields.frequency_hertz == field):
            return False
    if (messages.I2CBusStarted == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.bus == field):
            return True
        if (fields.frequency_hertz == field):
            return False
    if (messages.DS28E18QError == name and nodes.Edda_Telemetry == sender):
        if (fields.error == field):
            return False
        if (fields.board_index == field):
            return True
        if (fields.bus_index == field):
            return True
        if (fields.position_on_bus == field):
            return False
        if (fields.position_on_board == field):
            return False
    if (messages.PartialDebugMessage2 == name and nodes.Edda_Controller == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
    if (messages.PartialDebugMessage2 == name and nodes.Edda_Telemetry == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
    if (messages.PartialDebugMessage2 == name and nodes.Edda_Pressure_Top == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
    if (messages.PartialDebugMessage2 == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
    if (messages.OneWireSearchEnded == name and nodes.Edda_Telemetry == sender):
        if (fields.bus == field):
            return True
        if (fields.searched_family_code == field):
            return False
        if (fields.devices_successfully_found == field):
            return False
        if (fields.devices_insuccessfully_found == field):
            return False
        if (fields.search_time_ms == field):
            return False
    if (messages.I2CSearchStarted == name and nodes.Edda_Controller == sender):
        if (fields.bus == field):
            return True
    if (messages.I2CSearchStarted == name and nodes.Edda_Telemetry == sender):
        if (fields.bus == field):
            return True
    if (messages.I2CSearchStarted == name and nodes.Edda_Pressure_Top == sender):
        if (fields.bus == field):
            return True
    if (messages.I2CSearchStarted == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.bus == field):
            return True
    if (messages.MAX31850KError == name and nodes.Edda_Telemetry == sender):
        if (fields.error == field):
            return False
        if (fields.board_index == field):
            return True
        if (fields.sensor_index == field):
            return True
    if (messages.PartialDebugMessage3 == name and nodes.Edda_Controller == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
    if (messages.PartialDebugMessage3 == name and nodes.Edda_Telemetry == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
    if (messages.PartialDebugMessage3 == name and nodes.Edda_Pressure_Top == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
    if (messages.PartialDebugMessage3 == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
    if (messages.OneWireDeviceStartupSuccess == name and nodes.Edda_Telemetry == sender):
        if (fields.bus == field):
            return True
        if (fields.serial_byte0 == field):
            return False
        if (fields.serial_byte1 == field):
            return False
        if (fields.serial_byte2 == field):
            return False
        if (fields.serial_byte3 == field):
            return False
        if (fields.serial_byte4 == field):
            return False
        if (fields.serial_byte5 == field):
            return False
    if (messages.I2CSearchError == name and nodes.Edda_Controller == sender):
        if (fields.bus == field):
            return True
        if (fields.error == field):
            return False
        if (fields.scanned_address == field):
            return False
    if (messages.I2CSearchError == name and nodes.Edda_Telemetry == sender):
        if (fields.bus == field):
            return True
        if (fields.error == field):
            return False
        if (fields.scanned_address == field):
            return False
    if (messages.I2CSearchError == name and nodes.Edda_Pressure_Top == sender):
        if (fields.bus == field):
            return True
        if (fields.error == field):
            return False
        if (fields.scanned_address == field):
            return False
    if (messages.I2CSearchError == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.bus == field):
            return True
        if (fields.error == field):
            return False
        if (fields.scanned_address == field):
            return False
    if (messages.MAX31856Error == name and nodes.Edda_Telemetry == sender):
        if (fields.board_index == field):
            return True
        if (fields.sensor_index == field):
            return True
        if (fields.raw_fault_register == field):
            return False
    if (messages.PartialDebugMessage4 == name and nodes.Edda_Controller == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
    if (messages.PartialDebugMessage4 == name and nodes.Edda_Telemetry == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
    if (messages.PartialDebugMessage4 == name and nodes.Edda_Pressure_Top == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
    if (messages.PartialDebugMessage4 == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
    if (messages.OneWireDeviceStartupFailure == name and nodes.Edda_Telemetry == sender):
        if (fields.bus == field):
            return True
        if (fields.serial_byte0 == field):
            return False
        if (fields.serial_byte1 == field):
            return False
        if (fields.serial_byte2 == field):
            return False
        if (fields.serial_byte3 == field):
            return False
        if (fields.serial_byte4 == field):
            return False
        if (fields.serial_byte5 == field):
            return False
    if (messages.I2CSearchFoundDevice == name and nodes.Edda_Controller == sender):
        if (fields.bus == field):
            return True
        if (fields.found_device_address == field):
            return False
    if (messages.I2CSearchFoundDevice == name and nodes.Edda_Telemetry == sender):
        if (fields.bus == field):
            return True
        if (fields.found_device_address == field):
            return False
    if (messages.I2CSearchFoundDevice == name and nodes.Edda_Pressure_Top == sender):
        if (fields.bus == field):
            return True
        if (fields.found_device_address == field):
            return False
    if (messages.I2CSearchFoundDevice == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.bus == field):
            return True
        if (fields.found_device_address == field):
            return False
    if (messages.MAX31865Error == name and nodes.Edda_Telemetry == sender):
        if (fields.board_index == field):
            return True
        if (fields.sensor_index == field):
            return True
        if (fields.raw_fault_register == field):
            return False
    if (messages.PartialDebugMessage5 == name and nodes.Edda_Controller == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
        if (fields.byte4 == field):
            return False
    if (messages.PartialDebugMessage5 == name and nodes.Edda_Telemetry == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
        if (fields.byte4 == field):
            return False
    if (messages.PartialDebugMessage5 == name and nodes.Edda_Pressure_Top == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
        if (fields.byte4 == field):
            return False
    if (messages.PartialDebugMessage5 == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
        if (fields.byte4 == field):
            return False
    if (messages.I2CSearchEnded == name and nodes.Edda_Controller == sender):
        if (fields.bus == field):
            return True
        if (fields.devices_successfully_found == field):
            return False
        if (fields.addresses_with_error == field):
            return False
        if (fields.search_time_us == field):
            return False
    if (messages.I2CSearchEnded == name and nodes.Edda_Telemetry == sender):
        if (fields.bus == field):
            return True
        if (fields.devices_successfully_found == field):
            return False
        if (fields.addresses_with_error == field):
            return False
        if (fields.search_time_us == field):
            return False
    if (messages.I2CSearchEnded == name and nodes.Edda_Pressure_Top == sender):
        if (fields.bus == field):
            return True
        if (fields.devices_successfully_found == field):
            return False
        if (fields.addresses_with_error == field):
            return False
        if (fields.search_time_us == field):
            return False
    if (messages.I2CSearchEnded == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.bus == field):
            return True
        if (fields.devices_successfully_found == field):
            return False
        if (fields.addresses_with_error == field):
            return False
        if (fields.search_time_us == field):
            return False
    if (messages.PartialDebugMessage6 == name and nodes.Edda_Controller == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
        if (fields.byte4 == field):
            return False
        if (fields.byte5 == field):
            return False
    if (messages.PartialDebugMessage6 == name and nodes.Edda_Telemetry == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
        if (fields.byte4 == field):
            return False
        if (fields.byte5 == field):
            return False
    if (messages.PartialDebugMessage6 == name and nodes.Edda_Pressure_Top == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
        if (fields.byte4 == field):
            return False
        if (fields.byte5 == field):
            return False
    if (messages.PartialDebugMessage6 == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
        if (fields.byte4 == field):
            return False
        if (fields.byte5 == field):
            return False
    if (messages.PartialDebugMessage7 == name and nodes.Edda_Controller == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
        if (fields.byte4 == field):
            return False
        if (fields.byte5 == field):
            return False
        if (fields.byte6 == field):
            return False
    if (messages.PartialDebugMessage7 == name and nodes.Edda_Telemetry == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
        if (fields.byte4 == field):
            return False
        if (fields.byte5 == field):
            return False
        if (fields.byte6 == field):
            return False
    if (messages.PartialDebugMessage7 == name and nodes.Edda_Pressure_Top == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
        if (fields.byte4 == field):
            return False
        if (fields.byte5 == field):
            return False
        if (fields.byte6 == field):
            return False
    if (messages.PartialDebugMessage7 == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
        if (fields.byte4 == field):
            return False
        if (fields.byte5 == field):
            return False
        if (fields.byte6 == field):
            return False
    return False
def is_extended_id(id):
    if 1 == id:
        return null
    if 2 == id:
        return null
    if 2 == id:
        return null
    if 2 == id:
        return null
    if 2 == id:
        return null
    if 3 == id:
        return null
    if 4 == id:
        return null
    if 5 == id:
        return null
    if 6 == id:
        return null
    if 7 == id:
        return null
    if 8 == id:
        return null
    if 9 == id:
        return null
    if 10 == id:
        return null
    if 11 == id:
        return null
    if 12 == id:
        return null
    if 13 == id:
        return null
    if 48 == id:
        return null
    if 48 == id:
        return null
    if 48 == id:
        return null
    if 48 == id:
        return null
    if 49 == id:
        return null
    if 49 == id:
        return null
    if 49 == id:
        return null
    if 49 == id:
        return null
    if 50 == id:
        return null
    if 50 == id:
        return null
    if 51 == id:
        return null
    if 51 == id:
        return null
    if 52 == id:
        return null
    if 52 == id:
        return null
    if 64 == id:
        return null
    if 64 == id:
        return null
    if 65 == id:
        return null
    if 65 == id:
        return null
    if 66 == id:
        return null
    if 66 == id:
        return null
    if 67 == id:
        return null
    if 68 == id:
        return null
    if 69 == id:
        return null
    if 70 == id:
        return null
    if 144 == id:
        return null
    if 144 == id:
        return null
    if 144 == id:
        return null
    if 145 == id:
        return null
    if 146 == id:
        return null
    if 147 == id:
        return null
    if 148 == id:
        return null
    if 148 == id:
        return null
    if 148 == id:
        return null
    if 148 == id:
        return null
    if 149 == id:
        return null
    if 150 == id:
        return null
    if 151 == id:
        return null
    if 152 == id:
        return null
    if 153 == id:
        return null
    if 154 == id:
        return null
    if 155 == id:
        return null
    if 156 == id:
        return null
    if 157 == id:
        return null
    if 158 == id:
        return null
    if 159 == id:
        return null
    if 160 == id:
        return null
    if 161 == id:
        return null
    if 162 == id:
        return null
    if 163 == id:
        return null
    if 164 == id:
        return null
    if 165 == id:
        return null
    if 166 == id:
        return null
    if 167 == id:
        return null
    if 168 == id:
        return null
    if 169 == id:
        return null
    if 170 == id:
        return null
    if 171 == id:
        return null
    if 172 == id:
        return null
    if 173 == id:
        return null
    if 174 == id:
        return null
    if 175 == id:
        return null
    if 176 == id:
        return null
    if 177 == id:
        return null
    if 178 == id:
        return null
    if 179 == id:
        return null
    if 180 == id:
        return null
    if 181 == id:
        return null
    if 182 == id:
        return null
    if 183 == id:
        return null
    if 184 == id:
        return null
    if 185 == id:
        return null
    if 187 == id:
        return null
    if 188 == id:
        return null
    if 189 == id:
        return null
    if 190 == id:
        return null
    if 191 == id:
        return null
    if 192 == id:
        return null
    if 193 == id:
        return null
    if 198 == id:
        return null
    if 199 == id:
        return null
    if 200 == id:
        return null
    if 201 == id:
        return null
    if 202 == id:
        return null
    if 203 == id:
        return null
    if 204 == id:
        return null
    if 205 == id:
        return null
    if 207 == id:
        return null
    if 208 == id:
        return null
    if 209 == id:
        return null
    if 210 == id:
        return null
    if 215 == id:
        return null
    if 216 == id:
        return null
    if 217 == id:
        return null
    if 218 == id:
        return null
    if 219 == id:
        return null
    if 220 == id:
        return null
    if 221 == id:
        return null
    if 222 == id:
        return null
    if 223 == id:
        return null
    if 224 == id:
        return null
    if 225 == id:
        return null
    if 226 == id:
        return null
    if 227 == id:
        return null
    if 228 == id:
        return null
    if 229 == id:
        return null
    if 230 == id:
        return null
    if 231 == id:
        return null
    if 232 == id:
        return null
    if 233 == id:
        return null
    if 234 == id:
        return null
    if 235 == id:
        return null
    if 236 == id:
        return null
    if 237 == id:
        return null
    if 238 == id:
        return null
    if 239 == id:
        return null
    if 186 == id:
        return 1
    if 194 == id:
        return 1
    if 195 == id:
        return 1
    if 196 == id:
        return 1
    if 197 == id:
        return 1
    if 206 == id:
        return 1
    if 211 == id:
        return 1
    if 212 == id:
        return 1
    if 213 == id:
        return 1
    if 214 == id:
        return 1
    if 186 == id:
        return 2
    if 194 == id:
        return 2
    if 195 == id:
        return 2
    if 196 == id:
        return 2
    if 197 == id:
        return 2
    if 206 == id:
        return 2
    if 211 == id:
        return 2
    if 212 == id:
        return 2
    if 213 == id:
        return 2
    if 214 == id:
        return 2
    if 186 == id:
        return 3
    if 194 == id:
        return 3
    if 195 == id:
        return 3
    if 196 == id:
        return 3
    if 197 == id:
        return 3
    if 206 == id:
        return 3
    if 211 == id:
        return 3
    if 212 == id:
        return 3
    if 213 == id:
        return 3
    if 214 == id:
        return 3
    if 186 == id:
        return 4
    if 194 == id:
        return 4
    if 195 == id:
        return 4
    if 196 == id:
        return 4
    if 197 == id:
        return 4
    if 206 == id:
        return 4
    if 211 == id:
        return 4
    if 212 == id:
        return 4
    if 213 == id:
        return 4
    if 214 == id:
        return 4
    if 186 == id:
        return 5
    if 194 == id:
        return 5
    if 195 == id:
        return 5
    if 196 == id:
        return 5
    if 197 == id:
        return 5
    if 211 == id:
        return 5
    if 212 == id:
        return 5
    if 213 == id:
        return 5
    if 214 == id:
        return 5
    if 194 == id:
        return 6
    if 195 == id:
        return 6
    if 196 == id:
        return 6
    if 197 == id:
        return 6
    if 194 == id:
        return 7
    if 195 == id:
        return 7
    if 196 == id:
        return 7
    if 197 == id:
        return 7
    return
