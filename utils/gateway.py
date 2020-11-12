#todo
class Gateway():
    def __init__(self):
        self.data = {}
        self.read = False
        self.exit = True

    def __send_header(self, target, id):
        if not self.read:
            return -1

    def __wait_for_data(self, id):
        pass

    #stops the thread
    def stop(self):
        self.exit = True
    
    #pause the thread
    def pause(self):
        self.read = False
    
    #resume the thread
    def start(self):
        self.read = True

    def time_sync(self,):
        if not self.read:
            return -1

    def set_power_mode(self, TBD):
        if not self.read:
            return -1

    def set_radio_emitters(self, fpv, tm):
        if not self.read:
            return -1

    def set_parachute(self, armed, enable_1, enable_2):
        if not self.read:
            return -1

    def activate_outputs(self, a, b, c, d):
        if not self.read:
            return -1