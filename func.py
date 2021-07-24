#!/usr/bin/env python

#Defining functions for scipy
import numpy as np

#Gaussian
def gaussian(x, a, b, c):
    if a ==0 or c==0: #Unphysical to have no coefficent or width
        raise ValueError('Gaussian coefficient can not be 0')
    return a * np.exp((-(x-b)**2)/(2*c*c))

#Full Width at Half Maximum
def FWHM(sigma):
    if sigma ==0:#Unphysical to have no width
        raise ValueError('Width of Gaussian can not be 0')
    return 2*sigma*((2*np.log(2))**(1/2))

#Second-order coherence function
def g2_func(t,s):
    return 32 - 32*np.exp((-((t+0.6)**2))/(2*s**2))

