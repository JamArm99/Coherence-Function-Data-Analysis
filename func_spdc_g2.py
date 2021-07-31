#!/usr/bin/env python

#Defining functions for scipy
import numpy as np

#Gaussian
def gaussian(x, a, b, c):
    '''
    Function which generates a Gaussian function for a data set x. The Gaussian has a coefficient a, x offset b, and a width c.
    '''
    if a ==0 or c==0: #Unphysical to have no coefficent or width
        raise ValueError('Gaussian coefficient cannot be 0')
    return a * np.exp((-(x-b)**2)/(2*c*c))

#Full Width at Half Maximum
def FWHM(sigma):
    '''
    Function which gives the full width at half-maximum of a Gaussian from its width sigma.
    '''
    if sigma ==0:#Unphysical to have no width
        raise ValueError('Width of Gaussian cannot be 0')
    return 2*sigma*((2*np.log(2))**(1/2))

#Second-order coherence function
def g2_func(t,s):
    '''
    Numerical function for modelling the antibunching dip at time delay 0.
    '''
    return 32 - 32*np.exp((-((t+0.6)**2))/(2*s**2))

