#main.py
import sys
from threading import Thread, Event
import time
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

from utils.serial_wrapper import SerialWrapper, GatewayWrapper
from utils.data_functions import TimeSeries
from utils.threads import gateway_thread, telemetry_thread
import utils.widgets as widgets

def main():
    #init database, 
    database = {}
    database["misc"] = {
        "read_telemetry": False, #if the telemetry thread should be open and reading
        "last_telemetry_packet": 0, #when the last telemetry packet was reveived
        "read_gateway": False, #if the gateway thread should be open and reading
        "last_gateway_packet": 0, 

        "exit": False, #if the program should exit
        "relative_time": 0, #interpolated from the flight engine's time
        #when the relative was last updated, for the interpolation
        "relative_time_updated": time.time(),
        "xlimit": 60, #How far back in time the graphs go
        "start_time": time.time(), #when the dashboard was started
        
    }
    #There must be a better way to initialize everything...
    database["flight"] = {
        "altitude": TimeSeries(),
        "pressure": TimeSeries(),
        "acceleration": TimeSeries(),
        "gyrox": TimeSeries(),
        "gyroy": TimeSeries(),
        "gyroz": TimeSeries(),
        "ms_since_boot": TimeSeries()
    }
    database["engine"] = {
        "catastrophe": TimeSeries()
    }
    database["gateway"] = {
        
    }
    #init threads
    tm_serial = SerialWrapper()
    tm = Thread(target = telemetry_thread, args = (database, tm_serial))
    tm.start()

    gw_serial = GatewayWrapper()
    gw = Thread(target = gateway_thread, args = (database, gw_serial))
    gw.start()

    #init tk
    root = tk.Tk()
    
    #todo: a better way to organize this
    altitude = widgets.AltitudeGraph(root, database)
    pressure = widgets.PressureGraph(root, database)
    acceleration = widgets.AccelerationGraph(root, database)
    gyro = widgets.GyroGraph(root, database)
    button_5s = widgets.LimitButton(root, database, 5)
    button_30s = widgets.LimitButton(root, database, 30)
    button_60s = widgets.LimitButton(root, database, 60)
    engine_failure = widgets.TextLastValue(
        root, "engine failure: ", database["engine"]["catastrophe"])
    height_value = widgets.TextLastValue(
        root, "altitude: ", database["flight"]["altitude"])
    serial_button = widgets.OpenSerialButton(root, database)
    timeText = widgets.RelativeTime(root, database)

    altitude.widget.grid(padx = 10, pady = 10, column=0, row=0)
    pressure.widget.grid(padx = 10, pady = 10, column=1, row=0)
    acceleration.widget.grid(padx = 10, pady = 10, column=1, row=1)
    gyro.widget.grid(padx = 10, pady = 10, column=0, row=1)
    button_5s.place(x = 10, y = 900)
    button_30s.place(x = 50, y = 900)
    button_60s.place(x = 100, y = 900)
    engine_failure.widget.place(x = 30, y = 950)
    height_value.widget.place(x = 1500, y = 100)
    serial_button.place(x = 1500, y = 130)
    timeText.widget.place(x = 1500, y = 200)

    def on_close():
        database["misc"]["exit"] = True
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()

main()
