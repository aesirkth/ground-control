""" Simple script to test the link between two RFD900 modems

Use `python radio_test.py sender` to start sending data over the serial link
to the RFD900 that acts as a sender. Press 'Ctrl+C' to stop sending

Use `python radio_test.py receiver` on the receiver side. The number of reception
errors is recorded. Press 'Ctrl+C' to stop receiving and display the error rate

NB: the error count does not work

"""

import signal
import sys
import time

from utils import Gateway, Sensors, SerialWrapper


n_frames = 0
n_missed = 0
n_errors = 0


# This is triggered when 'Ctrl+C' is pressed
def signal_handler(sig, frame):
    if sys.argv[1] == 'receiver':
        print("Number of received frames : {}".format(n_frames))
        print("Number of missed frames : {}".format(n_missed))
        print("Number of errors : {}".format(n_errors))
    radio.serial.close_serial()
    # Exit the script
    sys.exit(0)


def send_data(radio):
    i = 0
    
    if not radio.serial.open_serial():
        print('Failed to open port')
    
    else:
        print('Started sending data')
        print('Press Ctrl+C to exit')
        while True:
            # Encoded using utf-8 in send_command(). Should use 1 Byte/symbol
            frame = "{:0>7}:abababababababababababababababababababab\n".format(i)  # 50 symbols
            radio.send_command(frame)
            i += 1
            if i >= 1e7:
                i = 0
            # This should give an output bit rate < 4 kbps
            time.sleep(0.1)


def receive_data(radio):
    global n_frames, n_errors, n_missed
    c = None

    if not radio.serial.open_serial():
        print('Failed to open port')
    
    else:
        while True:
            frames = radio.serial.readlines()
            
            for frame in frames:
                print(frame)
                try:
                    count, test = frame.replace('+++', '').split(':')
                    count = int(count)
                    n_frames += 1
                    if c is None:
                        c = count
                    else:
                        if count != c+1:
                            n_missed += count - c+1
                        c = int(count)
                        if c >= 1e7 - 1:
                            c = -1

                    if test != "abababababababababababababababababababab":
                        n_errors += 1
                except Exception as e:
                    print('Except', e)


if __name__ == "__main__":

    if not len(sys.argv) >= 2:
        print("Error : no argument received. Run script with 'sender' or 'receiver' as argument")

    else:
        sender = sys.argv[1] == "sender"
        receiver = sys.argv[1] == "receiver"

        if not sender and not receiver:
            print("Error : first argument not recognized. Use 'sender' or 'receiver'")

        else:
            role = sys.argv[1]

            # Use this with a RFD900 modem
            serial = SerialWrapper(115200, "Telemetry", rfd900=True)
            sensors = Sensors()
            radio = Gateway(serial, sensors, "./data")

            signal.signal(signal.SIGINT, signal_handler)

            if role == "sender":
                send_data(radio)
            elif role == "receiver":
                receive_data(radio)
