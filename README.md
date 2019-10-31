# Ground Station <!-- omit in toc -->


# Table of contents <!-- omit in toc -->
- [Purpose](#Purpose)
- [Requirements](#Requirements)
- [General description](#General-description)
  - [Sensors](#Sensors)
- [Ground Station](#Ground-Station)
  - [Ground Station Computer](#Ground-Station-Computer)
  - [Gateways](#Gateways)
    - [Purpose](#Purpose-1)
    - [Wiring](#Wiring)
      - [Telemetry Gateway](#Telemetry-Gateway)
      - [LPS Gateway](#LPS-Gateway)
- [How to install ?](#How-to-install-)
  - [Development](#Development)
  - [Flight conditions](#Flight-conditions)
- [Folder structure](#Folder-structure)


# Purpose

The software in this repository is everything needed to make the Ground Station work. This includes :

  - Managing the telemetry data:
    - Receiving the live telemetry data from the Rocket
    - Storing the received telemetry data in the computer's filesystem for later analysis
    - Display the received telemetry data in real time
  - Managing the Launch Pad Station:
    - Controling the Launch Pad Station
    - Monitoring the Launch Pad Station


# Requirements

- A computer running Windows or Linux (not tested on MacOS)
- One or two Arduino board with a USB port (for development)
- One Arduino board with a USB port connected to an `RFM96W` LoRa tranceiver (to communicate with the Launch Pad Station)
- One `RFD900` Radio Modem and FTDI cable (to receive telemetry data from the Rocket)


# General description

The following elements are the main part of the rocket :
  * Rocket (see [aesirkth/Sigmundr_embedded_system](https://github.com/aesirkth/Sigmundr_embedded_system))
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


# Ground Station

This repository contains all the software required to run the items in the grey box (Ground Station).


## Ground Station Computer

The Ground Station Computer sends and receives data through the gateways. It runs a dashboard ([dashboard](doc/dashboard.md)) that displays the telemetry received from the Rocket and controls the Launch Pad Station.

There is also a simplified version of the dashboard that only controls the Launch Pad Station ([lps_control](doc/lps_control.md)).


## Gateways


### Purpose

Gateways are added between the Ground Station Computer and the Rocket and between the Ground Station Computer(s) and the Launch Pad System. Their role is to allow wireless communication between the Ground Station Computer and the Rocket subsystems. The gateways are only forwarders. There is no logic embedded into them.

Here is a schematic of the data flow through the gateways :

![telemetry_link](/doc/diagrams/gateway.png)
>The diagram was made with [draw.io](https://www.draw.io)<br>
>To make changes to it, edit the source file `/doc/diagrams/gateway.xml`

In phase 1 : the computer finds the gateway

In phase 2 : actual communication through the gateway

`BONJOUR` is a unique string sent on serial connection initiation that is used to identify the Telemetry Gateway and the LPS Gateway among all the serial devices connected to the Ground Station Computer.


### Wiring


#### Telemetry Gateway

Connect the FTDI cable to the `RFD900`. The black cable should be connected to pin `1`. Connect a jumper between pin `4` and pin `6`.

See the pin layout and the FTDI cable connection in the [RFD900 Datasheet](http://files.rfdesign.com.au/Files/documents/RFD900%20DataSheet.pdf).

See the software requirements in the [RFD900 Software Manual](http://files.rfdesign.com.au/Files/documents/Software%20manual.pdf).


#### LPS Gateway

>TODO


# How to install ?


## Development

**Create a fake gateway**

Upload `dummy_gateway.ino` to any Arduino board with a USB port. Make sure to uncomment one of these two lines before :

```c
// Uncomment one of these to select the target gateway
// #define lps
// #define telemetry
```

**Install the GUI requirements**

Install `python 3.7.4`

> Earlier versions of python could work as well but have not been tested

Install the required python packages

```sh
python -m pip install -r requirements.txt
```

**Run the GUI**

Make sure the board is connected to your computer

Run `dashboard.py` for the complete interface

```
python ./dashboard.py
```

Or

Run `lps_control.py` to only control the Launch Pad Station

```
python ./lps_control.py
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
├── dummy_gateway/
│   └── dummy_gateway.ino       # Code to emulate a working gateway with an Arduino board
├── gui/
│   └── widgets.py              # Widgets used in the LPS control GUI
├── utils/
│   ├── gateway.py              # Class used to process data from the Gateways
│   ├── sensors.py              # Class used to process data from the sensors
│   └── serialwrapper.py        # Class used to read/write data from serial link
├── dashboard.py                # Dashboard
├── lps_control.py              # GUI to control the Launch Pad Station
└── requirements.txt
```