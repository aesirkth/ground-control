# The code for changing pages was derived from:
# http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/	

import tkinter as tk
from tkinter import ttk

import matplotlib
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
from matplotlib.figure import Figure

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
    pullData = open('./data/telemetry.csv', "r").read()
    dataList = pullData.split('\n')
    xList = []
    yList = []
    for eachLine in dataList[1:]:
        if len(eachLine) > 1:
            x, y = eachLine.split(',')[1:]
            xList.append(int(x))
            yList.append(int(y))

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
        label.pack(pady=10, padx=10)

        button3 = ttk.Button(self, text="Graph Page",
                            command=lambda: controller.show_frame(PageThree))
        button3.pack()


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        canvas1 = FigureCanvasTkAgg(f1, self)
        canvas1.draw()
        canvas1.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        canvas2 = FigureCanvasTkAgg(f2, self)
        canvas2.draw()
        canvas2.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        canvas3 = FigureCanvasTkAgg(f3, self)
        canvas3.draw()
        canvas3.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        canvas4 = FigureCanvasTkAgg(f4, self)
        canvas4.draw()
        canvas4.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)



app = SeaofBTCapp()
ani1 = animation.FuncAnimation(f1, animate, fargs=[a1], interval=100)
ani2 = animation.FuncAnimation(f2, animate, fargs=[a2], interval=200)
ani3 = animation.FuncAnimation(f3, animate, fargs=[a3], interval=400)
ani4 = animation.FuncAnimation(f4, animate, fargs=[a4], interval=800)
app.mainloop()
