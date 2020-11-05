#main.py
import sys
from threading import Thread, Event
import time
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

from utils.serial_wrapper import SerialWrapper
from utils.data_functions import data_functions, handle_data, TimeSeries
import utils.widgets as widgets

def serial_thread(database):
    SEPARATOR = [0x0A, 0x0D]
    ser = SerialWrapper()

    error= 1 #error variable for ser.openSerial()
    while error:
        #wait for user to start serial
        while not database["misc"]["read_telemetry"]:
            time.sleep(1)
            if database["misc"]["exit"]:
                return

        #init serial wrapper
        error = ser.open_serial('dummy')
        if error:
            print("could not open serial connection")
            print("The microcontroller needs to be reset after every run. Try unplugging it.")
            database["misc"]["read_telemetry"] = False

    #to keep track of the current time gathered from telemetry
    source_time = {}
    source_time_updated = {}
    frameId = 0
    while not database["misc"]["exit"]:
        if not database["misc"]["read_telemetry"]:
            time.sleep(1)
            continue
        
        #test for frame separator, read one byte at a time so it aligns itself
        if not (ser.read_bytes(1) == SEPARATOR[0] and
                ser.read_bytes(1) == SEPARATOR[1]):
            print("Invalid separator. last ID: " + str(frameId))
            continue

        frameId = ser.read_bytes(1)
        data = data_functions[frameId](ser)
        source = data[0].source
        if data[0].measurement == "ms_since_boot":
            source_time.setdefault(source, 0)
            source_time_updated.setdefault(source, 0)
            source_time[source] = data[0].value / 1000 #to seconds
            source_time_updated[source] = time.time()
            #update the dashboards time if it comes from the flight controller
            if source == "flight":
                database["misc"]["relative_time"] = data[0].value / 1000 #to seconds
                database["misc"]["relative_time_updated"] = time.time()
                
        relative_time = source_time[source] + time.time() - source_time_updated[source]
        handle_data(data, relative_time, database)

def main():
    #init database, 
    database = {}
    database["misc"] = {
        "xlimit": 60, #How far back in time the graphs go
        "start_time": time.time(), #when the dashboard was started
        "read_telemetry": False, #if the serial thread should be reading
        "exit": False, #if the program should exit
        "relative_time": 0, #interpolated from the flight engine's time
        #when the relative was last updated, for the interpolation
        "relative_time_updated": time.time() 
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
    
    #init serial thread
    t = Thread(target = serial_thread, args = (database, ))
    t.start()

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
