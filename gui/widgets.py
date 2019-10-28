import copy
import datetime
import threading
import tkinter as tk
from tkinter import E, N, S, W


class CommandButtons(tk.Frame):
    """ TKinter frame with two clickable buttons

    The buttons trigger a Serial write to the interface they are linked to

    Parameters
    ----------
    parent : TKinter Frame
        parent frame
    interface : Interface instance
        Interface to send commands to

    """

    def __init__(self, parent, interface, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.interface = interface

        self.button_A = tk.Button(self, text="Send 'A'",
                                  command=lambda: self.interface.send_command('A'))
        self.button_B = tk.Button(self, text="Send 'B'",
                                  command=lambda: self.interface.send_command('B'))

        self.button_A.grid(row=1, column=1)
        self.button_B.grid(row=1, column=2)

        self.update_buttons()

    def update_buttons(self):
        """ Set the buttons inactive when the interface is not ready

        """
        if self.interface.is_ready():
            self.button_A.config(state=tk.NORMAL)
            self.button_B.config(state=tk.NORMAL)
        else:
            self.button_A.config(state=tk.DISABLED)
            self.button_B.config(state=tk.DISABLED)
        # Call this function again after 100 ms
        self.parent.after(100, self.update_buttons)


class MessageBox(tk.Frame):
    """ TKinter frame to display the messages received from an interface

    The content of the Text box is updated with every new message received
    The time of reception is displayed before the message content

    See utils/interface.py for more details on how the messages are handled

    Parameters
    ----------
    parent : TKinter Frame
        parent frame
    interface : Interface instance
        Interface to read messages from

    """
    def __init__(self, parent, interface, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.interface = interface
        self.messages = []

        tk.Label(self, text="Messages :").grid(row=0, column=1, sticky=W)

        # TextBox and Scrollbar
        self.scroll_bar = tk.Scrollbar(self)
        self.message_box = tk.Text(self, height=10, width=60)
        self.scroll_bar.grid(row=1, column=2, sticky=W+E+N+S)
        self.message_box.grid(row=1, column=1, sticky=W+E+N+S)
        self.scroll_bar.config(command=self.message_box.yview)
        self.message_box.config(yscrollcommand=self.scroll_bar.set)

        self.update_messages()

    def diff_list(self, list1, list2):
        """ Return the elements that are only in one of the lists

        The content of the lists must be hashable

        Parameters
        ----------
        list1 : list
            first list to compare
        list2 : list
            second list to compare

        Returns
        -------
        diff : list
            a list with only elements that are in one or the other input lists

        """
        diff = list(set(list1) - set(list2))
        return diff

    def update_messages(self):
        """ Add new messages at the bottom of the Text box

        The Scrollbar goes to the bottom of the box every time a new message is received

        """
        # Get all messages received by the interface
        all_messages = self.interface.messages
        # Compare the previous list to the messages already displayed
        new_messages = self.diff_list(all_messages, self.messages)
        # Sort new messages by date (the first element is a datetime object)
        new_messages = sorted(new_messages, key=lambda tup: tup[0])

        if new_messages:
            # This complex line extracts the time and message content from each message
            # in the new_messages list
            new_lines = "".join(["{} : {}\n".format(
                m[0].time().replace(microsecond=0), m[1]) for m in new_messages])
            # Insert the new messages at the end of the Text content
            self.message_box.insert(tk.END, new_lines)
            # Move the Scrollbar cursor to the bottom
            self.message_box.yview_moveto(1)
            # Update the list of messages that are already displayed
            self.messages = copy.copy(all_messages)
        # Call this function again after 100 ms
        self.parent.after(100, self.update_messages)


class InterfaceStatus(tk.Frame):
    """ TKinter frame to monitor the status of the Serial link

    Reading from the Serial link is started in a separate thread with Threading and
    stopped on the destruction of this frame

    Parameters
    ----------
    parent : TKinter Frame
        parent frame
    interface : Interface instance
        Interface to monitor

    """
    def __init__(self, parent, interface, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.interface = interface

        # Button to open/close the Serial link
        self.button_var = tk.StringVar()
        self.read_button = tk.Button(self, textvariable=self.button_var)
        self.read_button.grid(row=0, column=0)
        # Label to display the interface's port name
        self.port_var = tk.StringVar()
        self.port_var.set("Port : {}".format(
            self.interface.serial.ser.port))
        tk.Label(self, textvariable=self.port_var).grid(
            row=0, column=1, sticky=W)

        self.update_port()
        self.update_button()

    def destroy(self):
        """" Catch the destruction of the widget and stop the Serial reading

        If this is not done properly the Threading thread that reads data from
        the Serial link cannot be stopped

        """
        self.stop_read()
        tk.Frame.destroy(self)

    def start_read(self):
        """ Start serial reading from the interface in a separate thread

        See utils.interface.start_read()

        """
        t = threading.Thread(target=self.interface.start_read)
        t.start()

    def stop_read(self):
        # This stops the infinite loop in utils.interface.start_read()
        self.interface.stop_read()

    def update_port(self):
        """ Update the port name displayed

        """
        self.port_var.set("Port : {}".format(
            self.interface.serial.ser.port))
        # Call this function again after 100 ms
        self.parent.after(100, self.update_port)

    def update_button(self):
        """ Set the behaviour of the button to open or close the Serial link

        """
        if self.interface.is_serial_open():
            self.button_var.set("Close link")
            self.read_button.config(command=self.stop_read)
        else:
            self.button_var.set("Open link")
            self.read_button.config(command=self.start_read)
        # Call this function again after 100 ms
        self.parent.after(100, self.update_button)
