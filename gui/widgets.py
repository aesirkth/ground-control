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


class LiveTimeGraphTemp(tk.Frame):
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
        # self.fig.set_label(self.field)
        # self.fig.tight_layout()
        self.time = []
        self.data = []

        self.canvas = FigureCanvasTkAgg(self.fig, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=1, column=1)

        ani = animation.FuncAnimation(self.fig, self.__update_data, blit=True, interval=10,
                                      repeat=False, init_func=self.__init_figure)

    def __init_figure(self):
        """ Set the initial values and settings of the figure

        """
        self.ax.set_ylim(0, 50)
        self.ax.set_xlim(0, 10)
        del self.time[:]
        del self.data[:]
        self.line.set_data(self.time, self.data)
        return self.line,

    def __update_data(self, data):
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
        tmin, tmax = self.ax.get_xlim()

        self.time = self.sensor.raw_data['Seconds_since_start']
        self.data = self.sensor.raw_data[self.field]

        if self.time:
            if max(self.time) > tmax:
                self.ax.set_xlim(tmin, 2*tmax)
                self.canvas.draw()

        self.line.set_data(self.time, self.data)

        return self.line,


class TelemetryWidget(tk.Frame):
    def __init__(self, parent, gateway, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.gateway = gateway
        self.sensors = self.gateway.sensors

        self.telemetry_status = GatewayStatus(self, self.gateway, 'Telemetry')
        self.button_set_reference = tk.Button()

        self.telemetry_status.grid(
            row=1, column=1, sticky=W, padx=10, pady=5)


class InitStatus(tk.Frame):
    def __init__(self, parent, gateway, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.gateway = gateway
        self.sensors = self.gateway.sensors

        self.title = tk.Label(self, text="Initialization status")
        self.title.grid(row=0, column=0, columnspan=2, sticky=W+E)

        self.imu2_status = BoolFieldIndicator(
            self, self.sensors.errmsg, "ERR_INIT_IMU2", "IMU2")
        # self.imu3_status = BoolFieldIndicator(
        #     self, self.sensors.errmsg, "ERR_INIT_IMU3", "IMU3")
        self.bmp2_status = BoolFieldIndicator(
            self, self.sensors.errmsg, "ERR_INIT_BMP2", "BMP2")
        self.bmp3_status = BoolFieldIndicator(
            self, self.sensors.errmsg, "ERR_INIT_BMP3", "BMP3")
        self.mag_status = BoolFieldIndicator(
            self, self.sensors.errmsg, "ERR_INIT_MAG", "MAG")
        self.adc_status = BoolFieldIndicator(
            self, self.sensors.errmsg, "ERR_INIT_ADC", "ADC")
        self.card_status = BoolFieldIndicator(
            self, self.sensors.errmsg, "ERR_INIT_SD_CARD", "SD")

        self.imu2_status.grid(
            row=1, column=0, sticky=W+E)
        # self.imu3_status.grid(
        #     row=2, column=0, sticky=W+E)
        self.bmp2_status.grid(
            row=2, column=0, sticky=W+E)
        self.bmp3_status.grid(
            row=3, column=0, sticky=W+E)
        self.mag_status.grid(
            row=1, column=1, sticky=W+E)
        self.adc_status.grid(
            row=2, column=1, sticky=W+E)
        self.card_status.grid(
            row=3, column=1, sticky=W+E)


class BatteryIndicator(tk.Frame):
    def __init__(self, parent, gateway, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.gateway = gateway

        self.battery1_txt = tk.StringVar()
        self.battery1 = tk.Label(self, textvar=self.battery1_txt)
        self.battery1.grid(row=0, column=0, sticky=W)

        self.battery2_txt = tk.StringVar()
        self.battery2 = tk.Label(self, textvar=self.battery2_txt)
        self.battery2.grid(row=1, column=0, sticky=W)

        self._update_label()

    def _update_label(self):
        voltage_battery1 = self.gateway.sensors.batteries.data['Battery1']
        txt1 = "Battery 1 : {:05.2f}V".format(voltage_battery1)
        self.battery1_txt.set(txt1)
        voltage_battery2 = self.gateway.sensors.batteries.data['Battery2']
        txt2 = "Battery 2 : {:3.2f}V".format(voltage_battery2)
        self.battery2_txt.set(txt2)

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

        self.timer_txt = tk.StringVar()
        self.timer = tk.Label(self, textvar=self.timer_txt)
        self.timer.grid(row=1, column=0)

        self._update_time()

    def _update_time(self):
        rtc_time = self.gateway.sensors.rtc.data
        txt = "{}:{:02d}:{:02d}.{:02.0f}".format(
            rtc_time['Hour'], rtc_time['Minute'], rtc_time['Second'], rtc_time['Microsecond']/1e4)
        self.rtc_txt.set(txt)

        timer_time = self.gateway.sensors.timer.data
        txt = "{}".format(timer_time['Timer'])
        self.timer_txt.set(txt)
        
        self.parent.after(100, self._update_time)


class RocketStatus(tk.Frame):
    def __init__(self, parent, gateway, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.gateway = gateway

        self.batteries = BatteryIndicator(self, self.gateway, bd=BD, relief="solid")
        self.batteries.grid(row=0, column=0, padx=10, pady=(5, 0))

        self.time = TimeIndicator(self, self.gateway, bd=BD, relief="solid")
        self.time.grid(row=0, column=1, padx=10, pady=(5, 0))

        self.init_status = InitStatus(self, self.gateway, bd=BD, relief="solid")
        self.init_status.grid(row=2, column=0, columnspan=2, padx=10, pady=(5, 5))


# ####################### #
#   Widgets for the LPS   #
# ####################### #


class LPSCommandButtons(tk.Frame):
    """ TKinter frame with two control the LPS

    Parameters
    ----------
    parent : TKinter Frame
        parent frame
    gateway : Gateway instance
        Gateway to send commands to

    """

    def __init__(self, parent, gateway, status, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.gateway = gateway
        self.status = status

        self.button_fill_text = tk.StringVar()
        self.button_fill = tk.Button(self, textvar=self.button_fill_text)
        self.button_vent_text = tk.StringVar()
        self.button_vent = tk.Button(self, textvar=self.button_vent_text)
        self.button_arm_text = tk.StringVar()
        self.button_arm = tk.Button(self, textvar=self.button_arm_text)
        self.button_fire_text = tk.StringVar()
        self.button_fire = tk.Button(self, textvar=self.button_fire_text)
        self.button_tm_text = tk.StringVar()
        self.button_tm = tk.Button(self, textvar=self.button_tm_text)

        self.button_fill.grid(row=1, column=1, sticky=W+E)
        self.button_vent.grid(row=1, column=2, sticky=W+E)
        self.button_arm.grid(row=2, column=1, sticky=W+E)
        self.button_fire.grid(row=2, column=2, sticky=W+E)
        self.button_tm.grid(row=3, column=1, columnspan=2, sticky=W+E)

        self._update_buttons()

    def _update_buttons(self):
        """ Set the buttons inactive when the gateway is not ready

        """
        if self.gateway.serial.is_ready:

            self.button_fill.config(state=tk.NORMAL)
            if not self.status.data['IS_FILLING']:
                self.button_fill_text.set("Start filling")
                self.button_fill.config(
                    command=lambda: self.gateway.send_command(bytes([0x61])))
            else:
                self.button_fill_text.set("Stop filling")
                self.button_fill.config(
                    command=lambda: self.gateway.send_command(bytes([0x62])))

            self.button_vent.config(state=tk.NORMAL)
            if not self.status.data['IS_VENTING']:
                self.button_vent_text.set("Start venting")
                self.button_vent.config(
                    command=lambda: self.gateway.send_command(bytes([0x63])))
            else:
                self.button_vent_text.set("Stop venting")
                self.button_vent.config(
                    command=lambda: self.gateway.send_command(bytes([0x64])))

            self.button_arm.config(state=tk.NORMAL)
            if not self.status.data['IS_ARMED']:
                self.button_arm_text.set("Arm")
                self.button_arm.config(
                    command=lambda: self.gateway.send_command(bytes([0x65])))
            else:
                self.button_arm_text.set("Disarm")
                self.button_arm.config(
                    command=lambda: self.gateway.send_command(bytes([0x66])))

            self.button_fire.config(state=tk.NORMAL)
            if not self.status.data['IS_FIRING']:
                self.button_fire_text.set("Start ignition")
                self.button_fire.config(
                    command=lambda: self.gateway.send_command(bytes([0x67])))
            else:
                self.button_fire_text.set("Stop ignition")
                self.button_fire.config(
                    command=lambda: self.gateway.send_command(bytes([0x68])))

            self.button_tm.config(state=tk.NORMAL)
            if not self.status.data['IS_TM_ENABLED']:
                self.button_tm_text.set("Enable telemetry ")
                self.button_tm.config(
                    command=lambda: self.gateway.send_command(bytes([0x41])))
            else:
                self.button_tm_text.set("Disable telemetry")
                self.button_tm.config(
                    command=lambda: self.gateway.send_command(bytes([0x42])))

        else:
            self.button_fill_text.set("Start filling")
            self.button_fill.config(state=tk.DISABLED)
            self.button_vent_text.set("Start venting")
            self.button_vent.config(state=tk.DISABLED)
            self.button_arm_text.set("Arm")
            self.button_arm.config(state=tk.DISABLED)
            self.button_fire_text.set("Start ignition")
            self.button_fire.config(state=tk.DISABLED)
            self.button_tm_text.set("Disable telemetry")
            self.button_tm.config(state=tk.DISABLED)

        # Call this function again after 100 ms
        self.parent.after(100, self._update_buttons)


class LPSState(tk.Frame):
    def __init__(self, parent, gateway, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.gateway = gateway

        Motor = tk.Frame(self, bd=2, relief="groove")
        Motor.grid(row=0, column=1, sticky=W+E, padx=2)

        self.motor_txt = tk.Label(Motor, text="  Motor  ")
        self.motor_state_txt = tk.StringVar()
        self.motor_state = tk.Label(Motor, textvar=self.motor_state_txt)
        self.default_bg = self.motor_state.cget("background")

        self.motor_txt.grid(row=0, column=0)
        self.motor_state.grid(row=1, column=0)

        Telemetry = tk.Frame(self, bd=2, relief="groove")
        Telemetry.grid(row=0, column=2, sticky=W+E, padx=(2, 0))

        self.tm_txt = tk.Label(Telemetry, text="  Telemetry  ")
        self.tm_state_txt = tk.StringVar()
        self.tm_state = tk.Label(Telemetry, textvar=self.tm_state_txt)

        self.tm_txt.grid(row=0, column=0)
        self.tm_state.grid(row=1, column=0)

        RSSI = tk.Frame(self, bd=2, relief="groove")
        RSSI.grid(row=0, column=0, rowspan=2, sticky=W+E, padx=(0, 2))

        self.rssi_txt = tk.Label(RSSI, text="  RSSI  ")
        self.rssi_value_txt = tk.StringVar()
        self.rssi_value = tk.Label(RSSI, textvar=self.rssi_value_txt)

        self.rssi_txt.grid(row=0, column=0)
        self.rssi_value.grid(row=1, column=0)

        self._ping_lps()
        self._update_state()

    def _update_state(self):
        if self.gateway.serial.is_ready:
            if self.gateway.sensors.status.data['IS_FILLING']:
                self.motor_state_txt.set('Filling')
                self.motor_state.config(bg="orange")
            elif self.gateway.sensors.status.data['IS_VENTING']:
                self.motor_state_txt.set('Venting')
                self.motor_state.config(bg="orange")
            elif self.gateway.sensors.status.data['IS_FIRING']:
                self.motor_state_txt.set('Ignition')
                self.motor_state.config(bg="green")
            elif self.gateway.sensors.status.data['IS_ARMED']:
                self.motor_state_txt.set('Armed')
                self.motor_state.config(bg="red")
            else:
                self.motor_state_txt.set('Default')
                self.motor_state.config(bg=self.default_bg)
            if self.gateway.sensors.status.data['IS_TM_ENABLED']:
                self.tm_state_txt.set('Enabled')
                self.tm_state.config(bg='green')
            else:
                self.tm_state_txt.set('Disabled')
                self.tm_state.config(bg='red')

            rssi = self.gateway.sensors.rssi.data['REMOTE_RSSI']
            self.rssi_value_txt.set(str(rssi))
        else:
            self.motor_state_txt.set('')
            self.motor_state.config(bg=self.default_bg)
            self.tm_state_txt.set('')
            self.tm_state.config(bg=self.default_bg)
            self.rssi_value_txt.set('')

        self.parent.after(100, self._update_state)

    def _ping_lps(self):
        # Unused command, just to get an answer
        self.gateway.send_command(bytes([0xFF]))

        self.parent.after(5000, self._ping_lps)


class LPSWidget(tk.Frame):
    def __init__(self, parent, gateway, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.gateway = gateway
        self.sensors = self.gateway.sensors

        self.gateway_controls = LPSCommandButtons(
            self, self.gateway, self.sensors.status, bd=BD, relief="solid")
        self.lps_status = GatewayStatus(self, self.gateway, 'LPS')
        self.state = LPSState(self, self.gateway)

        self.lps_status.grid(
            row=0, column=0, padx=10, pady=(5, 0), sticky=W)
        self.state.grid(
            row=1, column=0, padx=10, pady=(5, 0))
        self.gateway_controls.grid(
            row=2, column=0, padx=10, pady=(5, 5))
