from utils.serial_reader import SerialReader

class Telemetry(SerialReader):
    def __init__(self, **kwargs):
        super().__init__(device = "RFD", **kwargs)