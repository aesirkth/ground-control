# Ground Station <!-- omit in toc -->


# Table of contents <!-- omit in toc -->
- [Purpose](#purpose)
- [General description](#general-description)
  - [Interfaces](#interfaces)
  - [Sensors](#sensors)
- [Functionalities](#functionalities)
  - [Dashboard](#dashboard)
  - [LPS Control](#lps-control)
- [How to use ?](#how-to-use-)
  - [Development conditions](#development-conditions)
  - [Flight conditions](#flight-conditions)
- [Transmission protocol](#transmission-protocol)
- [File storage](#file-storage)
- [Folder structure](#folder-structure)


# Purpose

This software is designed to deal with the incomming data from the rocket and it's systems. Ability to control the Launch Pad Station is also included.

It runs with `python 3.7.4`


# General description

The following elements are the main systems:
  * Rocket
  * The Launch Pad Station
  * The Ground Station
  * The FPV System (*not described here*)

Here is a diagram of the data links between these main systems :

![data_link](/doc/diagrams/data_links.png)

The Dashboard can be one or two computers

>The diagram was made with [draw.io](https://www.draw.io)<br>
>To make changes to it, edit the source file `/doc/diagrams/data_links.xml`


## Interfaces

Interfaces are added between the Ground Station Computer(s) and the Rocket and between the Ground Station Computer(s) and the Launch Pad System. Their role is to allow wireless communication between the Dashboard and the Rocket subsystems. The interfaces are only forwarders. There is no logic embeded into them.

Here is a schematic of the data flow trough the interfaces :

![telemetry_link](/doc/diagrams/interface_link.png)

`BONJOUR` is a unique string sent on serial connection initiation that is used to identify the Telemetry Interface and the LPS Interface amoung all the serial devices connected to the Dashboard Computer

>The diagram was made with [draw.io](https://www.draw.io)<br>
>To make changes to it, edit the source file `/doc/diagrams/interface_link.xml`


## Sensors

The following sensors are embedded on the Rocket :
  * Inertial Motion Unit `ICM20602` from Invensense
  * Static pressure sensor `BMP280` from Bosch
  * Magnetometer `LIS3MDLTR` from STMicroelectronics
  * Dynamic pressure sensor `ABPDRRT005PG2A5` from Honeywell
  * GPS receiver `M8Q` from u-blox


# Functionalities


## Dashboard

The Ground Station Dashboard can display in real time the telemetry data sent from the rocket during the flight. The received data is stored on the Ground Station hard drive for future use.

The telemetry data is received via radio link by an Arduino board and sent to the computer in real time via serial link. The radio link is unidirectional : it is not possible to send data to the rocket during the flight.

The raw telemetry data is processed on the fly on the Ground Station and not on the rocket.


## LPS Control

The LPS Control GUI is extremely simple.

Click on "Open link" to open the Serial connection to to LPS Interface. Click on the buttons to send the desired command. The LPS replies to the commands by sending them back as messages. Such messages are displayed in the text box.

![lps_1](/doc/images/lps_control_1.png)
![lps_2](/doc/images/lps_control_2.png)


# How to use ?


## Development conditions

Install `python 3.7.4` on your computer

> Earlier versions of python could work as well but have not been tested

Install the required python packages

```sh
python3 -m pip install -r requirements.txt
```

Upload `dummy_interface.ino` to an Arduino board. Make sure to uncomment one of these two lines before :

```c
// Uncomment one of these to select the target interface
// #define lps
// #define telemetry
```

Make sure the board is connected to your computer

Run `dashboard.py` for the complete interface

```
python3 ./dashboard.py
```

**OR** 

Run `lps_control.py` to only control the Launch Pad Station

```
python3 ./lps_control.py
```

Enjoy


## Flight conditions

>TODO

# Transmission protocol

For phase 1, the above schematic should be self explaining.

For phase 2, see [this issue](https://github.com/aesirkth/GroundStation/issues/4)


# File storage

See [this issue](https://github.com/aesirkth/GroundStation/issues/4)


# Folder structure

``` py
.
├── README.md                   # This file
├── data/                       # (Ungitted) folder to store the received telemetry
├── doc/                        # The documentation goes there
├── dummy_interface/
│   └── dummy_interface.ino     # Example telemetry code for arduino
├── gui/
│   └── widgets.py              # Widgets used in the LPS control GUI
├── utils/
│   ├── interface.py            # Class used to process data from Interface devices
│   └── serialwrapper.py        # Class used to read/write data from serial link
├── dashboard.py                # Dashboard
├── lps_control.py              # GUI to control the Launch Pad Station
└── requirements.txt
```