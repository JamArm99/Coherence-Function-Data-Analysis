#!/usr/bin/env python

#Importing python libraries
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as spy
import os

#Uncomment the next two lines if the input .txt files are large.
#import sys
#sys.setrecursionlimit(N)

import func

#Defining plot params
fnt = 20
wht = 'bold'

#Creating folder for output csv files
if os.path.isdir('spdc_g2_csv_files') == True:
    pass#If folder already exists then do nothing to prevent os error
else:
     os.os.mkdir('spdc_g2_csv_files')

#Angular Dependence analysis

#Data collected in the quantum lab
X = [-1,-0.8,-0.6,-0.4,-0.2,0,0.2,0.4,0.6,0.8,1]#millimetres
x = 10*np.array(X)#centimetres
coincidence = [15,25,350,3000,5700,5800,4300,700,50,20,20]

#Uncomment the next lines if the file is to be loaded in via a .txt file
#x, coincidence = np.loadtxt('name of file', unpack = 'True', delimiter = 'delimiter in .txt file')

#xdata and inital params for scipy
xdata = np.linspace(x[0],x[-1], 1000)
amp = 5800
x0 = 0
sd = 0.03*(2*x[-1])

p = [amp,x0,sd]
popt, pcov  = spy.curve_fit(func.gaussian, x, coincidence, p)
ydata = func.gaussian(xdata,popt[0],popt[1],popt[2])

#matplotlib plot for angular dependence
fig = plt.figure(figsize = (10,8))
plt.plot(x,coincidence, 'o-', label = 'Data',color = 'black')
plt.plot(xdata,ydata, label = 'Gaussian Model', color = 'Red')
plt.xlabel(' Displacement [mm]', fontsize = fnt, fontweight = wht)
plt.ylabel('Coincidence Rate', fontsize = fnt, fontweight = wht)
plt.minorticks_on()
plt.ylim(0,7000)
plt.tick_params(labelsize = fnt)
plt.legend(fontsize = fnt)
plt.savefig('Angular_Dependence.png')
plt.show()

#Gaussian analysis printed to terminal
fwhm = func.FWHM(popt[2])
error = np.sqrt(pcov[2, 2]) / popt[2] * fwhm
print('*********************************************')
print('Angular dependence analysis:')
print('FWHM  =  %.1f +/- %.1f' % (fwhm, error))
print('Peak  =  %.f +/- %.f ' % ( popt[0], np.sqrt(pcov[0, 0])))
print('Peak Centre = %.1f +/- %.2f' % (popt[1], np.sqrt(pcov[1, 1])))
print('Sigma =  %.2f +/- %.2f ' % (popt[2], np.sqrt(pcov[2, 2])))

#Polarisation Dependence analysis (vars overwritten)

#Data collected in the quantum lab
polar = [-90,-80,-70,-60,-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90]
coincidence2 = [0,0,5,25,130,470,1160,2210,3200,3600,3400,2660,1624,699,239,48,4,0,0]

#Uncomment the next lines if the file is to be loaded in via a .txt file
#polar, coincidence2 = np.loadtxt('name of file', unpack = 'True', delimiter = 'delimiter in .txt file')

#xdata and inital params for scipy
xdata = np.linspace(polar[0],polar[-1], 1000)
amp = 3600
x0 = 0
sd = 0.03*(2*polar[-1])

p = [amp,x0,sd]
popt, pcov  = spy.curve_fit(func.gaussian, polar, coincidence2, p)
ydata = func.gaussian(xdata,popt[0],popt[1],popt[2])

#matplotlib plot for polarisation dependence
fig = plt.figure(figsize = (10,8))
plt.plot(polar,coincidence2, 'o-', label = 'Data',color = 'black')
plt.plot(xdata,ydata, label = 'Gaussian Model', color = 'Red')
plt.xlabel(r'$\Delta\Theta$ [$^\circ$]', fontsize = fnt, fontweight = wht)
plt.ylabel('Coincidence Rate', fontsize = fnt, fontweight = wht)
plt.minorticks_on()
plt.tick_params(labelsize = fnt)
plt.legend(fontsize = fnt)
plt.xlim(-90,90)
plt.ylim(0,4000)
plt.savefig('Polarisation_Dependence.png')
plt.show()

