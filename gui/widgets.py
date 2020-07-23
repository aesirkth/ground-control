import copy
import datetime
import tkinter as tk
from tkinter import E, N, S, W

import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

BD = 0


# ########################### #
#   General purpose widgets   #
# ########################### #


class GatewayStatus(tk.Frame):
    """ TKinter frame to monitor the status of the Serial link

    Reading from the Serial link is started in a separate thread with Threading and
    stopped on the destruction of this frame

    Parameters
    ----------
    parent : TKinter Frame
        parent frame
    gateway : Gateway instance
        Gateway to monitor
    field : GS or TM/FPV
    """

    def __init__(self, parent, gateway, name, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.gateway = gateway
        self.name = name

        # Name to separate the buttons
        tk.Label(self, text=self.name).grid(row=0, column=0)
        # Button to open/close the Serial link
        self.button_var = tk.StringVar()
        self.read_button = tk.Button(self, textvariable=self.button_var)
        self.read_button.grid(row=1, column=0)
        # Label to display the gateway's port name
        self.port_var = tk.StringVar()
        self.port_var.set("Port : {}".format(
            self.gateway.serial.ser.port))
        tk.Label(self, textvariable=self.port_var).grid(
            row=0, column=1, sticky=W)
        # Label to display the error status
        self.error_var = tk.StringVar()
        self.error_var.set("")
        tk.Label(self, textvariable=self.error_var).grid(
            row=1, column=1, sticky=W)

        self.__update_port()
        self.__update_error()
        self.__update_button()

    def destroy(self):
        """" Catch the destruction of the widget and stop the Serial reading

        If this is not done properly the Threading thread that reads data from
        the Serial link cannot be stopped

        """
        self.gateway.stop_read()
        tk.Frame.destroy(self)

    def __update_port(self):
        """ Update the port name displayed

        """
        self.port_var.set("Port : {}".format(
            self.gateway.serial.ser.port))
        # Call this function again after 100 ms
        self.parent.after(100, self.__update_port)

    def __update_error(self):
        """ Update the error displayed

        """
        failed = self.gateway.serial.failed
        if failed:
            message = self.gateway.serial.error
            self.error_var.set("Status : {}".format(message))
        else:
            self.error_var.set("Status : Ok")
        # Call this function again after 100 ms
        self.parent.after(100, self.__update_error)

    def __update_button(self):
        """ Set the behaviour of the button to open or close the Serial link

        """
        if self.gateway.serial.get_status():
            self.read_button.config(command=self.gateway.stop_read)
            self.button_var.set("Close link")
        else:
            self.read_button.config(command=self.gateway.start_read)
            self.button_var.set("Open link")

        # Call this function again after 100 ms
        self.parent.after(100, self.__update_button)


class BoolFieldIndicator(tk.Frame):
    """ TKinter frame that holds a TKinter square of color and a label

    The box changes color depending on status of sensor

    Parameters
    ----------
    parent : TKinter Frame
        parent frame
    sensor : attribute of a Sensors instance
        sensor to display status from
    field : str
        dictionary key of the field to check
    text : str
        text to display next to the indicator

    """

    def __init__(self, parent, sensor, field, text, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.sensor = sensor
        self.field = field
        self.text = text

        # Button to make a colored "box" for sensor
        # Style will be reflected on this button
        self.btn = tk.Button(self, text='', height=1,
                             width=1, state=tk.DISABLED)
        self.btn.grid(row=0, column=1, sticky=W+E)
        self.label = tk.Label(self, text=self.text)
        self.label.grid(row=0, column=2, padx=5, sticky=W+E)

        self.__update_button()

    def __update_button(self):
        """ Set the style of the button depending on the status of sensor.

        """
        if self.sensor.data[self.field] is None:
            self.btn.config(bg='grey')
        else:
            if self.sensor.data[self.field]:
                self.btn.config(bg='red')
            else:
                self.btn.config(bg='green')
        # Call this function again after 100 ms
        self.parent.after(100, self.__update_button)


class GeneralData(tk.Frame):
    """ TKinter frame that holds a label and displays changeable string

        The label is the name of measured value. The int/scalar shows the value for the value.

        Parameters
        ----------
        parent : TKinter Frame
            parent frame
        gateway : Gateway instance
            Gateway to monitor
        data(sensor?) : data from functions calculating or directly from the TM.
            data to display value from
        field : str
            name of the data to display

    """

    def __init__(self, parent, gateway, data, field, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.gateway = gateway
        self.data = data
        self.field = field

        self.label = tk.Label(self, text=self.field + ": ")
        self.label.grid(row=0, column=1)
        self.data_var = tk.StringVar()
        self.show_data = tk.Label(self, text=self.data_var)
        self.show_data.grid(row=0, column=2)

        self.__update_value()

    def __update_value(self):
        if self.field == "Battery":
            # This has to be changed to point to battery value.
            self.data_var.set(self.gateway.data)
        elif self.field == "|V|":
            # This has to be changed to point to calculated |V|.
            self.data_var.set(self.gateway.data)
        elif self.field == "Longitude":
            # This has to be changed to point to longitude value.
            self.data_var.set(self.gateway.data)
        elif self.field == "Latitude":
            # This has to be changed to point to latitude value.
            self.data_var.set(self.gateway.data)
        # Add an else of some sort, don't know where to print the error.
        else:
            print("General data could not be categorized")
        self.parent.after(100, self.__update_value)


# ############################# #
#   Widgets for the Telemetry   #
# ############################# #


class TelemetryWidget(tk.Frame):
    def __init__(self, parent, gateway, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.gateway = gateway
        self.sensors = self.gateway.sensors

        self.telemetry_status = GatewayStatus(self, self.gateway, 'Telemetry')

        self.telemetry_status.grid(
            row=1, column=1, sticky=W, padx=10, pady=8)

        self.Buttons = tk.Frame(self)
        self.Buttons.grid(
            row=2, column=1, sticky=W, padx=10, pady=(0, 5))

        self.button_set_reference = tk.Button(
            self.Buttons, text="Set reference", command=self._set_reference)
        self.button_set_reference.grid(row=0, column=0)

        self.button_reset = tk.Button(
            self.Buttons, text="Reset", command=self._reset)
        self.button_reset.grid(row=0, column=1)

        self.TimeInterval = tk.Frame(self)
        self.TimeInterval.grid(row=3, column=1, sticky=W, padx=10, pady=(0, 8))

        self.button_30s = tk.Button(
            self.TimeInterval, text="30s", command=self._set_30s)
        self.button_30s.grid(row=0, column=0)

        self.button_6min = tk.Button(
            self.TimeInterval, text="6min", command=self._set_6min)
        self.button_6min.grid(row=0, column=1)

        self.button_all = tk.Button(
            self.TimeInterval, text="All", command=self._set_all)
        self.button_all.grid(row=0, column=2)

        self.button_freeze= tk.Button(
            self.TimeInterval, text="Freeze", command=self._freeze)
        self.button_freeze.grid(row=0, column=3)

    def _set_reference(self):
        self.sensors.set_reference()

    def _reset(self):
        self.sensors.reset()
        self.gateway.reset()
    
    def _set_30s(self):
        self.sensors.time_interval = 30
    
    def _set_6min(self):
        self.sensors.time_interval = 6*60

    def _set_all(self):
        self.sensors.time_interval = float('inf')

    def _freeze(self):
        if self.sensors.update_plot:
            self.sensors.update_plot = False
        else:
            self.sensors.update_plot = True


################ Rocket Status ################


class ErrorState(tk.Frame):
    def __init__(self, parent, gateway, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.gateway = gateway
        self.sensors = self.gateway.sensors

        self.title = tk.Label(self, text="Errors")
        self.title.grid(row=0, column=0, columnspan=2, sticky=W+E)

        self.loop = BoolFieldIndicator(
            self, self.sensors.errmsg, "ERR_LOOP_TIME", "loop time")
        self.sd_write = BoolFieldIndicator(
            self, self.sensors.errmsg, "ERR_WRITE_SD", "write SD")
        self.sd_sync = BoolFieldIndicator(
            self, self.sensors.errmsg, "ERR_SYNC_SD", "sync SD")
        self.tm_send = BoolFieldIndicator(
            self, self.sensors.errmsg, "ERR_SEND_TM", "send TM")
        self.imu_read = BoolFieldIndicator(
            self, self.sensors.errmsg, "ERR_READ_IMU", "read imu")

        self.loop.grid(
            row=1, column=0, sticky=W+E)
        # self.imu3_status.grid(
        #     row=2, column=0, sticky=W+E)
        self.sd_write.grid(
            row=2, column=0, sticky=W+E)
        self.sd_sync.grid(
            row=3, column=0, sticky=W+E)
        self.tm_send.grid(
            row=1, column=1, sticky=W+E)
        self.imu_read.grid(
            row=2, column=1, sticky=W+E)


class BatteryIndicator(tk.Frame):
    def __init__(self, parent, gateway, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.gateway = gateway

        self.battery1_txt = tk.StringVar()
        self.battery1 = tk.Label(self, textvar=self.battery1_txt)
        self.battery1.grid(row=0, column=0, sticky=W)

        # self.battery2_txt = tk.StringVar()
        # self.battery2 = tk.Label(self, textvar=self.battery2_txt)
        # self.battery2.grid(row=1, column=0, sticky=W)

        self._update_label()

    def _update_label(self):
        voltage_battery1 = self.gateway.sensors.batteries.data['Battery1']
        txt1 = "Battery: {:05.2f}V".format(voltage_battery1)
        self.battery1_txt.set(txt1)
        # voltage_battery2 = self.gateway.sensors.batteries.data['Battery2']
        # txt2 = "Battery 2 : {:3.2f}V".format(voltage_battery2)
        # self.battery2_txt.set(txt2)

        # Call this function again after 100 ms
        self.parent.after(100, self._update_label)


class TimeIndicator(tk.Frame):
    def __init__(self, parent, gateway, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.gateway = gateway

        self.rtc_txt = tk.StringVar()
        self.rtc = tk.Label(self, textvar=self.rtc_txt)
        self.rtc.grid(row=0, column=0)

        # self.timer_txt = tk.StringVar()
        # self.timer = tk.Label(self, textvar=self.timer_txt)
        # self.timer.grid(row=1, column=0)

        self._update_time()

    def _update_time(self):
        rtc_time = self.gateway.sensors.rtc.data
        txt = "{}:{:02d}:{:02d}.{:02d}".format(
            rtc_time['Hour'], rtc_time['Minute'], rtc_time['Second'], int(rtc_time['Microsecond']/1e4))
        self.rtc_txt.set(txt)

        # timer_time = self.gateway.sensors.timer.data['Timer']
        # txt = "{:7.3f}".format(timer_time)
        # self.timer_txt.set(txt)
        
        self.parent.after(100, self._update_time)


class ParachuteIndicator(tk.Frame):
    def __init__(self, parent, gateway, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.gateway = gateway
        self.status = self.gateway.sensors.status

        self.parachute = tk.Label(self, text="Parachute")
        self.parachute.grid(row=0, column=0)

        self.parachute_ign_txt = tk.StringVar()
        self.parachute_ign = tk.Label(self, textvar=self.parachute_ign_txt)
        self.parachute_ign.grid(row=1, column=0, sticky=W)

        self.parachute_arduino_arm_txt = tk.StringVar()
        self.parachute_arduino_arm = tk.Label(self, textvar=self.parachute_arduino_arm_txt)
        self.parachute_arduino_arm.grid(row=2, column=0, sticky=W)

        self.parachute_arm_txt = tk.StringVar()
        self.parachute_arm = tk.Label(self, textvar=self.parachute_arm_txt)
        self.parachute_arm.grid(row=3, column=0, sticky=W)

        self.parachute_trig_txt = tk.StringVar()
        self.parachute_trig = tk.Label(self, textvar=self.parachute_trig_txt)
        self.parachute_trig.grid(row=4, column=0, sticky=W)

        self._update_parachute()
    
    def _update_parachute(self):
        if self.status.data['STATUS_1'] & 1 << 3:
            self.parachute_ign_txt.set('Igniting : yes')
            self.parachute_ign.config(bg='green')
        else:
            self.parachute_ign_txt.set('Igniting : no')
            self.parachute_ign.config(bg='grey')

        if self.status.data['STATUS_1'] & 1 << 4:
            self.parachute_arduino_arm_txt.set('Arduino arming : yes')
            self.parachute_arduino_arm.config(bg='green')
        else:
            self.parachute_arduino_arm_txt.set('Arduino arming : no')
            self.parachute_arduino_arm.config(bg='grey')

        if self.status.data['STATUS_2'] & 1 << 2:
            self.parachute_arm_txt.set('Arming : yes')
            self.parachute_arm.config(bg='green')
        else:
            self.parachute_arm_txt.set('Arming : no')
            self.parachute_arm.config(bg='grey')

        if self.status.data['STATUS_2'] & 1 << 7:
            self.parachute_trig_txt.set('Trigger : yes')
            self.parachute_trig.config(bg='green')
        else:
            self.parachute_trig_txt.set('Trigger : no')
            self.parachute_trig.config(bg='grey')
        
        self.parent.after(100, self._update_parachute)


class FlightStatus(tk.Frame):
    def __init__(self, parent, gateway, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.gateway = gateway
        self.status = self.gateway.sensors.status

        self.flight = tk.Label(self, text="Flight status")
        self.flight.grid(row=0, column=0)

        self.liftoff_txt = tk.StringVar()
        self.liftoff = tk.Label(self, textvar=self.liftoff_txt)
        self.liftoff.grid(row=1, column=0, sticky=W)

        self.apogee_txt = tk.StringVar()
        self.apogee = tk.Label(self, textvar=self.apogee_txt)
        self.apogee.grid(row=2, column=0, sticky=W)

        self._update_flight()
    
    def _update_flight(self):
        if self.status.data['STATUS_1'] & 1 << 1:
            self.liftoff_txt.set('Liftoff : yes')
            self.liftoff.config(bg='green')
        else:
            self.liftoff_txt.set('Liftoff : no')
            self.liftoff.config(bg='grey')

        if self.status.data['STATUS_1'] & 1 << 2:
            self.apogee_txt.set('Apogee : yes')
            self.apogee.config(bg='green')
        else:
            self.apogee_txt.set('Apogee : no')
            self.apogee.config(bg='grey')
        
        self.parent.after(100, self._update_flight)


class RocketStatus(tk.Frame):
    def __init__(self, parent, gateway, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.gateway = gateway

        self.batteries = BatteryIndicator(self, self.gateway, bd=BD, relief="solid")
        self.batteries.grid(row=0, column=0, padx=10, pady=(8, 0))

        self.time = TimeIndicator(self, self.gateway, bd=BD, relief="solid")
        self.time.grid(row=0, column=1, padx=10, pady=(5, 0))

        self.parachute = ParachuteIndicator(self, self.gateway, bd=BD, relief="solid")
        self.parachute.grid(row=1, column=0, columnspan=2, padx=10, pady=(5, 0), sticky=W)

        self.flight = FlightStatus(self, self.gateway, bd=BD, relief="solid")
        self.flight.grid(row=2, column=0, columnspan=2, padx=10, pady=(5, 0), sticky=W)

        self.error_status = ErrorState(self, self.gateway, bd=BD, relief="solid")
        self.error_status.grid(row=3, column=0, columnspan=2, padx=10, pady=(5, 8))

        self.update()


################ Plots ################


class LiveTimeGraphAirSpeed(tk.Frame):
    """ TKinter frame that holds a matplotlib graph that is frequently updated

    The graph is plotted against time. The sensor must have a data.time attribute.

    Parameters
    ----------
    parent : TKinter Frame
        parent frame
    gateway : Gateway instance
        Gateway to monitor
    sensor : attribute of a Sensors instance
        sensor to display data from
    field : str
        name of the data field to display

    """

    def __init__(self, parent, gateway, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.gateway = gateway
        self.sensors = self.gateway.sensors
        self.pitot = self.gateway.sensors.pitot

        self.last_update = 0

        self.fig = Figure(figsize=(5, 3.4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.line, = self.ax.plot([], [], lw=1)
        self.ax.grid()
        self.time = []
        self.data = []

        self.canvas = FigureCanvasTkAgg(self.fig, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=1, column=1)

        ani = animation.FuncAnimation(self.fig, self._update_data, blit=True, interval=10,
                                      repeat=False, init_func=self._init_figure)

    def _init_figure(self):
        """ Set the initial values and settings of the figure

        """
        self.ax.set_ylim(0, 150)
        self.ax.set_xlim(0, 1)
        self.ax.set_title("Pitot pressure (hPa)", y=1.1)
        self.canvas.draw()
        self.last_update = 0
        del self.time[:]
        del self.data[:]
        self.line.set_data(self.time, self.data)
        return self.line,

    def _update_data(self, data):
        """ Refresh the figure content

        Parameters
        ----------
        data : unused
            default parameter given by animation.FuncAnimation

        Returns
        -------
        tupple
            content of the figure for matplotlib        

        """
        if not self.sensors.update_plot:
            return self.line,

        if not self.pitot.is_pressure_graph_init:
            self._init_figure()
            self.pitot.is_pressure_graph_init = True

        self.time = self.pitot.raw_data['Seconds_since_start'][:]
        self.data = self.pitot.data['Air speed'][:]
        len_t = len(self.time)
        len_data = len(self.data)

        if len_t == len_data:
            if len_t > 0:
                max_time = self.time[-1]
                min_time = self.time[0]

                if max_time - min_time > self.sensors.time_interval:
                    index = [i for i, e in enumerate(self.time) if max_time - e > self.sensors.time_interval][-1]
                else:
                    index = 0

                new_tmax = self.time[-1]
                if new_tmax - self.last_update > 0.5:
                    self.last_update = new_tmax
                    new_tmin = self.time[index]
                    self.ax.set_xlim(new_tmin, new_tmax + (new_tmax-new_tmin)*0.1)
                    self.canvas.draw()

            self.line.set_data(self.time, self.data)

        return self.line,


class LiveTimeGraphAcc(tk.Frame):
    """ TKinter frame that holds a matplotlib graph that is frequently updated

    The graph is plotted against time. The sensor must have a data.time attribute.

    Parameters
    ----------
    parent : TKinter Frame
        parent frame
    gateway : Gateway instance
        Gateway to monitor
    sensor : attribute of a Sensors instance
        sensor to display data from
    field : str
        name of the data field to display

    """

    def __init__(self, parent, gateway, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.gateway = gateway
        self.sensors = self.gateway.sensors
        self.imu = gateway.sensors.imu2

        self.last_update = 0

        self.fig = Figure(figsize=(5, 3.4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.x_value, = self.ax.plot([], [], lw=1)
        self.y_value, = self.ax.plot([], [], lw=1)
        self.z_value, = self.ax.plot([], [], lw=1)
        self.x_value.set_label('x-axis')
        self.y_value.set_label('y-axis')
        self.z_value.set_label('z-axis')
        self.ax.legend(loc="upper left")
        self.ax.grid()
        self.time = []
        self.x_data = []
        self.y_data = []
        self.z_data = []

        self.canvas = FigureCanvasTkAgg(self.fig, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=1, column=1)

        ani = animation.FuncAnimation(self.fig, self._update_data, blit=True, interval=10,
                                      repeat=False, init_func=self._init_figure)

    def _init_figure(self):
        """ Set the initial values and settings of the figure

        """
        self.ax.set_ylim(-16, 16)
        self.ax.set_xlim(0, 1)
        self.ax.set_title("Accelerometer (g)", y=1.1)
        self.canvas.draw()
        self.last_update = 0
        del self.time[:]
        del self.x_data[:]
        del self.y_data[:]
        del self.z_data[:]
        self.x_value.set_data(self.time, self.x_data)
        self.y_value.set_data(self.time, self.y_data)
        self.z_value.set_data(self.time, self.z_data)
        return self.x_value, self.y_value, self.z_value,

    def _update_data(self, data):
        """ Refresh the figure content

        Parameters
        ----------
        data : unused
            default parameter given by animation.FuncAnimation

        Returns
        -------
        tupple
            content of the figure for matplotlib

        """
        if not self.sensors.update_plot:
            return self.x_value, self.y_value, self.z_value,

        if not self.imu.is_acc_graph_init:
            self._init_figure()
            self.imu.is_acc_graph_init = True

        self.time = self.imu.raw_data['Seconds_since_start'][:]
        self.x_data = self.imu.raw_data['Acc_X'][:]
        self.y_data = self.imu.raw_data['Acc_Y'][:]
        self.z_data = self.imu.raw_data['Acc_Z'][:]
        len_t = len(self.time)
        len_acc_x = len(self.x_data)
        len_acc_y = len(self.y_data)
        len_acc_z = len(self.z_data)

        if len_t == len_acc_x and len_t == len_acc_y and len_t == len_acc_z:
            if len_t > 0:
                max_time = self.time[-1]
                min_time = self.time[0]

                if max_time - min_time > self.sensors.time_interval:
                    index = [i for i, e in enumerate(self.time) if max_time - e > self.sensors.time_interval][-1]
                    
                else:
                    index = 0

                new_tmax = self.time[-1]
                if new_tmax - self.last_update > 0.5:
                    self.last_update = new_tmax
                    new_tmin = self.time[index]
                    self.ax.set_xlim(new_tmin, new_tmax + (new_tmax-new_tmin)*0.1)
                    self.canvas.draw()

            self.x_value.set_data(self.time, self.x_data)
            self.y_value.set_data(self.time, self.y_data)
            self.z_value.set_data(self.time, self.z_data)

        return self.x_value, self.y_value, self.z_value,


class LiveTimeGraphGyro(tk.Frame):
    """ TKinter frame that holds a matplotlib graph that is frequently updated

    The graph is plotted against time. The sensor must have a data.time attribute.

    Parameters
    ----------
    parent : TKinter Frame
        parent frame
    gateway : Gateway instance
        Gateway to monitor
    sensor : attribute of a Sensors instance
        sensor to display data from
    field : str
        name of the data field to display

    """

    def __init__(self, parent, gateway, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.gateway = gateway
        self.sensors = self.gateway.sensors
        self.imu = self.gateway.sensors.imu2

        self.last_update = 0

        self.fig = Figure(figsize=(5, 3.4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.x_value, = self.ax.plot([], [], lw=1)
        self.y_value, = self.ax.plot([], [], lw=1)
        self.z_value, = self.ax.plot([], [], lw=1)
        self.x_value.set_label('x-axis')
        self.y_value.set_label('y-axis')
        self.z_value.set_label('z-axis')
        self.ax.legend(loc="upper left")
        self.ax.grid()
        self.time = []
        self.x_data = []
        self.y_data = []
        self.z_data = []

        self.canvas = FigureCanvasTkAgg(self.fig, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=1, column=1)

        ani = animation.FuncAnimation(self.fig, self._update_data, blit=True, interval=10,
                                      repeat=False, init_func=self._init_figure)

    def _init_figure(self):
        """ Set the initial values and settings of the figure

        """
        self.ax.set_ylim(-1000, 1000)
        self.ax.set_xlim(0, 1)
        self.ax.set_title("Gyrometer (dps)", y=1.1)
        self.canvas.draw()
        self.last_update = 0
        del self.time[:]
        del self.x_data[:]
        del self.y_data[:]
        del self.z_data[:]
        self.x_value.set_data(self.time, self.x_data)
        self.y_value.set_data(self.time, self.y_data)
        self.z_value.set_data(self.time, self.z_data)
        return self.x_value, self.y_value, self.z_value,

    def _update_data(self, data):
        """ Refresh the figure content

        Parameters
        ----------
        data : unused
            default parameter given by animation.FuncAnimation

        Returns
        -------
        tupple
            content of the figure for matplotlib

        """
        if not self.sensors.update_plot:
             return self.x_value, self.y_value, self.z_value,

        if not self.imu.is_gyro_graph_init:
            self._init_figure()
            self.imu.is_gyro_graph_init = True

        self.time = self.imu.raw_data['Seconds_since_start'][:]
        self.x_data = self.imu.raw_data['Gyro_X'][:]
        self.y_data = self.imu.raw_data['Gyro_Y'][:]
        self.z_data = self.imu.raw_data['Gyro_Z'][:]
        len_t = len(self.time)
        len_gyro_x = len(self.x_data)
        len_gyro_y = len(self.y_data)
        len_gyro_z = len(self.z_data)

        if len_t == len_gyro_x and len_t == len_gyro_y and len_t == len_gyro_z:
            if len_t > 0:
                max_time = self.time[-1]
                min_time = self.time[0]

                if max_time - min_time > self.sensors.time_interval:
                    index = [i for i, e in enumerate(self.time) if max_time - e > self.sensors.time_interval][-1]
                    
                else:
                    index = 0

                new_tmax = self.time[-1]
                if new_tmax - self.last_update > 0.5:
                    self.last_update = new_tmax
                    new_tmin = self.time[index]
                    self.ax.set_xlim(new_tmin, new_tmax + (new_tmax-new_tmin)*0.1)
                    self.canvas.draw()

            self.x_value.set_data(self.time, self.x_data)
            self.y_value.set_data(self.time, self.y_data)
            self.z_value.set_data(self.time, self.z_data)

        return self.x_value, self.y_value, self.z_value,


class LiveTimeGraphAltitude(tk.Frame):
    """ TKinter frame that holds a matplotlib graph that is frequently updated

    The graph is plotted against time

    Parameters
    ----------
    parent : TKinter Frame
        parent frame
    gateway : Gateway instance
        Gateway to monitor

    """

    def __init__(self, parent, gateway, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.gateway = gateway
        self.sensors = self.gateway.sensors
        self.bmp2 = self.gateway.sensors.bmp2
        self.bmp3 = self.gateway.sensors.bmp3

        self.last_update = 0

        self.fig = Figure(figsize=(5, 3.4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.altitude1, = self.ax.plot([], [], lw=1)
        self.altitude2, = self.ax.plot([], [], lw=1)
        self.altitude1.set_label('BMP2')
        self.altitude2.set_label('BMP3')
        self.ax.legend(loc="upper left")
        self.ax.grid()
        self.time = []
        self.bmp1_data = []
        self.bmp2_data = []

        self.canvas = FigureCanvasTkAgg(self.fig, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=1, column=1)

        ani = animation.FuncAnimation(self.fig, self._update_data, blit=True, interval=10,
                                      repeat=False, init_func=self._init_figure)

    def _init_figure(self):
        """ Set the initial values and settings of the figure

        """
        self.ax.set_ylim(800, 1200)
        self.ax.set_xlim(0, 1)
        self.ax.set_title("Static pressure (hPa)", y=1.1)
        self.canvas.draw()
        self.last_update = 0
        del self.time[:]
        del self.bmp1_data[:]
        del self.bmp2_data[:]
        self.altitude1.set_data(self.time, self.bmp1_data)
        self.altitude2.set_data(self.time, self.bmp2_data)
        return self.altitude1, self.altitude2,

    def _update_data(self, data):
        """ Refresh the figure content

        Parameters
        ----------
        data : unused
            default parameter given by animation.FuncAnimation

        Returns
        -------
        tupple
            content of the figure for matplotlib

        """
        if not self.sensors.update_plot:
            return self.altitude1, self.altitude2,

        if not self.bmp2.is_pressure_graph_init:
            self._init_figure()
            self.bmp2.is_pressure_graph_init = True

        self.time = self.bmp2.raw_data['Seconds_since_start'][:]
        self.x_data = self.bmp2.data['Pressure hPa'][:]
        self.y_data = self.bmp3.data['Pressure hPa'][:]
        len_t = len(self.time)
        len_bmp2 = len(self.x_data)
        len_bmp3 = len(self.y_data)

        if len_t == len_bmp2 and len_t == len_bmp3:
            if len_t > 0:
                max_time = self.time[-1]
                min_time = self.time[0]

                if max_time - min_time > self.sensors.time_interval:
                    index = [i for i, e in enumerate(self.time) if max_time - e > self.sensors.time_interval][-1]
                    
                else:
                    index = 0

                new_tmax = self.time[-1]
                if new_tmax - self.last_update > 0.5:
                    self.last_update = new_tmax
                    new_tmin = self.time[index]
                    self.ax.set_xlim(new_tmin, new_tmax + (new_tmax-new_tmin)*0.1)
                    self.canvas.draw()

            self.altitude1.set_data(self.time, self.x_data)
            self.altitude2.set_data(self.time, self.y_data)

        return self.altitude1, self.altitude2,


################ GPS ################


class GPSValues(tk.Frame):
    def __init__(self, parent, gateway, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.gateway = gateway
        self.gps = self.gateway.sensors.gps

        self.latitude = tk.Label(self, text="Latitude:")
        self.latitude.grid(row=0, column=0, sticky=W, pady=(3, 0))
        self.latitude_txt = tk.StringVar()
        self.latitude_label = tk.Label(self, textvar=self.latitude_txt)
        self.latitude_label.grid(row=0, column=1, sticky=W, pady=(3, 0))

        self.longitude = tk.Label(self, text="Longitude:")
        self.longitude.grid(row=1, column=0, sticky=W, pady=(3, 0))
        self.longitude_txt = tk.StringVar()
        self.longitude_label = tk.Label(self, textvar=self.longitude_txt)
        self.longitude_label.grid(row=1, column=1, sticky=W, pady=(3, 0))

        self.altitude = tk.Label(self, text="Altitude:")
        self.altitude.grid(row=2, column=0, sticky=W, pady=(3, 0))
        self.altitude_txt = tk.StringVar()
        self.altitude_label = tk.Label(self, textvar=self.altitude_txt)
        self.altitude_label.grid(row=2, column=1, sticky=W, pady=(3, 0))

        self.heading = tk.Label(self, text="Heading:")
        self.heading.grid(row=3, column=0, sticky=W, pady=(3, 0))
        self.heading_txt = tk.StringVar()
        self.heading_label = tk.Label(self, textvar=self.heading_txt)
        self.heading_label.grid(row=3, column=1, sticky=W, pady=(3, 0))

        self.speed = tk.Label(self, text="Ground speed:")
        self.speed.grid(row=4, column=0, sticky=W, pady=(3, 0))
        self.speed_txt = tk.StringVar()
        self.speed_label = tk.Label(self, textvar=self.speed_txt)
        self.speed_label.grid(row=4, column=1, sticky=W, pady=(3, 0))

        self.distance = tk.Label(self, text="Distance:")
        self.distance.grid(row=5, column=0, sticky=W, pady=(3, 0))
        self.distance_txt = tk.StringVar()
        self.distance_label = tk.Label(self, textvar=self.distance_txt)
        self.distance_label.grid(row=5, column=1, sticky=W, pady=(3, 0))

        self.bearing = tk.Label(self, text="Bearing:")
        self.bearing.grid(row=6, column=0, sticky=W, pady=(3, 0))
        self.bearing_txt = tk.StringVar()
        self.bearing_label = tk.Label(self, textvar=self.bearing_txt)
        self.bearing_label.grid(row=6, column=1, sticky=W, pady=(3, 0))

        self._update_values()

    def _update_values(self):
        latitude = self.gps.data['Latitude'][-1]
        txt_lat = "{:7.5f}".format(latitude)
        self.latitude_txt.set(txt_lat)

        longitude = self.gps.data['Longitude'][-1]
        txt_long = "{:6.5f}".format(longitude)
        self.longitude_txt.set(txt_long)

        altitude = self.gps.data['Altitude'][-1]
        txt_alt = "{:3.1f} MAMSL".format(altitude)
        self.altitude_txt.set(txt_alt)

        heading = self.gps.data['Heading'][-1]
        txt_head = "{:3.1f}°".format(heading)
        self.heading_txt.set(txt_head)

        speed = self.gps.data['Ground_Speed'][-1]
        txt_speed = "{:5.3f} kph".format(speed)
        self.speed_txt.set(txt_speed)

        distance = self.gps.data['Distance'][-1]
        txt_distance = "{:3.1f} m".format(distance)
        self.distance_txt.set(txt_distance)

        bearing = self.gps.data['Bearing'][-1]
        txt_bearing = "{:3.1f}°".format(bearing)
        self.bearing_txt.set(txt_bearing)
    
        self.parent.after(100, self._update_values)


class GPSStatus(tk.Frame):
    def __init__(self, parent, gateway, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.gateway = gateway
        self.gps = self.gateway.sensors.gps

        self.validity = tk.Label(self, text="Fix validity:")
        self.validity.grid(row=0, column=0, sticky=W, pady=(3, 0))
        self.validity_txt = tk.StringVar()
        self.validity_label = tk.Label(self, textvar=self.validity_txt)
        self.validity_label.grid(row=0, column=1, sticky=W, pady=(3, 0))

        self.quality = tk.Label(self, text="Fix quality:")
        self.quality.grid(row=1, column=0, sticky=W, pady=(3, 0))
        self.quality_txt = tk.StringVar()
        self.quality_label = tk.Label(self, textvar=self.quality_txt)
        self.quality_label.grid(row=1, column=1, sticky=W, pady=(3, 0))

        self.status = tk.Label(self, text="Fix status:")
        self.status.grid(row=2, column=0, sticky=W, pady=(3, 0))
        self.status_txt = tk.StringVar()
        self.status_label = tk.Label(self, textvar=self.status_txt)
        self.status_label.grid(row=2, column=1, sticky=W, pady=(3, 0))

        self.pdop = tk.Label(self, text="Position DOP:")
        self.pdop.grid(row=3, column=0, sticky=W, pady=(3, 0))
        self.pdop_txt = tk.StringVar()
        self.pdop_label = tk.Label(self, textvar=self.pdop_txt)
        self.pdop_label.grid(row=3, column=1, sticky=W, pady=(3, 0))

        self.hdop = tk.Label(self, text="Horizontal DOP:")
        self.hdop.grid(row=4, column=0, sticky=W, pady=(3, 0))
        self.hdop_txt = tk.StringVar()
        self.hdop_label = tk.Label(self, textvar=self.hdop_txt)
        self.hdop_label.grid(row=4, column=1, sticky=W, pady=(3, 0))

        self.vdop = tk.Label(self, text="Vertical DOP")
        self.vdop.grid(row=5, column=0, sticky=W, pady=(3, 0))
        self.vdop_txt = tk.StringVar()
        self.vdop_label = tk.Label(self, textvar=self.vdop_txt)
        self.vdop_label.grid(row=5, column=1, sticky=W, pady=(3, 0))

        self.default_bg = self.validity.cget('background')

        self._update_status()
    
    def _update_status(self):
        validity = self.gps.data['Fix_Validity'][-1]
        if validity:
            txt_validity = "DATA VALID"
            self.validity_label.config(bg="green")
        else:
            txt_validity = "DATA INVALID"
            self.validity_label.config(bg="red")
        self.validity_txt.set(txt_validity)

        quality = self.gps.data['Fix_Quality'][-1]
        if quality == 0:
            txt_quality = "Invalid"
            self.quality_label.config(bg="red")
        elif quality == 1:
            txt_quality = "GPS Fix"
            self.quality_label.config(bg='green')
        else:
            txt_quality = "Other value {}".format(quality)
            self.quality_label.config(bg='green')
        self.quality_txt.set(txt_quality)

        status = self.gps.data['Fix_Status'][-1]
        if status == 1:
            txt_status = "no fix"
            self.status_label.config(bg='red')
        elif status == 2:
            txt_status = "2D fix"
            self.status_label.config(bg='green yellow')
        elif status == 3:
            txt_status = "3D fix"
            self.status_label.config(bg='green')
        else:
            txt_status = "-"
            self.quality_label.config(bg=self.default_bg)
        self.status_txt.set(txt_status)

        pdop = self.gps.data['pDOP'][-1]
        pdop_txt = "{:4.2f}".format(pdop)
        self.pdop_txt.set(pdop_txt)

        hdop = self.gps.data['hDOP'][-1]
        hdop_txt = "{:4.2f}".format(hdop)
        self.hdop_txt.set(hdop_txt)

        vdop = self.gps.data['vDOP'][-1]
        vdop_txt = "{:4.2f}".format(vdop)
        self.vdop_txt.set(vdop_txt)

        self.parent.after(100, self._update_status)


class GPSGraph(tk.Frame):
    def __init__(self, parent, gateway, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.gateway = gateway
        self.gps = self.gateway.sensors.gps

        self.rmax_init = 40

        self.fig = Figure(figsize=(3.2, 3.5), dpi=100)
        self.ax = self.fig.add_subplot(111, projection='polar')
        self.line, = self.ax.plot([], [], lw=1)
        self.ax.grid()

        self.bearing = []
        self.distance = []

        self.canvas = FigureCanvasTkAgg(self.fig, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=1, column=1)

        ani = animation.FuncAnimation(self.fig, self._update_data, blit=True, interval=10,
                                      repeat=False, init_func=self._init_figure)

    def _init_figure(self):
        """ Set the initial values and settings of the figure

        """
        rmax = self.rmax_init
        self.ax.set_rlim(0, rmax)
        self.ax.set_rticks([rmax/4., rmax/2., 3*rmax/4., rmax])
        self.ax.set_rlabel_position(67.5)
        self.ax.set_theta_direction(-1)
        self.ax.set_theta_zero_location('N')
        self.ax.set_title("Position from launch pad", y=1.1)
        self.ax.grid(True)
        self.canvas.draw()
        del self.bearing[:]
        del self.distance[:]
        self.line.set_data(self.bearing, self.distance)
        return self.line,

    def _update_data(self, data):
        """ Refresh the figure content

        Parameters
        ----------
        data : unused
            default parameter given by animation.FuncAnimation

        Returns
        -------
        tupple
            content of the figure for matplotlib        

        """
        if not self.gps.is_graph_init:
            self._init_figure()
            self.gps.is_graph_init = True

        rmin, rmax = self.ax.get_ylim()

        bearing_tmp = self.gps.data['Bearing_rad'][:]
        distance_tmp = self.gps.data['Distance'][:]

        len_b = len(self.bearing)
        len_d = len(self.distance)

        self.bearing = []
        self.distance = []

        if len_b == len_d:
            for i, e in enumerate(bearing_tmp):
                bearing = bearing_tmp[i]
                distance = distance_tmp[i]
                if str(bearing) != 'nan' and str(distance) != 'nan' and distance < 10000.:
                    self.bearing.append(bearing)
                    self.distance.append(distance)

            if self.distance:
                if max(self.distance) > 0.8*rmax:
                    rmax = rmax + self.rmax_init
                    if rmax < 5000:
                        self.ax.set_rlim(rmin, rmax)
                        self.ax.set_rticks([rmax/4., rmax/2., 3*rmax/4., rmax])
                        self.canvas.draw()

            self.line.set_data(self.bearing, self.distance)

        return self.line,


class GPSWidget(tk.Frame):
    def __init__(self, parent, gateway, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.gateway = gateway
        self.sensors = self.gateway.sensors

        self.values = GPSValues(self, self.gateway)
        self.values.grid(row=0, column=0, sticky=W, padx=15, pady=10)

        self.graph = GPSGraph(self, self.gateway)
        self.graph.grid(row=1, column=0)

        self.status = GPSStatus(self, self.gateway)
        self.status.grid(row=2, column=0, sticky=W, padx=15, pady=10)


# ####################### #
#   Widgets for the LPS   #
# ####################### #


class LaunchpadCommandButtons(tk.Frame):
    """ TKinter frame with two control the LPS

    Parameters
    ----------
    parent : TKinter Frame
        parent frame
    gateway : Gateway instance
        Gateway to send commands to

    """

    def __init__(self, parent, gateway, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.gateway = gateway
        self.status = self.gateway.sensors.status

        self.button_output1_text = tk.StringVar()
        self.button_output1 = tk.Button(self, textvar=self.button_output1_text)
        self.button_output2_text = tk.StringVar()
        self.button_output2 = tk.Button(self, textvar=self.button_output2_text)
        self.button_output3_text = tk.StringVar()
        self.button_output3 = tk.Button(self, textvar=self.button_output3_text)
        self.button_output4_text = tk.StringVar()
        self.button_output4 = tk.Button(self, textvar=self.button_output4_text)

        self.button_output1.grid(row=1, column=1, sticky=W+E)
        self.button_output2.grid(row=2, column=1, sticky=W+E)
        self.button_output3.grid(row=1, column=2, sticky=W+E)
        self.button_output4.grid(row=2, column=2, sticky=W+E)

        self._update_buttons()

    def _update_buttons(self):
        """ Set the buttons inactive when the gateway is not ready

        """
        is_output1_en = self.status.data['IS_OUTPUT1_EN']
        is_output2_en = self.status.data['IS_OUTPUT2_EN']
        is_output3_en = self.status.data['IS_OUTPUT3_EN']
        is_output4_en = self.status.data['IS_OUTPUT4_EN']

        # Update text and commands for buttons
        if not is_output1_en:
            self.button_output1_text.set("Enable OUT1")
            self.button_output1.config(command=lambda: self.gateway.send_command(bytes([0x26, 0x63, 0x61, 0x01])))
        else:
            self.button_output1_text.set("Disable OUT1")
            self.button_output1.config(command=lambda: self.gateway.send_command(bytes([0x26, 0x63, 0x61, 0x00])))
        if not is_output2_en:
            self.button_output2_text.set("Enable OUT2")
            self.button_output2.config(command=lambda: self.gateway.send_command(bytes([0x26, 0x63, 0x62, 0x01])))
        else:
            self.button_output2_text.set("Disable OUT2")
            self.button_output2.config(command=lambda: self.gateway.send_command(bytes([0x26, 0x63, 0x62, 0x00])))
        if not is_output3_en:
            self.button_output3_text.set("Enable OUT3")
            self.button_output3.config(command=lambda: self.gateway.send_command(bytes([0x26, 0x63, 0x63, 0x01])))
        else:
            self.button_output3_text.set("Disable OUT3")
            self.button_output3.config(command=lambda: self.gateway.send_command(bytes([0x26, 0x63, 0x63, 0x00])))
        if not is_output4_en:
            self.button_output4_text.set("Enable OUT4")
            self.button_output4.config(command=lambda: self.gateway.send_command(bytes([0x26, 0x63, 0x64, 0x01])))
        else:
            self.button_output4_text.set("Disable OUT4")
            self.button_output4.config(command=lambda: self.gateway.send_command(bytes([0x26, 0x63, 0x64, 0x00])))
        
        # Enable the relevant buttons
        if self.gateway.serial.is_ready:
            self.button_output1.config(state=tk.NORMAL)
            self.button_output2.config(state=tk.NORMAL)
            self.button_output3.config(state=tk.NORMAL)
            self.button_output4.config(state=tk.NORMAL)

        else:
            self.button_output1.config(state=tk.DISABLED)
            self.button_output2.config(state=tk.DISABLED)
            self.button_output3.config(state=tk.DISABLED)
            self.button_output4.config(state=tk.DISABLED)

        # Call this function again after 100 ms
        self.parent.after(100, self._update_buttons)


class LaunchpadState(tk.Frame):
    def __init__(self, parent, gateway, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.gateway = gateway

        RSSI = tk.Frame(self, bd=0)
        RSSI.grid(row=0, column=0, sticky=W+E, padx=(0, 2))

        self.rssi_txt = tk.Label(RSSI, text="RSSI: ")
        self.rssi_value_txt = tk.StringVar()
        self.rssi_value = tk.Label(RSSI, textvar=self.rssi_value_txt)

        self.rssi_txt.grid(row=0, column=0)
        self.rssi_value.grid(row=0, column=1)

        OUTPUT = tk.Frame(self, bd=2, relief="groove")
        OUTPUT.grid(row=3, column=0, rowspan=2, sticky=W+E, padx=(0, 2))

        self.output_txt = tk.Label(OUTPUT, text="  OUTPUT  ")
        self.output_legend= tk.Label(OUTPUT, text="     1  -12V-  2            3  -24V-  4     ")
        self.output1_txt = tk.StringVar()
        self.output1 = tk.Label(OUTPUT, textvar=self.output1_txt)
        self.output2_txt = tk.StringVar()
        self.output2 = tk.Label(OUTPUT, textvar=self.output2_txt)
        self.output3_txt = tk.StringVar()
        self.output3 = tk.Label(OUTPUT, textvar=self.output3_txt)
        self.output4_txt = tk.StringVar()
        self.output4 = tk.Label(OUTPUT, textvar=self.output4_txt)

        self.output_txt.grid(row=0, column=0, columnspan=4)
        self.output_legend.grid(row=1, column=0, columnspan=4)
        self.output1.grid(row=2, column=0)
        self.output2.grid(row=2, column=1)
        self.output3.grid(row=2, column=2)
        self.output4.grid(row=2, column=3)

        self.default_bg = self.output1.cget("background")

        self._ping_launchpad()
        self._update_state()

    def _update_state(self):
        if self.gateway.serial.is_ready:
            rssi = self.gateway.sensors.rssi.data['REMOTE_RSSI']
            self.rssi_value_txt.set(str(rssi))

            if self.gateway.sensors.status.data['IS_OUTPUT1_EN']:
                self.output1_txt.set('on ')
                self.output1.config(bg='yellow green')
            else:
                self.output1_txt.set('off')
                self.output1.config(bg=self.default_bg)

            if self.gateway.sensors.status.data['IS_OUTPUT2_EN']:
                self.output2_txt.set('on ')
                self.output2.config(bg='yellow green')
            else:
                self.output2_txt.set('off')
                self.output2.config(bg=self.default_bg)

            if self.gateway.sensors.status.data['IS_OUTPUT3_EN']:
                self.output3_txt.set('on ')
                self.output3.config(bg='yellow green')
            else:
                self.output3_txt.set('off')
                self.output3.config(bg=self.default_bg)

            if self.gateway.sensors.status.data['IS_OUTPUT4_EN']:
                self.output4_txt.set('on ')
                self.output4.config(bg='yellow green')
            else:
                self.output4_txt.set('off')
                self.output4.config(bg=self.default_bg)

        else:
            self.rssi_value_txt.set('')
            self.output1_txt.set(' - ')
            self.output2_txt.set(' - ')
            self.output3_txt.set(' - ')
            self.output4_txt.set(' - ')

        self.parent.after(100, self._update_state)

    def _ping_launchpad(self):
        # Unused command, just to get a reply from the controller
        self.gateway.send_command(bytes([0x26, 0x63, 0xFF, 0xFF]))

        self.parent.after(5000, self._ping_launchpad)


class LaunchpadWidget(tk.Frame):
    def __init__(self, parent, gateway, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.gateway = gateway

        self.gateway_controls = LaunchpadCommandButtons(self, self.gateway, bd=BD, relief="solid")
        self.launchpad_status = GatewayStatus(self, self.gateway, 'LPS')
        self.state = LaunchpadState(self, self.gateway)

        self.launchpad_status.grid(
            row=0, column=0, padx=10, pady=(8, 0), sticky=W)
        self.state.grid(
            row=1, column=0, padx=10, pady=(5, 0))
        self.gateway_controls.grid(
            row=2, column=0, padx=10, pady=(5, 8))
