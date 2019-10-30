import tkinter as tk
from tkinter import E, N, S, W

import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from gui import GatewayStatus, MessageBox
from utils import Gateway, Sensors, SerialWrapper


class LiveTimeGraph(tk.Frame):
    def __init__(self, parent, gateway, sensor, field, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.gateway = gateway
        self.sensor = sensor
        self.field = field

        self.fig = Figure(figsize=(4, 3), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.line, = self.ax.plot([], [], lw=2)
        self.ax.grid()
        self.time = []
        self.data = []

        self.canvas = FigureCanvasTkAgg(self.fig, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=1, column=1)

        ani = animation.FuncAnimation(self.fig, self.__update_data, blit=True, interval=10,
                                      repeat=False, init_func=self.__init_figure)

    def __init_figure(self):
        self.ax.set_ylim(0, 50)
        self.ax.set_xlim(0, 10000)
        del self.time[:]
        del self.data[:]
        self.line.set_data(self.time, self.data)
        return self.line,

    def __update_data(self, data):
        tmin, tmax = self.ax.get_xlim()

        self.time = self.sensor.data.time.tolist()
        self.data = self.sensor.data[self.field].tolist()

        if self.time:
            if max(self.time) > tmax:
                self.ax.set_xlim(tmin, 2*tmax)

        self.line.set_data(self.time, self.data)

        return self.line,


class MainApplication(tk.Frame):
    """ TKinter frame holding some useful widgets to control the Launch Pad Station

    Parameters
    ----------
    parent : Tkinter TK() instance
        TK() instance to hold the widgets
    gateway : Gateway instance
        Gateway instance correctly set for the LPS Gateway

    """

    def __init__(self, parent, gateway, sensors, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.gateway = gateway
        self.sensors = sensors

        self.gateway_messages = MessageBox(
            self, gateway=self.gateway, borderwidth=2, relief="groove")
        self.graph = LiveTimeGraph(
            self, gateway=self.gateway, sensor=self.sensors.imu, field="velocity")
        self.gateway_status = GatewayStatus(self, gateway=self.gateway)

        self.gateway_status.grid(
            row=0, column=1, sticky=W+E+N+S, padx=5, pady=5)
        self.graph.grid(
            row=0, rowspan=2, column=2, sticky=W+E+N+S, padx=5, pady=5)
        self.gateway_messages.grid(
            row=1, column=1, sticky=W+E+N+S, padx=5, pady=5)


if __name__ == "__main__":
    baudrate = 115200
    path = './data'

    serial = SerialWrapper(baudrate=baudrate, bonjour="TELEMETRY")
    sensors = Sensors(imu="Test")
    telemetry = Gateway(serial=serial, sensors=sensors,
                        path=path, name="telemetry")

    root = tk.Tk()
    root.title("Launch Pad Control")

    MainApplication(parent=root, gateway=telemetry, sensors=sensors).pack(
        side="top", fill="both", expand=True)

    root.mainloop()
