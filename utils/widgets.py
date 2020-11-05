#widgets.py

from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from time import time
from tkinter import *
import math

from utils.data_functions import TimeSeries

REFRESH = 66 #delay in ms


########################################
#Generic classes
########################################

##################
#Class to display TimeSeries
##################
#
#__init__(root, database, datalists)
#root - TKinter root window
#database - the database used for serial communication
#dataLists - a list with datalists to display

class GenericGraph():
    def __init__(self, root, database, time_series, width = 6, height = 4):
        self.database = database
        self.time_series = time_series
        self.fig = plt.Figure(figsize=(width, height), dpi=100)
        self.ax = self.fig.add_subplot(111)    
        self.lines = []
        #create a line for every series
        for _ in time_series:
            line, = self.ax.plot([], [])
            self.lines.append(line)
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.widget = self.canvas.get_tk_widget()
        self.ani = animation.FuncAnimation(
            self.fig, self.update, interval=REFRESH)
    
    def update(self, i): 
        relative_time = self.database["misc"]["relative_time"] + \
                       time() - self.database["misc"]["relative_time_updated"]
        self.ax.set_xlim(
            relative_time - self.database["misc"]["xlimit"], relative_time)
        for i in range(len(self.time_series)):
            self.lines[i].set_data(self.time_series[i].x, self.time_series[i].y)
        return self.lines,

###################
#class to display the latest value from a TimeSeries
###################
#
#__init__(self, root, text, value)
#root - tkinter root
#text - displayed before the value
#value - the datalist that the value will be taken from

class TextLastValue():
    def __init__(self, root, text, value):
        self.text = text
        self.stringVar = StringVar()
        self.stringVar.set(text)
        self.widget = Label(root, textvariable = self.stringVar)
        self.value = value
        self.root = root
        self.update()

    def update(self):
        self.root.after(REFRESH, self.update)
        #return if there is no value
        if len(self.value.y) == 0:
            return
        self.stringVar.set(self.text + str(self.value.y[-1]))


########################################
#Specific Classes
########################################

class GyroGraph(GenericGraph):
    def __init__(self, root, database):
        dataLists = [
            database["flight"]["gyrox"],
            database["flight"]["gyroy"],
            database["flight"]["gyroz"]
        ]
        super().__init__(root, database, dataLists)
        self.ax.set_ylim(0, 255)
        self.ax.set_title("rotation - degrees")

class AltitudeGraph(GenericGraph):
    def __init__(self, root, database):
        super().__init__(root, database, [database["flight"]["altitude"]])
        self.ax.set_ylim(0, 2 ** 12)
        self.ax.set_title("altitude - m")

class PressureGraph(GenericGraph):
    def __init__(self, root, database):
        super().__init__(root, database, [database["flight"]["pressure"]])
        self.ax.set_ylim(0, 22000)
        self.ax.set_title("pressure - bar")


class AccelerationGraph(GenericGraph):
    def __init__(self, root, database):
        super().__init__(root, database, [database["flight"]["acceleration"]])
        self.ax.set_ylim(0, 8)
        self.ax.set_title("acceleration - m/s²")

class LimitButton(Button):
    def __init__(self, root, database, seconds):
        super().__init__(root, text=str(seconds) + "s", command =  self.update)
        self.seconds = seconds
        self.database = database

    def update(self):
        self.database["misc"]["xlimit"] = self.seconds

class OpenSerialButton(Button):
    def __init__(self, root, database):
        super().__init__(root, text="Open serial", command = self.open_serial)
        self.database = database

    def open_serial(self):
        self.database["misc"]["read_telemetry"] = True

class RelativeTime():
    def __init__(self, root, database):
        self.stringVar = StringVar()
        self.widget = Label(root, textvariable = self.stringVar)
        self.root = root
        self.database = database
        self.update()

    def update(self):
        self.root.after(REFRESH, self.update)
        misc = self.database["misc"]
        relative_time_interpolated = \
            misc["relative_time"] + time() - misc["relative_time_updated"]
        self.stringVar.set("time: " + str(math.floor(relative_time_interpolated)))
