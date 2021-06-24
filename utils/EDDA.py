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
    currentMillis = 0
    currentMicros = 1
    roundTripTime_us = 2
    destination_node_id = 3
    debugMessagesMode = 4
    debugStatusLedsMode = 5
    powerMode = 6
    uptime_ms = 7
    maxTxQueueSize = 8
    maxRxQueueSize = 9
    meanTxQueueSize = 10
    meanRxQueueSize = 11
    w = 12
    e = 13
    n = 14
    h = 15
    o = 16
    p = 17
    receiver_node_id = 18
    messages = 19
    statusLeds = 20
    mode = 21
    timeSpentAwake_ms = 22
    timeSpentSleeping_us = 23
    current_amperes = 24
    voltage_volts = 25
    power_watts = 26
    error = 27
    sensor_index = 28
    pressure_pascal = 29
    pressure_millibars = 30
    coefficient_index = 31
    coefficient_value = 32
    sensor_type = 33
    temperature_celsius = 34
    resistance_ohms = 35
    ratio_fraction = 36
    bus_index = 37
    type = 38
    timeForMeasurement_microseconds = 39
    chip_index = 40
    truncated_serial = 41
    family_code = 42
    crc_code = 43
    raw_fault_register = 44
    distance_mm = 45
    relative_humidity = 46
    acceleration_x_gforce = 47
    acceleration_y_gforce = 48
    acceleration_z_gforce = 49
    length = 50
    byte0 = 51
    byte1 = 52
    byte2 = 53
    byte3 = 54
    byte4 = 55
    byte5 = 56
    byte6 = 57
    thread_id = 58
    taskTime_microseconds = 59
    loopTime_microseconds = 60
    power_control_channel_id = 61
    requested_state = 62
    circumvent_arming_checks = 63
    requested_circumvent_arming_checks = 64
    result = 65
    channel_state = 66
    gate_state = 67
    voltage_3v3_volts = 68
    voltage_input_volts = 69
    source = 70
    estimated_current_amperes = 71
    estimated_power_amperes = 72
    this_number_must_be_positive_1 = 73
    this_number_must_be_negative_2 = 74
    this_number_must_be_positive_4 = 75
    this_number_must_be_negative_8 = 76
    this_number_must_be_positive_16 = 77
    this_number_must_be_negative_32 = 78
    this_number_must_be_positive_64 = 79
    this_number_must_be_negative_128 = 80
class messages(Enum):
    CurrentTimePing = 0
    CanLatency = 1
    CurrentTimePong = 2
    SayHi = 3
    Hello = 4
    CanStatistics = 5
    WenHop = 6
    SetDebugModeRequest = 7
    SetPowerModeRequest = 8
    GoingToSleep = 9
    WokeUp = 10
    RequestReset = 11
    PowerInputMeasurement = 12
    PowerInputMeasurementError = 13
    RawTransducerVoltage = 14
    TransducerPressure = 15
    AmbientPressure = 16
    TransducerError = 17
    AmbientPressureError = 18
    AmbientPressureCoefficient = 19
    ColdSideTemperature = 20
    PlatinumSensorTemperature = 21
    PlatinumSensorResistance = 22
    PlatinumSensorRatio = 23
    OneWireBusError = 24
    ThermocoupleTypeKTemperature = 25
    SensorMeasurementInfo = 26
    DS28E18QTransactionError = 27
    CouldNotFindDS28E18Q = 28
    MAX31850KError = 29
    MAX31856Error = 30
    MAX31865Error = 31
    ValveActuation = 32
    ValveActuationError = 33
    Humidity = 34
    HumidityError = 35
    Acceleration = 36
    AccelerationError = 37
    PartialDebugMessage = 38
    TaskInfo = 39
    LoopInfo = 40
    PowerControlNewStateRequest = 41
    PowerControlNewStateResponse = 42
    PowerControlGetState = 43
    PowerControlState = 44
    PowerControlVoltages = 45
    PowerControlResistance = 46
    PowerControlEstimates = 47
    PowerControlLoadMeasurement = 48
    PowerControlLoadMeasurementError = 49
    PowerControlResistanceMeasurementError = 50
    PerformIgnition = 51
    IgnitionHappened = 52
    IgnitionCannotHappen = 53
class categories(Enum):
    none = 0
class nodes(Enum):
    Flight_Controller = 0
    Edda_Controller = 1
    Edda_Telemetry = 2
    Edda_Pressure_Top = 3
    Edda_Pressure_Bottom = 4
    Edda_Simulator = 5
    Ground_Controller = 16
class PowerMode(Enum):
    Active = 0
    Hibernate = 1
class DebugMessagesMode(Enum):
    Enabled = 0
    Disabled = 1
class DebugStatusLedsMode(Enum):
    Enabled = 0
    Disabled = 1
class SensorMeasurementInfo(Enum):
    MAX31850K_Conversion = 0
    MAX31850K_Read = 1
    DS2482_StatusCheck = 2
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
class LoopType(Enum):
    MainLoop = 0
    ChitchatLoop = 1
    RGBLoop = 2
    GenericThreadLoop = 3
    EddaLoop = 4
class PowerControlChannel(Enum):
    MainValveSolenoid = 0
    VentingSolenoid = 1
    IgnitionCircuit = 2
class PowerControlChannelStateRequest(Enum):
    RequestToArm = 0
    RequestToDisarm = 1
    RequestToStartPower = 2
    RequestToStopPower = 3
class CircumventArmingCheck(Enum):
    SafelyUseArmingChecks = 0
    DangerouslyIgnoreArmingChecks = 1
class PowerControlChannelStateRequestResult(Enum):
    Success = 0
    Failure = 1
class PowerControlChannelState(Enum):
    Idle = 0
    Arming = 1
    Armed = 2
    Firing = 3
class owerControlChannelGateState(Enum):
    Grounded = 0
    ResistanceMeasurement = 1
    High = 2
class AccelerationError(Enum):
    CRCMismatch = 0
    I2CUnknownError = 1
    I2CAddressNack = 2
    I2CDataNack = 3
class PowerInputMeasurementError(Enum):
    CRCMismatch = 0
    I2CUnknownError = 1
    I2CAddressNack = 2
    I2CDataNack = 3
    I2CTransmitBufferFull = 4
    UnexpectedManufacturer = 5
    UnexpectedDie = 6
    UnexpectedConfiguration = 7
    UnexpectedMask = 8
    UnexpectedAlertLimit = 9
    Unknown = 10
class OneWireBusError(Enum):
    NoError = 0
    BusShortDetected = 1
    NoDevicesResponded = 2
    ConfigError = 3
    WaitOnBusyTimeout = 4
    ResetFailure = 5
    WireDataTooLong = 6
    WireNackOnAddress = 7
    WireNackOnDataTransmission = 8
    WireUnknownError = 9
class DS28E18QTransactionError(Enum):
    RequestCRCFailure = 0
    ResponseCRCFailure = 1
    InvalidLength = 2
    TransactionFailedSuccessfully = 3
    UnableToFindDevice = 4
class HumidityError(Enum):
    CRCMismatch = 0
    I2CUnknownError = 1
    I2CAddressNack = 2
    I2CDataNack = 3
class PowerControlResistanceSource(Enum):
    Estimate = 0
    HighPrecision = 1
class PowerControlLoadMeasurementError(Enum):
    CRCMismatch = 0
    I2CUnknownError = 1
    I2CAddressNack = 2
    I2CDataNack = 3
class PowerControlResistanceMeasurementError(Enum):
    CRCMismatch = 0
    I2CUnknownError = 1
    I2CAddressNack = 2
    I2CDataNack = 3
class TransducerError(Enum):
    CRCMismatch = 0
    I2CUnknownError = 1
    I2CAddressNack = 2
    I2CDataNack = 3
    Undervoltage = 4
    Overvoltage = 5
    Unknown = 6
class AmbientPressureError(Enum):
    CRCMismatch = 0
    I2CUnknownError = 1
    I2CAddressNack = 2
    I2CDataNack = 3
    D1BelowBounds = 4
    D1AboveBounds = 5
    D2BelowBounds = 6
    D2AboveBounds = 7
    Value_dT_BelowBounds = 8
    Value_dT_AboveBounds = 9
    Value_TEMP_BelowBounds = 10
    Value_TEMP_AboveBounds = 11
    Value_OFF_BelowBounds = 12
    Value_OFF_AboveBounds = 13
    Value_SENS_BelowBounds = 14
    Value_SENS_AboveBounds = 15
    Value_P_BelowBounds = 16
    Value_P_AboveBounds = 17
    Unknown = 18
class ColdSideTemperatureSensorType(Enum):
    InternalTemperature = 0
    PowerRegulator = 1
    AmbientPressureSensor = 2
    ThermocoupleColdSide = 3
class MAX31850KError(Enum):
    CRCMismatch = 0
    OneWireUnknownError = 1
    SensorShortToVDD = 2
    SensorShortToGND = 3
    SensorOpenCircuit = 4
class ValveActuationError(Enum):
    CRCMismatch = 0
    I2CUnknownError = 1
    I2CAddressNack = 2
    I2CDataNack = 3
