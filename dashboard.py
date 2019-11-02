import tkinter as tk
from tkinter import E, N, S, W

from gui import GatewayStatus, LiveTimeGraph, MessageBox
from utils import Gateway, Sensors, SerialWrapper


class MainApplication(tk.Frame):
    """ TKinter frame holding some useful widgets to control the Launch Pad Station

    Parameters
    ----------
    parent : Tkinter TK() instance
        TK() instance to hold the widgets
    gateway : Gateway instance
        Gateway instance correctly set for the LPS Gateway

    """

    def __init__(self, parent, gateway, sensors, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.gateway = gateway
        self.sensors = sensors

        self.gateway_messages = MessageBox(
            self, gateway=self.gateway, borderwidth=2, relief="groove")
        self.graph = LiveTimeGraph(
            self, gateway=self.gateway, sensor=self.sensors.imu, field="velocity")
        self.gateway_status = GatewayStatus(self, gateway=self.gateway)

        self.gateway_status.grid(
            row=0, column=1, sticky=W+E+N+S, padx=5, pady=5)
        self.graph.grid(
            row=0, rowspan=2, column=2, sticky=W+E+N+S, padx=5, pady=5)
        self.gateway_messages.grid(
            row=1, column=1, sticky=W+E+N+S, padx=5, pady=5)


if __name__ == "__main__":
    # Use this with a RFD900 modem
    # serial = SerialWrapper(baudrate=57600, name="Telemetry", rfd900=True)
    # Use this for testing with an Arduino board and `dummy_telemetry.ino`
    serial = SerialWrapper(baudrate=115200, name="Telemetry", bonjour="TELEMETRY")

    sensors = Sensors(imu="Test")
    
    telemetry = Gateway(serial=serial, sensors=sensors, path="./data")

    root = tk.Tk()
    root.title("Sigmundr Dashboard")

    MainApplication(parent=root, gateway=telemetry, sensors=sensors).pack(
        side="top", fill="both", expand=True)

    root.mainloop()
