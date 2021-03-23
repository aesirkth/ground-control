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
controller.py - starts the Qt GUI for the flight and engien controllers
engine_dashbord.py - starts the Qt GUI for the engine dashboard

utils/
├─ data_handling.py - functions and datatypes to handle the raw serial data
├─ definitions.py - 
├─ edda_messages.json
├─ gateway.py - all the code for the gateway
├─ serial_reader.py - reader around pyserial also contains the base for the 
                      telecommand and telemetry thread
├─ telecommand.py - all the code for the telecommand downlink
├─ telemetry.py - all the code for the telemetry downlink
├─ widgets_ec.py - GUI widgets for the engine part of controller.py
├─ widgets_edb.py - GUI widgets for the engine dashboard
├─ widgets_fc.py - GUI widgets for the flight part of controller.py
```