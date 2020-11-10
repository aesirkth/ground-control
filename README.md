![image](docs/img.png)

## dummy modem
It uses the same teensy lc as https://github.com/klownfish/aesir-grafana-dashboard

## dependencies
Install the python dependencies\
`python -m pip install -r requirements.txt`

Tkinter is included with Python since Python 3.1

## file structure
```
main.py - spawns the GUI and the thread that handles serial
utils/
├─ widgets.py - GUI widgets
├─ serial_wrapper.py - wrapper around pyserial
├─ gateway.py - all the code for the gateway
├─ telemetry.py - all the code for the telemetry
├─ data_functions.py - functions and datatypes to handle the raw serial data
├─ data_functionsp.py - W.I.P implementaion of the real protocol
├─ data/ - backups of the raw serial communication
```
things to do:
* Make serial wrapper init communication with a RFD modem and the launchpad gateway.
* Implement gateway transmission protocol

* Work on the UI
    * Figure out a better way to represent widgets,\
    * Start grouping widgets together in a frame so you don't have to place everything manually\
    * implement the map thing from the old dashboard\
    * A actual map that shows the rocket position would be cool\
    * create two windows, for engine and flight controller\
