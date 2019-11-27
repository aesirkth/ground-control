import sys
import tkinter as tk
from tkinter import E, N, S, W

from gui import LiveTimeGraphTemp, LPSWidget, SensorIndicator, TelemetryWidget
from utils import (DummySerialWrapper, Gateway, LaunchPadStation,
                   SerialWrapper, Sigmundr)


class MainApplication(tk.Frame):
    """ TKinter frame holding some useful widgets to control the Launch Pad Station

    Parameters
    ----------
    parent : Tkinter TK() instance
        TK() instance to hold the widgets
    telemetry : Gateway instance
        Gateway instance correctly set for the LPS Gateway

    """

    def __init__(self, parent, telemetry, lps,*args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.telemetry = telemetry
        self.sensors = self.telemetry.sensors


        self.lps_widget = LPSWidget(self, lps, borderwidth=2, relief="ridge")
        self.lps_widget.grid(row=0, column=1)

        self.tm_widget = TelemetryWidget(self, self.telemetry, borderwidth=2, relief="ridge")
        self.tm_widget.grid(row=1, column=1, sticky=W+E+N+S)

        self.temp_graph = LiveTimeGraphTemp(
            self, self.telemetry, self.sensors.bmp2, field="Temperature")
        self.imu2_status = SensorIndicator(
            self, self.telemetry, self.sensors.errmsg, field="ERR_INIT_IMU2")
        self.imu3_status = SensorIndicator(
            self, self.telemetry, self.sensors.errmsg, field="ERR_INIT_IMU3")
        self.bmp2_status = SensorIndicator(
            self, self.telemetry, self.sensors.errmsg, field="ERR_INIT_BMP2")
        self.bmp3_status = SensorIndicator(
            self, self.telemetry, self.sensors.errmsg, field="ERR_INIT_BMP3")
        self.mag_status = SensorIndicator(
            self, self.telemetry, self.sensors.errmsg, field="ERR_INIT_MAG")
        self.adc_status = SensorIndicator(
            self, self.telemetry, self.sensors.errmsg, field="ERR_INIT_ADC")
        self.card_status = SensorIndicator(
            self, self.telemetry, self.sensors.errmsg, field="ERR_INIT_SD_CARD")

        self.temp_graph.grid(
            row=2, rowspan=7, column=3, sticky=W+E+N+S, padx=5, pady=5)
        self.imu2_status.grid(
            row=3, column=1, sticky=W, padx=10, pady=0)
        self.imu3_status.grid(
            row=4, column=1, sticky=W, padx=10, pady=0)
        self.bmp2_status.grid(
            row=5, column=1, sticky=W, padx=10, pady=0)
        self.bmp3_status.grid(
            row=6, column=1, sticky=W, padx=10, pady=0)
        self.mag_status.grid(
            row=7, column=1, sticky=W, padx=10, pady=0)
        self.adc_status.grid(
            row=8, column=1, sticky=W, padx=10, pady=0)
        self.card_status.grid(
            row=9, column=1, sticky=W, padx=10, pady=0)


if __name__ == "__main__":
    # Get the first argument given
    if len(sys.argv) >= 2:
        if sys.argv[1] == "rfd":
            # Use this with a RFD900 modem
            serial_telemetry = SerialWrapper(115200, "Telemetry", rfd900=True)
        elif sys.argv[1] == "dummy":
            # Use this to simulate a telemetry data flow
            serial_telemetry = DummySerialWrapper('Dummy')
        else:
            serial_telemetry = SerialWrapper(115200, "Telemetry", rfd900=True)
    else:
        serial_telemetry = SerialWrapper(115200, "Telemetry", rfd900=True)
    
    rocket_sensors = Sigmundr()
    telemetry = Gateway(serial_telemetry, rocket_sensors, "./data")

    serial_lps = SerialWrapper(115200, "LPS", bonjour="LAUNCHPADSTATION")
    lps_sensors = LaunchPadStation()
    lps = Gateway(serial_lps, lps_sensors, "./data")

    root = tk.Tk()
    root.title("Sigmundr Dashboard")

    MainApplication(root, telemetry, lps).pack(
        side="top", fill="both", expand=True)

    root.mainloop()
