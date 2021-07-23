#!/usr/bin/env python

#Defining functions for scipy
import numpy as np

#Gaussian
def gaussian(x, a, b, c):
    return a * np.exp((-(x-b)**2)/(2*c*c))

#Full Width at Half Maximum
def FWHM(sigma):
    return 2*sigma*((2*np.log(2))**(1/2))

#Second-order coherence function
def g2_func(t,s):
    return 32 - 32*np.exp((-((t+0.6)**2))/(2*s**2))

