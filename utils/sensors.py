""" Utilities to deal with the sensors

The class GenericSensor contains all the logic required to extract the sensors' data from
a bytearray

Write GenericSensor child class for each sensor with a 'field' and 'sample_size' attributes. Add an 'update_data()'
method that calls the parent's 'update_raw_data()' method to update the sensor's values. It is possible
to add a specific processing in 'update_data()' if necessary

"""

import datetime
import math
import struct


class GenericSensor:
    """ This is a generic class to deal with most sensors

    Parameters
    ----------
    start_position: int
        position of the first byte in the frame. Count starts from 0
    fields: dict
        dictionary with the following structure
            {'Name_of_the_field': {
                'start': #Position of the first byte in the field,
                'size': #Size of the field in bytes,
                'conversion_function': #lamdba fonction to convert the values,
                'byte_order': #'big' or 'little,
                'signed': #True or False,
                },
            {'Name_of_an_other_field'}: {...},
            }
    sample_size: int
        number of bytes in the field
    nb_sample: int
        (optional) number of samples. Samples must be ordered from oldest to newest
    sample_rate: float
        (optional) frequency of data acquisition in Hz. Required if nb_samples != 1
    is_rtc: bool
        True if the sensor is a Real Time Clock

    """

    def __init__(self, start_position, fields, sample_size, nb_samples=1, sample_rate=0, is_rtc=False):
        self.start_position = start_position
        self.fields = fields
        self.sample_size = sample_size  # Byte
        self.nb_samples = nb_samples
        self.sample_rate = sample_rate  # Hz
        self.is_rtc = is_rtc

        self.set_default_values()

    def set_default_values(self):
        fields = ['Time'] + ['Seconds_since_start'] + list(self.fields.keys())
        self.raw_data = {key: [] for key in fields}

    def _extract_samples(self, frame):
        """ Read a frame and return a view of it with only the relevant bytes

        The relevant bytes are those located between self.start_position and
        self.sample_size. If multiple samples are present (ie. self.nb_samples
        is greater that 1) all samples are returned as elements of a list

        Parameters
        ----------
        frame: bytearray
            array containing all the sensors values

        Returns
        -------
        samples: list
            list of the samples related to the sensor

        """
        start = self.start_position
        size = self.sample_size*self.nb_samples
        frame = frame[start: start + size]

        samples = []
        for i in range(0, len(frame), self.sample_size):
            sample = frame[i: i + self.sample_size]
            samples.append(sample)
   
        return samples

    def _extract_field_values(self, sample, field):
        """ Use self.field data to extract and convert the field values

        Parameters
        ----------
        sample: bytearray
        
        Returns
        -------
        value: int or float or bool
            converted value of the field

        """
        start = self.fields[field]['start']
        size = self.fields[field]['size']
        field_type = self.fields[field]['type']
        convert = self.fields[field]['conversion_function']
        byte_order = self.fields[field]['byte_order']
        signed = self.fields[field]['signed']

        field_bytes = sample[start: start + size]

        if field_type == 'int':
            value = int.from_bytes(field_bytes, byte_order, signed=signed)
        elif field_type == 'float':
            if byte_order == 'big':
                [value] = struct.unpack('>f', field_bytes)
            else:
                [value] = struct.unpack('<f', field_bytes)

        value = convert(value)

        return value

    def update_raw_data(self, frame, frame_time=None):
        """ Read values from the telemetry frame and update the sensor's values

        Parameters
        ----------
        frame: bytearray
            telemetry frame
        frame_time: datetime.time object
            (optional) timestamp of the frame. Not need when reading the RTC

        """
        samples = self._extract_samples(frame)

        for i, sample in enumerate(samples):

            for field in self.fields.keys():
                value = self._extract_field_values(sample, field)
                self.raw_data[field].append(value)

            # frame_time is None when updating the RTC values
            if self.is_rtc:
                hour = self.raw_data['Hour'][-1]
                minute = self.raw_data['Minute'][-1]
                second = self.raw_data['Second'][-1]
                microsecond = int(self.raw_data['Microsecond'][-1])
                frame_time = datetime.time(hour, minute, second, microsecond)

            if self.raw_data['Time']:
                start_time = datetime.datetime.combine(datetime.date.today(), self.raw_data['Time'][0])
                    
                now = datetime.datetime.combine(datetime.date.today(), frame_time)
                delta = now - start_time
                delta = delta.total_seconds()
            else:
                delta = 0.
            
            self.raw_data['Time'].append(frame_time)
            if self.sample_rate:
                self.raw_data['Seconds_since_start'].append(delta-(self.nb_samples-i+1)/self.sample_rate)
            else:
                self.raw_data['Seconds_since_start'].append(delta)