#Gaussian analysis printed to terminal
fwhm = func.FWHM(popt[2])
error = np.sqrt(pcov[2, 2]) / popt[2] * fwhm
print('*********************************************')
print('Polarisation dependence analysis:')
print('FWHM  =  %.2f +/- %.2f' % (fwhm, error))
print('Peak  =  %.f +/- %.f ' % ( popt[0], np.sqrt(pcov[0, 0])))
print('Peak Centre = %.1f +/- %.2f' % (popt[1], np.sqrt(pcov[1, 1])))
print('Sigma =  %.2f +/- %.2f ' % (popt[2], np.sqrt(pcov[2, 2])))

#Laser Emission Spectrum (vars overwritten)

#Loading data from .txt files
wavelength, intensity = np.loadtxt('Emission.txt', unpack = 'True')

#xdata and inital params for scipy
xdata = np.linspace(770,830, 1000)
amp = 150
x0 = 808
sd = 0.03*(2*wavelength[-1])

p = [amp,x0,sd]
popt, pcov  = spy.curve_fit(func.gaussian, wavelength, intensity, p)
ydata = func.gaussian(xdata,popt[0],popt[1],popt[2])

#matplotlib plot for laser
fig = plt.figure(figsize = (10,8))
plt.plot(wavelength,intensity,label = 'Data', color = 'black')
plt.plot(xdata,ydata, label = 'Gaussian Model', linewidth = 3, color = 'Red')
plt.xlabel('$\lambda$ [nm]', fontsize = fnt, fontweight = wht)
plt.ylabel('Intensity [a.u]', fontsize = fnt, fontweight = wht)
plt.minorticks_on()
plt.tick_params(labelsize = fnt)
plt.legend(fontsize = fnt)
plt.savefig('Emission.png')
plt.show()

#Gaussian analysis printed to terminal
fwhm= func.FWHM(popt[2])
error = np.sqrt(pcov[2, 2]) / popt[2] * fwhm
print('*********************************************')
print('Laser Emission analysis:')
print('FWHM  =  %.1f +/- %.2f' % (fwhm, error))
print('Peak  =  %.f +/- %.f ' % ( popt[0], np.sqrt(pcov[0, 0])))
print('Peak Centre = %.1f +/- %.2f' % (popt[1], np.sqrt(pcov[1, 1])))
print('Sigma =  %.2f +/- %.2f ' % (popt[2], np.sqrt(pcov[2, 2])))

#Histogram (vars overwritten)

#Loading data from .txt files
time_diffs, counts = np.loadtxt('Histogram.txt', unpack = 'True', delimiter = ';')
time_diffs_nm = time_diffs * 1e9

#xdata and inital params for scipy
xdata = np.linspace(0,4, 1000)
amp = 5000
x0 = 1.5
sd = 1

p = [amp,x0,sd]
popt, pcov  = spy.curve_fit(func.gaussian, time_diffs_nm, counts, p)
ydata = func.gaussian(xdata,1.45*popt[0],popt[1],popt[2])

#matplotlib plot for histogram
fig = plt.figure(figsize = (10,8))
plt.bar(time_diffs_nm,counts, width = 0.081 , edgecolor = 'black', label = 'Data',color = 'black')# alpha = 0.8 for opacity
#plt.plot(time_diffs_nm,counts, label = 'Raw Data (Midpoints)',color = '#5DFC0A')
plt.plot(xdata,ydata, label = 'Gaussian Model', linewidth = 4, color = 'Red')
plt.xlabel('Time Delay [ns]', fontsize = fnt, fontweight = wht)
plt.ylabel('Coincidences', fontsize = fnt, fontweight = wht)
plt.minorticks_on()
plt.tick_params(labelsize = fnt)
plt.legend(fontsize = fnt)
plt.savefig('Histogram.png')
plt.show()

