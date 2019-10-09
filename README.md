# Ground Station <!-- omit in toc -->


# Table of contents <!-- omit in toc -->
- [Purpose](#purpose)
- [Functionalities](#functionalities)
- [Hardware](#hardware)
- [Sensors](#sensors)
- [Transmission protocol](#transmission-protocol)
- [File storage](#file-storage)
- [How to use ?](#how-to-use-)
  - [Testing](#testing)
  - [Flight conditions](#flight-conditions)
- [Folder structure](#folder-structure)


# Purpose

This software is designed to deal with the incomming data from the rocket and it's systems. Ability to control the Launch Pad Station should also be included here.

It runs with `python 3.7.4`


# Functionalities

The Ground Station can display in real time the telemetry data sent from the rocket during the flight. The received data is stored on the Ground Station hard drive for future use.

The telemetry data is received via radio link by an Arduino board and sent to the computer in real time via serial link. The radio link is unidirectional : it is not possible to send data to the rocket during the flight.

The raw telemetry data is processed on the fly on the Ground Station and not on the rocket.

This software should :

* [x] Read the raw data from serial connection
* [x] Record all the received data for future utilisation
* [ ] Convert the raw data from sensors
* [ ] Display the following values in real time (time related curves if possible)
  * [ ] Altitude
  * [ ] Pressure
  * [ ] Speed
  * [ ] GPS position
  * [ ] Engine status
  * [ ] ...


*Tick the tasks once successfully implemented and tested*


# Hardware

The hardware is made of the following elements :
  * Rocket
  * The Launch Pad Station
  * The Telemetry Receiver 
  * The Ground Station
  * The FPV System (*not described here*)


Here is a diagram of the data links between the subsystems :

![data_link](/doc/diagrams/data_links.png)


>The diagram was made with [draw.io](https://www.draw.io)<br>
>To make changes to it, edit the source file `/doc/diagrams/data_links.xml`


The Telemetry Interface and Launch Pad Station Interface are only forwarders. There is no logic embeded into them.

Here is a schematic of the data flow trough the interfaces :

![telemetry_link](/doc/diagrams/interface_link.png)

`BONJOUR` is a unique string sent on serial connection initiation that is used to identify the Telemetry Interface and the LPS Interface amoung all the serial devices connected to the Dashboard Computer


# Sensors

The following sensors are embedded on the Rocket :
  * Inertial Motion Unit `ICM20602` from Invensense
  * Static pressure sensor `BMP280` from Bosch
  * Magnetometer `LIS3MDLTR` from STMicroelectronics
  * Dynamic pressure sensor `ABPDRRT005PG2A5` from Honeywell
  * GPS receiver `M8Q` from u-blox


# Transmission protocol

For phase 1, the above schematic should be self explaining.

For phase 2, see [this issue](https://github.com/aesirkth/GroundStation/issues/4)


# File storage

See [this issue](https://github.com/aesirkth/GroundStation/issues/4)


# How to use ?


## Testing

Install `python 3.7.4` on your computer

> Earlier versions of python could work as well but have not been tested

Install the required python packages

```sh
python3 -m pip install -r requirements.txt
```

Upload `dummy_telemetry.ino` to an Arduino board

Make sure the board is connected to your computer

Run `dashboard.py`

```
python3 ./dashboard.py
```

Enjoy


## Flight conditions

>TODO


# Folder structure

``` py
.
├── README.md                   # This file
├── data/                       # (Ungitted) folder to store the received telemetry
├── doc/                        # The documentation goes there
├── dummy_telemetry/
│   └── dummy_telemetry.ino     # Example telemetry code for arduino
├── utils/
│   ├── interface.py            # Class used to process data from Interface devices
│   └── serialwrapper.py        # Class used to read/write data from serial link
├── dashboard.py                # Dashboard
└── requirements.txt
```