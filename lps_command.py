import threading
import tkinter as tk
from tkinter import E, N, S, W

from utils import Interface
from gui import CommandButtons, MessageBox


class MainApplication(tk.Frame):
    def __init__(self, parent, interface, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.interface = interface

        self.messagebox = MessageBox(self, borderwidth=2, relief="groove")
        self.commandbuttons = CommandButtons(self)

        self.commandbuttons.grid(
            row=1, column=1, sticky=W+E+N+S, padx=5, pady=5)
        self.messagebox.grid(row=2, column=1, sticky=W+E+N+S, padx=5, pady=5)

        self.start_read()

        # Catch window deletion to kill the thread that reads data from serial
        self.parent.protocol("WM_DELETE_WINDOW", self._delete_window)

    def _delete_window(self):
        """ Catch window deletion to kill the thread that reads data from serial

        """
        try:
            self.interface.stop_read()
            self.parent.destroy()
        except:
            print("Error while deleting the window")

    def start_read(self):
        """ Start serial reading from the interface in a separate thread

        """
        t = threading.Thread(target=self.interface.start_read)
        t.start()


if __name__ == "__main__":
    baudrate = 115200
    path = './data'
    lps = Interface(baudrate=baudrate, path=path, bonjour="LAUNCHPADSTATION")

    root = tk.Tk()
    root.title("Launch Pad Command")

    MainApplication(root, lps).pack(side="top", fill="both", expand=True)

    root.mainloop()
