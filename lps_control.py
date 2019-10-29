""" Simple Graphical User Gateway that can control the Launch Pad Station

This GUI can:
    - Open and close the Serial link to the LPS Gateway
    - Send commands to the LPS Gateway via simple buttons
    - Display the messages received from the LPS Gateway
"""

import tkinter as tk
from tkinter import E, N, S, W

from gui import CommandButtons, GatewayStatus, MessageBox
from utils import Gateway, SerialWrapper


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
        self.lps = gateway

        self.lps_messages = MessageBox(self, self.lps, borderwidth=2, relief="groove")
        self.lps_controls = CommandButtons(self, self.lps)
        self.lps_status = GatewayStatus(self, self.lps)

        self.lps_status.grid(
            row=0, column=1, sticky=W+E+N+S, padx=5, pady=5)
        self.lps_controls.grid(
            row=1, column=1, sticky=W+E+N+S, padx=5, pady=5)
        self.lps_messages.grid(
            row=2, column=1, sticky=W+E+N+S, padx=5, pady=5)


if __name__ == "__main__":
    baudrate = 115200
    path = './data'
    serial = SerialWrapper(baudrate=baudrate, bonjour = "LAUNCHPADSTATION")
    lps = Gateway(serial=serial, path=path, name="lps")

    root = tk.Tk()
    root.title("Launch Pad Control")

    MainApplication(root, lps).pack(side="top", fill="both", expand=True)

    root.mainloop()
