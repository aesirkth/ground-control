#main.py
import sys
import time
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

import utils.widgets as widgets
from utils.telemetry import Telemetry
def main():
    #init threads
    tm = Telemetry()
    
    #init tk
    root = tk.Tk()

    altitude = widgets.AltitudeGraph(root, tm)
    pressure = widgets.PressureGraph(root, tm)
    acceleration = widgets.AccelerationGraph(root, tm)
    gyro = widgets.GyroGraph(root, tm)
    serial_button = widgets.OpenSerialButton(root, tm)
    timeText = widgets.TimeText(root, tm)

    altitude.widget.grid(padx = 10, pady = 10, column=0, row=0)
    pressure.widget.grid(padx = 10, pady = 10, column=1, row=0)
    acceleration.widget.grid(padx = 10, pady = 10, column=1, row=1)
    gyro.widget.grid(padx = 10, pady = 10, column=0, row=1)
    serial_button.place(x = 1500, y = 130)
    timeText.widget.place(x = 1500, y = 200)

    def on_close():
        tm.exit = True
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()

main()
