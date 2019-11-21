import sys
import tkinter as tk
from tkinter import E, N, S, W

from gui import GatewayStatus, LiveTimeGraph, SensorIndicator, GeneralData, EngineControl
from utils import DummySerialWrapper, Gateway, SerialWrapper, Sigmundr


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

        self.speed_graph = LiveTimeGraph(
            self, gateway=self.gateway, sensor=self.sensors.imu, field="velocity")
        self.gateway_status = GatewayStatus(self, gateway=self.gateway, field="GS")
        # self.tm_status = GatewayStatus(self, gateway=self.gateway, field="FM/FPV")
        self.imu2_status = SensorIndicator(self, gateway=self.gateway, sensor=self.sensors.imu, field="IMU2")
        self.imu3_status = SensorIndicator(self, gateway=self.gateway, sensor=self.sensors.imu, field="IMU3")
        self.bmd2_status = SensorIndicator(self, gateway=self.gateway, sensor=self.sensors.imu, field="BMP2")
        self.bmd3_status = SensorIndicator(self, gateway=self.gateway, sensor=self.sensors.imu, field="BMP3")
        self.gps_status = SensorIndicator(self, gateway=self.gateway, sensor=self.sensors.imu, field="GPS")
        self.SD_status = SensorIndicator(self, gateway=self.gateway, sensor=self.sensors.imu, field="SD-Card")
        self.magneto_status = SensorIndicator(self, gateway=self.gateway, sensor=self.sensors.imu, field="Magnetometer")
        self.tm_indicator = SensorIndicator(self, gateway=self.gateway, sensor=self.sensors.imu,
                                            field="Telemetry Status")
        self.calibration_status = SensorIndicator(self, gateway=self.gateway, sensor=self.sensors.imu,
                                                  field="Calibration")
        self.parachute_status = SensorIndicator(self, gateway=self.gateway, sensor=self.sensors.imu,
                                                  field="Parachute Deployed")
        self.fuel_control = EngineControl(self, gateway=self.gateway, sensor=self.sensors.imu, field="Fueling")
        # self.ignition_control = EngineControl(self, gateway=self.gateway, sensor=self.sensors.imu, field="Ignition")
        self.abs_vel = GeneralData(self, gateway=self.gateway, data=self.gateway.data, field="|V|")

        self.gateway_status.grid(
            row=0, column=1, sticky=W+E+N+S, padx=5, pady=5)
        # self.tm_status.grid(
        #    row=0, column=2, sticky=W+E+N+S, padx=5, pady=5)
        self.abs_vel.grid(
            row=0, column=3, sticky=W, padx=10, pady=5)
        self.speed_graph.grid(
            row=1, rowspan=7, column=3, sticky=W+E+N+S, padx=5, pady=5)
        self.imu2_status.grid(
            row=2, column=1, sticky=W, padx=10, pady=0)
        self.imu3_status.grid(
            row=3, column=1, sticky=W, padx=10, pady=0)
        self.bmd2_status.grid(
            row=4, column=1, sticky=W, padx=10, pady=0)
        self.bmd3_status.grid(
            row=5, column=1, sticky=W, padx=10, pady=0)
        self.gps_status.grid(
            row=2, column=2, sticky=W, padx=20, pady=0)
        self.SD_status.grid(
            row=3, column=2, sticky=W, padx=20, pady=0)
        self.magneto_status.grid(
            row=4, column=2, sticky=W, padx=20, pady=0)
        self.tm_indicator.grid(
            row=6, column=1, sticky=W, padx=10, pady=5)
        self.calibration_status.grid(
            row=6, column=2, sticky=W, padx=20, pady=5)
        self.parachute_status.grid(
            row=7, column=1, sticky=W, padx=10, pady=5)
        self.fuel_control.grid(
            row=8, column=1, padx=20, pady=20)
        # self.ignition_control.grid(
        #    row=9, column=2, padx=20, pady=20)


if __name__ == "__main__":
    # Get the first argument given
    if len(sys.argv) >= 2:
        if sys.argv[1] == "rfd":
            # Use this with a RFD900 modem
            serial = SerialWrapper(baudrate=115200, name="Telemetry", rfd900=True)
        elif sys.argv[1] == "gw":
            # Use this for testing with an Arduino board and `dummy_telemetry.ino`
            serial = SerialWrapper(baudrate=115200, name="Telemetry", bonjour="TELEMETRY")
        elif sys.argv[1] == "dummy":
            # Use this for testing with an Arduino board and `dummy_telemetry.ino`
            serial = DummySerialWrapper('Dummy')
        else:
            serial = SerialWrapper(baudrate=115200, name="Telemetry", bonjour="TELEMETRY")
    else:
        serial = SerialWrapper(baudrate=115200, name="Telemetry", bonjour="TELEMETRY")

    sensors = Sigmundr()
    
    telemetry = Gateway(serial=serial, sensors=sensors, path="./data")

    root = tk.Tk()
    root.title("Sigmundr Dashboard")

    MainApplication(parent=root, gateway=telemetry, sensors=sensors).pack(
        side="top", fill="both", expand=True)

    root.mainloop()
