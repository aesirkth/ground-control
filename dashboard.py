import sys
import tkinter as tk
from tkinter import E, N, S, W

from gui import (GPSWidget, LiveTimeGraphTemp, LPSWidget, RocketStatus,
                 TelemetryWidget)
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

    def __init__(self, parent, telemetry, lps, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.telemetry = telemetry
        self.sensors = self.telemetry.sensors

        self.left_column = tk.Frame(self)
        self.left_column.grid(row=1, column=0)

        self.lps_widget = LPSWidget(
            self.left_column, lps, bd=2, relief="ridge")
        self.lps_widget.grid(row=0, column=1, sticky=W+E+N+S)

        self.tm_widget = TelemetryWidget(
            self.left_column, self.telemetry, bd=2, relief="ridge")
        self.tm_widget.grid(row=1, column=1, sticky=W+E+N+S)

        self.rocket_status = RocketStatus(
            self.left_column, self.telemetry, bd=2, relief="ridge")
        self.rocket_status.grid(row=2, column=1, sticky=W+E+N+S)

        self.temp_graph = LiveTimeGraphTemp(
            self, self.telemetry, self.sensors.bmp2, field="Temperature")
        self.temp_graph.grid(
            row=1, column=2, padx=5, pady=5)

        self.gps = GPSWidget(self, self.telemetry, bd=2, relief="ridge")
        self.gps.grid(row=0, column=4)


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
