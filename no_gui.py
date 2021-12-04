from signal import signal, SIGINT
from utils.telemetry import Telemetry
from datetime import datetime
import sys
from utils.save import save_data_to_file_csv
import time

def handler(signal, frame):
    now = datetime.now()
    name = "no_gui_" + now.strftime("%Y-%m-%d-%H-%M-%S")
    print(f"saving to {name}")
    save_data_to_file_csv(tm.data, name)
    tm.stop()
    sys.exit(0)

tm = Telemetry()

if len(sys.argv) > 1:
    tm.open_flash_file(sys.argv[1])
else:
    tm.open_serial()


signal(SIGINT, handler)