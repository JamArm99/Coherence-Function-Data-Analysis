import unittest
import func_spdc_g2
import numpy as np
from scipy.stats import shapiro

class TestSPDC(unittest.TestCase):

    #Test Gaussian function
    def test_gaus(self):
        xdata = np.linspace(-1,1,100)#Create some xdata for gaussian
        stat, p = shapiro(func_spdc_g2.gaussian(xdata,1,0,0.1))#Statistical power 

        self.assertLessEqual(p, 0.05)#Shapiro-Wilk test for Gaussian distribution
        
        with self.assertRaises(ValueError):
            func_spdc_g2.gaussian(xdata,0,0,1)#0 coefficient is not allowed
            func_spdc_g2.gaussian(xdata,1,0,0)#0 sigma is not allowed
            func_spdc_g2.gaussian(xdata,0,0,0)#Both sigma and coefficient

    def test_fwhm(self):
        with self.assertRaises(ValueError):
            func_spdc_g2.FWHM(0)#0 sigma
        

#Running unittest directly in terminal/editor
if __name__ == '__main__':
    unittest.main()
#Default is python3 -m unittest test_spdc_g2.py