#Gaussian analysis printed to terminal
fwhm= func.FWHM(popt[2])
error = np.sqrt(pcov[2, 2]) / popt[2] * fwhm
print('*********************************************')
print('Histogram analysis:')
print('FWHM  =  %.1f +/- %.1f' % (fwhm, error))
print('Peak  =  %.f +/- %.f ' % ( 1.45*popt[0], np.sqrt(pcov[0, 0])))
print('Peak Centre = %.1f +/- %.2f' % (popt[1], np.sqrt(pcov[1, 1])))
print('Sigma =  %.2f +/- %.2f ' % (popt[2], np.sqrt(pcov[2, 2])))

#g2 heralded and unheralded photons. Styled to mimic output.

#Loading data from .txt files
delay, g2 = np.loadtxt('Heralded.txt', unpack = 'True')
delay2, g2_2 = np.loadtxt('Unheralded.txt', unpack = 'True')

#matplotlib plot for heralded photon experiment
fig = plt.figure(figsize = (10,8))
#plt.style.use('dark_background')
plt.plot(delay,g2, 'o', label = 'Heralded', color = 'blue')
plt.plot(delay,g2, color = 'black', linewidth = 2)
plt.xlabel(r' $ \tau $ [ns]', fontsize = fnt, fontweight = wht)
plt.ylabel(r'$g^{2}(\tau)$', fontsize = fnt, fontweight = wht)
plt.minorticks_on()
plt.tick_params(labelsize = fnt)
plt.legend(fontsize = fnt)
plt.xlim(-20,20)
plt.ylim(-5,75)
plt.savefig('Heralded.png')
plt.show()

#matplotlib plot for unheralded photon experiment
fig = plt.figure(figsize = (10,8))
#plt.style.use('dark_background')
plt.plot(delay2,g2_2, 'o', label = 'Unhearlded', color = 'blue')
plt.plot(delay2,g2_2, color = 'black', linewidth = 2)
plt.xlabel(r' $ \tau $ [ns]', fontsize = fnt, fontweight = wht)
plt.ylabel(r'$g^{2}(\tau)$', fontsize = fnt, fontweight = wht)
plt.minorticks_on()
plt.tick_params(labelsize = fnt)
plt.legend(fontsize = fnt)
plt.savefig('Unheralded.png')
plt.show()

#Modelling the dip at time delay 0 for unheralded photons

Tot = zip(delay,g2)#Pairing function

#Lists to append into for data selection
g2_value = []
delay_value = []

#Select data close to Gaussian tails. Extreme value not wanted
for i,j in Tot:
    if -15 < i < 15:
        g2_value.append(j)
        delay_value.append(i)

#Gaussian fit to model g2 dip at 0 time delay
xdata = np.linspace(-15,15, 1000)
ydata = func.g2_func(xdata,1.1)

#matplotlib plot for heralded photon Gaussian fitting
fig = plt.figure(figsize = (10,8))
#plt.style.use('dark_background')
plt.plot(delay_value,g2_value, color = 'black', linewidth = 2)
plt.plot(delay,g2, 'o', label = 'Heralded', color = 'blue')
plt.plot(xdata, ydata, label = 'Gaussian Model', linewidth = 4, color = 'red')
plt.xlabel(r' $ \tau $ [ns]', fontsize = fnt, fontweight = wht)
plt.ylabel(r'$g^{2}(\tau)$', fontsize = fnt, fontweight = wht)
plt.minorticks_on()
plt.tick_params(labelsize = fnt)
plt.legend(fontsize = fnt)
plt.xlim(-10,10)
plt.ylim(-5,75)
plt.savefig('Heralded_fitting.png')
plt.show()

#Final g2 calculation for heralded and unheralded photons

print('*********************************************')
print('g2 calculation:')

Tot = zip(delay,g2)

g2_list = []

for i,j in Tot: 
    if -1 < i < -0.1:
        g2_list.append(j)

#g2 calculation
g2_0 = np.mean(g2_list)
err_g2 = np.std(g2_list)/np.sqrt(len(g2_list))#standard error
print('g2(0) = %.1f +/- %.1f' % (g2_0,err_g2))

tot = zip(delay2,g2_2)#Pairing function for unheralded data

g22 = []

for i,j in tot:
    if -10 < i < 30:
        g22.append(j)

#g2 calculation       
g222 = np.mean(g22)
err_g222 = np.std(g22)/np.sqrt(len(g22))#standard error
print('g2(t) = %f +/- %f' % (g222,err_g222))
