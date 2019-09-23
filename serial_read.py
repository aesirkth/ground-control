import csv
import datetime
from os import mkdir
from os.path import dirname, isdir

import serial

# Change this to the right port you want to read
port = 'COM3'
baudrate = 115200
path = './data/telemetry.csv'

# See ./dummy_telemetry/dummy_telemetry.ino for the description of the protocol
newline = "N"
newhead = "H"
endline = "E"
sepdata = "\t"


def resetCSV(path=path):
    base = dirname(path)
    
    if not isdir(base):
        mkdir(base)
    
    with open(path, 'w+'):
        print("CVS file flushed")


def writeCSV(dataArray):
    with open(path, 'a', newline='') as csvFile:
        writer = csv.writer(csvFile, delimiter=',')
        writer.writerow(dataArray)


def check_header(line):
    return len(line) > 0 and line[0] == newhead and line[-1] == endline


def check_line(line):
    return len(line) > 0 and line[0] == newline and line[-1] == endline


def main():
    # NB: need to find a way to catch timeouts
    with serial.Serial(port, baudrate=baudrate, timeout=0.1) as ser:
        def get_line():
            line = ser.readline()
            line = line.decode('ascii')
            line = line.replace("\r\n", "")
            return line

        resetCSV()
        ser.reset_input_buffer() #reset the buffer

        got_header = False
        print("Waiting for header...")
        while not got_header:
            line = get_line()
            if check_header(line):
                header_data = ["Time"] + line[1:-1].split(sepdata)
                writeCSV(header_data)
                got_header = True
                print("Header received : {}".format(",".join(header_data)))

        while True:
            line = get_line()
            now = datetime.datetime.utcnow().isoformat()
            
            if check_line(line):
                print(line)
                line_data = [now] + line[1:-1].split(sepdata)
                writeCSV(line_data)




if __name__ == "__main__":
    main()