# ############################### #
#      Sensors for Sigmundr       #
# ############################### #


class Status(GenericSensor):
    fields = {
        'PARACHUTE_DEPLOYED': {
            'start': 0,
            'size': 1,  # Byte
            'type': 'int',
            'conversion_function': lambda x: (x & 1<<7) >> 7,
            'byte_order': 'big',
            'signed': False,
        },
    }
    sample_size = 1

    def __init__(self, start_position, **kwargs):
        super().__init__(start_position, self.fields, self.sample_size, **kwargs)

        self.reset()
    
    def reset(self):
        self.data = {field: None for field in self.fields.keys()}
        self.set_default_values()

    def update_data(self, frame, frame_time=None):
        self.update_raw_data(frame, frame_time)
        for field in self.fields.keys():
            self.data[field] = self.raw_data[field][-1]


class ErrMsg(GenericSensor):
    fields = {
        'ERR_INIT_IMU2': {
            'start': 0,
            'size': 2,  # Byte
            'type': 'int',
            'conversion_function': lambda x: x & 1<<0,
            'byte_order': 'big',
            'signed': False,
        },
        'ERR_INIT_IMU3': {
            'start': 0,
            'size': 2,
            'type': 'int',
            'conversion_function': lambda x: (x & 1<<1) >> 1,
            'byte_order': 'big',
            'signed': False,
        },
        'ERR_INIT_BMP2': {
            'start': 0,
            'size': 2,
            'type': 'int',
            'conversion_function': lambda x: (x & 1<<2) >> 2,
            'byte_order': 'big',
            'signed': False,
        },
        'ERR_INIT_BMP3': {
            'start': 0,
            'size': 2,
            'type': 'int',
            'conversion_function': lambda x: (x & 1<<3) >> 3,
            'byte_order': 'big',
            'signed': False,
        },
        'ERR_INIT_MAG': {
            'start': 0,
            'size': 2,
            'type': 'int',
            'conversion_function': lambda x: (x & 1<<4) >> 4,
            'byte_order': 'big',
            'signed': False,
        },
        'ERR_INIT_ADC': {
            'start': 0,
            'size': 2,
            'type': 'int',
            'conversion_function': lambda x: (x & 1<<5) >> 5,
            'byte_order': 'big',
            'signed': False,
        },
        'ERR_INIT_SD_CARD': {
            'start': 0,
            'size': 2,
            'type': 'int',
            'conversion_function': lambda x: (x & 1<<6) >> 6,
            'byte_order': 'big',
            'signed': False,
        },
        'ERR_LOOP_TIME': {
            'start': 0,
            'size': 2,
            'type': 'int',
            'conversion_function': lambda x: (x & 1<<7) >> 7,
            'byte_order': 'big',
            'signed': False,
        },
        'ERR_SPI2_ERRORCALLBACK': {
            'start': 0,
            'size': 2,
            'type': 'int',
            'conversion_function': lambda x: (x & 1<<8) >> 8,
            'byte_order': 'big',
            'signed': False,
        },
        'ERR_SPI3_ERRORCALLBACK': {
            'start': 0,
            'size': 2,
            'type': 'int',
            'conversion_function': lambda x: (x & 1<<9) >> 9,
            'byte_order': 'big',
            'signed': False,
        },
        'ERR_ADC_ERRORCALLBACK': {
            'start': 0,
            'size': 2,
            'type': 'int',
            'conversion_function': lambda x: (x & 1<<10) >> 10,
            'byte_order': 'big',
            'signed': False,
        },
        'ERR_UART_ERRORCALLBACK': {
            'start': 0,
            'size': 2,
            'type': 'int',
            'conversion_function': lambda x: (x & 1<<11) >> 11,
            'byte_order': 'big',
            'signed': False,
        },
        'WAIT_IMU2_FINISH_BEFORE_GPS': {
            'start': 0,
            'size': 2,
            'type': 'int',
            'conversion_function': lambda x: (x & 1<<12) >> 12,
            'byte_order': 'big',
            'signed': False,
        },
        'WAIT_IMU3_FINISH_BEFORE_BMP3': {
            'start': 0,
            'size': 2,
            'type': 'int',
            'conversion_function': lambda x: (x & 1<<13) >> 13,
            'byte_order': 'big',
            'signed': False,
        },
        'WAIT_GPS_FINISH_BEFORE_BMP2': {
            'start': 0,
            'size': 2,
            'type': 'int',
            'conversion_function': lambda x: (x & 1<<14) >> 14,
            'byte_order': 'big',
            'signed': False,
        },
        'WAIT_ADC_TO_FINISH': {
            'start': 0,
            'size': 2,
            'type': 'int',
            'conversion_function': lambda x: (x & 1<<15) >> 15,
            'byte_order': 'big',
            'signed': False,
        },
    }
    sample_size = 2

    def __init__(self, start_position, **kwargs):
        super().__init__(start_position, self.fields, self.sample_size, **kwargs)

        self.reset()
    
    def reset(self):
        self.data = {field: None for field in self.fields.keys()}
        self.set_default_values()

    def update_data(self, frame, frame_time=None):
        self.update_raw_data(frame, frame_time)
        for field in self.fields.keys():
            self.data[field] = self.raw_data[field][-1]


