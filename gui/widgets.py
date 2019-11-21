import copy
import datetime
import tkinter as tk
from tkinter import E, N, S, W

import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class LPSCommandButtons(tk.Frame):
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
        self.is_filling = False
        self.is_venting = False
        self.is_armed = False
        self.is_firing = False
        self.is_tm_enabled = True

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
        self.button_cal_text = tk.StringVar()
        self.button_cal = tk.Button(
            self, textvar=self.button_cal_text, command=self._trigger_calibration)

        self.button_fill.grid(row=1, column=1, sticky=W+E)
        self.button_vent.grid(row=1, column=2, sticky=W+E)
        self.button_arm.grid(row=2, column=1, sticky=W+E)
        self.button_fire.grid(row=2, column=2, sticky=W+E)
        self.button_tm.grid(row=3, column=1, sticky=W+E)
        self.button_cal.grid(row=3, column=2, sticky=W+E)

        self._update_buttons()

    def _update_buttons(self):
        """ Set the buttons inactive when the gateway is not ready

        """
        if self.gateway.serial.is_ready:

            self.button_fill.config(state=tk.NORMAL)
            if not self.is_filling:
                self.button_fill_text.set("Start filling")
                self.button_fill.config(command=lambda: self._toggle_filling('START'))
            else:
                self.button_fill_text.set("Stop filling")
                self.button_fill.config(command=lambda: self._toggle_filling('STOP'))

            self.button_vent.config(state=tk.NORMAL)
            if not self.is_venting:
                self.button_vent_text.set("Start venting")
                self.button_vent.config(command=lambda: self._toggle_venting('START'))
            else:
                self.button_vent_text.set("Stop venting")
                self.button_vent.config(command=lambda: self._toggle_venting('STOP'))

            self.button_arm.config(state=tk.NORMAL)
            if not self.is_armed:
                self.button_arm_text.set("Arm")
                self.button_arm.config(command=lambda: self._toggle_arm('ARM'))
            else:
                self.button_arm_text.set("Disarm")
                self.button_arm.config(command=lambda: self._toggle_arm('DISARM'))

            self.button_fire.config(state=tk.NORMAL)
            if not self.is_firing:
                self.button_fire_text.set("Start ignition")
                self.button_fire.config(command=lambda: self._toggle_ignition('START'))
            else:
                self.button_fire_text.set("Stop ignition")
                self.button_fire.config(command=lambda: self._toggle_ignition('STOP'))

            self.button_tm.config(state=tk.NORMAL)
            if not self.is_tm_enabled:
                self.button_tm_text.set("Enable telemetry ")
                self.button_tm.config(command=lambda: self._toggle_telemetry('ENABLE'))
            else:
                self.button_tm_text.set("Disable telemetry")
                self.button_tm.config(command=lambda: self._toggle_telemetry('DISABLE'))

            self.button_cal.config(state=tk.NORMAL)

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
            self.button_cal_text.set("Trigger calibration")
            self.button_cal.config(state=tk.DISABLED)

        # Call this function again after 100 ms
        self.parent.after(100, self._update_buttons)

    def _toggle_filling(self, command):
        if command == 'START':
            self.gateway.send_command(0x61)
            self.is_filling = True
        elif command == 'STOP':
            self.gateway.send_command(0x62)
            self.is_filling = False
        self._update_buttons()

    def _toggle_venting(self, command):
        if command == 'START':
            self.gateway.send_command(0x63)
            self.is_venting = True
        elif command == 'STOP':
            self.gateway.send_command(0x64)
            self.is_venting = False
        self._update_buttons()

    def _toggle_arm(self, command):
        if command == 'ARM':
            self.gateway.send_command(0x65)
            self.is_armed = True
        elif command == 'DISARM':
            self.gateway.send_command(0x66)
            self.is_armed = False
        self._update_buttons()

    def _toggle_ignition(self, command):
        if command == 'START':
            self.gateway.send_command(0x67)
            self.is_firing = True
        elif command == 'DISARM':
            self.gateway.send_command(0x68)
            self.is_firing = False
        self._update_buttons()

    def _toggle_telemetry(self, command):
        if command == 'ENABLE':
            self.gateway.send_command(0x41)
            self.is_tm_enabled = True
        elif command == 'DISABLE':
            self.gateway.send_command(0x42)
            self.is_tm_enabled = False
        self._update_buttons()

    def _trigger_calibration(self):
        self.gateway.send_command(0x43)


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
            row=1, column=1, sticky=W+E)

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


class LiveTimeGraph(tk.Frame):
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


class SensorIndicator(tk.Frame):
    """ TKinter frame that holds a TKinter square of color and a label for sensor.name

    The box changes color depending on status of sensor. The sensor must have a self.status attribute.

    Parameters
    ----------
    parent : TKinter Frame
        parent frame
    gateway : Gateway instance
        Gateway to monitor
    sensor : attribute of a Sensors instance
        sensor to display status from
    field : str
        name of the sensor to display

    """

    def __init__(self, parent, gateway, sensor, field, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.gateway = gateway
        self.sensor = sensor
        self.field = field

        # Button to make a colored "box" for sensor
        # Style will be reflected on this button
        self.btn = tk.Button(self, text='')
        # self.btn = tk.Button(self)
        self.btn.grid(row=0, column=1)
        # Label to display the gateway's port name
        self.label = tk.Label(self, text=self.field)
        self.label.grid(
            row=0, column=2, padx=5)

        self.__update_button()

    def __update_button(self):
        """ Set the style of the button depending on the status of sensor.

        """
        if self.sensor.data[self.field] is None:
            self.btn.config(bg='grey', state=tk.DISABLED, width=1)
        else:
            if self.sensor.data[self.field]:
                self.btn.config(bg='red', height=1, state=tk.DISABLED, width=1)
            else:
                self.btn.config(bg='green', height=1,
                                state=tk.DISABLED, width=1)
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


class EngineControl(tk.Frame):
    """ TKinter frame that holds a label and button with changeable string

    The label is what's being controlled. The button controls output to LoRa.

    Parameters
    ----------
    parent : TKinter Frame
        parent frame
    gateway : Gateway instance (LPS)
        Gateway to monitor
    field : str
        name of controlled LPS function

    """

    def __init__(self, parent, gateway, sensor, field, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.gateway = gateway
        self.sensor = sensor
        self.field = field

        # Button to make a colored "box" for sensor
        # Style will be reflected on this button
        self.text_var = tk.StringVar()
        self.text_var.set("Start")
        self.btn = tk.Button(self, text=self.field, height=4, width=10)
        self.btn.grid(row=0, column=1)
        # Label to display the gateway's port name
        self.label = tk.Label(self, text=self.field)
        self.label.grid(
            row=1, column=1, pady=10)

        self.__update_button()

    def __update_button(self):
        """ Set the behaviour of the button to open or close the Serial link

        """
        if self.gateway.serial.get_status():
            self.text_var.set("Stop")
            if self.field == "Fueling":
                self.btn.config(
                    command=self.gateway.send_command("Start Fuel"))
            elif self.field == "Ignite":
                self.btn.config(command=self.gateway.send_command("Ignite"))
            else:
                print("Change name of field for action")
        else:
            self.text_var.set("Start")
            if self.field == "Fueling":
                self.btn.config(command=self.gateway.send_command("Stop Fuel"))
            elif self.field == "Ignite":
                self.btn.config(command=self.gateway.send_command(
                    "Should we send something here?"))
            else:
                print("Change name of field for action")
        # Call this function again after 100 ms
        self.parent.after(100, self.__update_button)
