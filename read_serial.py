# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 13:37:10 2019

@author: noe
"""

import serial
import csv
from test2 import live_plotter
import numpy as np
#import time


def writeCSV(dataArray):
    with open('writtenData.csv', 'a+') as csvFile:
        writer = csv.writer(csvFile, delimiter=',')
        writer.writerow(dataArray)


size = 100
x_vec = np.linspace(0,1,size)
y1_vec = [0 for i in range(size)]
y2_vec = [0 for i in range(size)]
line1 = []
line2 = []


data_read = [0,0,0,0,0]
ser = serial.Serial('COM6', 9600) #change the serial port with the good one
print(str(ser))

ser.reset_input_buffer() #reset the buffer
while True :
    while ser.inWaiting() >= 5 :
        data_read = ser.read(5)
        print(data_read)
        print(data_read[0],data_read[1],data_read[2],data_read[3],data_read[4])
        #time.sleep(0.1)
        y1_vec[-1] = data_read[0]
        y2_vec[-1] = data_read[1]
        [line1,line2] = live_plotter(x_vec,y1_vec,y2_vec,line1,line2)
        y1_vec = np.append(y1_vec[1:],0)
        y2_vec = np.append(y2_vec[1:],0)
        writeCSV(data_read)
        
        
        
        