class RTC(GenericSensor):
    """ Time since OBC boot

    """
    fields = {
        'Hour': {
            'start': 0,
            'size': 1,  # Byte
            'type': 'int',
            'conversion_function': lambda x: x,  # h
            'byte_order': 'big',
            'signed': False,
        },
        'Minute': {
            'start': 1,
            'size': 1,
            'type': 'int',
            'conversion_function': lambda x: x,  # min
            'byte_order': 'big',
            'signed': False,
        },
        'Second': {
            'start': 2,
            'size': 1,
            'type': 'int',
            'conversion_function': lambda x: x,  # s
            'byte_order': 'big',
            'signed': False,
        },
        'Microsecond': {
            'start': 3,
            'size': 1,
            'type': 'int',
            'conversion_function': lambda x: x*1000*1000/256.,  # ms
            'byte_order': 'big',
            'signed': False,
        },
    }
    sample_size = 4

    def __init__(self, start_position, **kwargs):
        super().__init__(start_position, self.fields, self.sample_size, **kwargs)

        self.reset()
    
    def reset(self):
        self.data = {
            'Time': datetime.time(0, 0, 0, 0),
            'Hour': 0,
            'Minute': 0,
            'Second': 0,
            'Microsecond': 0,
        }
        self.set_default_values()
    
    def update_data(self, frame, frame_time=None):
        self.update_raw_data(frame, frame_time)
        self.data['Time'] = self.raw_data['Time'][-1]
        self.data['Hour'] = self.raw_data['Hour'][-1]
        self.data['Minute'] = self.raw_data['Minute'][-1]
        self.data['Second'] = self.raw_data['Second'][-1]
        self.data['Microsecond'] = self.raw_data['Microsecond'][-1]


class Timer(GenericSensor):
    """ Time elapsed since the rocket was launched

    """
    fields = {
        'Timer': {
            'start': 0,
            'size': 4,  # Byte
            'type': 'int',
            'conversion_function': lambda x: x*5e-4,  # s
            'byte_order': 'little',
            'signed': False,
        },
    }
    sample_size = 4

    def __init__(self, start_position, **kwargs):
        super().__init__(start_position, self.fields, self.sample_size, **kwargs)

        self.reset()
    
    def reset(self):
        self.data = {'Timer': 0}
        self.set_default_values()

    def update_data(self, frame, frame_time=None):
        self.update_raw_data(frame, frame_time)
        self.data['Timer'] = self.raw_data['Timer'][-1]


