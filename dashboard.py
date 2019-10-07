# The code for changing pages was derived from:
# http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/

import threading
import tkinter as tk
from tkinter import ttk

import matplotlib
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
from matplotlib.figure import Figure

from serial_read.serial_read import Telemetry

baudrate = 115200
path = './data'

telemetry = Telemetry(baudrate=baudrate, path=path)
data_path = telemetry.data_path


def run_telemetry():
    
    if not telemetry.port:
        telemetry.find_serial(bonjour="TELEMETRY")
    t = threading.Thread(target=telemetry.start_read)
    t.start()


def stop_telemetry():
    telemetry.stop_read()


matplotlib.use("TkAgg")

LARGE_FONT = ("Verdana", 12)
style.use("ggplot")

f1 = Figure(figsize=(4, 3), dpi=100)
a1 = f1.add_subplot(111)

f2 = Figure(figsize=(4, 3), dpi=100)
a2 = f2.add_subplot(111)

f3 = Figure(figsize=(4, 3), dpi=100)
a3 = f3.add_subplot(111)

f4 = Figure(figsize=(4, 3), dpi=100)
a4 = f4.add_subplot(111)


def animate(i, sub):
    xList = telemetry.data[1]
    yList = telemetry.data[2]

    sub.clear()
    sub.plot(xList, yList)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # tk.Tk.iconbitmap(self, default="clienticon.ico")
        tk.Tk.wm_title(self, "AESIR Dashboard")
        container = tk.Frame(self)
        container.pack(fill=tk.BOTH, expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageThree):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.grid(pady=10, padx=10)

        button3 = ttk.Button(self, text="Graph Page",
                             command=lambda: controller.show_frame(PageThree))
        button3.grid()


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
        label.grid(padx=15, pady=10)
        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.grid(row=1, column=0)
        button2 = ttk.Button(self, text="Start",
                             command=lambda: run_telemetry())
        button2.grid(row=0, column=1)
        button3 = ttk.Button(self, text="Stop",
                             command=lambda: stop_telemetry())
        button3.grid(row=0, column=2)

        canvas1 = FigureCanvasTkAgg(f1, self)
        canvas1.draw()
        canvas1.get_tk_widget().grid(row=1, column=1)

        canvas2 = FigureCanvasTkAgg(f2, self)
        canvas2.draw()
        canvas2.get_tk_widget().grid(row=1, column=2)

        canvas3 = FigureCanvasTkAgg(f3, self)
        canvas3.draw()
        canvas3.get_tk_widget().grid(row=2, column=1)

        canvas4 = FigureCanvasTkAgg(f4, self)
        canvas4.draw()
        canvas4.get_tk_widget().grid(row=2, column=2)


app = SeaofBTCapp()
ani1 = animation.FuncAnimation(f1, animate, fargs=[a1], interval=100)
ani2 = animation.FuncAnimation(f2, animate, fargs=[a2], interval=200)
ani3 = animation.FuncAnimation(f3, animate, fargs=[a3], interval=400)
ani4 = animation.FuncAnimation(f4, animate, fargs=[a4], interval=800)
app.mainloop()
# Stop the serial reading
telemetry.stop_read()
