import copy
import threading
import datetime
import tkinter as tk
from tkinter import E, N, S, W

from utils import Interface

baudrate = 115200
path = './data'

lps = Interface(baudrate=baudrate, path=path, bonjour="LAUNCHPADSTATION")

old_messages = []

t = threading.Thread(target=lps.start_read)
t.start()


def diff_list(list1, list2):
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


def update_messages():
    global old_messages
    all_messages = lps.messages
    # print(all_messages)
    new_messages = diff_list(all_messages, old_messages)
    new_messages = sorted(new_messages, key=lambda tup: tup[0])
    old_messages = copy.copy(all_messages)
    new_lines = "".join(["{} : {}\n".format(
        e[0].time().replace(microsecond=0), e[1]) for e in new_messages])
    message_box.insert(tk.END, new_lines)
    message_box.yview_moveto(1)

    Root.after(100, update_messages)


Root = tk.Tk()
Root.title("Launch Pad Command")
frame_main = tk.Frame(Root)
frame_main.grid(row=1, column=1, sticky=W+E+N+S)

frame_buttons = tk.Frame(frame_main)
frame_buttons.grid(row=1, column=1, sticky=W+E+N+S)

button_A = tk.Button(frame_buttons, text="Send 'A'",
                     command=lambda: lps.send_command('A'))
button_B = tk.Button(frame_buttons, text="Send 'B'",
                     command=lambda: lps.send_command('B'))
button_A.grid(row=1, column=1)
button_B.grid(row=1, column=2)

frame_messages = tk.Frame(frame_main)
frame_messages.grid(row=2, column=1, sticky=W+E+N+S)

scroll_bar = tk.Scrollbar(frame_messages)
scroll_bar.grid(row=1, column=2, sticky=W+E+N+S)
message_box = tk.Text(frame_messages, height=10, width=100)
message_box.grid(row=1, column=1, sticky=W+E+N+S)
scroll_bar.config(command=message_box.yview)
message_box.config(yscrollcommand=scroll_bar.set)


update_messages()

Root.mainloop()

# Do not forget to stop reading from the serial link
lps.stop_read()