class Batteries(GenericSensor):
    """ Analog reading of the embedded batteries voltage

    """
    fields = {
        'Battery1': {
            'start': 0,
            'size': 2,  # Byte
            'type': 'int',
            'conversion_function': lambda x: x*3.3/4096*4.030,  # Volt
            'byte_order': 'little',
            'signed': False,
        },
        'Battery2': {
            'start': 2,
            'size': 2,
            'type': 'int',
            'conversion_function': lambda x: x*3.3/4096*2.786,  # Volt
            'byte_order': 'little',
            'signed': False,
        },
    }
    sample_size = 4

    def __init__(self, start_position, **kwargs):
        super().__init__(start_position, self.fields, self.sample_size, **kwargs)

        self.reset()
    
    def reset(self):
        self.data = {field: 0 for field in self.fields.keys()}
        self.set_default_values()

    def update_data(self, frame, frame_time=None):
        self.update_raw_data(frame, frame_time)
        for field in self.fields.keys():
            self.data[field] = self.raw_data[field][-1]


class ICM20602(GenericSensor):
    """ Inertial Motion Unit

    Acceleration scale: +- 16g
    Gyro scale: +- 1000 dps

    """
    fields = {
        'Acc_X': {
            'start': 0,
            'size': 2,  # Byte
            'type': 'int',
            'conversion_function': lambda x: x/2048.,  # g
            'byte_order': 'big',
            'signed': True,
        },
        'Acc_Y': {
            'start': 2,
            'size': 2,
            'type': 'int',
            'conversion_function': lambda x: x/2048.,  # g
            'byte_order': 'big',
            'signed': True,
        },
        'Acc_Z': {
            'start': 4,
            'size': 2,
            'type': 'int',
            'conversion_function': lambda x: x/2048.,  # g
            'byte_order': 'big',
            'signed': True,
        },
        'Temp': {
            'start': 6,
            'size': 2,
            'type': 'int',
            'conversion_function': lambda x: x/326.8 + 25,  # °C
            'byte_order': 'big',
            'signed': True,
        },
        'Gyro_X': {
            'start': 8,
            'size': 2,
            'type': 'int',
            'conversion_function': lambda x: x/32.8,  # dps
            'byte_order': 'big',
            'signed': True,
        },
        'Gyro_Y': {
            'start': 10,
            'size': 2,
            'type': 'int',
            'conversion_function': lambda x: x/32.8,  # dps
            'byte_order': 'big',
            'signed': True,
        },
        'Gyro_Z': {
            'start': 12,
            'size': 2,
            'type': 'int',
            'conversion_function': lambda x: x/32.8,  # dps
            'byte_order': 'big',
            'signed': True,
        },
    }
    sample_size = 14

    def __init__(self, start_position, **kwargs):
        super().__init__(start_position, self.fields, self.sample_size, **kwargs)

        self.reset()
    
    def reset(self):
        self.data = {}
        self.set_default_values()

    def update_data(self, frame, frame_time=None):
        self.update_raw_data(frame, frame_time)


class BMP280(GenericSensor):
    """ Pressure sensor

    On sigmundr this sensor is used to measure the static pressure

    """
    fields = {
        'Temperature': {
            'start': 0,
            'size': 4,  # Byte
            'type': 'int',
            'conversion_function': lambda x: x/100.,  # °C
            'byte_order': 'little',
            'signed': True,
        },
        'Pressure': {
            'start': 4,
            'size': 4,
            'type': 'int',
            'conversion_function': lambda x: x/256.,  # Pa
            'byte_order': 'little',
            'signed': True,
        },
    }
    sample_size = 8

    def __init__(self, start_position, **kwargs):
        super().__init__(start_position, self.fields, self.sample_size, **kwargs)

        self.reset()
    
    def reset(self):
        self.data = {}
        self.set_default_values()

    def update_data(self, frame, frame_time=None):
        self.update_raw_data(frame, frame_time)


