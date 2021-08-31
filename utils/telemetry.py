from utils.serial_reader import SerialReader
from utils.simulator import World, Body, Vector
from threading import Thread

MPU_NOISE = 0
BMP_NOISE = 0
MS_NOISE = 0
H3L_NOISE = 0

class Telemetry(SerialReader):
    def __init__(self, **kwargs):
        super().__init__(device = "flight_controller", **kwargs)
        self._rocket = Body()