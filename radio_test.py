import signal
import sys
import time

from utils import Gateway, Sensors, SerialWrapper


n_errors = 0
n_missed = 0
n_frames = 0


def signal_handler(sig, frame):
    if sys.argv[1] == 'receiver':
        print("Number of received frames : {}".format(n_frames))
        print("Number of errors : {}".format(n_errors))
        print("Number of missed frames : {}".format(n_missed))
    sys.exit(0)


def sender(radio):
    i = 0
    print('Started sending data')
    while True:
        # Encoded using utf-8 in send_command(). Should use 1 Byte/symbol
        frame = "{:0<7}:ababababababababababababababababababababa".format(i) # 50 symbols
        radio.send_command(frame)
        i += 1
        if i >= 1e7:
            i = 0
        # This should give an output bit rate < 4 kbps
        time.sleep(0.1)


def receiver(radio):
    global n_frames, n_errors, n_missed
    c = -1
    if radio.serial.open_serial():
        while True:
            
                frames = radio.serial.readlines()
                for frame in frames:
                    n_frames += 1
                    count, test = frame.split(":")
                    if int(count) != c+1:
                        n_missed += 1
                    c = int(count)
                    if c >= 1e7 - 1:
                        c = -1

                    if test != "ababababababababababababababababababababa":
                        n_errors += 1
    else:
        print("Failed to open port")


if __name__ == "__main__":

    if not len(sys.argv) >= 2:
        print("Error : run script with 'sender' or 'receiver' as argument")
    
    else:
        if not sys.argv[1] == "sender" and not sys.argv[1] == "receiver":
            print("Error : first argument not recognized. Use 'sender' or 'receiver'")

        else:
            role = sys.argv[1]

            # Use this with a RFD900 modem
            serial = SerialWrapper(baudrate=115200, name="Telemetry", rfd900=True)            
            sensors = Sensors()
            radio = Gateway(serial=serial, sensors=sensors, path="./data")

            signal.signal(signal.SIGINT, signal_handler)

            print('Press Ctrl+C to exit')

            if role == "sender":
                sender(radio)
            elif role == "receiver":
                receiver(radio)