class LIS3MDLTR(GenericSensor):
    """ Digital magnetic sensor

    """
    fields = {
        'Mag_X': {
            'start': 0,
            'size': 2,  # Byte
            'type': 'int',
            'conversion_function': lambda x: x/6842.,  # Gauss
            'byte_order': 'big',
            'signed': True,
        },
        'Mag_Y': {
            'start': 2,
            'size': 2,
            'type': 'int',
            'conversion_function': lambda x: x/6842.,  # Gauss
            'byte_order': 'big',
            'signed': True,
        },
        'Mag_Z': {
            'start': 4,
            'size': 2,
            'type': 'int',
            'conversion_function': lambda x: x/6842.,  # Gauss
            'byte_order': 'big',
            'signed': True,
        },
    }
    sample_size = 6

    def __init__(self, start_position, **kwargs):
        super().__init__(start_position, self.fields, self.sample_size, **kwargs)

        self.reset()
    
    def reset(self):
        self.data = {}
        self.set_default_values()

    def update_data(self, frame, frame_time=None):
        self.update_raw_data(frame, frame_time)


class ABP(GenericSensor):
    """ Pressure Sensor

    On Sigmundr this sensor is used to measure the dynamic pressure

    """
    fields = {
        'Pressure': {
            'start': 0,
            'size': 2,  # Byte
            'type': 'int',
            'conversion_function': lambda x: (x - 1638.) / (14747. - 1638.) * 5. * 34474.,  # Pa
            'byte_order': 'big',
            'signed': False,
        },
    }
    sample_size = 2

    def __init__(self, start_position, **kwargs):
        super().__init__(start_position, self.fields, self.sample_size, **kwargs)

        self.reset()
    
    def reset(self):
        self.data = {}
        self.set_default_values()

    def update_data(self, frame, frame_time=None):
        self.update_raw_data(frame, frame_time)


