# -*- coding: utf-8 -*-
"""
Created on Thu May  7 22:35:59 2020

@author: tanusha.goswami
"""
from math import sin
import numpy as np
from matplotlib import pyplot as plt


def plot_growth(growth_rate, initial_value, flag = 1):
    N = 10000
    x = np.zeros(N)
    x[0] = initial_value
    for i in range(1,N):
        x[i] = growth_rate*np.sin(x[i-1])
    plt.plot(x)  
    if flag == 1:
        return x
    
    
subplot_count = 1
for rate in np.linspace(0,5,10):
    fig = plt.figure(figsize = (10,30))
    plt.subplot(10,1,subplot_count)
    plot_growth(rate, 0.4)
    plt.title('Growth Rate: ' + str(rate))
    subplot_count +=1 
    
plt.show()
    

    




    