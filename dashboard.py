import sys
import tkinter as tk
from tkinter import E, N, S, W

from gui import GatewayStatus, LiveTimeGraph, SensorIndicator, GeneralData
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

    def __init__(self, parent, gateway, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.gateway = gateway
        self.sensors = self.gateway.sensors

        self.speed_graph = LiveTimeGraph(
            self, self.gateway, self.sensors.bmp2, field="Temperature")
        self.gateway_status = GatewayStatus(self, self.gateway, "Telemetry")
        # self.tm_status = GatewayStatus(self, self.gateway, field="FM/FPV")
        self.imu2_status = SensorIndicator(
            self, self.gateway, self.sensors.errmsg, field="ERR_INIT_IMU2")
        self.imu3_status = SensorIndicator(
            self, self.gateway, self.sensors.errmsg, field="ERR_INIT_IMU3")
        self.bmp2_status = SensorIndicator(
            self, self.gateway, self.sensors.errmsg, field="ERR_INIT_BMP2")
        self.bmp3_status = SensorIndicator(
            self, self.gateway, self.sensors.errmsg, field="ERR_INIT_BMP3")
        self.mag_status = SensorIndicator(
            self, self.gateway, self.sensors.errmsg, field="ERR_INIT_MAG")
        self.adc_status = SensorIndicator(
            self, self.gateway, self.sensors.errmsg, field="ERR_INIT_ADC")
        self.card_status = SensorIndicator(
            self, self.gateway, self.sensors.errmsg, field="ERR_INIT_SD_CARD")
        # self.tm_indicator = SensorIndicator(self, self.gateway, self.sensors.imu,
        #                                     field="Telemetry Status")
        # self.abs_vel = GeneralData(self, self.gateway, data=self.gateway.data, field="|V|")

        self.gateway_status.grid(
            row=0, column=1, sticky=W+E+N+S, padx=5, pady=5)
        # self.tm_status.grid(
        #    row=0, column=2, sticky=W+E+N+S, padx=5, pady=5)
        # self.abs_vel.grid(
        #     row=0, column=3, sticky=W, padx=10, pady=5)
        self.speed_graph.grid(
            row=1, rowspan=7, column=3, sticky=W+E+N+S, padx=5, pady=5)
        self.imu2_status.grid(
            row=2, column=1, sticky=W, padx=10, pady=0)
        self.imu3_status.grid(
            row=3, column=1, sticky=W, padx=10, pady=0)
        self.bmp2_status.grid(
            row=4, column=1, sticky=W, padx=10, pady=0)
        self.bmp3_status.grid(
            row=5, column=1, sticky=W, padx=10, pady=0)
        self.mag_status.grid(
            row=6, column=1, sticky=W, padx=10, pady=0)
        self.adc_status.grid(
            row=7, column=1, sticky=W, padx=10, pady=0)
        self.card_status.grid(
            row=8, column=1, sticky=W, padx=10, pady=0)


if __name__ == "__main__":
    # Get the first argument given
    if len(sys.argv) >= 2:
        if sys.argv[1] == "rfd":
            # Use this with a RFD900 modem
            serial = SerialWrapper(115200, "Telemetry", rfd900=True)
        elif sys.argv[1] == "gw":
            # Use this for testing with an Arduino board and `dummy_telemetry.ino`
            serial = SerialWrapper(115200, "Telemetry", bonjour="TELEMETRY")
        elif sys.argv[1] == "dummy":
            # Use this for testing with an Arduino board and `dummy_telemetry.ino`
            serial = DummySerialWrapper('Dummy')
        else:
            serial = SerialWrapper(115200, "Telemetry", bonjour="TELEMETRY")
    else:
        serial = SerialWrapper(115200, "Telemetry", bonjour="TELEMETRY")

    sensors = Sigmundr()

    telemetry = Gateway(serial, sensors, "./data")

    root = tk.Tk()
    root.title("Sigmundr Dashboard")

    MainApplication(root, telemetry).pack(
        side="top", fill="both", expand=True)

    root.mainloop()
