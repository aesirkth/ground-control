import copy
import datetime
import threading
import tkinter as tk
from tkinter import E, N, S, W


class CommandButtons(tk.Frame):
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
        if self.interface.is_reading:
            self.button_A.config(state=tk.NORMAL)
            self.button_B.config(state=tk.NORMAL)
        else:
            self.button_A.config(state=tk.DISABLED)
            self.button_B.config(state=tk.DISABLED)

        self.parent.after(100, self.update_buttons)


class MessageBox(tk.Frame):
    def __init__(self, parent, interface, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.interface = interface
        self.messages = []

        tk.Label(self, text="Messages :").grid(row=0, column=1, sticky=W)

        self.scroll_bar = tk.Scrollbar(self)
        self.scroll_bar.grid(row=1, column=2, sticky=W+E+N+S)
        self.message_box = tk.Text(self, height=10, width=60)
        self.message_box.grid(row=1, column=1, sticky=W+E+N+S)
        self.scroll_bar.config(command=self.message_box.yview)
        self.message_box.config(yscrollcommand=self.scroll_bar.set)

        self.update_messages()

    def diff_list(self, list1, list2):
        """ Returns the elements that are only in one of the lists

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
        diff = (list(set(list1) - set(list2)))
        return diff

    def update_messages(self):
        all_messages = self.interface.messages
        new_messages = self.diff_list(all_messages, self.messages)
        new_messages = sorted(new_messages, key=lambda tup: tup[0])
        self.messages = copy.copy(all_messages)
        new_lines = "".join(["{} : {}\n".format(
            e[0].time().replace(microsecond=0), e[1]) for e in new_messages])
        self.message_box.insert(tk.END, new_lines)
        if new_messages:
            self.message_box.yview_moveto(1)

        self.parent.after(100, self.update_messages)


class InterfaceStatus(tk.Frame):
    def __init__(self, parent, interface, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.interface = interface

        self.button_var = tk.StringVar()
        self.read_button = tk.Button(self, textvariable=self.button_var)
        self.read_button.grid(row=0, column=0)

        self.port_var = tk.StringVar()
        self.port_var.set("Port : {}".format(
            self.interface.serial.ser.port))
        tk.Label(self, textvariable=self.port_var).grid(
            row=0, column=1, sticky=W)

        self.update_port()
        self.update_button()

    def destroy(self):
        self.stop_read()
        tk.Frame.destroy(self)

    def stop_read(self):
        self.interface.stop_read()

    def start_read(self):
        """ Start serial reading from the interface in a separate thread

        """
        t = threading.Thread(target=self.interface.start_read)
        t.start()

    def update_port(self):
        self.port_var.set("Port : {}".format(
            self.interface.serial.ser.port))

        self.parent.after(100, self.update_port)

    def update_button(self):
        if self.interface.is_reading:
            self.button_var.set("Close link")
            self.read_button.config(command=self.stop_read)
        else:
            self.button_var.set("Open link")
            self.read_button.config(command=self.start_read)

        self.parent.after(100, self.update_button)
