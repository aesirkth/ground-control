import time

class SerialWrapper:
    def __init__(self, device):
        self.ser = open("data/test", "rb")

    #read x bytes as an integer, little endian
    def read_bytes(self, amount):
        time.sleep(0.002)
        bytes = self.ser.read(amount)
        total = 0
        count = 0
        for v in bytes:
            total += v << (count * 8)
            count += 1
        return total

    #read x amount of bytes as a string
    def read_string(self, amount):
        val = self.ser.read(amount)
        return str(val)
    
    #tries to initialize a device
    #user self.ser to read and write since it does not need to be saved
    def init_device(self):
        return 1
    
    #finds devices that are safe to communicate with
    def get_safe_devices(self):
        return [0]

    #returns -1 if it fails
    def open_serial(self):
        return 0