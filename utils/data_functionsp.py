#W.I.P datafunctions for real protocol

dataFunctions = {}

class Data:
    def __init__(self, source, measurement, value):
        self.source = source #flight or engine
        self.measurement = measurement #name of data
        self.value = value

class TimeSeries:
    def __init__(self):
        self.x = []
        self.y = []

def handle_data(dataList, time, database):
    for data in dataList:
        if data.source not in database:
            database[data.source] = {}
        if data.measurement not in database[data.source]:
            database[data.source][data.measurement] = TimeSeries()

        database[data.source][data.measurement].x.append(time)
        database[data.source][data.measurement].y.append(data)

#ms since boot engine controller
def f0x10(ser):
    value = ser.read_bytes(4)
    return [Data("engine", "ms_since_boot", value)]
dataFunctions[0x10] = f0x10

#μs since boot engine controller
def f0x11(ser):
    value = ser.read_bytes(8)
    return [Data("engine", "us_since_boot", value)]
dataFunctions[0x11] = f0x11

#ms since boot flight controller
def f0x90(ser):
    value = ser.read_bytes(4)
    return [Data("flight", "ms_since_boot", value)]
dataFunctions[0x90] = f0x90

#us since boot flight controller
def f0x91(ser):
    value = ser.read_bytes(8)
    return [Data("flight", "us_since_boot", value)]
dataFunctions[0x91] = f0x91

#GNSS time
def f0x92(ser):
    value = ser.read_bytes(2)
    return [Data("flight", "gps_time", value)]
dataFunctions[0x92] = f0x92

#GNSS data, too lazy for this one
def f0x93(ser):
    value = ser.read_bytes(54)
    return[Data("flight", "gps_data", value)]
dataFunctions[0x93] = f0x93

#hardware state
def f0x95(ser):
    value = ser.read_bytes(1)
    return [
        Data("flight", "is_parachute_armed", value & 0b1),
        Data("flight", "is_parachute1_en", value & 0b10),
        Data("flight", "is_parachute2_en", value & 0b100),
        Data("flight", "is_fpv_en", value & 0b1000),
        Data("flight", "is_telemetry_en", value & 0b10000)
    ]
dataFunctions[0x95] = f0x95

#static pressure
def f0x96(ser):
    return [
        Data("flight", "pressure_1", ser.read_bytes(4)) * 100,
        Data("flight", "temperature_1", ser.read_bytes(4)) * 100,
        Data("flight", "pressure_2", ser.read_bytes(4)) * 100,
        Data("flight", "temperature_2", ser.read_bytes(4) * 100)
    ]
dataFunctions[0x96] = f0x96

#static pressure - no temp
def f0x97(ser):
    return [
        Data("flight", "pressure_1", ser.read_bytes(4) * 100),
        Data("flight", "pressure_2", ser.read_bytes(4) * 100)
    ]
dataFunctions[0x97] = f0x97

#On-board battery voltage
def f0x99(ser):
    bat1_raw = ser.read_bytes(2) * 100
    bat2_raw = ser.read_bytes(2) * 100 
    #calibration taken from old code
    bat1 = 2.555e-5 * bat1_raw ** 2 - 0.0835 * bat1_raw + 81.83 
    bat2 = 8.885e-6 * bat2_raw ** 2 - 0.0316 * bat2_raw + 34.780
    return [
        Data("flight", "voltage_battery_1_raw", bat1_raw),
        Data("flight", "voltage_battery_2_raw", bat2_raw),
        Data("flight", "voltage_battery_1", bat1),
        Data("flight", "voltage_battery_2", bat2)
    ]
dataFunctions[0x99] = f0x99

#Air temperature
def f0x9A(ser):
    return [
        Data("flight", "ext_temp_1", ser.read_bytes(2) * 100),
        Data("flight", "ext_temp_2", ser.read_bytes(2) * 100)
    ]
dataFunctions[0x9A] = f0x9A