class GPS(GenericSensor):
    """ Pressure Sensor

    GPS receiver on Sigmundr

    """
    fields = {
        'Latitude': {
            'start': 0,
            'size': 4,  # Byte
            'type': 'float',
            'conversion_function': lambda x: x/100.,
            'byte_order': 'little',
            'signed': True,
        },
        'Longitude': {
            'start': 4,
            'size': 4,  # Byte
            'type': 'float',
            'conversion_function': lambda x: x/100.,
            'byte_order': 'little',
            'signed': True,
        },
        'Altitude': {
            'start': 8,
            'size': 4,  # Byte
            'type': 'float',
            'conversion_function': lambda x: x,
            'byte_order': 'little',
            'signed': True,
        },
        'pDOP': {
            'start': 12,
            'size': 4,  # Byte
            'type': 'float',
            'conversion_function': lambda x: x,
            'byte_order': 'little',
            'signed': True,
        },
        'hDOP': {
            'start': 16,
            'size': 4,  # Byte
            'type': 'float',
            'conversion_function': lambda x: x,
            'byte_order': 'little',
            'signed': True,
        },
        'vDOP': {
            'start': 20,
            'size': 4,  # Byte
            'type': 'float',
            'conversion_function': lambda x: x,
            'byte_order': 'little',
            'signed': True,
        },
        'Heading': {
            'start': 24,
            'size': 4,  # Byte
            'type': 'float',
            'conversion_function': lambda x: x,
            'byte_order': 'little',
            'signed': True,
        },
        'Ground_Speed': {
            'start': 28,
            'size': 4,  # Byte
            'type': 'float',
            'conversion_function': lambda x: x,
            'byte_order': 'little',
            'signed': True,
        },
        'Fix_Validity': {
            'start': 32,
            'size': 1,  # Byte
            'type': 'int',
            'conversion_function': lambda x: x & 1,
            'byte_order': 'little',
            'signed': True,
        },
        'Fix_Quality': {
            'start': 32,
            'size': 1,  # Byte
            'type': 'int',
            'conversion_function': lambda x: (x & 0x06) >> 1,
            'byte_order': 'little',
            'signed': True,
        },
        'Fix_Status': {
            'start': 32,
            'size': 1,  # Byte
            'type': 'int',
            'conversion_function': lambda x: (x & 0x18) >> 3,
            'byte_order': 'big',
            'signed': True,
        },
    }
    sample_size = 33

    def __init__(self, start_position, **kwargs):
        super().__init__(start_position, self.fields, self.sample_size, **kwargs)

        self.reset()

    def reset(self):
        self.data = {field: [0] for field in self.fields.keys()}
        self.data['Distance'] = [0]
        self.data['Bearing'] = [0]
        self.data['Bearing_rad'] = [0]
        self.reference_coord = None
        self.set_default_values()
        self.is_graph_init = False
    
    def set_reference(self):
        self.reference_coord = (self.data['Latitude'][-1], self.data['Longitude'][-1])
    
    def distance_haversine(self, coord1, coord2):
        """ Compute the distance between two GPS points

        Coordinates must be in decimal degrees format

        Parameters
        ----------
        coord1 : (float, float)
            first coordinates in DD.MMMM format
        coord2 : (float, float)
            second coordinates in DD.MMMM format

        Returns
        -------
        d : float
            distance between the two points

        """
        R = 6372800  # Earth radius in meters
        lat1, lon1 = coord1
        lat2, lon2 = coord2
        
        phi1 = math.radians(lat1)
        phi2 = math.radians(lat2) 
        dphi = math.radians(lat2 - lat1)
        dlambda = math.radians(lon2 - lon1)
        
        a = math.sin(dphi/2)**2 + \
            math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2

        c = 2*math.atan2(math.sqrt(a), math.sqrt(1 - a))

        d = R*c
        
        return d

    def bearing(self, coord1, coord2):
        """
        Calculates the bearing between two points.
        The formulae used is the following:
            θ = atan2(sin(Δlong).cos(lat2),
                    cos(lat1).sin(lat2) − sin(lat1).cos(lat2).cos(Δlong))
        Parameters
        ----------
        coord1: (float, float) 
            tuple representing the latitude/longitude for the first point
            Latitude and longitude must be in decimal degrees
        coord2: (float, float) 
            tuple representing the latitude/longitude for the second point
            Latitude and longitude must be in decimal degrees
        
        Returns
        -------
        compass_bearing : float
            bearing in degrees

        """
        lat1, lon1 = coord1
        lat2, lon2 = coord2

        lat1 = math.radians(lat1)
        lat2 = math.radians(lat2)

        diffLong = math.radians(lon2 - lon1)

        x = math.sin(diffLong) * math.cos(lat2)
        y = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1)
                * math.cos(lat2) * math.cos(diffLong))

        initial_bearing = math.atan2(x, y)

        # Now we have the initial bearing but math.atan2 return values
        # from -180° to + 180° which is not what we want for a compass bearing
        # The solution is to normalize the initial bearing as shown below
        initial_bearing = math.degrees(initial_bearing)
        compass_bearing = (initial_bearing + 360) % 360

        return compass_bearing

    def update_data(self, frame, frame_time=None):
        self.update_raw_data(frame, frame_time)
        for field in self.fields.keys():
            self.data[field].append(self.raw_data[field][-1])

        if not self.reference_coord is None:
            current_coord = (self.data['Latitude'][-1], self.data['Longitude'][-1])

            distance = self.distance_haversine(self.reference_coord, current_coord)
            bearing = self.bearing(self.reference_coord, current_coord)
            
            self.data['Distance'].append(distance)
            self.data['Bearing'].append(bearing)
            self.data['Bearing_rad'].append(math.radians(bearing))
        else:
            self.data['Distance'].append(0)
            self.data['Bearing'].append(0)
            self.data['Bearing_rad'].append(0)


