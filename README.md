# Ground Station <!-- omit in toc -->


# Table of contents <!-- omit in toc -->
- [Purpose](#purpose)
- [Requirements](#requirements)
- [General description](#general-description)
  - [Sensors](#sensors)
- [Ground Station](#ground-station)
  - [Ground Station Computer](#ground-station-computer)
  - [Gateways](#gateways)
    - [Purpose](#purpose-1)
    - [Telemetry Gateway](#telemetry-gateway)
    - [LPS Gateway](#lps-gateway)
- [How to install ?](#how-to-install-)
  - [Development](#development)
    - [Telemetry link](#telemetry-link)
    - [Launch Pad Station link](#launch-pad-station-link)
  - [Flight conditions](#flight-conditions)
- [Folder structure](#folder-structure)


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

`BONJOUR` is a unique string sent on serial connection initiation that is used to identify the LPS Gateway among all the serial devices connected to the Ground Station Computer. The Telemetry Gatewa is found by trying to initiate the AT command mode.


### Telemetry Gateway

The Telemetry Gateway is a `RFD900` modem.

See [RFD900](/doc/RFD900.md)


### LPS Gateway

>TODO


# How to install ?


## Development

**Install the GUI requirements**

Install `python 3.7.4`

> Earlier versions of python could work as well but have not been tested

Install the required python packages

```sh
python -m pip install -r requirements.txt
```

### Telemetry link

**Create a fake Telemetry Gateway**

Upload `dummy_gateway.ino` to any Arduino board with a USB port. Make sure to uncomment one of these two lines before :

```c
// Uncomment one of these to select the target gateway
// #define lps
#define telemetry
```


**Run the GUI**

Make sure the board is connected to your computer

Make sure `dashboard.py` is set to use the fake gateway

```py
if __name__ == "__main__":
    # Use this with a RFD900 modem
    # serial = SerialWrapper(baudrate=57600, name="Telemetry", rfd900=True)
    # Use this for testing with an Arduino board and `dummy_telemetry.ino`
    serial = SerialWrapper(baudrate=115200, name="Telemetry", bonjour="TELEMETRY")
```

Run `dashboard.py`

```
python ./dashboard.py
```

Enjoy


### Launch Pad Station link

**Create a fake LPS Gateway**

Upload `dummy_gateway.ino` to any Arduino board with a USB port. Make sure to uncomment one of these two lines before :

```c
// Uncomment one of these to select the target gateway
#define lps
// #define telemetry
```


**Run the GUI**

Make sure the board is connected to your computer

Make sure `lps_control.py` is set to use the fake gateway

```py
if __name__ == "__main__":
    serial = SerialWrapper(baudrate=115200, name="LPS", bonjour="LAUNCHPADSTATION")
```

Run `lps_control.py`

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