
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from time import time
from tkinter import *
import math

from utils.data_handling import TimeSeries

REFRESH = 16 #delay in ms


########################################
#Generic classes
########################################

##################
#Class to display TimeSeries
##################
#
#__init__(root, database, datalists)
#root - TKinter root window
#clock - the clock that will be used
#time_serise - a list with TimeSeries to display

class GenericGraph():
    def __init__(self, root, clock, time_series, width = 6, height = 4):
        self.clock = clock
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
        relative_time = self.clock.get_current_time()
        self.ax.set_xlim(
            relative_time - 60, relative_time)
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
#value - the TimeSeries that the value will be taken from

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
        if len(self.value.y) == 0:
            return
        self.stringVar.set(self.text + str(self.value.y[-1]))


########################################
#Specific Classes
########################################

class GyroGraph(GenericGraph):
    def __init__(self, root, tm):
        dataLists = [
            tm.data["flight"]["gyrox"],
            tm.data["flight"]["gyroy"],
            tm.data["flight"]["gyroz"]
        ]
        super().__init__(root, tm.clocks["flight"], dataLists)
        self.ax.set_ylim(0, 255)
        self.ax.set_title("rotation - degrees")

class AltitudeGraph(GenericGraph):
    def __init__(self, root, tm):
        super().__init__(root, tm.clocks["flight"], [tm.data["flight"]["altitude"]])
        self.ax.set_ylim(0, 2 ** 12)
        self.ax.set_title("altitude - m")

class PressureGraph(GenericGraph):
    def __init__(self, root, tm):
        super().__init__(root, tm.clocks["flight"], [tm.data["flight"]["pressure"]])
        self.ax.set_ylim(0, 22000)
        self.ax.set_title("pressure - bar")


class AccelerationGraph(GenericGraph):
    def __init__(self, root, tm):
        super().__init__(root, tm.clocks["flight"], [tm.data["flight"]["acceleration"]])
        self.ax.set_ylim(0, 8)
        self.ax.set_title("acceleration - m/s²")

class OpenSerialButton(Button):
    def __init__(self, root, tm):
        super().__init__(root, text="Open serial", command = tm.open_serial)
        self.tm = tm

    def open_serial(self):
        self.tm.start()

class TimeText():
    def __init__(self, root, tm):
        self.stringVar = StringVar()
        self.tm = tm
        self.widget = Label(root, textvariable = self.stringVar)
        self.root = root
        self.update()

    def update(self):
        self.root.after(REFRESH, self.update)    
        self.stringVar.set("time: " + str(int(self.tm.clocks["flight"].get_current_time())))