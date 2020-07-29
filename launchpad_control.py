""" Simple Graphical User Gateway that can control the Launchpad Controller

This GUI can:
    - Open and close the Serial link to the Launchpad Gateway
    - Send commands to the Launchpad Gateway via simple buttons
    - Display the messages received from the Launchpad Gateway
"""

import tkinter as tk
from tkinter import E, N, S, W

from gui import LaunchpadWidget
from utils import Gateway, LaunchpadControl, SerialWrapper


class MainApplication(tk.Frame):
    """ TKinter frame holding some useful widgets to control the Launch Pad Station

    Parameters
    ----------
    parent : Tkinter TK() instance
        TK() instance to hold the widgets
    gateway : Gateway instance
        Gateway instance correctly set for the Launchpad Gateway

    """

    def __init__(self, parent, lps, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        
        self.widget = LaunchpadWidget(self, lps, *args, **kwargs)
        self.widget.grid(row=1, column=0)


if __name__ == "__main__":
    serial = SerialWrapper(115200, "LC", bonjour="LAUNCHPADCONTROLLER")

    sensors = LaunchpadControl()

    lps = Gateway(serial, sensors, "./data")

    root = tk.Tk()
    root.title("Launchpad Control")

    MainApplication(root, lps).pack(side="top", fill="both", expand=True)

    root.mainloop()
