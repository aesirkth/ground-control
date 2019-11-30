import sys
import tkinter as tk
from tkinter import E, N, S, W

from gui import (GPSWidget, LiveTimeGraphAcc, LiveTimeGraphAirSpeed,
                 LiveTimeGraphAltitude, LiveTimeGraphGyro, LPSWidget,
                 RocketStatus, TelemetryWidget)
from utils import (DummySerialWrapper, Gateway, LaunchPadStation,
                   SerialWrapper, Sigmundr)


class MainApplication(tk.Frame):
    """ TKinter frame holding some useful widgets to control the Launch Pad Station

    Parameters
    ----------
    parent : Tkinter TK() instance
        TK() instance to hold the widgets
    telemetry : Gateway instance
        Gateway instance correctly set for the Telemetry Gateway
    lps : Gateway instance
        Gateway instance correctly set for the LPS gateway

    """

    def __init__(self, parent, telemetry, lps, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.telemetry = telemetry
        self.lps = lps

        self.left_column = tk.Frame(self)
        self.left_column.grid(row=1, column=0, sticky=W+N)

        self.lps_widget = LPSWidget(
            self.left_column, self.lps, bd=2, relief="ridge")
        self.lps_widget.grid(row=0, column=1, sticky=W+E+N+S)

        self.tm_widget = TelemetryWidget(
            self.left_column, self.telemetry, bd=2, relief="ridge")
        self.tm_widget.grid(row=1, column=1, sticky=W+E+N+S)

        self.rocket_status = RocketStatus(
            self.left_column, self.telemetry, bd=2, relief="ridge")
        self.rocket_status.grid(row=2, column=1, sticky=W+E+N+S)

        self.middle_column = tk.Frame(self)
        self.middle_column.grid(row=1, column=1, sticky=W+N)

        self.speed_graph = LiveTimeGraphAirSpeed(
            self.middle_column, self.telemetry, self.telemetry.sensors.pitot, field="Pressure")
        self.speed_graph.grid(
            row=1, column=2, padx=5, pady=5)

        self.acceleration_graph = LiveTimeGraphAcc(
            self.middle_column, self.telemetry, self.telemetry.sensors.imu2, field="Acceleration")
        self.acceleration_graph.grid(
            row=2, column=2, padx=5, pady=5)

        self.alt_graph = LiveTimeGraphGyro(
            self.middle_column, self.telemetry, self.telemetry.sensors.imu2, field="Acceleration")
        self.alt_graph.grid(
            row=1, column=3, padx=5, pady=5)

        self.gyro_graph = LiveTimeGraphAltitude(
            self.middle_column, self.telemetry, self.telemetry.sensors.bmp2, self.telemetry.sensors.bmp3, field="Acceleration")
        self.gyro_graph.grid(
            row=2, column=3, padx=5, pady=5)

        self.gps = GPSWidget(self, self.telemetry, bd=2, relief="ridge")
        self.gps.grid(row=1, column=4, sticky=N)


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