class CurrentTimePing_from_Flight_Controller_to_Edda_Controller:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Controller
        self._message = messages.CurrentTimePing
        self._category = categories.none
        self._id = 0
        self._size = 8
        self._currentMillis = 0
        self._currentMicros = 0
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
    def set_currentMillis(self, value):
        self._currentMillis = value
    def set_currentMicros(self, value):
        self._currentMicros = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._currentMillis)
        buf += struct.pack("<L", self._currentMicros)
        return buf
    def get_currentMillis(self):
        return self._currentMillis
    def get_currentMicros(self):
        return self._currentMicros
    def get_all_data(self):
        data = []
        data.append((fields.currentMillis, self.get_currentMillis()))
        data.append((fields.currentMicros, self.get_currentMicros()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._currentMillis = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._currentMicros = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class CurrentTimePing_from_Flight_Controller_to_Edda_Telemetry:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Telemetry
        self._message = messages.CurrentTimePing
        self._category = categories.none
        self._id = 0
        self._size = 8
        self._currentMillis = 0
        self._currentMicros = 0
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
    def set_currentMillis(self, value):
        self._currentMillis = value
    def set_currentMicros(self, value):
        self._currentMicros = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._currentMillis)
        buf += struct.pack("<L", self._currentMicros)
        return buf
    def get_currentMillis(self):
        return self._currentMillis
    def get_currentMicros(self):
        return self._currentMicros
    def get_all_data(self):
        data = []
        data.append((fields.currentMillis, self.get_currentMillis()))
        data.append((fields.currentMicros, self.get_currentMicros()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._currentMillis = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._currentMicros = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class CurrentTimePing_from_Flight_Controller_to_Edda_Pressure_Top:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Pressure_Top
        self._message = messages.CurrentTimePing
        self._category = categories.none
        self._id = 0
        self._size = 8
        self._currentMillis = 0
        self._currentMicros = 0
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
    def set_currentMillis(self, value):
        self._currentMillis = value
    def set_currentMicros(self, value):
        self._currentMicros = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._currentMillis)
        buf += struct.pack("<L", self._currentMicros)
        return buf
    def get_currentMillis(self):
        return self._currentMillis
    def get_currentMicros(self):
        return self._currentMicros
    def get_all_data(self):
        data = []
        data.append((fields.currentMillis, self.get_currentMillis()))
        data.append((fields.currentMicros, self.get_currentMicros()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._currentMillis = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._currentMicros = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class CurrentTimePing_from_Flight_Controller_to_Edda_Pressure_Bottom:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Pressure_Bottom
        self._message = messages.CurrentTimePing
        self._category = categories.none
        self._id = 0
        self._size = 8
        self._currentMillis = 0
        self._currentMicros = 0
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
    def set_currentMillis(self, value):
        self._currentMillis = value
    def set_currentMicros(self, value):
        self._currentMicros = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._currentMillis)
        buf += struct.pack("<L", self._currentMicros)
        return buf
    def get_currentMillis(self):
        return self._currentMillis
    def get_currentMicros(self):
        return self._currentMicros
    def get_all_data(self):
        data = []
        data.append((fields.currentMillis, self.get_currentMillis()))
        data.append((fields.currentMicros, self.get_currentMicros()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._currentMillis = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._currentMicros = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class CurrentTimePing_from_Flight_Controller_to_Edda_Simulator:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Simulator
        self._message = messages.CurrentTimePing
        self._category = categories.none
        self._id = 0
        self._size = 8
        self._currentMillis = 0
        self._currentMicros = 0
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
    def set_currentMillis(self, value):
        self._currentMillis = value
    def set_currentMicros(self, value):
        self._currentMicros = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._currentMillis)
        buf += struct.pack("<L", self._currentMicros)
        return buf
    def get_currentMillis(self):
        return self._currentMillis
    def get_currentMicros(self):
        return self._currentMicros
    def get_all_data(self):
        data = []
        data.append((fields.currentMillis, self.get_currentMillis()))
        data.append((fields.currentMicros, self.get_currentMicros()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._currentMillis = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._currentMicros = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class CanLatency_from_Flight_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.CanLatency
        self._category = categories.none
        self._id = 144
        self._size = 5
        self._roundTripTime_us = 0
        self._destination_node_id = 0
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
    def set_roundTripTime_us(self, value):
        self._roundTripTime_us = value
    def set_destination_node_id(self, value):
        self._destination_node_id = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._roundTripTime_us)
        buf += struct.pack("<B", self._destination_node_id)
        return buf
    def get_roundTripTime_us(self):
        return self._roundTripTime_us
    def get_destination_node_id(self):
        return self._destination_node_id
    def get_all_data(self):
        data = []
        data.append((fields.roundTripTime_us, self.get_roundTripTime_us()))
        data.append((fields.destination_node_id, self.get_destination_node_id()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._roundTripTime_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._destination_node_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class CanLatency_from_Flight_Controller_to_Edda_Controller:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Controller
        self._message = messages.CanLatency
        self._category = categories.none
        self._id = 144
        self._size = 5
        self._roundTripTime_us = 0
        self._destination_node_id = 0
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
    def set_roundTripTime_us(self, value):
        self._roundTripTime_us = value
    def set_destination_node_id(self, value):
        self._destination_node_id = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._roundTripTime_us)
        buf += struct.pack("<B", self._destination_node_id)
        return buf
    def get_roundTripTime_us(self):
        return self._roundTripTime_us
    def get_destination_node_id(self):
        return self._destination_node_id
    def get_all_data(self):
        data = []
        data.append((fields.roundTripTime_us, self.get_roundTripTime_us()))
        data.append((fields.destination_node_id, self.get_destination_node_id()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._roundTripTime_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._destination_node_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class CanLatency_from_Flight_Controller_to_Edda_Telemetry:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Telemetry
        self._message = messages.CanLatency
        self._category = categories.none
        self._id = 144
        self._size = 5
        self._roundTripTime_us = 0
        self._destination_node_id = 0
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
    def set_roundTripTime_us(self, value):
        self._roundTripTime_us = value
    def set_destination_node_id(self, value):
        self._destination_node_id = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._roundTripTime_us)
        buf += struct.pack("<B", self._destination_node_id)
        return buf
    def get_roundTripTime_us(self):
        return self._roundTripTime_us
    def get_destination_node_id(self):
        return self._destination_node_id
    def get_all_data(self):
        data = []
        data.append((fields.roundTripTime_us, self.get_roundTripTime_us()))
        data.append((fields.destination_node_id, self.get_destination_node_id()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._roundTripTime_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._destination_node_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class CanLatency_from_Flight_Controller_to_Edda_Pressure_Top:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Pressure_Top
        self._message = messages.CanLatency
        self._category = categories.none
        self._id = 144
        self._size = 5
        self._roundTripTime_us = 0
        self._destination_node_id = 0
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
    def set_roundTripTime_us(self, value):
        self._roundTripTime_us = value
    def set_destination_node_id(self, value):
        self._destination_node_id = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._roundTripTime_us)
        buf += struct.pack("<B", self._destination_node_id)
        return buf
    def get_roundTripTime_us(self):
        return self._roundTripTime_us
    def get_destination_node_id(self):
        return self._destination_node_id
    def get_all_data(self):
        data = []
        data.append((fields.roundTripTime_us, self.get_roundTripTime_us()))
        data.append((fields.destination_node_id, self.get_destination_node_id()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._roundTripTime_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._destination_node_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class CanLatency_from_Flight_Controller_to_Edda_Pressure_Bottom:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Pressure_Bottom
        self._message = messages.CanLatency
        self._category = categories.none
        self._id = 144
        self._size = 5
        self._roundTripTime_us = 0
        self._destination_node_id = 0
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
    def set_roundTripTime_us(self, value):
        self._roundTripTime_us = value
    def set_destination_node_id(self, value):
        self._destination_node_id = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._roundTripTime_us)
        buf += struct.pack("<B", self._destination_node_id)
        return buf
    def get_roundTripTime_us(self):
        return self._roundTripTime_us
    def get_destination_node_id(self):
        return self._destination_node_id
    def get_all_data(self):
        data = []
        data.append((fields.roundTripTime_us, self.get_roundTripTime_us()))
        data.append((fields.destination_node_id, self.get_destination_node_id()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._roundTripTime_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._destination_node_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class CanLatency_from_Flight_Controller_to_Edda_Simulator:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Simulator
        self._message = messages.CanLatency
        self._category = categories.none
        self._id = 144
        self._size = 5
        self._roundTripTime_us = 0
        self._destination_node_id = 0
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
    def set_roundTripTime_us(self, value):
        self._roundTripTime_us = value
    def set_destination_node_id(self, value):
        self._destination_node_id = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._roundTripTime_us)
        buf += struct.pack("<B", self._destination_node_id)
        return buf
    def get_roundTripTime_us(self):
        return self._roundTripTime_us
    def get_destination_node_id(self):
        return self._destination_node_id
    def get_all_data(self):
        data = []
        data.append((fields.roundTripTime_us, self.get_roundTripTime_us()))
        data.append((fields.destination_node_id, self.get_destination_node_id()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._roundTripTime_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._destination_node_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class CurrentTimePong_from_Edda_Controller_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Flight_Controller
        self._message = messages.CurrentTimePong
        self._category = categories.none
        self._id = 4
        self._size = 8
        self._currentMillis = 0
        self._currentMicros = 0
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
    def set_currentMillis(self, value):
        self._currentMillis = value
    def set_currentMicros(self, value):
        self._currentMicros = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._currentMillis)
        buf += struct.pack("<L", self._currentMicros)
        return buf
    def get_currentMillis(self):
        return self._currentMillis
    def get_currentMicros(self):
        return self._currentMicros
    def get_all_data(self):
        data = []
        data.append((fields.currentMillis, self.get_currentMillis()))
        data.append((fields.currentMicros, self.get_currentMicros()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._currentMillis = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._currentMicros = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class CurrentTimePong_from_Edda_Telemetry_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Flight_Controller
        self._message = messages.CurrentTimePong
        self._category = categories.none
        self._id = 5
        self._size = 8
        self._currentMillis = 0
        self._currentMicros = 0
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
    def set_currentMillis(self, value):
        self._currentMillis = value
    def set_currentMicros(self, value):
        self._currentMicros = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._currentMillis)
        buf += struct.pack("<L", self._currentMicros)
        return buf
    def get_currentMillis(self):
        return self._currentMillis
    def get_currentMicros(self):
        return self._currentMicros
    def get_all_data(self):
        data = []
        data.append((fields.currentMillis, self.get_currentMillis()))
        data.append((fields.currentMicros, self.get_currentMicros()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._currentMillis = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._currentMicros = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class CurrentTimePong_from_Edda_Pressure_Top_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Flight_Controller
        self._message = messages.CurrentTimePong
        self._category = categories.none
        self._id = 6
        self._size = 8
        self._currentMillis = 0
        self._currentMicros = 0
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
    def set_currentMillis(self, value):
        self._currentMillis = value
    def set_currentMicros(self, value):
        self._currentMicros = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._currentMillis)
        buf += struct.pack("<L", self._currentMicros)
        return buf
    def get_currentMillis(self):
        return self._currentMillis
    def get_currentMicros(self):
        return self._currentMicros
    def get_all_data(self):
        data = []
        data.append((fields.currentMillis, self.get_currentMillis()))
        data.append((fields.currentMicros, self.get_currentMicros()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._currentMillis = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._currentMicros = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class CurrentTimePong_from_Edda_Pressure_Bottom_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Flight_Controller
        self._message = messages.CurrentTimePong
        self._category = categories.none
        self._id = 7
        self._size = 8
        self._currentMillis = 0
        self._currentMicros = 0
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
    def set_currentMillis(self, value):
        self._currentMillis = value
    def set_currentMicros(self, value):
        self._currentMicros = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._currentMillis)
        buf += struct.pack("<L", self._currentMicros)
        return buf
    def get_currentMillis(self):
        return self._currentMillis
    def get_currentMicros(self):
        return self._currentMicros
    def get_all_data(self):
        data = []
        data.append((fields.currentMillis, self.get_currentMillis()))
        data.append((fields.currentMicros, self.get_currentMicros()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._currentMillis = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._currentMicros = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class CurrentTimePong_from_Edda_Simulator_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Flight_Controller
        self._message = messages.CurrentTimePong
        self._category = categories.none
        self._id = 8
        self._size = 8
        self._currentMillis = 0
        self._currentMicros = 0
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
    def set_currentMillis(self, value):
        self._currentMillis = value
    def set_currentMicros(self, value):
        self._currentMicros = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._currentMillis)
        buf += struct.pack("<L", self._currentMicros)
        return buf
    def get_currentMillis(self):
        return self._currentMillis
    def get_currentMicros(self):
        return self._currentMicros
    def get_all_data(self):
        data = []
        data.append((fields.currentMillis, self.get_currentMillis()))
        data.append((fields.currentMicros, self.get_currentMicros()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._currentMillis = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._currentMicros = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class SayHi_from_Flight_Controller_to_Edda_Controller:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Controller
        self._message = messages.SayHi
        self._category = categories.none
        self._id = 1
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
class SayHi_from_Flight_Controller_to_Edda_Telemetry:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Telemetry
        self._message = messages.SayHi
        self._category = categories.none
        self._id = 1
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
class SayHi_from_Flight_Controller_to_Edda_Pressure_Top:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Pressure_Top
        self._message = messages.SayHi
        self._category = categories.none
        self._id = 1
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
class SayHi_from_Flight_Controller_to_Edda_Pressure_Bottom:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Pressure_Bottom
        self._message = messages.SayHi
        self._category = categories.none
        self._id = 1
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
class SayHi_from_Flight_Controller_to_Edda_Simulator:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Simulator
        self._message = messages.SayHi
        self._category = categories.none
        self._id = 1
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
class Hello_from_Edda_Controller_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Flight_Controller
        self._message = messages.Hello
        self._category = categories.none
        self._id = 9
        self._size = 7
        self._debugMessagesMode = 0
        self._debugStatusLedsMode = 0
        self._powerMode = 0
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
    def set_debugMessagesMode(self, value):
        self._debugMessagesMode = value.value
    def set_debugStatusLedsMode(self, value):
        self._debugStatusLedsMode = value.value
    def set_powerMode(self, value):
        self._powerMode = value.value
    def set_uptime_ms(self, value):
        self._uptime_ms = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._debugMessagesMode)
        buf += struct.pack("<B", self._debugStatusLedsMode)
        buf += struct.pack("<B", self._powerMode)
        buf += struct.pack("<L", self._uptime_ms)
        return buf
    def get_debugMessagesMode(self):
        return DebugMessagesMode(self._debugMessagesMode)
    def get_debugStatusLedsMode(self):
        return DebugStatusLedsMode(self._debugStatusLedsMode)
    def get_powerMode(self):
        return PowerMode(self._powerMode)
    def get_uptime_ms(self):
        return self._uptime_ms
    def get_all_data(self):
        data = []
        data.append((fields.debugMessagesMode, self.get_debugMessagesMode()))
        data.append((fields.debugStatusLedsMode, self.get_debugStatusLedsMode()))
        data.append((fields.powerMode, self.get_powerMode()))
        data.append((fields.uptime_ms, self.get_uptime_ms()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._debugMessagesMode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._debugStatusLedsMode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._powerMode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._uptime_ms = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class Hello_from_Edda_Telemetry_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Flight_Controller
        self._message = messages.Hello
        self._category = categories.none
        self._id = 10
        self._size = 7
        self._debugMessagesMode = 0
        self._debugStatusLedsMode = 0
        self._powerMode = 0
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
    def set_debugMessagesMode(self, value):
        self._debugMessagesMode = value.value
    def set_debugStatusLedsMode(self, value):
        self._debugStatusLedsMode = value.value
    def set_powerMode(self, value):
        self._powerMode = value.value
    def set_uptime_ms(self, value):
        self._uptime_ms = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._debugMessagesMode)
        buf += struct.pack("<B", self._debugStatusLedsMode)
        buf += struct.pack("<B", self._powerMode)
        buf += struct.pack("<L", self._uptime_ms)
        return buf
    def get_debugMessagesMode(self):
        return DebugMessagesMode(self._debugMessagesMode)
    def get_debugStatusLedsMode(self):
        return DebugStatusLedsMode(self._debugStatusLedsMode)
    def get_powerMode(self):
        return PowerMode(self._powerMode)
    def get_uptime_ms(self):
        return self._uptime_ms
    def get_all_data(self):
        data = []
        data.append((fields.debugMessagesMode, self.get_debugMessagesMode()))
        data.append((fields.debugStatusLedsMode, self.get_debugStatusLedsMode()))
        data.append((fields.powerMode, self.get_powerMode()))
        data.append((fields.uptime_ms, self.get_uptime_ms()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._debugMessagesMode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._debugStatusLedsMode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._powerMode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._uptime_ms = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class Hello_from_Edda_Pressure_Top_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Flight_Controller
        self._message = messages.Hello
        self._category = categories.none
        self._id = 11
        self._size = 7
        self._debugMessagesMode = 0
        self._debugStatusLedsMode = 0
        self._powerMode = 0
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
    def set_debugMessagesMode(self, value):
        self._debugMessagesMode = value.value
    def set_debugStatusLedsMode(self, value):
        self._debugStatusLedsMode = value.value
    def set_powerMode(self, value):
        self._powerMode = value.value
    def set_uptime_ms(self, value):
        self._uptime_ms = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._debugMessagesMode)
        buf += struct.pack("<B", self._debugStatusLedsMode)
        buf += struct.pack("<B", self._powerMode)
        buf += struct.pack("<L", self._uptime_ms)
        return buf
    def get_debugMessagesMode(self):
        return DebugMessagesMode(self._debugMessagesMode)
    def get_debugStatusLedsMode(self):
        return DebugStatusLedsMode(self._debugStatusLedsMode)
    def get_powerMode(self):
        return PowerMode(self._powerMode)
    def get_uptime_ms(self):
        return self._uptime_ms
    def get_all_data(self):
        data = []
        data.append((fields.debugMessagesMode, self.get_debugMessagesMode()))
        data.append((fields.debugStatusLedsMode, self.get_debugStatusLedsMode()))
        data.append((fields.powerMode, self.get_powerMode()))
        data.append((fields.uptime_ms, self.get_uptime_ms()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._debugMessagesMode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._debugStatusLedsMode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._powerMode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._uptime_ms = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class Hello_from_Edda_Pressure_Bottom_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Flight_Controller
        self._message = messages.Hello
        self._category = categories.none
        self._id = 12
        self._size = 7
        self._debugMessagesMode = 0
        self._debugStatusLedsMode = 0
        self._powerMode = 0
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
    def set_debugMessagesMode(self, value):
        self._debugMessagesMode = value.value
    def set_debugStatusLedsMode(self, value):
        self._debugStatusLedsMode = value.value
    def set_powerMode(self, value):
        self._powerMode = value.value
    def set_uptime_ms(self, value):
        self._uptime_ms = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._debugMessagesMode)
        buf += struct.pack("<B", self._debugStatusLedsMode)
        buf += struct.pack("<B", self._powerMode)
        buf += struct.pack("<L", self._uptime_ms)
        return buf
    def get_debugMessagesMode(self):
        return DebugMessagesMode(self._debugMessagesMode)
    def get_debugStatusLedsMode(self):
        return DebugStatusLedsMode(self._debugStatusLedsMode)
    def get_powerMode(self):
        return PowerMode(self._powerMode)
    def get_uptime_ms(self):
        return self._uptime_ms
    def get_all_data(self):
        data = []
        data.append((fields.debugMessagesMode, self.get_debugMessagesMode()))
        data.append((fields.debugStatusLedsMode, self.get_debugStatusLedsMode()))
        data.append((fields.powerMode, self.get_powerMode()))
        data.append((fields.uptime_ms, self.get_uptime_ms()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._debugMessagesMode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._debugStatusLedsMode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._powerMode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._uptime_ms = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class Hello_from_Edda_Simulator_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Flight_Controller
        self._message = messages.Hello
        self._category = categories.none
        self._id = 13
        self._size = 7
        self._debugMessagesMode = 0
        self._debugStatusLedsMode = 0
        self._powerMode = 0
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
    def set_debugMessagesMode(self, value):
        self._debugMessagesMode = value.value
    def set_debugStatusLedsMode(self, value):
        self._debugStatusLedsMode = value.value
    def set_powerMode(self, value):
        self._powerMode = value.value
    def set_uptime_ms(self, value):
        self._uptime_ms = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._debugMessagesMode)
        buf += struct.pack("<B", self._debugStatusLedsMode)
        buf += struct.pack("<B", self._powerMode)
        buf += struct.pack("<L", self._uptime_ms)
        return buf
    def get_debugMessagesMode(self):
        return DebugMessagesMode(self._debugMessagesMode)
    def get_debugStatusLedsMode(self):
        return DebugStatusLedsMode(self._debugStatusLedsMode)
    def get_powerMode(self):
        return PowerMode(self._powerMode)
    def get_uptime_ms(self):
        return self._uptime_ms
    def get_all_data(self):
        data = []
        data.append((fields.debugMessagesMode, self.get_debugMessagesMode()))
        data.append((fields.debugStatusLedsMode, self.get_debugStatusLedsMode()))
        data.append((fields.powerMode, self.get_powerMode()))
        data.append((fields.uptime_ms, self.get_uptime_ms()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._debugMessagesMode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._debugStatusLedsMode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._powerMode = struct.unpack_from("<B", buf, index)[0]
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
        self._id = 145
        self._size = 8
        self._maxTxQueueSize = 0
        self._maxRxQueueSize = 0
        self._meanTxQueueSize = 0
        self._meanRxQueueSize = 0
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
    def set_maxTxQueueSize(self, value):
        self._maxTxQueueSize = value
    def set_maxRxQueueSize(self, value):
        self._maxRxQueueSize = value
    def set_meanTxQueueSize(self, value):
        self._meanTxQueueSize = value
    def set_meanRxQueueSize(self, value):
        self._meanRxQueueSize = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._maxTxQueueSize)
        buf += struct.pack("<H", self._maxRxQueueSize)
        buf += struct.pack("<H", self._meanTxQueueSize)
        buf += struct.pack("<H", self._meanRxQueueSize)
        return buf
    def get_maxTxQueueSize(self):
        return self._maxTxQueueSize
    def get_maxRxQueueSize(self):
        return self._maxRxQueueSize
    def get_meanTxQueueSize(self):
        return self._meanTxQueueSize
    def get_meanRxQueueSize(self):
        return self._meanRxQueueSize
    def get_all_data(self):
        data = []
        data.append((fields.maxTxQueueSize, self.get_maxTxQueueSize()))
        data.append((fields.maxRxQueueSize, self.get_maxRxQueueSize()))
        data.append((fields.meanTxQueueSize, self.get_meanTxQueueSize()))
        data.append((fields.meanRxQueueSize, self.get_meanRxQueueSize()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._maxTxQueueSize = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._maxRxQueueSize = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._meanTxQueueSize = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._meanRxQueueSize = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class CanStatistics_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.CanStatistics
        self._category = categories.none
        self._id = 146
        self._size = 8
        self._maxTxQueueSize = 0
        self._maxRxQueueSize = 0
        self._meanTxQueueSize = 0
        self._meanRxQueueSize = 0
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
    def set_maxTxQueueSize(self, value):
        self._maxTxQueueSize = value
    def set_maxRxQueueSize(self, value):
        self._maxRxQueueSize = value
    def set_meanTxQueueSize(self, value):
        self._meanTxQueueSize = value
    def set_meanRxQueueSize(self, value):
        self._meanRxQueueSize = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._maxTxQueueSize)
        buf += struct.pack("<H", self._maxRxQueueSize)
        buf += struct.pack("<H", self._meanTxQueueSize)
        buf += struct.pack("<H", self._meanRxQueueSize)
        return buf
    def get_maxTxQueueSize(self):
        return self._maxTxQueueSize
    def get_maxRxQueueSize(self):
        return self._maxRxQueueSize
    def get_meanTxQueueSize(self):
        return self._meanTxQueueSize
    def get_meanRxQueueSize(self):
        return self._meanRxQueueSize
    def get_all_data(self):
        data = []
        data.append((fields.maxTxQueueSize, self.get_maxTxQueueSize()))
        data.append((fields.maxRxQueueSize, self.get_maxRxQueueSize()))
        data.append((fields.meanTxQueueSize, self.get_meanTxQueueSize()))
        data.append((fields.meanRxQueueSize, self.get_meanRxQueueSize()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._maxTxQueueSize = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._maxRxQueueSize = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._meanTxQueueSize = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._meanRxQueueSize = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class CanStatistics_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.CanStatistics
        self._category = categories.none
        self._id = 147
        self._size = 8
        self._maxTxQueueSize = 0
        self._maxRxQueueSize = 0
        self._meanTxQueueSize = 0
        self._meanRxQueueSize = 0
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
    def set_maxTxQueueSize(self, value):
        self._maxTxQueueSize = value
    def set_maxRxQueueSize(self, value):
        self._maxRxQueueSize = value
    def set_meanTxQueueSize(self, value):
        self._meanTxQueueSize = value
    def set_meanRxQueueSize(self, value):
        self._meanRxQueueSize = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._maxTxQueueSize)
        buf += struct.pack("<H", self._maxRxQueueSize)
        buf += struct.pack("<H", self._meanTxQueueSize)
        buf += struct.pack("<H", self._meanRxQueueSize)
        return buf
    def get_maxTxQueueSize(self):
        return self._maxTxQueueSize
    def get_maxRxQueueSize(self):
        return self._maxRxQueueSize
    def get_meanTxQueueSize(self):
        return self._meanTxQueueSize
    def get_meanRxQueueSize(self):
        return self._meanRxQueueSize
    def get_all_data(self):
        data = []
        data.append((fields.maxTxQueueSize, self.get_maxTxQueueSize()))
        data.append((fields.maxRxQueueSize, self.get_maxRxQueueSize()))
        data.append((fields.meanTxQueueSize, self.get_meanTxQueueSize()))
        data.append((fields.meanRxQueueSize, self.get_meanRxQueueSize()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._maxTxQueueSize = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._maxRxQueueSize = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._meanTxQueueSize = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._meanRxQueueSize = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class CanStatistics_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.CanStatistics
        self._category = categories.none
        self._id = 148
        self._size = 8
        self._maxTxQueueSize = 0
        self._maxRxQueueSize = 0
        self._meanTxQueueSize = 0
        self._meanRxQueueSize = 0
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
    def set_maxTxQueueSize(self, value):
        self._maxTxQueueSize = value
    def set_maxRxQueueSize(self, value):
        self._maxRxQueueSize = value
    def set_meanTxQueueSize(self, value):
        self._meanTxQueueSize = value
    def set_meanRxQueueSize(self, value):
        self._meanRxQueueSize = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._maxTxQueueSize)
        buf += struct.pack("<H", self._maxRxQueueSize)
        buf += struct.pack("<H", self._meanTxQueueSize)
        buf += struct.pack("<H", self._meanRxQueueSize)
        return buf
    def get_maxTxQueueSize(self):
        return self._maxTxQueueSize
    def get_maxRxQueueSize(self):
        return self._maxRxQueueSize
    def get_meanTxQueueSize(self):
        return self._meanTxQueueSize
    def get_meanRxQueueSize(self):
        return self._meanRxQueueSize
    def get_all_data(self):
        data = []
        data.append((fields.maxTxQueueSize, self.get_maxTxQueueSize()))
        data.append((fields.maxRxQueueSize, self.get_maxRxQueueSize()))
        data.append((fields.meanTxQueueSize, self.get_meanTxQueueSize()))
        data.append((fields.meanRxQueueSize, self.get_meanRxQueueSize()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._maxTxQueueSize = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._maxRxQueueSize = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._meanTxQueueSize = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._meanRxQueueSize = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class CanStatistics_from_Edda_Simulator_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Ground_Controller
        self._message = messages.CanStatistics
        self._category = categories.none
        self._id = 149
        self._size = 8
        self._maxTxQueueSize = 0
        self._maxRxQueueSize = 0
        self._meanTxQueueSize = 0
        self._meanRxQueueSize = 0
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
    def set_maxTxQueueSize(self, value):
        self._maxTxQueueSize = value
    def set_maxRxQueueSize(self, value):
        self._maxRxQueueSize = value
    def set_meanTxQueueSize(self, value):
        self._meanTxQueueSize = value
    def set_meanRxQueueSize(self, value):
        self._meanRxQueueSize = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._maxTxQueueSize)
        buf += struct.pack("<H", self._maxRxQueueSize)
        buf += struct.pack("<H", self._meanTxQueueSize)
        buf += struct.pack("<H", self._meanRxQueueSize)
        return buf
    def get_maxTxQueueSize(self):
        return self._maxTxQueueSize
    def get_maxRxQueueSize(self):
        return self._maxRxQueueSize
    def get_meanTxQueueSize(self):
        return self._meanTxQueueSize
    def get_meanRxQueueSize(self):
        return self._meanRxQueueSize
    def get_all_data(self):
        data = []
        data.append((fields.maxTxQueueSize, self.get_maxTxQueueSize()))
        data.append((fields.maxRxQueueSize, self.get_maxRxQueueSize()))
        data.append((fields.meanTxQueueSize, self.get_meanTxQueueSize()))
        data.append((fields.meanRxQueueSize, self.get_meanRxQueueSize()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._maxTxQueueSize = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._maxRxQueueSize = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._meanTxQueueSize = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._meanRxQueueSize = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class WenHop_from_Edda_Controller_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
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
class WenHop_from_Edda_Telemetry_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
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
class WenHop_from_Edda_Pressure_Top_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
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
class WenHop_from_Edda_Pressure_Bottom_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Flight_Controller
        self._message = messages.WenHop
        self._category = categories.none
        self._id = 153
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
class WenHop_from_Edda_Simulator_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Flight_Controller
        self._message = messages.WenHop
        self._category = categories.none
        self._id = 154
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
class SetDebugModeRequest_from_Flight_Controller_to_Edda_Controller:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Controller
        self._message = messages.SetDebugModeRequest
        self._category = categories.none
        self._id = 48
        self._size = 3
        self._receiver_node_id = 0
        self._messages = 0
        self._statusLeds = 0
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
    def set_receiver_node_id(self, value):
        self._receiver_node_id = value
    def set_messages(self, value):
        self._messages = value.value
    def set_statusLeds(self, value):
        self._statusLeds = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._receiver_node_id)
        buf += struct.pack("<B", self._messages)
        buf += struct.pack("<B", self._statusLeds)
        return buf
    def get_receiver_node_id(self):
        return self._receiver_node_id
    def get_messages(self):
        return DebugMessagesMode(self._messages)
    def get_statusLeds(self):
        return DebugStatusLedsMode(self._statusLeds)
    def get_all_data(self):
        data = []
        data.append((fields.receiver_node_id, self.get_receiver_node_id()))
        data.append((fields.messages, self.get_messages()))
        data.append((fields.statusLeds, self.get_statusLeds()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._receiver_node_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._messages = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._statusLeds = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class SetDebugModeRequest_from_Flight_Controller_to_Edda_Telemetry:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Telemetry
        self._message = messages.SetDebugModeRequest
        self._category = categories.none
        self._id = 48
        self._size = 3
        self._receiver_node_id = 0
        self._messages = 0
        self._statusLeds = 0
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
    def set_receiver_node_id(self, value):
        self._receiver_node_id = value
    def set_messages(self, value):
        self._messages = value.value
    def set_statusLeds(self, value):
        self._statusLeds = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._receiver_node_id)
        buf += struct.pack("<B", self._messages)
        buf += struct.pack("<B", self._statusLeds)
        return buf
    def get_receiver_node_id(self):
        return self._receiver_node_id
    def get_messages(self):
        return DebugMessagesMode(self._messages)
    def get_statusLeds(self):
        return DebugStatusLedsMode(self._statusLeds)
    def get_all_data(self):
        data = []
        data.append((fields.receiver_node_id, self.get_receiver_node_id()))
        data.append((fields.messages, self.get_messages()))
        data.append((fields.statusLeds, self.get_statusLeds()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._receiver_node_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._messages = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._statusLeds = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class SetDebugModeRequest_from_Flight_Controller_to_Edda_Pressure_Top:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Pressure_Top
        self._message = messages.SetDebugModeRequest
        self._category = categories.none
        self._id = 48
        self._size = 3
        self._receiver_node_id = 0
        self._messages = 0
        self._statusLeds = 0
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
    def set_receiver_node_id(self, value):
        self._receiver_node_id = value
    def set_messages(self, value):
        self._messages = value.value
    def set_statusLeds(self, value):
        self._statusLeds = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._receiver_node_id)
        buf += struct.pack("<B", self._messages)
        buf += struct.pack("<B", self._statusLeds)
        return buf
    def get_receiver_node_id(self):
        return self._receiver_node_id
    def get_messages(self):
        return DebugMessagesMode(self._messages)
    def get_statusLeds(self):
        return DebugStatusLedsMode(self._statusLeds)
    def get_all_data(self):
        data = []
        data.append((fields.receiver_node_id, self.get_receiver_node_id()))
        data.append((fields.messages, self.get_messages()))
        data.append((fields.statusLeds, self.get_statusLeds()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._receiver_node_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._messages = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._statusLeds = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class SetDebugModeRequest_from_Flight_Controller_to_Edda_Pressure_Bottom:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Pressure_Bottom
        self._message = messages.SetDebugModeRequest
        self._category = categories.none
        self._id = 48
        self._size = 3
        self._receiver_node_id = 0
        self._messages = 0
        self._statusLeds = 0
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
    def set_receiver_node_id(self, value):
        self._receiver_node_id = value
    def set_messages(self, value):
        self._messages = value.value
    def set_statusLeds(self, value):
        self._statusLeds = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._receiver_node_id)
        buf += struct.pack("<B", self._messages)
        buf += struct.pack("<B", self._statusLeds)
        return buf
    def get_receiver_node_id(self):
        return self._receiver_node_id
    def get_messages(self):
        return DebugMessagesMode(self._messages)
    def get_statusLeds(self):
        return DebugStatusLedsMode(self._statusLeds)
    def get_all_data(self):
        data = []
        data.append((fields.receiver_node_id, self.get_receiver_node_id()))
        data.append((fields.messages, self.get_messages()))
        data.append((fields.statusLeds, self.get_statusLeds()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._receiver_node_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._messages = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._statusLeds = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class SetDebugModeRequest_from_Flight_Controller_to_Edda_Simulator:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Simulator
        self._message = messages.SetDebugModeRequest
        self._category = categories.none
        self._id = 48
        self._size = 3
        self._receiver_node_id = 0
        self._messages = 0
        self._statusLeds = 0
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
    def set_receiver_node_id(self, value):
        self._receiver_node_id = value
    def set_messages(self, value):
        self._messages = value.value
    def set_statusLeds(self, value):
        self._statusLeds = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._receiver_node_id)
        buf += struct.pack("<B", self._messages)
        buf += struct.pack("<B", self._statusLeds)
        return buf
    def get_receiver_node_id(self):
        return self._receiver_node_id
    def get_messages(self):
        return DebugMessagesMode(self._messages)
    def get_statusLeds(self):
        return DebugStatusLedsMode(self._statusLeds)
    def get_all_data(self):
        data = []
        data.append((fields.receiver_node_id, self.get_receiver_node_id()))
        data.append((fields.messages, self.get_messages()))
        data.append((fields.statusLeds, self.get_statusLeds()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._receiver_node_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._messages = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._statusLeds = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class SetPowerModeRequest_from_Flight_Controller_to_Edda_Controller:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Controller
        self._message = messages.SetPowerModeRequest
        self._category = categories.none
        self._id = 49
        self._size = 2
        self._receiver_node_id = 0
        self._mode = 0
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
    def set_receiver_node_id(self, value):
        self._receiver_node_id = value
    def set_mode(self, value):
        self._mode = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._receiver_node_id)
        buf += struct.pack("<B", self._mode)
        return buf
    def get_receiver_node_id(self):
        return self._receiver_node_id
    def get_mode(self):
        return PowerMode(self._mode)
    def get_all_data(self):
        data = []
        data.append((fields.receiver_node_id, self.get_receiver_node_id()))
        data.append((fields.mode, self.get_mode()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._receiver_node_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._mode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class SetPowerModeRequest_from_Flight_Controller_to_Edda_Telemetry:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Telemetry
        self._message = messages.SetPowerModeRequest
        self._category = categories.none
        self._id = 49
        self._size = 2
        self._receiver_node_id = 0
        self._mode = 0
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
    def set_receiver_node_id(self, value):
        self._receiver_node_id = value
    def set_mode(self, value):
        self._mode = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._receiver_node_id)
        buf += struct.pack("<B", self._mode)
        return buf
    def get_receiver_node_id(self):
        return self._receiver_node_id
    def get_mode(self):
        return PowerMode(self._mode)
    def get_all_data(self):
        data = []
        data.append((fields.receiver_node_id, self.get_receiver_node_id()))
        data.append((fields.mode, self.get_mode()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._receiver_node_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._mode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class SetPowerModeRequest_from_Flight_Controller_to_Edda_Pressure_Top:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Pressure_Top
        self._message = messages.SetPowerModeRequest
        self._category = categories.none
        self._id = 49
        self._size = 2
        self._receiver_node_id = 0
        self._mode = 0
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
    def set_receiver_node_id(self, value):
        self._receiver_node_id = value
    def set_mode(self, value):
        self._mode = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._receiver_node_id)
        buf += struct.pack("<B", self._mode)
        return buf
    def get_receiver_node_id(self):
        return self._receiver_node_id
    def get_mode(self):
        return PowerMode(self._mode)
    def get_all_data(self):
        data = []
        data.append((fields.receiver_node_id, self.get_receiver_node_id()))
        data.append((fields.mode, self.get_mode()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._receiver_node_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._mode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class SetPowerModeRequest_from_Flight_Controller_to_Edda_Pressure_Bottom:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Pressure_Bottom
        self._message = messages.SetPowerModeRequest
        self._category = categories.none
        self._id = 49
        self._size = 2
        self._receiver_node_id = 0
        self._mode = 0
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
    def set_receiver_node_id(self, value):
        self._receiver_node_id = value
    def set_mode(self, value):
        self._mode = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._receiver_node_id)
        buf += struct.pack("<B", self._mode)
        return buf
    def get_receiver_node_id(self):
        return self._receiver_node_id
    def get_mode(self):
        return PowerMode(self._mode)
    def get_all_data(self):
        data = []
        data.append((fields.receiver_node_id, self.get_receiver_node_id()))
        data.append((fields.mode, self.get_mode()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._receiver_node_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._mode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class SetPowerModeRequest_from_Flight_Controller_to_Edda_Simulator:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Simulator
        self._message = messages.SetPowerModeRequest
        self._category = categories.none
        self._id = 49
        self._size = 2
        self._receiver_node_id = 0
        self._mode = 0
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
    def set_receiver_node_id(self, value):
        self._receiver_node_id = value
    def set_mode(self, value):
        self._mode = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._receiver_node_id)
        buf += struct.pack("<B", self._mode)
        return buf
    def get_receiver_node_id(self):
        return self._receiver_node_id
    def get_mode(self):
        return PowerMode(self._mode)
    def get_all_data(self):
        data = []
        data.append((fields.receiver_node_id, self.get_receiver_node_id()))
        data.append((fields.mode, self.get_mode()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._receiver_node_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._mode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class GoingToSleep_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.GoingToSleep
        self._category = categories.none
        self._id = 64
        self._size = 4
        self._timeSpentAwake_ms = 0
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
    def set_timeSpentAwake_ms(self, value):
        self._timeSpentAwake_ms = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._timeSpentAwake_ms)
        return buf
    def get_timeSpentAwake_ms(self):
        return self._timeSpentAwake_ms
    def get_all_data(self):
        data = []
        data.append((fields.timeSpentAwake_ms, self.get_timeSpentAwake_ms()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._timeSpentAwake_ms = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class GoingToSleep_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.GoingToSleep
        self._category = categories.none
        self._id = 65
        self._size = 4
        self._timeSpentAwake_ms = 0
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
    def set_timeSpentAwake_ms(self, value):
        self._timeSpentAwake_ms = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._timeSpentAwake_ms)
        return buf
    def get_timeSpentAwake_ms(self):
        return self._timeSpentAwake_ms
    def get_all_data(self):
        data = []
        data.append((fields.timeSpentAwake_ms, self.get_timeSpentAwake_ms()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._timeSpentAwake_ms = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class GoingToSleep_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.GoingToSleep
        self._category = categories.none
        self._id = 66
        self._size = 4
        self._timeSpentAwake_ms = 0
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
    def set_timeSpentAwake_ms(self, value):
        self._timeSpentAwake_ms = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._timeSpentAwake_ms)
        return buf
    def get_timeSpentAwake_ms(self):
        return self._timeSpentAwake_ms
    def get_all_data(self):
        data = []
        data.append((fields.timeSpentAwake_ms, self.get_timeSpentAwake_ms()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._timeSpentAwake_ms = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class GoingToSleep_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.GoingToSleep
        self._category = categories.none
        self._id = 67
        self._size = 4
        self._timeSpentAwake_ms = 0
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
    def set_timeSpentAwake_ms(self, value):
        self._timeSpentAwake_ms = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._timeSpentAwake_ms)
        return buf
    def get_timeSpentAwake_ms(self):
        return self._timeSpentAwake_ms
    def get_all_data(self):
        data = []
        data.append((fields.timeSpentAwake_ms, self.get_timeSpentAwake_ms()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._timeSpentAwake_ms = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class GoingToSleep_from_Edda_Simulator_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Ground_Controller
        self._message = messages.GoingToSleep
        self._category = categories.none
        self._id = 68
        self._size = 4
        self._timeSpentAwake_ms = 0
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
    def set_timeSpentAwake_ms(self, value):
        self._timeSpentAwake_ms = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._timeSpentAwake_ms)
        return buf
    def get_timeSpentAwake_ms(self):
        return self._timeSpentAwake_ms
    def get_all_data(self):
        data = []
        data.append((fields.timeSpentAwake_ms, self.get_timeSpentAwake_ms()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._timeSpentAwake_ms = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class WokeUp_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.WokeUp
        self._category = categories.none
        self._id = 69
        self._size = 4
        self._timeSpentSleeping_us = 0
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
    def set_timeSpentSleeping_us(self, value):
        self._timeSpentSleeping_us = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._timeSpentSleeping_us)
        return buf
    def get_timeSpentSleeping_us(self):
        return self._timeSpentSleeping_us
    def get_all_data(self):
        data = []
        data.append((fields.timeSpentSleeping_us, self.get_timeSpentSleeping_us()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._timeSpentSleeping_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class WokeUp_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.WokeUp
        self._category = categories.none
        self._id = 70
        self._size = 4
        self._timeSpentSleeping_us = 0
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
    def set_timeSpentSleeping_us(self, value):
        self._timeSpentSleeping_us = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._timeSpentSleeping_us)
        return buf
    def get_timeSpentSleeping_us(self):
        return self._timeSpentSleeping_us
    def get_all_data(self):
        data = []
        data.append((fields.timeSpentSleeping_us, self.get_timeSpentSleeping_us()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._timeSpentSleeping_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class WokeUp_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.WokeUp
        self._category = categories.none
        self._id = 71
        self._size = 4
        self._timeSpentSleeping_us = 0
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
    def set_timeSpentSleeping_us(self, value):
        self._timeSpentSleeping_us = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._timeSpentSleeping_us)
        return buf
    def get_timeSpentSleeping_us(self):
        return self._timeSpentSleeping_us
    def get_all_data(self):
        data = []
        data.append((fields.timeSpentSleeping_us, self.get_timeSpentSleeping_us()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._timeSpentSleeping_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class WokeUp_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.WokeUp
        self._category = categories.none
        self._id = 72
        self._size = 4
        self._timeSpentSleeping_us = 0
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
    def set_timeSpentSleeping_us(self, value):
        self._timeSpentSleeping_us = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._timeSpentSleeping_us)
        return buf
    def get_timeSpentSleeping_us(self):
        return self._timeSpentSleeping_us
    def get_all_data(self):
        data = []
        data.append((fields.timeSpentSleeping_us, self.get_timeSpentSleeping_us()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._timeSpentSleeping_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class WokeUp_from_Edda_Simulator_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Ground_Controller
        self._message = messages.WokeUp
        self._category = categories.none
        self._id = 73
        self._size = 4
        self._timeSpentSleeping_us = 0
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
    def set_timeSpentSleeping_us(self, value):
        self._timeSpentSleeping_us = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._timeSpentSleeping_us)
        return buf
    def get_timeSpentSleeping_us(self):
        return self._timeSpentSleeping_us
    def get_all_data(self):
        data = []
        data.append((fields.timeSpentSleeping_us, self.get_timeSpentSleeping_us()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._timeSpentSleeping_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class RequestReset_from_Ground_Controller_to_Edda_Controller:
    def __init__(self):
        self._sender = nodes.Ground_Controller
        self._receiver = nodes.Edda_Controller
        self._message = messages.RequestReset
        self._category = categories.none
        self._id = 50
        self._size = 1
        self._receiver_node_id = 0
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
    def set_receiver_node_id(self, value):
        self._receiver_node_id = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._receiver_node_id)
        return buf
    def get_receiver_node_id(self):
        return self._receiver_node_id
    def get_all_data(self):
        data = []
        data.append((fields.receiver_node_id, self.get_receiver_node_id()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._receiver_node_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class RequestReset_from_Ground_Controller_to_Edda_Telemetry:
    def __init__(self):
        self._sender = nodes.Ground_Controller
        self._receiver = nodes.Edda_Telemetry
        self._message = messages.RequestReset
        self._category = categories.none
        self._id = 50
        self._size = 1
        self._receiver_node_id = 0
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
    def set_receiver_node_id(self, value):
        self._receiver_node_id = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._receiver_node_id)
        return buf
    def get_receiver_node_id(self):
        return self._receiver_node_id
    def get_all_data(self):
        data = []
        data.append((fields.receiver_node_id, self.get_receiver_node_id()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._receiver_node_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class RequestReset_from_Ground_Controller_to_Edda_Pressure_Top:
    def __init__(self):
        self._sender = nodes.Ground_Controller
        self._receiver = nodes.Edda_Pressure_Top
        self._message = messages.RequestReset
        self._category = categories.none
        self._id = 50
        self._size = 1
        self._receiver_node_id = 0
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
    def set_receiver_node_id(self, value):
        self._receiver_node_id = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._receiver_node_id)
        return buf
    def get_receiver_node_id(self):
        return self._receiver_node_id
    def get_all_data(self):
        data = []
        data.append((fields.receiver_node_id, self.get_receiver_node_id()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._receiver_node_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class RequestReset_from_Ground_Controller_to_Edda_Pressure_Bottom:
    def __init__(self):
        self._sender = nodes.Ground_Controller
        self._receiver = nodes.Edda_Pressure_Bottom
        self._message = messages.RequestReset
        self._category = categories.none
        self._id = 50
        self._size = 1
        self._receiver_node_id = 0
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
    def set_receiver_node_id(self, value):
        self._receiver_node_id = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._receiver_node_id)
        return buf
    def get_receiver_node_id(self):
        return self._receiver_node_id
    def get_all_data(self):
        data = []
        data.append((fields.receiver_node_id, self.get_receiver_node_id()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._receiver_node_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class RequestReset_from_Ground_Controller_to_Edda_Simulator:
    def __init__(self):
        self._sender = nodes.Ground_Controller
        self._receiver = nodes.Edda_Simulator
        self._message = messages.RequestReset
        self._category = categories.none
        self._id = 50
        self._size = 1
        self._receiver_node_id = 0
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
    def set_receiver_node_id(self, value):
        self._receiver_node_id = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._receiver_node_id)
        return buf
    def get_receiver_node_id(self):
        return self._receiver_node_id
    def get_all_data(self):
        data = []
        data.append((fields.receiver_node_id, self.get_receiver_node_id()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._receiver_node_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerInputMeasurement_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerInputMeasurement
        self._category = categories.none
        self._id = 155
        self._size = 6
        self._current_amperes = 0
        self._voltage_volts = 0
        self._power_watts = 0
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
    def set_current_amperes(self, value):
        self._current_amperes = packedFloat_to_uint(value, -15, 15, 2)
    def set_voltage_volts(self, value):
        self._voltage_volts = packedFloat_to_uint(value, 0, 36, 2)
    def set_power_watts(self, value):
        self._power_watts = packedFloat_to_uint(value, -540, 540, 2)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._current_amperes)
        buf += struct.pack("<H", self._voltage_volts)
        buf += struct.pack("<H", self._power_watts)
        return buf
    def get_current_amperes(self):
        return uint_to_scaledFloat(self._current_amperes, -15, 15, 2)
    def get_voltage_volts(self):
        return uint_to_scaledFloat(self._voltage_volts, 0, 36, 2)
    def get_power_watts(self):
        return uint_to_scaledFloat(self._power_watts, -540, 540, 2)
    def get_all_data(self):
        data = []
        data.append((fields.current_amperes, self.get_current_amperes()))
        data.append((fields.voltage_volts, self.get_voltage_volts()))
        data.append((fields.power_watts, self.get_power_watts()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._current_amperes = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._voltage_volts = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._power_watts = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class PowerInputMeasurement_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerInputMeasurement
        self._category = categories.none
        self._id = 156
        self._size = 6
        self._current_amperes = 0
        self._voltage_volts = 0
        self._power_watts = 0
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
    def set_current_amperes(self, value):
        self._current_amperes = packedFloat_to_uint(value, -15, 15, 2)
    def set_voltage_volts(self, value):
        self._voltage_volts = packedFloat_to_uint(value, 0, 36, 2)
    def set_power_watts(self, value):
        self._power_watts = packedFloat_to_uint(value, -540, 540, 2)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._current_amperes)
        buf += struct.pack("<H", self._voltage_volts)
        buf += struct.pack("<H", self._power_watts)
        return buf
    def get_current_amperes(self):
        return uint_to_scaledFloat(self._current_amperes, -15, 15, 2)
    def get_voltage_volts(self):
        return uint_to_scaledFloat(self._voltage_volts, 0, 36, 2)
    def get_power_watts(self):
        return uint_to_scaledFloat(self._power_watts, -540, 540, 2)
    def get_all_data(self):
        data = []
        data.append((fields.current_amperes, self.get_current_amperes()))
        data.append((fields.voltage_volts, self.get_voltage_volts()))
        data.append((fields.power_watts, self.get_power_watts()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._current_amperes = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._voltage_volts = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._power_watts = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class PowerInputMeasurement_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerInputMeasurement
        self._category = categories.none
        self._id = 157
        self._size = 6
        self._current_amperes = 0
        self._voltage_volts = 0
        self._power_watts = 0
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
    def set_current_amperes(self, value):
        self._current_amperes = packedFloat_to_uint(value, -15, 15, 2)
    def set_voltage_volts(self, value):
        self._voltage_volts = packedFloat_to_uint(value, 0, 36, 2)
    def set_power_watts(self, value):
        self._power_watts = packedFloat_to_uint(value, -540, 540, 2)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._current_amperes)
        buf += struct.pack("<H", self._voltage_volts)
        buf += struct.pack("<H", self._power_watts)
        return buf
    def get_current_amperes(self):
        return uint_to_scaledFloat(self._current_amperes, -15, 15, 2)
    def get_voltage_volts(self):
        return uint_to_scaledFloat(self._voltage_volts, 0, 36, 2)
    def get_power_watts(self):
        return uint_to_scaledFloat(self._power_watts, -540, 540, 2)
    def get_all_data(self):
        data = []
        data.append((fields.current_amperes, self.get_current_amperes()))
        data.append((fields.voltage_volts, self.get_voltage_volts()))
        data.append((fields.power_watts, self.get_power_watts()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._current_amperes = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._voltage_volts = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._power_watts = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class PowerInputMeasurement_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerInputMeasurement
        self._category = categories.none
        self._id = 158
        self._size = 6
        self._current_amperes = 0
        self._voltage_volts = 0
        self._power_watts = 0
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
    def set_current_amperes(self, value):
        self._current_amperes = packedFloat_to_uint(value, -15, 15, 2)
    def set_voltage_volts(self, value):
        self._voltage_volts = packedFloat_to_uint(value, 0, 36, 2)
    def set_power_watts(self, value):
        self._power_watts = packedFloat_to_uint(value, -540, 540, 2)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._current_amperes)
        buf += struct.pack("<H", self._voltage_volts)
        buf += struct.pack("<H", self._power_watts)
        return buf
    def get_current_amperes(self):
        return uint_to_scaledFloat(self._current_amperes, -15, 15, 2)
    def get_voltage_volts(self):
        return uint_to_scaledFloat(self._voltage_volts, 0, 36, 2)
    def get_power_watts(self):
        return uint_to_scaledFloat(self._power_watts, -540, 540, 2)
    def get_all_data(self):
        data = []
        data.append((fields.current_amperes, self.get_current_amperes()))
        data.append((fields.voltage_volts, self.get_voltage_volts()))
        data.append((fields.power_watts, self.get_power_watts()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._current_amperes = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._voltage_volts = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._power_watts = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class PowerInputMeasurement_from_Edda_Simulator_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerInputMeasurement
        self._category = categories.none
        self._id = 159
        self._size = 6
        self._current_amperes = 0
        self._voltage_volts = 0
        self._power_watts = 0
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
    def set_current_amperes(self, value):
        self._current_amperes = packedFloat_to_uint(value, -15, 15, 2)
    def set_voltage_volts(self, value):
        self._voltage_volts = packedFloat_to_uint(value, 0, 36, 2)
    def set_power_watts(self, value):
        self._power_watts = packedFloat_to_uint(value, -540, 540, 2)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._current_amperes)
        buf += struct.pack("<H", self._voltage_volts)
        buf += struct.pack("<H", self._power_watts)
        return buf
    def get_current_amperes(self):
        return uint_to_scaledFloat(self._current_amperes, -15, 15, 2)
    def get_voltage_volts(self):
        return uint_to_scaledFloat(self._voltage_volts, 0, 36, 2)
    def get_power_watts(self):
        return uint_to_scaledFloat(self._power_watts, -540, 540, 2)
    def get_all_data(self):
        data = []
        data.append((fields.current_amperes, self.get_current_amperes()))
        data.append((fields.voltage_volts, self.get_voltage_volts()))
        data.append((fields.power_watts, self.get_power_watts()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._current_amperes = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._voltage_volts = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._power_watts = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class PowerInputMeasurementError_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerInputMeasurementError
        self._category = categories.none
        self._id = 160
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
        return PowerInputMeasurementError(self._error)
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
        return PowerInputMeasurementError(self._error)
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
        return PowerInputMeasurementError(self._error)
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
        return PowerInputMeasurementError(self._error)
    def get_all_data(self):
        data = []
        data.append((fields.error, self.get_error()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerInputMeasurementError_from_Edda_Simulator_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
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
        return PowerInputMeasurementError(self._error)
    def get_all_data(self):
        data = []
        data.append((fields.error, self.get_error()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class RawTransducerVoltage_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.RawTransducerVoltage
        self._category = categories.none
        self._id = 165
        self._size = 5
        self._sensor_index = 0
        self._voltage_volts = 0
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
        self._sensor_index = value
    def set_voltage_volts(self, value):
        self._voltage_volts = packedFloat_to_uint(value, 0, 5, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._voltage_volts)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_voltage_volts(self):
        return uint_to_scaledFloat(self._voltage_volts, 0, 5, 4)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.voltage_volts, self.get_voltage_volts()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._voltage_volts = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class RawTransducerVoltage_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.RawTransducerVoltage
        self._category = categories.none
        self._id = 166
        self._size = 5
        self._sensor_index = 0
        self._voltage_volts = 0
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
        self._sensor_index = value
    def set_voltage_volts(self, value):
        self._voltage_volts = packedFloat_to_uint(value, 0, 5, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._voltage_volts)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_voltage_volts(self):
        return uint_to_scaledFloat(self._voltage_volts, 0, 5, 4)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.voltage_volts, self.get_voltage_volts()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._voltage_volts = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class TransducerPressure_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.TransducerPressure
        self._category = categories.none
        self._id = 167
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
        self._sensor_index = value
    def set_pressure_pascal(self, value):
        self._pressure_pascal = packedFloat_to_uint(value, 0, 10000000, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._pressure_pascal)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_pressure_pascal(self):
        return uint_to_scaledFloat(self._pressure_pascal, 0, 10000000, 4)
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
class TransducerPressure_from_Edda_Pressure_Top_to_Edda_Telemetry:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Edda_Telemetry
        self._message = messages.TransducerPressure
        self._category = categories.none
        self._id = 167
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
        self._sensor_index = value
    def set_pressure_pascal(self, value):
        self._pressure_pascal = packedFloat_to_uint(value, 0, 10000000, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._pressure_pascal)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_pressure_pascal(self):
        return uint_to_scaledFloat(self._pressure_pascal, 0, 10000000, 4)
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
        self._id = 168
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
        self._sensor_index = value
    def set_pressure_pascal(self, value):
        self._pressure_pascal = packedFloat_to_uint(value, 0, 10000000, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._pressure_pascal)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_pressure_pascal(self):
        return uint_to_scaledFloat(self._pressure_pascal, 0, 10000000, 4)
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
class TransducerPressure_from_Edda_Pressure_Bottom_to_Edda_Telemetry:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Edda_Telemetry
        self._message = messages.TransducerPressure
        self._category = categories.none
        self._id = 168
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
        self._sensor_index = value
    def set_pressure_pascal(self, value):
        self._pressure_pascal = packedFloat_to_uint(value, 0, 10000000, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._pressure_pascal)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_pressure_pascal(self):
        return uint_to_scaledFloat(self._pressure_pascal, 0, 10000000, 4)
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
class TransducerPressure_from_Edda_Simulator_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Ground_Controller
        self._message = messages.TransducerPressure
        self._category = categories.none
        self._id = 169
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
        self._sensor_index = value
    def set_pressure_pascal(self, value):
        self._pressure_pascal = packedFloat_to_uint(value, 0, 10000000, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._pressure_pascal)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_pressure_pascal(self):
        return uint_to_scaledFloat(self._pressure_pascal, 0, 10000000, 4)
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
class TransducerPressure_from_Edda_Simulator_to_Edda_Telemetry:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Edda_Telemetry
        self._message = messages.TransducerPressure
        self._category = categories.none
        self._id = 169
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
        self._sensor_index = value
    def set_pressure_pascal(self, value):
        self._pressure_pascal = packedFloat_to_uint(value, 0, 10000000, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._pressure_pascal)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_pressure_pascal(self):
        return uint_to_scaledFloat(self._pressure_pascal, 0, 10000000, 4)
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
class AmbientPressure_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.AmbientPressure
        self._category = categories.none
        self._id = 170
        self._size = 5
        self._sensor_index = 0
        self._pressure_millibars = 0
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
        self._sensor_index = value
    def set_pressure_millibars(self, value):
        self._pressure_millibars = packedFloat_to_uint(value, 0, 10000, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._pressure_millibars)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_pressure_millibars(self):
        return uint_to_scaledFloat(self._pressure_millibars, 0, 10000, 4)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.pressure_millibars, self.get_pressure_millibars()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._pressure_millibars = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class AmbientPressure_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.AmbientPressure
        self._category = categories.none
        self._id = 171
        self._size = 5
        self._sensor_index = 0
        self._pressure_millibars = 0
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
        self._sensor_index = value
    def set_pressure_millibars(self, value):
        self._pressure_millibars = packedFloat_to_uint(value, 0, 10000, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._pressure_millibars)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_pressure_millibars(self):
        return uint_to_scaledFloat(self._pressure_millibars, 0, 10000, 4)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.pressure_millibars, self.get_pressure_millibars()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._pressure_millibars = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class AmbientPressure_from_Edda_Simulator_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Ground_Controller
        self._message = messages.AmbientPressure
        self._category = categories.none
        self._id = 172
        self._size = 5
        self._sensor_index = 0
        self._pressure_millibars = 0
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
        self._sensor_index = value
    def set_pressure_millibars(self, value):
        self._pressure_millibars = packedFloat_to_uint(value, 0, 10000, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._pressure_millibars)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_pressure_millibars(self):
        return uint_to_scaledFloat(self._pressure_millibars, 0, 10000, 4)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.pressure_millibars, self.get_pressure_millibars()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._pressure_millibars = struct.unpack_from("<L", buf, index)[0]
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
        self._sensor_index = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_error(self, value):
        self._error = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<B", self._error)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_error(self):
        return TransducerError(self._error)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.error, self.get_error()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
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
        self._sensor_index = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_error(self, value):
        self._error = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<B", self._error)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_error(self):
        return TransducerError(self._error)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.error, self.get_error()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class AmbientPressureError_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.AmbientPressureError
        self._category = categories.none
        self._id = 175
        self._size = 2
        self._sensor_index = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_error(self, value):
        self._error = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<B", self._error)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_error(self):
        return AmbientPressureError(self._error)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.error, self.get_error()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class AmbientPressureError_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.AmbientPressureError
        self._category = categories.none
        self._id = 176
        self._size = 2
        self._sensor_index = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_error(self, value):
        self._error = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<B", self._error)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_error(self):
        return AmbientPressureError(self._error)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.error, self.get_error()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class AmbientPressureCoefficient_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.AmbientPressureCoefficient
        self._category = categories.none
        self._id = 177
        self._size = 4
        self._sensor_index = 0
        self._coefficient_index = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_coefficient_index(self, value):
        self._coefficient_index = value
    def set_coefficient_value(self, value):
        self._coefficient_value = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<B", self._coefficient_index)
        buf += struct.pack("<H", self._coefficient_value)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_coefficient_index(self):
        return self._coefficient_index
    def get_coefficient_value(self):
        return self._coefficient_value
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.coefficient_index, self.get_coefficient_index()))
        data.append((fields.coefficient_value, self.get_coefficient_value()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._coefficient_index = struct.unpack_from("<B", buf, index)[0]
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
        self._size = 4
        self._sensor_index = 0
        self._coefficient_index = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_coefficient_index(self, value):
        self._coefficient_index = value
    def set_coefficient_value(self, value):
        self._coefficient_value = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<B", self._coefficient_index)
        buf += struct.pack("<H", self._coefficient_value)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_coefficient_index(self):
        return self._coefficient_index
    def get_coefficient_value(self):
        return self._coefficient_value
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.coefficient_index, self.get_coefficient_index()))
        data.append((fields.coefficient_value, self.get_coefficient_value()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._coefficient_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._coefficient_value = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class ColdSideTemperature_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.ColdSideTemperature
        self._category = categories.none
        self._id = 179
        self._size = 6
        self._sensor_type = 0
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
    def set_sensor_type(self, value):
        self._sensor_type = value.value
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_temperature_celsius(self, value):
        self._temperature_celsius = packedFloat_to_uint(value, -55, 125, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_type)
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._temperature_celsius)
        return buf
    def get_sensor_type(self):
        return ColdSideTemperatureSensorType(self._sensor_type)
    def get_sensor_index(self):
        return self._sensor_index
    def get_temperature_celsius(self):
        return uint_to_scaledFloat(self._temperature_celsius, -55, 125, 4)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_type, self.get_sensor_type()))
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.temperature_celsius, self.get_temperature_celsius()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_type = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._temperature_celsius = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class ColdSideTemperature_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.ColdSideTemperature
        self._category = categories.none
        self._id = 180
        self._size = 6
        self._sensor_type = 0
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
    def set_sensor_type(self, value):
        self._sensor_type = value.value
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_temperature_celsius(self, value):
        self._temperature_celsius = packedFloat_to_uint(value, -55, 125, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_type)
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._temperature_celsius)
        return buf
    def get_sensor_type(self):
        return ColdSideTemperatureSensorType(self._sensor_type)
    def get_sensor_index(self):
        return self._sensor_index
    def get_temperature_celsius(self):
        return uint_to_scaledFloat(self._temperature_celsius, -55, 125, 4)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_type, self.get_sensor_type()))
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.temperature_celsius, self.get_temperature_celsius()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_type = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._temperature_celsius = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class ColdSideTemperature_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.ColdSideTemperature
        self._category = categories.none
        self._id = 181
        self._size = 6
        self._sensor_type = 0
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
    def set_sensor_type(self, value):
        self._sensor_type = value.value
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_temperature_celsius(self, value):
        self._temperature_celsius = packedFloat_to_uint(value, -55, 125, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_type)
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._temperature_celsius)
        return buf
    def get_sensor_type(self):
        return ColdSideTemperatureSensorType(self._sensor_type)
    def get_sensor_index(self):
        return self._sensor_index
    def get_temperature_celsius(self):
        return uint_to_scaledFloat(self._temperature_celsius, -55, 125, 4)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_type, self.get_sensor_type()))
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.temperature_celsius, self.get_temperature_celsius()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_type = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._temperature_celsius = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class ColdSideTemperature_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.ColdSideTemperature
        self._category = categories.none
        self._id = 182
        self._size = 6
        self._sensor_type = 0
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
    def set_sensor_type(self, value):
        self._sensor_type = value.value
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_temperature_celsius(self, value):
        self._temperature_celsius = packedFloat_to_uint(value, -55, 125, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_type)
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._temperature_celsius)
        return buf
    def get_sensor_type(self):
        return ColdSideTemperatureSensorType(self._sensor_type)
    def get_sensor_index(self):
        return self._sensor_index
    def get_temperature_celsius(self):
        return uint_to_scaledFloat(self._temperature_celsius, -55, 125, 4)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_type, self.get_sensor_type()))
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.temperature_celsius, self.get_temperature_celsius()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_type = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._temperature_celsius = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class PlatinumSensorTemperature_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.PlatinumSensorTemperature
        self._category = categories.none
        self._id = 183
        self._size = 5
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
        self._sensor_index = value
    def set_temperature_celsius(self, value):
        self._temperature_celsius = packedFloat_to_uint(value, -200, 850, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._temperature_celsius)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_temperature_celsius(self):
        return uint_to_scaledFloat(self._temperature_celsius, -200, 850, 4)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.temperature_celsius, self.get_temperature_celsius()))
        return data
    def parse_buf(self, buf):
        index = 0
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
        self._id = 184
        self._size = 5
        self._sensor_index = 0
        self._resistance_ohms = 0
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
        self._sensor_index = value
    def set_resistance_ohms(self, value):
        self._resistance_ohms = packedFloat_to_uint(value, 0, 5000, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._resistance_ohms)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_resistance_ohms(self):
        return uint_to_scaledFloat(self._resistance_ohms, 0, 5000, 4)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.resistance_ohms, self.get_resistance_ohms()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._resistance_ohms = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class PlatinumSensorRatio_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.PlatinumSensorRatio
        self._category = categories.none
        self._id = 185
        self._size = 5
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
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_ratio_fraction(self, value):
        self._ratio_fraction = packedFloat_to_uint(value, 0, 1, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._ratio_fraction)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_ratio_fraction(self):
        return uint_to_scaledFloat(self._ratio_fraction, 0, 1, 4)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.ratio_fraction, self.get_ratio_fraction()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._ratio_fraction = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class OneWireBusError_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.OneWireBusError
        self._category = categories.none
        self._id = 186
        self._size = 2
        self._bus_index = 0
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
    def set_bus_index(self, value):
        self._bus_index = value
    def set_error(self, value):
        self._error = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus_index)
        buf += struct.pack("<B", self._error)
        return buf
    def get_bus_index(self):
        return self._bus_index
    def get_error(self):
        return OneWireBusError(self._error)
    def get_all_data(self):
        data = []
        data.append((fields.bus_index, self.get_bus_index()))
        data.append((fields.error, self.get_error()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class ThermocoupleTypeKTemperature_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.ThermocoupleTypeKTemperature
        self._category = categories.none
        self._id = 187
        self._size = 5
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
        self._sensor_index = value
    def set_temperature_celsius(self, value):
        self._temperature_celsius = packedFloat_to_uint(value, -200, 1350, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._temperature_celsius)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_temperature_celsius(self):
        return uint_to_scaledFloat(self._temperature_celsius, -200, 1350, 4)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.temperature_celsius, self.get_temperature_celsius()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._temperature_celsius = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class ThermocoupleTypeKTemperature_from_Edda_Simulator_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Ground_Controller
        self._message = messages.ThermocoupleTypeKTemperature
        self._category = categories.none
        self._id = 188
        self._size = 5
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
        self._sensor_index = value
    def set_temperature_celsius(self, value):
        self._temperature_celsius = packedFloat_to_uint(value, -200, 1350, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._temperature_celsius)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_temperature_celsius(self):
        return uint_to_scaledFloat(self._temperature_celsius, -200, 1350, 4)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.temperature_celsius, self.get_temperature_celsius()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._temperature_celsius = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class SensorMeasurementInfo_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.SensorMeasurementInfo
        self._category = categories.none
        self._id = 189
        self._size = 6
        self._type = 0
        self._sensor_index = 0
        self._timeForMeasurement_microseconds = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_timeForMeasurement_microseconds(self, value):
        self._timeForMeasurement_microseconds = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._type)
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._timeForMeasurement_microseconds)
        return buf
    def get_type(self):
        return SensorMeasurementInfo(self._type)
    def get_sensor_index(self):
        return self._sensor_index
    def get_timeForMeasurement_microseconds(self):
        return self._timeForMeasurement_microseconds
    def get_all_data(self):
        data = []
        data.append((fields.type, self.get_type()))
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.timeForMeasurement_microseconds, self.get_timeForMeasurement_microseconds()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._type = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._timeForMeasurement_microseconds = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class SensorMeasurementInfo_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.SensorMeasurementInfo
        self._category = categories.none
        self._id = 190
        self._size = 6
        self._type = 0
        self._sensor_index = 0
        self._timeForMeasurement_microseconds = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_timeForMeasurement_microseconds(self, value):
        self._timeForMeasurement_microseconds = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._type)
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._timeForMeasurement_microseconds)
        return buf
    def get_type(self):
        return SensorMeasurementInfo(self._type)
    def get_sensor_index(self):
        return self._sensor_index
    def get_timeForMeasurement_microseconds(self):
        return self._timeForMeasurement_microseconds
    def get_all_data(self):
        data = []
        data.append((fields.type, self.get_type()))
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.timeForMeasurement_microseconds, self.get_timeForMeasurement_microseconds()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._type = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._timeForMeasurement_microseconds = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class SensorMeasurementInfo_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.SensorMeasurementInfo
        self._category = categories.none
        self._id = 191
        self._size = 6
        self._type = 0
        self._sensor_index = 0
        self._timeForMeasurement_microseconds = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_timeForMeasurement_microseconds(self, value):
        self._timeForMeasurement_microseconds = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._type)
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._timeForMeasurement_microseconds)
        return buf
    def get_type(self):
        return SensorMeasurementInfo(self._type)
    def get_sensor_index(self):
        return self._sensor_index
    def get_timeForMeasurement_microseconds(self):
        return self._timeForMeasurement_microseconds
    def get_all_data(self):
        data = []
        data.append((fields.type, self.get_type()))
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.timeForMeasurement_microseconds, self.get_timeForMeasurement_microseconds()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._type = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._timeForMeasurement_microseconds = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class SensorMeasurementInfo_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.SensorMeasurementInfo
        self._category = categories.none
        self._id = 192
        self._size = 6
        self._type = 0
        self._sensor_index = 0
        self._timeForMeasurement_microseconds = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_timeForMeasurement_microseconds(self, value):
        self._timeForMeasurement_microseconds = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._type)
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._timeForMeasurement_microseconds)
        return buf
    def get_type(self):
        return SensorMeasurementInfo(self._type)
    def get_sensor_index(self):
        return self._sensor_index
    def get_timeForMeasurement_microseconds(self):
        return self._timeForMeasurement_microseconds
    def get_all_data(self):
        data = []
        data.append((fields.type, self.get_type()))
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.timeForMeasurement_microseconds, self.get_timeForMeasurement_microseconds()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._type = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._timeForMeasurement_microseconds = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class DS28E18QTransactionError_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.DS28E18QTransactionError
        self._category = categories.none
        self._id = 193
        self._size = 6
        self._chip_index = 0
        self._truncated_serial = 0
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
    def set_chip_index(self, value):
        self._chip_index = value
    def set_truncated_serial(self, value):
        self._truncated_serial = value
    def set_error(self, value):
        self._error = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._chip_index)
        buf += struct.pack("<L", self._truncated_serial)
        buf += struct.pack("<B", self._error)
        return buf
    def get_chip_index(self):
        return self._chip_index
    def get_truncated_serial(self):
        return self._truncated_serial
    def get_error(self):
        return DS28E18QTransactionError(self._error)
    def get_all_data(self):
        data = []
        data.append((fields.chip_index, self.get_chip_index()))
        data.append((fields.truncated_serial, self.get_truncated_serial()))
        data.append((fields.error, self.get_error()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._chip_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._truncated_serial = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class DS28E18QTransactionError_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.DS28E18QTransactionError
        self._category = categories.none
        self._id = 194
        self._size = 6
        self._chip_index = 0
        self._truncated_serial = 0
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
    def set_chip_index(self, value):
        self._chip_index = value
    def set_truncated_serial(self, value):
        self._truncated_serial = value
    def set_error(self, value):
        self._error = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._chip_index)
        buf += struct.pack("<L", self._truncated_serial)
        buf += struct.pack("<B", self._error)
        return buf
    def get_chip_index(self):
        return self._chip_index
    def get_truncated_serial(self):
        return self._truncated_serial
    def get_error(self):
        return DS28E18QTransactionError(self._error)
    def get_all_data(self):
        data = []
        data.append((fields.chip_index, self.get_chip_index()))
        data.append((fields.truncated_serial, self.get_truncated_serial()))
        data.append((fields.error, self.get_error()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._chip_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._truncated_serial = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class DS28E18QTransactionError_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.DS28E18QTransactionError
        self._category = categories.none
        self._id = 195
        self._size = 6
        self._chip_index = 0
        self._truncated_serial = 0
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
    def set_chip_index(self, value):
        self._chip_index = value
    def set_truncated_serial(self, value):
        self._truncated_serial = value
    def set_error(self, value):
        self._error = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._chip_index)
        buf += struct.pack("<L", self._truncated_serial)
        buf += struct.pack("<B", self._error)
        return buf
    def get_chip_index(self):
        return self._chip_index
    def get_truncated_serial(self):
        return self._truncated_serial
    def get_error(self):
        return DS28E18QTransactionError(self._error)
    def get_all_data(self):
        data = []
        data.append((fields.chip_index, self.get_chip_index()))
        data.append((fields.truncated_serial, self.get_truncated_serial()))
        data.append((fields.error, self.get_error()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._chip_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._truncated_serial = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class DS28E18QTransactionError_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.DS28E18QTransactionError
        self._category = categories.none
        self._id = 196
        self._size = 6
        self._chip_index = 0
        self._truncated_serial = 0
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
    def set_chip_index(self, value):
        self._chip_index = value
    def set_truncated_serial(self, value):
        self._truncated_serial = value
    def set_error(self, value):
        self._error = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._chip_index)
        buf += struct.pack("<L", self._truncated_serial)
        buf += struct.pack("<B", self._error)
        return buf
    def get_chip_index(self):
        return self._chip_index
    def get_truncated_serial(self):
        return self._truncated_serial
    def get_error(self):
        return DS28E18QTransactionError(self._error)
    def get_all_data(self):
        data = []
        data.append((fields.chip_index, self.get_chip_index()))
        data.append((fields.truncated_serial, self.get_truncated_serial()))
        data.append((fields.error, self.get_error()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._chip_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._truncated_serial = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class CouldNotFindDS28E18Q_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.CouldNotFindDS28E18Q
        self._category = categories.none
        self._id = 197
        self._size = 7
        self._chip_index = 0
        self._family_code = 0
        self._truncated_serial = 0
        self._crc_code = 0
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
    def set_chip_index(self, value):
        self._chip_index = value
    def set_family_code(self, value):
        self._family_code = value
    def set_truncated_serial(self, value):
        self._truncated_serial = value
    def set_crc_code(self, value):
        self._crc_code = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._chip_index)
        buf += struct.pack("<B", self._family_code)
        buf += struct.pack("<L", self._truncated_serial)
        buf += struct.pack("<B", self._crc_code)
        return buf
    def get_chip_index(self):
        return self._chip_index
    def get_family_code(self):
        return self._family_code
    def get_truncated_serial(self):
        return self._truncated_serial
    def get_crc_code(self):
        return self._crc_code
    def get_all_data(self):
        data = []
        data.append((fields.chip_index, self.get_chip_index()))
        data.append((fields.family_code, self.get_family_code()))
        data.append((fields.truncated_serial, self.get_truncated_serial()))
        data.append((fields.crc_code, self.get_crc_code()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._chip_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._family_code = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._truncated_serial = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._crc_code = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class CouldNotFindDS28E18Q_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.CouldNotFindDS28E18Q
        self._category = categories.none
        self._id = 198
        self._size = 7
        self._chip_index = 0
        self._family_code = 0
        self._truncated_serial = 0
        self._crc_code = 0
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
    def set_chip_index(self, value):
        self._chip_index = value
    def set_family_code(self, value):
        self._family_code = value
    def set_truncated_serial(self, value):
        self._truncated_serial = value
    def set_crc_code(self, value):
        self._crc_code = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._chip_index)
        buf += struct.pack("<B", self._family_code)
        buf += struct.pack("<L", self._truncated_serial)
        buf += struct.pack("<B", self._crc_code)
        return buf
    def get_chip_index(self):
        return self._chip_index
    def get_family_code(self):
        return self._family_code
    def get_truncated_serial(self):
        return self._truncated_serial
    def get_crc_code(self):
        return self._crc_code
    def get_all_data(self):
        data = []
        data.append((fields.chip_index, self.get_chip_index()))
        data.append((fields.family_code, self.get_family_code()))
        data.append((fields.truncated_serial, self.get_truncated_serial()))
        data.append((fields.crc_code, self.get_crc_code()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._chip_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._family_code = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._truncated_serial = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._crc_code = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class CouldNotFindDS28E18Q_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.CouldNotFindDS28E18Q
        self._category = categories.none
        self._id = 199
        self._size = 7
        self._chip_index = 0
        self._family_code = 0
        self._truncated_serial = 0
        self._crc_code = 0
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
    def set_chip_index(self, value):
        self._chip_index = value
    def set_family_code(self, value):
        self._family_code = value
    def set_truncated_serial(self, value):
        self._truncated_serial = value
    def set_crc_code(self, value):
        self._crc_code = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._chip_index)
        buf += struct.pack("<B", self._family_code)
        buf += struct.pack("<L", self._truncated_serial)
        buf += struct.pack("<B", self._crc_code)
        return buf
    def get_chip_index(self):
        return self._chip_index
    def get_family_code(self):
        return self._family_code
    def get_truncated_serial(self):
        return self._truncated_serial
    def get_crc_code(self):
        return self._crc_code
    def get_all_data(self):
        data = []
        data.append((fields.chip_index, self.get_chip_index()))
        data.append((fields.family_code, self.get_family_code()))
        data.append((fields.truncated_serial, self.get_truncated_serial()))
        data.append((fields.crc_code, self.get_crc_code()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._chip_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._family_code = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._truncated_serial = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._crc_code = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class CouldNotFindDS28E18Q_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.CouldNotFindDS28E18Q
        self._category = categories.none
        self._id = 200
        self._size = 7
        self._chip_index = 0
        self._family_code = 0
        self._truncated_serial = 0
        self._crc_code = 0
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
    def set_chip_index(self, value):
        self._chip_index = value
    def set_family_code(self, value):
        self._family_code = value
    def set_truncated_serial(self, value):
        self._truncated_serial = value
    def set_crc_code(self, value):
        self._crc_code = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._chip_index)
        buf += struct.pack("<B", self._family_code)
        buf += struct.pack("<L", self._truncated_serial)
        buf += struct.pack("<B", self._crc_code)
        return buf
    def get_chip_index(self):
        return self._chip_index
    def get_family_code(self):
        return self._family_code
    def get_truncated_serial(self):
        return self._truncated_serial
    def get_crc_code(self):
        return self._crc_code
    def get_all_data(self):
        data = []
        data.append((fields.chip_index, self.get_chip_index()))
        data.append((fields.family_code, self.get_family_code()))
        data.append((fields.truncated_serial, self.get_truncated_serial()))
        data.append((fields.crc_code, self.get_crc_code()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._chip_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._family_code = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._truncated_serial = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._crc_code = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class MAX31850KError_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.MAX31850KError
        self._category = categories.none
        self._id = 201
        self._size = 2
        self._sensor_index = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_error(self, value):
        self._error = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<B", self._error)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_error(self):
        return MAX31850KError(self._error)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.error, self.get_error()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class MAX31856Error_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.MAX31856Error
        self._category = categories.none
        self._id = 202
        self._size = 2
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
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_raw_fault_register(self, value):
        self._raw_fault_register = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<B", self._raw_fault_register)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_raw_fault_register(self):
        return self._raw_fault_register
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.raw_fault_register, self.get_raw_fault_register()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._raw_fault_register = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class MAX31865Error_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.MAX31865Error
        self._category = categories.none
        self._id = 203
        self._size = 2
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
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_raw_fault_register(self, value):
        self._raw_fault_register = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<B", self._raw_fault_register)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_raw_fault_register(self):
        return self._raw_fault_register
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.raw_fault_register, self.get_raw_fault_register()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._raw_fault_register = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class ValveActuation_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.ValveActuation
        self._category = categories.none
        self._id = 204
        self._size = 5
        self._sensor_index = 0
        self._distance_mm = 0
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
        self._sensor_index = value
    def set_distance_mm(self, value):
        self._distance_mm = packedFloat_to_uint(value, -500, 500, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._distance_mm)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_distance_mm(self):
        return uint_to_scaledFloat(self._distance_mm, -500, 500, 4)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.distance_mm, self.get_distance_mm()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._distance_mm = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class ValveActuationError_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.ValveActuationError
        self._category = categories.none
        self._id = 205
        self._size = 2
        self._sensor_index = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_error(self, value):
        self._error = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<B", self._error)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_error(self):
        return ValveActuationError(self._error)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.error, self.get_error()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class Humidity_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.Humidity
        self._category = categories.none
        self._id = 206
        self._size = 2
        self._relative_humidity = 0
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
    def set_relative_humidity(self, value):
        self._relative_humidity = packedFloat_to_uint(value, 0, 100, 2)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._relative_humidity)
        return buf
    def get_relative_humidity(self):
        return uint_to_scaledFloat(self._relative_humidity, 0, 100, 2)
    def get_all_data(self):
        data = []
        data.append((fields.relative_humidity, self.get_relative_humidity()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._relative_humidity = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class HumidityError_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.HumidityError
        self._category = categories.none
        self._id = 207
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
        return HumidityError(self._error)
    def get_all_data(self):
        data = []
        data.append((fields.error, self.get_error()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class Acceleration_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.Acceleration
        self._category = categories.none
        self._id = 208
        self._size = 6
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
        self._acceleration_z_gforce = packedFloat_to_uint(value, -20, 20, 2)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._acceleration_x_gforce)
        buf += struct.pack("<H", self._acceleration_y_gforce)
        buf += struct.pack("<H", self._acceleration_z_gforce)
        return buf
    def get_acceleration_x_gforce(self):
        return uint_to_scaledFloat(self._acceleration_x_gforce, -20, 20, 2)
    def get_acceleration_y_gforce(self):
        return uint_to_scaledFloat(self._acceleration_y_gforce, -20, 20, 2)
    def get_acceleration_z_gforce(self):
        return uint_to_scaledFloat(self._acceleration_z_gforce, -20, 20, 2)
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
        self._acceleration_z_gforce = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class AccelerationError_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.AccelerationError
        self._category = categories.none
        self._id = 209
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
        return AccelerationError(self._error)
    def get_all_data(self):
        data = []
        data.append((fields.error, self.get_error()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.PartialDebugMessage
        self._category = categories.none
        self._id = 210
        self._size = 8
        self._length = 0
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
    def set_length(self, value):
        self._length = value
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
        buf += struct.pack("<B", self._length)
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        buf += struct.pack("<B", self._byte5)
        buf += struct.pack("<B", self._byte6)
        return buf
    def get_length(self):
        return self._length
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
        data.append((fields.length, self.get_length()))
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
        self._length = struct.unpack_from("<B", buf, index)[0]
        index += 1
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
class PartialDebugMessage_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PartialDebugMessage
        self._category = categories.none
        self._id = 211
        self._size = 8
        self._length = 0
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
    def set_length(self, value):
        self._length = value
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
        buf += struct.pack("<B", self._length)
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        buf += struct.pack("<B", self._byte5)
        buf += struct.pack("<B", self._byte6)
        return buf
    def get_length(self):
        return self._length
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
        data.append((fields.length, self.get_length()))
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
        self._length = struct.unpack_from("<B", buf, index)[0]
        index += 1
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
class PartialDebugMessage_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.PartialDebugMessage
        self._category = categories.none
        self._id = 212
        self._size = 8
        self._length = 0
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
    def set_length(self, value):
        self._length = value
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
        buf += struct.pack("<B", self._length)
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        buf += struct.pack("<B", self._byte5)
        buf += struct.pack("<B", self._byte6)
        return buf
    def get_length(self):
        return self._length
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
        data.append((fields.length, self.get_length()))
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
        self._length = struct.unpack_from("<B", buf, index)[0]
        index += 1
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
class PartialDebugMessage_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.PartialDebugMessage
        self._category = categories.none
        self._id = 213
        self._size = 8
        self._length = 0
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
    def set_length(self, value):
        self._length = value
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
        buf += struct.pack("<B", self._length)
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        buf += struct.pack("<B", self._byte5)
        buf += struct.pack("<B", self._byte6)
        return buf
    def get_length(self):
        return self._length
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
        data.append((fields.length, self.get_length()))
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
        self._length = struct.unpack_from("<B", buf, index)[0]
        index += 1
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
class TaskInfo_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.TaskInfo
        self._category = categories.none
        self._id = 214
        self._size = 6
        self._type = 0
        self._thread_id = 0
        self._taskTime_microseconds = 0
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
    def set_thread_id(self, value):
        self._thread_id = value
    def set_taskTime_microseconds(self, value):
        self._taskTime_microseconds = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._type)
        buf += struct.pack("<B", self._thread_id)
        buf += struct.pack("<L", self._taskTime_microseconds)
        return buf
    def get_type(self):
        return TaskType(self._type)
    def get_thread_id(self):
        return self._thread_id
    def get_taskTime_microseconds(self):
        return self._taskTime_microseconds
    def get_all_data(self):
        data = []
        data.append((fields.type, self.get_type()))
        data.append((fields.thread_id, self.get_thread_id()))
        data.append((fields.taskTime_microseconds, self.get_taskTime_microseconds()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._type = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._thread_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._taskTime_microseconds = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class TaskInfo_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.TaskInfo
        self._category = categories.none
        self._id = 215
        self._size = 6
        self._type = 0
        self._thread_id = 0
        self._taskTime_microseconds = 0
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
    def set_thread_id(self, value):
        self._thread_id = value
    def set_taskTime_microseconds(self, value):
        self._taskTime_microseconds = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._type)
        buf += struct.pack("<B", self._thread_id)
        buf += struct.pack("<L", self._taskTime_microseconds)
        return buf
    def get_type(self):
        return TaskType(self._type)
    def get_thread_id(self):
        return self._thread_id
    def get_taskTime_microseconds(self):
        return self._taskTime_microseconds
    def get_all_data(self):
        data = []
        data.append((fields.type, self.get_type()))
        data.append((fields.thread_id, self.get_thread_id()))
        data.append((fields.taskTime_microseconds, self.get_taskTime_microseconds()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._type = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._thread_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._taskTime_microseconds = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class TaskInfo_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.TaskInfo
        self._category = categories.none
        self._id = 216
        self._size = 6
        self._type = 0
        self._thread_id = 0
        self._taskTime_microseconds = 0
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
    def set_thread_id(self, value):
        self._thread_id = value
    def set_taskTime_microseconds(self, value):
        self._taskTime_microseconds = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._type)
        buf += struct.pack("<B", self._thread_id)
        buf += struct.pack("<L", self._taskTime_microseconds)
        return buf
    def get_type(self):
        return TaskType(self._type)
    def get_thread_id(self):
        return self._thread_id
    def get_taskTime_microseconds(self):
        return self._taskTime_microseconds
    def get_all_data(self):
        data = []
        data.append((fields.type, self.get_type()))
        data.append((fields.thread_id, self.get_thread_id()))
        data.append((fields.taskTime_microseconds, self.get_taskTime_microseconds()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._type = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._thread_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._taskTime_microseconds = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class TaskInfo_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.TaskInfo
        self._category = categories.none
        self._id = 217
        self._size = 6
        self._type = 0
        self._thread_id = 0
        self._taskTime_microseconds = 0
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
    def set_thread_id(self, value):
        self._thread_id = value
    def set_taskTime_microseconds(self, value):
        self._taskTime_microseconds = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._type)
        buf += struct.pack("<B", self._thread_id)
        buf += struct.pack("<L", self._taskTime_microseconds)
        return buf
    def get_type(self):
        return TaskType(self._type)
    def get_thread_id(self):
        return self._thread_id
    def get_taskTime_microseconds(self):
        return self._taskTime_microseconds
    def get_all_data(self):
        data = []
        data.append((fields.type, self.get_type()))
        data.append((fields.thread_id, self.get_thread_id()))
        data.append((fields.taskTime_microseconds, self.get_taskTime_microseconds()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._type = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._thread_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._taskTime_microseconds = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class LoopInfo_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.LoopInfo
        self._category = categories.none
        self._id = 218
        self._size = 6
        self._type = 0
        self._thread_id = 0
        self._loopTime_microseconds = 0
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
    def set_thread_id(self, value):
        self._thread_id = value
    def set_loopTime_microseconds(self, value):
        self._loopTime_microseconds = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._type)
        buf += struct.pack("<B", self._thread_id)
        buf += struct.pack("<L", self._loopTime_microseconds)
        return buf
    def get_type(self):
        return LoopType(self._type)
    def get_thread_id(self):
        return self._thread_id
    def get_loopTime_microseconds(self):
        return self._loopTime_microseconds
    def get_all_data(self):
        data = []
        data.append((fields.type, self.get_type()))
        data.append((fields.thread_id, self.get_thread_id()))
        data.append((fields.loopTime_microseconds, self.get_loopTime_microseconds()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._type = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._thread_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._loopTime_microseconds = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class LoopInfo_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.LoopInfo
        self._category = categories.none
        self._id = 219
        self._size = 6
        self._type = 0
        self._thread_id = 0
        self._loopTime_microseconds = 0
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
    def set_thread_id(self, value):
        self._thread_id = value
    def set_loopTime_microseconds(self, value):
        self._loopTime_microseconds = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._type)
        buf += struct.pack("<B", self._thread_id)
        buf += struct.pack("<L", self._loopTime_microseconds)
        return buf
    def get_type(self):
        return LoopType(self._type)
    def get_thread_id(self):
        return self._thread_id
    def get_loopTime_microseconds(self):
        return self._loopTime_microseconds
    def get_all_data(self):
        data = []
        data.append((fields.type, self.get_type()))
        data.append((fields.thread_id, self.get_thread_id()))
        data.append((fields.loopTime_microseconds, self.get_loopTime_microseconds()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._type = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._thread_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._loopTime_microseconds = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class LoopInfo_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.LoopInfo
        self._category = categories.none
        self._id = 220
        self._size = 6
        self._type = 0
        self._thread_id = 0
        self._loopTime_microseconds = 0
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
    def set_thread_id(self, value):
        self._thread_id = value
    def set_loopTime_microseconds(self, value):
        self._loopTime_microseconds = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._type)
        buf += struct.pack("<B", self._thread_id)
        buf += struct.pack("<L", self._loopTime_microseconds)
        return buf
    def get_type(self):
        return LoopType(self._type)
    def get_thread_id(self):
        return self._thread_id
    def get_loopTime_microseconds(self):
        return self._loopTime_microseconds
    def get_all_data(self):
        data = []
        data.append((fields.type, self.get_type()))
        data.append((fields.thread_id, self.get_thread_id()))
        data.append((fields.loopTime_microseconds, self.get_loopTime_microseconds()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._type = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._thread_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._loopTime_microseconds = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class LoopInfo_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.LoopInfo
        self._category = categories.none
        self._id = 221
        self._size = 6
        self._type = 0
        self._thread_id = 0
        self._loopTime_microseconds = 0
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
    def set_thread_id(self, value):
        self._thread_id = value
    def set_loopTime_microseconds(self, value):
        self._loopTime_microseconds = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._type)
        buf += struct.pack("<B", self._thread_id)
        buf += struct.pack("<L", self._loopTime_microseconds)
        return buf
    def get_type(self):
        return LoopType(self._type)
    def get_thread_id(self):
        return self._thread_id
    def get_loopTime_microseconds(self):
        return self._loopTime_microseconds
    def get_all_data(self):
        data = []
        data.append((fields.type, self.get_type()))
        data.append((fields.thread_id, self.get_thread_id()))
        data.append((fields.loopTime_microseconds, self.get_loopTime_microseconds()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._type = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._thread_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._loopTime_microseconds = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class PowerControlNewStateRequest_from_Ground_Controller_to_Edda_Controller:
    def __init__(self):
        self._sender = nodes.Ground_Controller
        self._receiver = nodes.Edda_Controller
        self._message = messages.PowerControlNewStateRequest
        self._category = categories.none
        self._id = 51
        self._size = 3
        self._power_control_channel_id = 0
        self._requested_state = 0
        self._circumvent_arming_checks = 0
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
    def set_power_control_channel_id(self, value):
        self._power_control_channel_id = value.value
    def set_requested_state(self, value):
        self._requested_state = value.value
    def set_circumvent_arming_checks(self, value):
        self._circumvent_arming_checks = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._power_control_channel_id)
        buf += struct.pack("<B", self._requested_state)
        buf += struct.pack("<B", self._circumvent_arming_checks)
        return buf
    def get_power_control_channel_id(self):
        return PowerControlChannel(self._power_control_channel_id)
    def get_requested_state(self):
        return PowerControlChannelStateRequest(self._requested_state)
    def get_circumvent_arming_checks(self):
        return CircumventArmingCheck(self._circumvent_arming_checks)
    def get_all_data(self):
        data = []
        data.append((fields.power_control_channel_id, self.get_power_control_channel_id()))
        data.append((fields.requested_state, self.get_requested_state()))
        data.append((fields.circumvent_arming_checks, self.get_circumvent_arming_checks()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._power_control_channel_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._requested_state = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._circumvent_arming_checks = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerControlNewStateResponse_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerControlNewStateResponse
        self._category = categories.none
        self._id = 74
        self._size = 4
        self._power_control_channel_id = 0
        self._requested_state = 0
        self._requested_circumvent_arming_checks = 0
        self._result = 0
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
    def set_power_control_channel_id(self, value):
        self._power_control_channel_id = value.value
    def set_requested_state(self, value):
        self._requested_state = value.value
    def set_requested_circumvent_arming_checks(self, value):
        self._requested_circumvent_arming_checks = value.value
    def set_result(self, value):
        self._result = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._power_control_channel_id)
        buf += struct.pack("<B", self._requested_state)
        buf += struct.pack("<B", self._requested_circumvent_arming_checks)
        buf += struct.pack("<B", self._result)
        return buf
    def get_power_control_channel_id(self):
        return PowerControlChannel(self._power_control_channel_id)
    def get_requested_state(self):
        return PowerControlChannelStateRequest(self._requested_state)
    def get_requested_circumvent_arming_checks(self):
        return CircumventArmingCheck(self._requested_circumvent_arming_checks)
    def get_result(self):
        return PowerControlChannelStateRequestResult(self._result)
    def get_all_data(self):
        data = []
        data.append((fields.power_control_channel_id, self.get_power_control_channel_id()))
        data.append((fields.requested_state, self.get_requested_state()))
        data.append((fields.requested_circumvent_arming_checks, self.get_requested_circumvent_arming_checks()))
        data.append((fields.result, self.get_result()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._power_control_channel_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._requested_state = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._requested_circumvent_arming_checks = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._result = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerControlGetState_from_Ground_Controller_to_Edda_Controller:
    def __init__(self):
        self._sender = nodes.Ground_Controller
        self._receiver = nodes.Edda_Controller
        self._message = messages.PowerControlGetState
        self._category = categories.none
        self._id = 52
        self._size = 1
        self._power_control_channel_id = 0
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
    def set_power_control_channel_id(self, value):
        self._power_control_channel_id = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._power_control_channel_id)
        return buf
    def get_power_control_channel_id(self):
        return PowerControlChannel(self._power_control_channel_id)
    def get_all_data(self):
        data = []
        data.append((fields.power_control_channel_id, self.get_power_control_channel_id()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._power_control_channel_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerControlState_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerControlState
        self._category = categories.none
        self._id = 75
        self._size = 3
        self._power_control_channel_id = 0
        self._channel_state = 0
        self._gate_state = 0
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
    def set_power_control_channel_id(self, value):
        self._power_control_channel_id = value.value
    def set_channel_state(self, value):
        self._channel_state = value.value
    def set_gate_state(self, value):
        self._gate_state = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._power_control_channel_id)
        buf += struct.pack("<B", self._channel_state)
        buf += struct.pack("<B", self._gate_state)
        return buf
    def get_power_control_channel_id(self):
        return PowerControlChannel(self._power_control_channel_id)
    def get_channel_state(self):
        return PowerControlChannelState(self._channel_state)
    def get_gate_state(self):
        return owerControlChannelGateState(self._gate_state)
    def get_all_data(self):
        data = []
        data.append((fields.power_control_channel_id, self.get_power_control_channel_id()))
        data.append((fields.channel_state, self.get_channel_state()))
        data.append((fields.gate_state, self.get_gate_state()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._power_control_channel_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._channel_state = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._gate_state = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerControlVoltages_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerControlVoltages
        self._category = categories.none
        self._id = 222
        self._size = 5
        self._power_control_channel_id = 0
        self._voltage_3v3_volts = 0
        self._voltage_input_volts = 0
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
    def set_power_control_channel_id(self, value):
        self._power_control_channel_id = value.value
    def set_voltage_3v3_volts(self, value):
        self._voltage_3v3_volts = packedFloat_to_uint(value, 0, 5, 2)
    def set_voltage_input_volts(self, value):
        self._voltage_input_volts = packedFloat_to_uint(value, 0, 30, 2)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._power_control_channel_id)
        buf += struct.pack("<H", self._voltage_3v3_volts)
        buf += struct.pack("<H", self._voltage_input_volts)
        return buf
    def get_power_control_channel_id(self):
        return PowerControlChannel(self._power_control_channel_id)
    def get_voltage_3v3_volts(self):
        return uint_to_scaledFloat(self._voltage_3v3_volts, 0, 5, 2)
    def get_voltage_input_volts(self):
        return uint_to_scaledFloat(self._voltage_input_volts, 0, 30, 2)
    def get_all_data(self):
        data = []
        data.append((fields.power_control_channel_id, self.get_power_control_channel_id()))
        data.append((fields.voltage_3v3_volts, self.get_voltage_3v3_volts()))
        data.append((fields.voltage_input_volts, self.get_voltage_input_volts()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._power_control_channel_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._voltage_3v3_volts = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._voltage_input_volts = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class PowerControlResistance_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerControlResistance
        self._category = categories.none
        self._id = 223
        self._size = 6
        self._power_control_channel_id = 0
        self._resistance_ohms = 0
        self._source = 0
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
    def set_power_control_channel_id(self, value):
        self._power_control_channel_id = value.value
    def set_resistance_ohms(self, value):
        self._resistance_ohms = packedFloat_to_uint(value, 0, 100000, 4)
    def set_source(self, value):
        self._source = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._power_control_channel_id)
        buf += struct.pack("<L", self._resistance_ohms)
        buf += struct.pack("<B", self._source)
        return buf
    def get_power_control_channel_id(self):
        return PowerControlChannel(self._power_control_channel_id)
    def get_resistance_ohms(self):
        return uint_to_scaledFloat(self._resistance_ohms, 0, 100000, 4)
    def get_source(self):
        return PowerControlResistanceSource(self._source)
    def get_all_data(self):
        data = []
        data.append((fields.power_control_channel_id, self.get_power_control_channel_id()))
        data.append((fields.resistance_ohms, self.get_resistance_ohms()))
        data.append((fields.source, self.get_source()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._power_control_channel_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._resistance_ohms = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._source = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerControlEstimates_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerControlEstimates
        self._category = categories.none
        self._id = 224
        self._size = 5
        self._power_control_channel_id = 0
        self._estimated_current_amperes = 0
        self._estimated_power_amperes = 0
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
    def set_power_control_channel_id(self, value):
        self._power_control_channel_id = value.value
    def set_estimated_current_amperes(self, value):
        self._estimated_current_amperes = packedFloat_to_uint(value, 0, 100, 2)
    def set_estimated_power_amperes(self, value):
        self._estimated_power_amperes = packedFloat_to_uint(value, 0, 3000, 2)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._power_control_channel_id)
        buf += struct.pack("<H", self._estimated_current_amperes)
        buf += struct.pack("<H", self._estimated_power_amperes)
        return buf
    def get_power_control_channel_id(self):
        return PowerControlChannel(self._power_control_channel_id)
    def get_estimated_current_amperes(self):
        return uint_to_scaledFloat(self._estimated_current_amperes, 0, 100, 2)
    def get_estimated_power_amperes(self):
        return uint_to_scaledFloat(self._estimated_power_amperes, 0, 3000, 2)
    def get_all_data(self):
        data = []
        data.append((fields.power_control_channel_id, self.get_power_control_channel_id()))
        data.append((fields.estimated_current_amperes, self.get_estimated_current_amperes()))
        data.append((fields.estimated_power_amperes, self.get_estimated_power_amperes()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._power_control_channel_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._estimated_current_amperes = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._estimated_power_amperes = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class PowerControlLoadMeasurement_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerControlLoadMeasurement
        self._category = categories.none
        self._id = 225
        self._size = 7
        self._power_control_channel_id = 0
        self._voltage_volts = 0
        self._current_amperes = 0
        self._power_watts = 0
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
    def set_power_control_channel_id(self, value):
        self._power_control_channel_id = value.value
    def set_voltage_volts(self, value):
        self._voltage_volts = packedFloat_to_uint(value, 0, 30, 2)
    def set_current_amperes(self, value):
        self._current_amperes = packedFloat_to_uint(value, -30, 30, 2)
    def set_power_watts(self, value):
        self._power_watts = packedFloat_to_uint(value, -450, 450, 2)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._power_control_channel_id)
        buf += struct.pack("<H", self._voltage_volts)
        buf += struct.pack("<H", self._current_amperes)
        buf += struct.pack("<H", self._power_watts)
        return buf
    def get_power_control_channel_id(self):
        return PowerControlChannel(self._power_control_channel_id)
    def get_voltage_volts(self):
        return uint_to_scaledFloat(self._voltage_volts, 0, 30, 2)
    def get_current_amperes(self):
        return uint_to_scaledFloat(self._current_amperes, -30, 30, 2)
    def get_power_watts(self):
        return uint_to_scaledFloat(self._power_watts, -450, 450, 2)
    def get_all_data(self):
        data = []
        data.append((fields.power_control_channel_id, self.get_power_control_channel_id()))
        data.append((fields.voltage_volts, self.get_voltage_volts()))
        data.append((fields.current_amperes, self.get_current_amperes()))
        data.append((fields.power_watts, self.get_power_watts()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._power_control_channel_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._voltage_volts = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._current_amperes = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._power_watts = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class PowerControlLoadMeasurementError_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerControlLoadMeasurementError
        self._category = categories.none
        self._id = 226
        self._size = 2
        self._power_control_channel_id = 0
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
    def set_power_control_channel_id(self, value):
        self._power_control_channel_id = value.value
    def set_error(self, value):
        self._error = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._power_control_channel_id)
        buf += struct.pack("<B", self._error)
        return buf
    def get_power_control_channel_id(self):
        return PowerControlChannel(self._power_control_channel_id)
    def get_error(self):
        return PowerControlLoadMeasurementError(self._error)
    def get_all_data(self):
        data = []
        data.append((fields.power_control_channel_id, self.get_power_control_channel_id()))
        data.append((fields.error, self.get_error()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._power_control_channel_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerControlResistanceMeasurementError_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerControlResistanceMeasurementError
        self._category = categories.none
        self._id = 227
        self._size = 2
        self._power_control_channel_id = 0
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
    def set_power_control_channel_id(self, value):
        self._power_control_channel_id = value.value
    def set_error(self, value):
        self._error = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._power_control_channel_id)
        buf += struct.pack("<B", self._error)
        return buf
    def get_power_control_channel_id(self):
        return PowerControlChannel(self._power_control_channel_id)
    def get_error(self):
        return PowerControlResistanceMeasurementError(self._error)
    def get_all_data(self):
        data = []
        data.append((fields.power_control_channel_id, self.get_power_control_channel_id()))
        data.append((fields.error, self.get_error()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._power_control_channel_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PerformIgnition_from_Ground_Controller_to_Edda_Controller:
    def __init__(self):
        self._sender = nodes.Ground_Controller
        self._receiver = nodes.Edda_Controller
        self._message = messages.PerformIgnition
        self._category = categories.none
        self._id = 53
        self._size = 8
        self._this_number_must_be_positive_1 = 0
        self._this_number_must_be_negative_2 = 0
        self._this_number_must_be_positive_4 = 0
        self._this_number_must_be_negative_8 = 0
        self._this_number_must_be_positive_16 = 0
        self._this_number_must_be_negative_32 = 0
        self._this_number_must_be_positive_64 = 0
        self._this_number_must_be_negative_128 = 0
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
    def set_this_number_must_be_positive_1(self, value):
        self._this_number_must_be_positive_1 = value
    def set_this_number_must_be_negative_2(self, value):
        self._this_number_must_be_negative_2 = value
    def set_this_number_must_be_positive_4(self, value):
        self._this_number_must_be_positive_4 = value
    def set_this_number_must_be_negative_8(self, value):
        self._this_number_must_be_negative_8 = value
    def set_this_number_must_be_positive_16(self, value):
        self._this_number_must_be_positive_16 = value
    def set_this_number_must_be_negative_32(self, value):
        self._this_number_must_be_negative_32 = value
    def set_this_number_must_be_positive_64(self, value):
        self._this_number_must_be_positive_64 = value
    def set_this_number_must_be_negative_128(self, value):
        self._this_number_must_be_negative_128 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<b", self._this_number_must_be_positive_1)
        buf += struct.pack("<b", self._this_number_must_be_negative_2)
        buf += struct.pack("<b", self._this_number_must_be_positive_4)
        buf += struct.pack("<b", self._this_number_must_be_negative_8)
        buf += struct.pack("<b", self._this_number_must_be_positive_16)
        buf += struct.pack("<b", self._this_number_must_be_negative_32)
        buf += struct.pack("<b", self._this_number_must_be_positive_64)
        buf += struct.pack("<b", self._this_number_must_be_negative_128)
        return buf
    def get_this_number_must_be_positive_1(self):
        return self._this_number_must_be_positive_1
    def get_this_number_must_be_negative_2(self):
        return self._this_number_must_be_negative_2
    def get_this_number_must_be_positive_4(self):
        return self._this_number_must_be_positive_4
    def get_this_number_must_be_negative_8(self):
        return self._this_number_must_be_negative_8
    def get_this_number_must_be_positive_16(self):
        return self._this_number_must_be_positive_16
    def get_this_number_must_be_negative_32(self):
        return self._this_number_must_be_negative_32
    def get_this_number_must_be_positive_64(self):
        return self._this_number_must_be_positive_64
    def get_this_number_must_be_negative_128(self):
        return self._this_number_must_be_negative_128
    def get_all_data(self):
        data = []
        data.append((fields.this_number_must_be_positive_1, self.get_this_number_must_be_positive_1()))
        data.append((fields.this_number_must_be_negative_2, self.get_this_number_must_be_negative_2()))
        data.append((fields.this_number_must_be_positive_4, self.get_this_number_must_be_positive_4()))
        data.append((fields.this_number_must_be_negative_8, self.get_this_number_must_be_negative_8()))
        data.append((fields.this_number_must_be_positive_16, self.get_this_number_must_be_positive_16()))
        data.append((fields.this_number_must_be_negative_32, self.get_this_number_must_be_negative_32()))
        data.append((fields.this_number_must_be_positive_64, self.get_this_number_must_be_positive_64()))
        data.append((fields.this_number_must_be_negative_128, self.get_this_number_must_be_negative_128()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._this_number_must_be_positive_1 = struct.unpack_from("<b", buf, index)[0]
        index += 1
        self._this_number_must_be_negative_2 = struct.unpack_from("<b", buf, index)[0]
        index += 1
        self._this_number_must_be_positive_4 = struct.unpack_from("<b", buf, index)[0]
        index += 1
        self._this_number_must_be_negative_8 = struct.unpack_from("<b", buf, index)[0]
        index += 1
        self._this_number_must_be_positive_16 = struct.unpack_from("<b", buf, index)[0]
        index += 1
        self._this_number_must_be_negative_32 = struct.unpack_from("<b", buf, index)[0]
        index += 1
        self._this_number_must_be_positive_64 = struct.unpack_from("<b", buf, index)[0]
        index += 1
        self._this_number_must_be_negative_128 = struct.unpack_from("<b", buf, index)[0]
        index += 1
        return
class IgnitionHappened_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.IgnitionHappened
        self._category = categories.none
        self._id = 76
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
class IgnitionHappened_from_Edda_Controller_to_Edda_Telemetry:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Edda_Telemetry
        self._message = messages.IgnitionHappened
        self._category = categories.none
        self._id = 76
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
class IgnitionHappened_from_Edda_Controller_to_Edda_Pressure_Top:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Edda_Pressure_Top
        self._message = messages.IgnitionHappened
        self._category = categories.none
        self._id = 76
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
class IgnitionHappened_from_Edda_Controller_to_Edda_Pressure_Bottom:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Edda_Pressure_Bottom
        self._message = messages.IgnitionHappened
        self._category = categories.none
        self._id = 76
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
class IgnitionCannotHappen_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.IgnitionCannotHappen
        self._category = categories.none
        self._id = 77
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
def id_to_message_class(id):
    if id == 0:
        receiver = CurrentTimePing_from_Flight_Controller_to_Edda_Controller()
        return receiver
    if id == 0:
        receiver = CurrentTimePing_from_Flight_Controller_to_Edda_Telemetry()
        return receiver
    if id == 0:
        receiver = CurrentTimePing_from_Flight_Controller_to_Edda_Pressure_Top()
        return receiver
    if id == 0:
        receiver = CurrentTimePing_from_Flight_Controller_to_Edda_Pressure_Bottom()
        return receiver
    if id == 0:
        receiver = CurrentTimePing_from_Flight_Controller_to_Edda_Simulator()
        return receiver
    if id == 144:
        receiver = CanLatency_from_Flight_Controller_to_Ground_Controller()
        return receiver
    if id == 144:
        receiver = CanLatency_from_Flight_Controller_to_Edda_Controller()
        return receiver
    if id == 144:
        receiver = CanLatency_from_Flight_Controller_to_Edda_Telemetry()
        return receiver
    if id == 144:
        receiver = CanLatency_from_Flight_Controller_to_Edda_Pressure_Top()
        return receiver
    if id == 144:
        receiver = CanLatency_from_Flight_Controller_to_Edda_Pressure_Bottom()
        return receiver
    if id == 144:
        receiver = CanLatency_from_Flight_Controller_to_Edda_Simulator()
        return receiver
    if id == 4:
        receiver = CurrentTimePong_from_Edda_Controller_to_Flight_Controller()
        return receiver
    if id == 5:
        receiver = CurrentTimePong_from_Edda_Telemetry_to_Flight_Controller()
        return receiver
    if id == 6:
        receiver = CurrentTimePong_from_Edda_Pressure_Top_to_Flight_Controller()
        return receiver
    if id == 7:
        receiver = CurrentTimePong_from_Edda_Pressure_Bottom_to_Flight_Controller()
        return receiver
    if id == 8:
        receiver = CurrentTimePong_from_Edda_Simulator_to_Flight_Controller()
        return receiver
    if id == 1:
        receiver = SayHi_from_Flight_Controller_to_Edda_Controller()
        return receiver
    if id == 1:
        receiver = SayHi_from_Flight_Controller_to_Edda_Telemetry()
        return receiver
    if id == 1:
        receiver = SayHi_from_Flight_Controller_to_Edda_Pressure_Top()
        return receiver
    if id == 1:
        receiver = SayHi_from_Flight_Controller_to_Edda_Pressure_Bottom()
        return receiver
    if id == 1:
        receiver = SayHi_from_Flight_Controller_to_Edda_Simulator()
        return receiver
    if id == 9:
        receiver = Hello_from_Edda_Controller_to_Flight_Controller()
        return receiver
    if id == 10:
        receiver = Hello_from_Edda_Telemetry_to_Flight_Controller()
        return receiver
    if id == 11:
        receiver = Hello_from_Edda_Pressure_Top_to_Flight_Controller()
        return receiver
    if id == 12:
        receiver = Hello_from_Edda_Pressure_Bottom_to_Flight_Controller()
        return receiver
    if id == 13:
        receiver = Hello_from_Edda_Simulator_to_Flight_Controller()
        return receiver
    if id == 145:
        receiver = CanStatistics_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 146:
        receiver = CanStatistics_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 147:
        receiver = CanStatistics_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 148:
        receiver = CanStatistics_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 149:
        receiver = CanStatistics_from_Edda_Simulator_to_Ground_Controller()
        return receiver
    if id == 150:
        receiver = WenHop_from_Edda_Controller_to_Flight_Controller()
        return receiver
    if id == 151:
        receiver = WenHop_from_Edda_Telemetry_to_Flight_Controller()
        return receiver
    if id == 152:
        receiver = WenHop_from_Edda_Pressure_Top_to_Flight_Controller()
        return receiver
    if id == 153:
        receiver = WenHop_from_Edda_Pressure_Bottom_to_Flight_Controller()
        return receiver
    if id == 154:
        receiver = WenHop_from_Edda_Simulator_to_Flight_Controller()
        return receiver
    if id == 48:
        receiver = SetDebugModeRequest_from_Flight_Controller_to_Edda_Controller()
        return receiver
    if id == 48:
        receiver = SetDebugModeRequest_from_Flight_Controller_to_Edda_Telemetry()
        return receiver
    if id == 48:
        receiver = SetDebugModeRequest_from_Flight_Controller_to_Edda_Pressure_Top()
        return receiver
    if id == 48:
        receiver = SetDebugModeRequest_from_Flight_Controller_to_Edda_Pressure_Bottom()
        return receiver
    if id == 48:
        receiver = SetDebugModeRequest_from_Flight_Controller_to_Edda_Simulator()
        return receiver
    if id == 49:
        receiver = SetPowerModeRequest_from_Flight_Controller_to_Edda_Controller()
        return receiver
    if id == 49:
        receiver = SetPowerModeRequest_from_Flight_Controller_to_Edda_Telemetry()
        return receiver
    if id == 49:
        receiver = SetPowerModeRequest_from_Flight_Controller_to_Edda_Pressure_Top()
        return receiver
    if id == 49:
        receiver = SetPowerModeRequest_from_Flight_Controller_to_Edda_Pressure_Bottom()
        return receiver
    if id == 49:
        receiver = SetPowerModeRequest_from_Flight_Controller_to_Edda_Simulator()
        return receiver
    if id == 64:
        receiver = GoingToSleep_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 65:
        receiver = GoingToSleep_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 66:
        receiver = GoingToSleep_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 67:
        receiver = GoingToSleep_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 68:
        receiver = GoingToSleep_from_Edda_Simulator_to_Ground_Controller()
        return receiver
    if id == 69:
        receiver = WokeUp_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 70:
        receiver = WokeUp_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 71:
        receiver = WokeUp_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 72:
        receiver = WokeUp_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 73:
        receiver = WokeUp_from_Edda_Simulator_to_Ground_Controller()
        return receiver
    if id == 50:
        receiver = RequestReset_from_Ground_Controller_to_Edda_Controller()
        return receiver
    if id == 50:
        receiver = RequestReset_from_Ground_Controller_to_Edda_Telemetry()
        return receiver
    if id == 50:
        receiver = RequestReset_from_Ground_Controller_to_Edda_Pressure_Top()
        return receiver
    if id == 50:
        receiver = RequestReset_from_Ground_Controller_to_Edda_Pressure_Bottom()
        return receiver
    if id == 50:
        receiver = RequestReset_from_Ground_Controller_to_Edda_Simulator()
        return receiver
    if id == 155:
        receiver = PowerInputMeasurement_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 156:
        receiver = PowerInputMeasurement_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 157:
        receiver = PowerInputMeasurement_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 158:
        receiver = PowerInputMeasurement_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 159:
        receiver = PowerInputMeasurement_from_Edda_Simulator_to_Ground_Controller()
        return receiver
    if id == 160:
        receiver = PowerInputMeasurementError_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 161:
        receiver = PowerInputMeasurementError_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 162:
        receiver = PowerInputMeasurementError_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 163:
        receiver = PowerInputMeasurementError_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 164:
        receiver = PowerInputMeasurementError_from_Edda_Simulator_to_Ground_Controller()
        return receiver
    if id == 165:
        receiver = RawTransducerVoltage_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 166:
        receiver = RawTransducerVoltage_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 167:
        receiver = TransducerPressure_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 167:
        receiver = TransducerPressure_from_Edda_Pressure_Top_to_Edda_Telemetry()
        return receiver
    if id == 168:
        receiver = TransducerPressure_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 168:
        receiver = TransducerPressure_from_Edda_Pressure_Bottom_to_Edda_Telemetry()
        return receiver
    if id == 169:
        receiver = TransducerPressure_from_Edda_Simulator_to_Ground_Controller()
        return receiver
    if id == 169:
        receiver = TransducerPressure_from_Edda_Simulator_to_Edda_Telemetry()
        return receiver
    if id == 170:
        receiver = AmbientPressure_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 171:
        receiver = AmbientPressure_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 172:
        receiver = AmbientPressure_from_Edda_Simulator_to_Ground_Controller()
        return receiver
    if id == 173:
        receiver = TransducerError_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 174:
        receiver = TransducerError_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 175:
        receiver = AmbientPressureError_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 176:
        receiver = AmbientPressureError_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 177:
        receiver = AmbientPressureCoefficient_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 178:
        receiver = AmbientPressureCoefficient_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 179:
        receiver = ColdSideTemperature_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 180:
        receiver = ColdSideTemperature_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 181:
        receiver = ColdSideTemperature_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 182:
        receiver = ColdSideTemperature_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 183:
        receiver = PlatinumSensorTemperature_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 184:
        receiver = PlatinumSensorResistance_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 185:
        receiver = PlatinumSensorRatio_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 186:
        receiver = OneWireBusError_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 187:
        receiver = ThermocoupleTypeKTemperature_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 188:
        receiver = ThermocoupleTypeKTemperature_from_Edda_Simulator_to_Ground_Controller()
        return receiver
    if id == 189:
        receiver = SensorMeasurementInfo_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 190:
        receiver = SensorMeasurementInfo_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 191:
        receiver = SensorMeasurementInfo_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 192:
        receiver = SensorMeasurementInfo_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 193:
        receiver = DS28E18QTransactionError_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 194:
        receiver = DS28E18QTransactionError_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 195:
        receiver = DS28E18QTransactionError_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 196:
        receiver = DS28E18QTransactionError_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 197:
        receiver = CouldNotFindDS28E18Q_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 198:
        receiver = CouldNotFindDS28E18Q_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 199:
        receiver = CouldNotFindDS28E18Q_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 200:
        receiver = CouldNotFindDS28E18Q_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 201:
        receiver = MAX31850KError_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 202:
        receiver = MAX31856Error_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 203:
        receiver = MAX31865Error_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 204:
        receiver = ValveActuation_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 205:
        receiver = ValveActuationError_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 206:
        receiver = Humidity_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 207:
        receiver = HumidityError_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 208:
        receiver = Acceleration_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 209:
        receiver = AccelerationError_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 210:
        receiver = PartialDebugMessage_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 211:
        receiver = PartialDebugMessage_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 212:
        receiver = PartialDebugMessage_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 213:
        receiver = PartialDebugMessage_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 214:
        receiver = TaskInfo_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 215:
        receiver = TaskInfo_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 216:
        receiver = TaskInfo_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 217:
        receiver = TaskInfo_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 218:
        receiver = LoopInfo_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 219:
        receiver = LoopInfo_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 220:
        receiver = LoopInfo_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 221:
        receiver = LoopInfo_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 51:
        receiver = PowerControlNewStateRequest_from_Ground_Controller_to_Edda_Controller()
        return receiver
    if id == 74:
        receiver = PowerControlNewStateResponse_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 52:
        receiver = PowerControlGetState_from_Ground_Controller_to_Edda_Controller()
        return receiver
    if id == 75:
        receiver = PowerControlState_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 222:
        receiver = PowerControlVoltages_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 223:
        receiver = PowerControlResistance_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 224:
        receiver = PowerControlEstimates_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 225:
        receiver = PowerControlLoadMeasurement_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 226:
        receiver = PowerControlLoadMeasurementError_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 227:
        receiver = PowerControlResistanceMeasurementError_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 53:
        receiver = PerformIgnition_from_Ground_Controller_to_Edda_Controller()
        return receiver
    if id == 76:
        receiver = IgnitionHappened_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 76:
        receiver = IgnitionHappened_from_Edda_Controller_to_Edda_Telemetry()
        return receiver
    if id == 76:
        receiver = IgnitionHappened_from_Edda_Controller_to_Edda_Pressure_Top()
        return receiver
    if id == 76:
        receiver = IgnitionHappened_from_Edda_Controller_to_Edda_Pressure_Bottom()
        return receiver
    if id == 77:
        receiver = IgnitionCannotHappen_from_Edda_Controller_to_Ground_Controller()
        return receiver
