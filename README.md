![image](docs/img.png)

## dummy RFD modem
Use [this](https://github.com/klownfish/serial-dummy) to emulate a basic version of the RFD modem.
It runs on a teensy LC (might run on anything if you change the target).

The data will stored in the following dicts
```
tm.["flight"]["pressure"]
tm.["flight"]["altitude"]
tm.["flight"]["gyrox"]
tm.["flight"]["gyroy"]
tm.["flight"]["gyroz"]
tm.["flight"]["acceleration"]
tm.["engine"]["catastrophe"]
```

## dependencies
Install the python dependencies\
`python -m pip install -r requirements.txt`

Tkinter is included with Python since Python 3.1

## file structure
```
main.py - starts a basic tkinter GUI Only used for debugging
main_qt.py - starts the QT GUI
utils/
├─ widgets.py - GUI widgets for tkinter (only used for debugging)
├─ serial_wrapper.py - wrapper around pyserial also contains the base for the 
                       telecommand and telemetry thread
├─ gateway.py - all the code for the gateway
├─ telemetry.py - all the code for the telemetry downlink
├─ telecommand.py - all the code for the telecommand downlink
├─ data_handling.py - functions and datatypes to handle the raw serial data
├─ widgets_qt - GUI widgets for the dashboard
├─ data/
   ├─   backups of the raw serial communication
```