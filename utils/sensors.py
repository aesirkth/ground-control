import pandas as pd


class ImuTest:
    def __init__(self, idx_time, idx_velocity):
        self.idx_time = idx_time
        self.idx_velocity = idx_velocity

        self.data = pd.DataFrame(columns=['time', 'velocity'])

    def update(self, data):
        time = int(data[self.idx_time])
        velocity = int(data[self.idx_velocity])

        self.data = self.data.append({
            'time': time,
            'velocity': velocity
        }, ignore_index=True)


class Sensors:
    def __init__(self, imu=None):
        if imu == "Test":
            self.imu = ImuTest(idx_time=1, idx_velocity=2)

    def update_sensors(self, data):
        if self.imu:
            self.imu.update(data)
