# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:55:16 2019

@author: noe
"""

import matplotlib.pyplot as plt
import numpy as np

# use ggplot style for more sophisticated visuals
plt.style.use('ggplot')

def live_plotter(x_vec,y1_data,y2_data,line1,line2,identifier='',pause_time=0.05):
    if line1==[]:
        # this is the call to matplotlib that allows dynamic plotting
        plt.ion()
        fig = plt.figure(figsize=(13,6))
        ax1 = fig.add_subplot(1,2,1)
        ax2 = fig.add_subplot(1,2,2)
        # create a variable for the line so we can later update it
        line1, = ax1.plot(x_vec,y1_data,'-o',alpha=0.8)
        line2, = ax2.plot(x_vec,y2_data,'-o',alpha=0.8)         
        #update plot label/title
        plt.ylabel('Y Label')
        plt.title('Title: {}'.format(identifier))
        plt.show()
    
    # after the figure, axis, and line are created, we only need to update the y-data
    line1.set_ydata(y1_data)
    line2.set_ydata(y2_data)
    # adjust limits if new data goes beyond bounds
    if np.min(y1_data)<=line1.axes.get_ylim()[0] or np.max(y1_data)>=line1.axes.get_ylim()[1]:
        plt.subplot(121).set_ylim([np.min(y1_data)-np.std(y1_data),np.max(y1_data)+np.std(y1_data)])
    if np.min(y2_data)<=line2.axes.get_ylim()[0] or np.max(y2_data)>=line2.axes.get_ylim()[1]:
        plt.subplot(122).set_ylim([np.min(y2_data)-np.std(y2_data),np.max(y2_data)+np.std(y2_data)])
    # this pauses the data so the figure/axis can catch up - the amount of pause can be altered above
    plt.pause(pause_time)
    
    # return line so we can update it again in the next iteration
    return line1,line2
