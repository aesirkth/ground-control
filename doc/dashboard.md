# Dashboard

`dashboard.py`

The dashboard can receive and display in real time the telemetry data sent from the rocket during the flight. The received data is stored on the Ground Station hard drive for future use.

The telemetry data is received via radio link by an Arduino board and sent to the computer in real time via serial link. The radio link is unidirectional : it is not possible to send data to the rocket during the flight.

The raw telemetry data is processed on the fly on the Ground Station and not on the rocket.


# Transmission protocol

See [this issue](https://github.com/aesirkth/GroundStation/issues/4)


# File storage

See [this issue](https://github.com/aesirkth/GroundStation/issues/4)