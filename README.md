# Ground Station <!-- omit in toc -->

This software is intended to read the data received by the receiver in real time and display it in a clear way to follow the flight parameters.

It runs using `python 3.7.4`

- [Functionalities](#functionalities)
- [TODO](#todo)
- [Hardware](#hardware)
- [Transmission protocol](#transmission-protocol)
- [Installation](#installation)
- [Folder structure](#folder-structure)

# Functionalities

This software should :

* [ ] Read the raw data from serial connection
* [ ] Convert the raw data from sensors
* [ ] Record all the received data for future utilisation
* [ ] Display the following values in real time (time related curves if possible)
  * [ ] Altitude
  * [ ] Pressure
  * [ ] Speed
  * [ ] GPS position
  * [ ] Engine status
  * [ ] ...


*Tick the tasks once successfully implemented and tested*

It is assumed that the sensors' data is not processed in any way by the embedded computer. The data received is raw and should be converted to readable values by the ground station.

>NB : how do we deal with the calibration of the sensors ?

# TODO

* [ ] Get the list of the sensors to be read
* [ ] Define precisely what data to plot and which graph to use
* [ ] Define the data format for the recordings

# Hardware

This software should run on a standard computer running Windows. It should work as well on Unix systems but has not been tested.

# Transmission protocol

See the example telemetry code [here](./dummy_telemetry/dummy_telemetry.ino)

# Installation

Install `python 3.7.4`

Run `python3 -m pip install -r requirements.txt`

Enjoy

# Folder structure

``` py
.
├── README.md                   # This file
├── data/                       # (Ungitted) folder to store the received telemetry
├── dummy_telemetry/
│   └── dummy_telemetry.ino     # Example telemetry code for arduino
├── read_serial.py              # unused
├── requirements.txt
├── serial_read.py
└── test2.py                    # unused
```