class Sigmundr:
    """ Extract data from a Telemetry frame received from Sigmundr

    """

    def __init__(self):
        self.status = Status(1)
        self.errmsg = ErrMsg(2)
        self.rtc = RTC(4, is_rtc=True)
        self.timer = Timer(8)
        self.batteries = Batteries(12)
        self.imu2 = ICM20602(16, nb_samples=4, sample_rate=200)
        self.bmp2 = BMP280(72)
        self.bmp3 = BMP280(80)
        self.mag = LIS3MDLTR(88)
        self.pitot = ABP(92)
        self.gps = GPS(100)

    def update_sensors(self, frame):
        if len(frame) > 0:
            if frame[0] == 0x01 or frame[0] == 0x02:
                if len(frame) == 94 or len(frame) == 140:
                    self.rtc.update_data(frame)
                    frame_time = self.rtc.data['Time']
                    self.errmsg.update_data(frame, frame_time)
                    self.status.update_data(frame, frame_time)
                    self.timer.update_data(frame, frame_time)
                    self.batteries.update_data(frame, frame_time)
                    self.imu2.update_data(frame, frame_time)
                    self.bmp2.update_data(frame, frame_time)
                    self.bmp3.update_data(frame, frame_time)
                    self.mag.update_data(frame, frame_time)
                    self.pitot.update_data(frame, frame_time)
            if frame[0] == 0x02:
                if len(frame) == 140:
                    self.gps.update_data(frame, frame_time)
    
    def reset(self):
        self.errmsg.reset()
        self.status.reset()
        self.rtc.reset()
        self.timer.reset()
        self.batteries.reset()
        self.imu2.reset()
        self.bmp2.reset()
        self.bmp3.reset()
        self.mag.reset()
        self.pitot.reset()
        self.gps.reset()
    
    def set_reference(self):
        self.gps.set_reference()


# ########################## #
#      Sensors for LPS       #
# ########################## #


class LPSStatus(GenericSensor):
    fields = {
        'IS_FILLING': {
            'start': 0,
            'size': 1,  # Byte
            'type': 'int',
            'conversion_function': lambda x: x & 1<<0,
            'byte_order': 'big',
            'signed': False,
        },
        'IS_VENTING': {
            'start': 0,
            'size': 1,
            'type': 'int',
            'conversion_function': lambda x: (x & 1<<1) >> 1,
            'byte_order': 'big',
            'signed': False,
        },
        'IS_ARMED': {
            'start': 0,
            'size': 1,
            'type': 'int',
            'conversion_function': lambda x: (x & 1<<2) >> 2,
            'byte_order': 'big',
            'signed': False,
        },
        'IS_FIRING': {
            'start': 0,
            'size': 1,
            'type': 'int',
            'conversion_function': lambda x: (x & 1<<3) >> 3,
            'byte_order': 'big',
            'signed': False,
        },
        'IS_TM_ENABLED': {
            'start': 0,
            'size': 1,
            'type': 'int',
            'conversion_function': lambda x: (x & 1<<4) >> 4,
            'byte_order': 'big',
            'signed': False,
        },
        'IS_SAFE_MODE': {
            'start': 0,
            'size': 1,
            'type': 'int',
            'conversion_function': lambda x: (x & 1<<5) >> 5,
            'byte_order': 'big',
            'signed': False,
        },
    }
    sample_size = 1

    def __init__(self, start_position, **kwargs):
        super().__init__(start_position, self.fields, self.sample_size, **kwargs)

        self.reset()
    
    def reset(self):
        self.data = {field: 0 for field in self.fields.keys()}
        self.data['IS_TM_ENABLED'] = 1
        self.set_default_values()

    def update_data(self, frame, frame_time=None):
        self.update_raw_data(frame, frame_time)
        for field in self.fields.keys():
            self.data[field] = self.raw_data[field][-1]


class RSSI(GenericSensor):
    fields = {
        'REMOTE_RSSI': {
            'start': 0,
            'size': 2,  # Byte
            'type': 'int',
            'conversion_function': lambda x: x,
            'byte_order': 'big',
            'signed': True,
        },
    }
    sample_size = 2

    def __init__(self, start_position, **kwargs):
        super().__init__(start_position, self.fields, self.sample_size, **kwargs)

        self.reset()
    
    def reset(self):
        self.data = {field: 0 for field in self.fields.keys()}
        self.set_default_values()

    def update_data(self, frame, frame_time=None):
        self.update_raw_data(frame, frame_time)
        for field in self.fields.keys():
            self.data[field] = self.raw_data[field][-1]


class LaunchPadStation:
    def __init__(self):
        self.status = LPSStatus(0)
        self.rssi = RSSI(1)
    
    def update_sensors(self, frame):
        if len(frame) == 3:
            time = datetime.datetime.now().time()
            self.status.update_data(frame, frame_time=time)
            self.rssi.update_data(frame, frame_time=time)
    
    def reset(self):
        self.status.reset()
        self.rssi.reset()
