import sys
import tkinter as tk
from tkinter import E, N, S, W

from gui import GatewayStatus, LiveTimeGraph, MessageBox, SensorIndicator
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
        self.gateway_status = GatewayStatus(self, gateway=self.gateway, field="GS")
        self.tm_status = GatewayStatus(self, gateway=self.gateway, field="FM/FPV")
        self.imu1_status = SensorIndicator(self, gateway=self.gateway, sensor=self.sensors.imu, field="IMU1")
        self.imu2_status = SensorIndicator(self, gateway=self.gateway, sensor=self.sensors.imu, field="IMU2")
        self.bmd1_status = SensorIndicator(self, gateway=self.gateway, sensor=self.sensors.imu, field="BMP1")
        self.bmd2_status = SensorIndicator(self, gateway=self.gateway, sensor=self.sensors.imu, field="BMP2")
        self.gps_status = SensorIndicator(self, gateway=self.gateway, sensor=self.sensors.imu, field="GPS")
        self.pito_status = SensorIndicator(self, gateway=self.gateway, sensor=self.sensors.imu, field="Pitotube")
        self.magneto_status = SensorIndicator(self, gateway=self.gateway, sensor=self.sensors.imu, field="Magnetometer")
        self.tm_indicator = SensorIndicator(self, gateway=self.gateway, sensor=self.sensors.imu, field="Telemetry Status")

        self.gateway_status.grid(
            row=0, column=1, sticky=W+E+N+S, padx=5, pady=5)
        self.tm_status.grid(
            row=0, column=2, sticky=W+E+N+S, padx=5, pady=5)
        self.graph.grid(
            row=0, rowspan=2, column=3, sticky=W+E+N+S, padx=5, pady=5)
        self.gateway_messages.grid(
            row=1, rowspan=2, column=1, columnspan=2, sticky=W+E+N+S, padx=5, pady=5)
        self.imu1_status.grid(
            row=3, column=1, sticky=W, padx=10, pady=5)
        self.imu2_status.grid(
            row=4, column=1, sticky=W, padx=10, pady=5)
        self.bmd1_status.grid(
            row=5, column=1, sticky=W, padx=10, pady=5)
        self.bmd2_status.grid(
            row=6, column=1, sticky=W, padx=10, pady=5)
        self.gps_status.grid(
            row=3, column=2, sticky=W, padx=20, pady=5)
        self.pito_status.grid(
            row=4, column=2, sticky=W, padx=20, pady=5)
        self.magneto_status.grid(
            row=5, column=2, sticky=W, padx=20, pady=5)
        self.tm_indicator.grid(
            row=7, column=1, sticky=W, padx=20, pady=5)


if __name__ == "__main__":
    # Get the first argument given
    if len(sys.argv) >= 2:
        if sys.argv[1] == "rfd":
            # Use this with a RFD900 modem
            serial = SerialWrapper(baudrate=115200, name="Telemetry", rfd900=True)
        elif sys.argv[1] == "gw":
            # Use this for testing with an Arduino board and `dummy_telemetry.ino`
            serial = SerialWrapper(baudrate=115200, name="Telemetry", bonjour="TELEMETRY")
        else:
            serial = SerialWrapper(baudrate=115200, name="Telemetry", bonjour="TELEMETRY")
    else:
        serial = SerialWrapper(baudrate=115200, name="Telemetry", bonjour="TELEMETRY")

    sensors = Sensors(imu="Test")
    
    telemetry = Gateway(serial=serial, sensors=sensors, path="./data")

    root = tk.Tk()
    root.title("Sigmundr Dashboard")

    MainApplication(parent=root, gateway=telemetry, sensors=sensors).pack(
        side="top", fill="both", expand=True)

    root.mainloop()
