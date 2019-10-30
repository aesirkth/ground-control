import pandas as pd


class ImuTest:
    def __init__(self, idx_time, idx_velocity):
        self.idx_time = idx_time
        self.idx_velocity = idx_velocity

        self.calibration_data = {
            "BMP80_dig_T1": None,
        }
        self.got_calibration = False

        self.data = pd.DataFrame(columns=['time', 'velocity'])

    def update(self, data):
        time = int(data[self.idx_time])
        velocity = int(data[self.idx_velocity])

        self.data = self.data.append({
            'time': time,
            'velocity': velocity
        }, ignore_index=True)
    
    def calibrate(self, calibration):
        for cal in self.calibration_data:
            if cal in calibration:
                self.calibration_data[cal] = calibration[cal]
        # Check if all calibration data has been received
        if not None in self.calibration_data.values():
            self.got_calibration = True


class Sensors:
    def __init__(self, imu=None):
        if imu == "Test":
            self.imu = ImuTest(idx_time=1, idx_velocity=2)

    def update_sensors(self, data):
        if self.imu:
            self.imu.update(data)
    
    def update_calibration(self, calibration):
        if self.imu:
            self.imu.calibrate(calibration)
