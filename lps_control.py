import tkinter as tk
from tkinter import E, N, S, W

from gui import CommandButtons, InterfaceStatus, MessageBox
from utils import Interface


class MainApplication(tk.Frame):
    def __init__(self, parent, interface, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.lps = interface

        self.messagebox = MessageBox(self, self.lps, borderwidth=2, relief="groove")
        self.commandbuttons = CommandButtons(self, self.lps)
        self.interfacestatus = InterfaceStatus(self, self.lps)

        self.interfacestatus.grid(
            row=0, column=1, sticky=W+E+N+S, padx=5, pady=5)
        self.commandbuttons.grid(
            row=1, column=1, sticky=W+E+N+S, padx=5, pady=5)
        self.messagebox.grid(row=2, column=1, sticky=W+E+N+S, padx=5, pady=5)


if __name__ == "__main__":
    baudrate = 115200
    path = './data'
    lps = Interface(baudrate=baudrate, path=path, bonjour="LAUNCHPADSTATION")

    root = tk.Tk()
    root.title("Launch Pad Command")

    MainApplication(root, lps).pack(side="top", fill="both", expand=True)

    root.mainloop()
