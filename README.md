# Ground Station <!-- omit in toc -->


# Table of contents <!-- omit in toc -->
- [Purpose](#Purpose)
- [Requirements](#Requirements)
- [General description](#General-description)
  - [Sensors](#Sensors)
  - [Gateways](#Gateways)
    - [Telemetry Gateway](#Telemetry-Gateway)
    - [Launch Pad Station Gateway](#Launch-Pad-Station-Gateway)
- [How to install ?](#How-to-install-)
  - [Development](#Development)
    - [Dashboard](#Dashboard)
    - [Launch Pad Station control](#Launch-Pad-Station-control)
  - [Flight conditions](#Flight-conditions)
    - [Dashboard](#Dashboard-1)
    - [Launch Pad Station control](#Launch-Pad-Station-control-1)
- [Folder structure](#Folder-structure)


# Purpose

The software in this repository is everything needed to make the Ground Station for the Sigmundr Rocket work. This includes :

  - Managing the telemetry data:
    - Receiving the live telemetry data from the Rocket
    - Storing the received telemetry data in the computer's filesystem for later analysis
    - Displaying the received telemetry data in real time
  - Managing the Launch Pad Station:
    - Controling the Launch Pad Station
    - Monitoring the Launch Pad Station


# Requirements

- A laptop running Windows or Linux (not tested on MacOS)


# General description

The following elements are the main part of the rocket :
  * Sigmundr (Rocket) (see [aesirkth/Sigmundr_embedded_system](https://github.com/aesirkth/Sigmundr_embedded_system))
  * The Launch Pad Station (see [aesirkth/LaunchPadStation](https://github.com/aesirkth/LaunchPadStation))
  * The Ground Station (see this repository)
  * The FPV System (*not described here*)

Here is a diagram of the data links between these main systems :

![data_link](/doc/diagrams/data_links.png)
>The diagram was made with [draw.io](https://www.draw.io)<br>
>To make changes to it, edit the source file `/doc/diagrams/data_links.xml`

## Sensors

The following sensors are embedded on the Rocket :
  * Inertial Motion Unit `ICM20602` from Invensense
  * Static pressure sensor `BMP280` from Bosch
  * Magnetometer `LIS3MDLTR` from STMicroelectronics
  * Dynamic pressure sensor `ABPDRRT005PG2A5` from Honeywell
  * GPS receiver `M8Q` from u-blox


## Gateways

Gateways are added between the Ground Station and the Rocket and between the Ground Station and the Launch Pad System. Their role is to allow wireless communication between the Ground Station and the Rocket subsystems. The gateways are only forwarders. There is no logic embedded into them.

Here is a schematic of the data flow through the gateways :

![telemetry_link](/doc/diagrams/gateway.png)
>The diagram was made with [draw.io](https://www.draw.io)<br>
>To make changes to it, edit the source file `/doc/diagrams/gateway.xml`

In phase 1 : the computer finds the gateway

In phase 2 : actual communication through the gateway

`BONJOUR` is a unique string sent on serial connection initiation that is used to identify the LPS Gateway among all the serial devices connected to the Ground Station. The Telemetry Gatewa is found by trying to initiate the AT command mode


### Telemetry Gateway

The Telemetry Gateway is a `RFD900` modem.

See [RFD900](/doc/RFD900.md)


### Launch Pad Station Gateway

The *Launch Pad Station Gateway* is an Arduino with a USB port connected to a `RFM9XW` LoRa module

See [aesirkth/LaunchPadStation](https://github.com/aesirkth/LaunchPadStation)


# How to install ?

**Install the GUI requirements**

Install `python 3.7.4`

> Earlier versions of python could work as well but have not been tested

Install the required python packages

```sh
python -m pip install -r requirements.txt
```


## Development


### Dashboard

**Run the GUI**

Run `dashboard.py` with a dummy telemetry link

```
python ./dashboard.py dummy
```

Enjoy


### Launch Pad Station control

Get the *Launch Pad Station Board* up and running. See [aesirkth/LaunchPadStation](https://github.com/aesirkth/LaunchPadStation)


**Run the GUI**

Make sure the board is connected to your computer

Run `lps_control.py`

```
python ./lps_control.py
```

Enjoy


## Flight conditions


### Dashboard

**Run the GUI**

Run `dashboard.py` with a `RFD900` modem

```
python ./dashboard.py rfd
```

Enjoy


### Launch Pad Station control

Get the *LPS Board* and the *LPS Gateway* up and running. See [aesirkth/LaunchPadStation](https://github.com/aesirkth/LaunchPadStation)


**Run the GUI**

Make sure the gateway is connected to your computer. Make sure the *LPS Board* is powered.

Run `lps_control.py`

```
python ./lps_control.py
```

Enjoy


# Folder structure

``` py
.
├── README.md                   # This file
├── data/                       # (Ungitted) folder to store the received telemetry
├── doc/                        # The documentation goes there
├── gui/
│   └── widgets.py              # Widgets used in the LPS control GUI
├── utils/
│   ├── gateway.py              # Class used to process data from the Gateways
│   ├── sensors.py              # Class used to process data from the sensors
│   └── serialwrapper.py        # Class used to read/write data from serial link
├── dashboard.py                # Dashboard
├── lps_control.py              # GUI to control the Launch Pad Station
├── radio_test.py               # Small utility to test the telemetry radio link
└── requirements.txt
```