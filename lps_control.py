""" Simple Graphical User Gateway that can control the Launch Pad Station

This GUI can:
    - Open and close the Serial link to the LPS Gateway
    - Send commands to the LPS Gateway via simple buttons
    - Display the messages received from the LPS Gateway
"""

import tkinter as tk
from tkinter import E, N, S, W

from gui import (EngineControl, GatewayStatus, GeneralData, LiveTimeGraph,
                 LPSCommandButtons, SensorIndicator)
from utils import Gateway, LaunchPadStation, SerialWrapper


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

        self.gateway_controls = LPSCommandButtons(self, self.gateway, self.sensors.status)
        self.gateway_status = GatewayStatus(self, self.gateway, 'LPS')

        self.gateway_status.grid(
            row=0, column=1, sticky=W+E+N+S, padx=5, pady=5)
        self.gateway_controls.grid(
            row=1, column=1, sticky=W+E+N+S, padx=5, pady=5)


if __name__ == "__main__":
    serial = SerialWrapper(115200, "LPS", bonjour="LAUNCHPADSTATION")

    sensors = LaunchPadStation()

    lps = Gateway(serial, sensors, "./data")

    root = tk.Tk()
    root.title("Launch Pad Control")

    MainApplication(root, lps).pack(side="top", fill="both", expand=True)

    root.mainloop()
