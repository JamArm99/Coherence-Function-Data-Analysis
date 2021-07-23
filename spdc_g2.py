#!/usr/bin/env python

#Importing python libraries
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.function_base import angle
import scipy.optimize as spy
import os
import csv

import func

#Uncomment the next two lines if the input .txt files are large.
#import sys
#sys.setrecursionlimit(N)

#Defining plot and file params
fnt = 20
wht = 'bold'
fieldnames = ['Parameter', 'Value', 'Error']

#Creating folder for output csv files
if os.path.isdir('spdc_g2_csv_files') == True:
    pass#If folder already exists then do nothing to prevent os error
else:
    print('Creating folder named spdc_g2_csv_files for data output')
    os.mkdir('spdc_g2_csv_files')

#Creating folder for ouput png files
if os.path.isdir('spdc_g2_png_files') == True:
    pass
else:
    print('Creating folder named spdc_g2_png_files for image output')
    os.mkdir('spdc_g2_png_files')

#Angular Dependence analysis

#Data collected in the quantum lab
x_cm = [-1,-0.8,-0.6,-0.4,-0.2,0,0.2,0.4,0.6,0.8,1]#cm
x_mm = 10*np.array(x_cm)#mm conversion
coincidence_angle = [15,25,350,3000,5700,5800,4300,700,50,20,20]

#Uncomment the next lines if the file is to be loaded in via a .txt file
#x, coincidence = np.loadtxt('name of file', unpack = 'True', delimiter = 'delimiter in .txt file')

#xdata and inital params for scipy
xdata_angle = np.linspace(x_mm[0],x_mm[-1], 1000)#xdata to pass through scipy function
amp_angle = 5800
x0_angle = 0
sd_angle = 0.03*(2*x_mm[-1])

p_angle = [amp_angle,x0_angle,sd_angle]#Initial guess list for scipy optimise
#Optimised parameters and covarience matrix for angluar dependence
popt_angle, pcov_angle  = spy.curve_fit(func.gaussian, x_mm, coincidence_angle, p_angle)

angle_dic = {}

#Gaussian parameters stored in dictionary
for i in range(0,3):
    if i == 0:
        angle_dic['Peak'] = popt_angle[i],np.sqrt(pcov_angle[i,i])#Optimised peak height and error
    elif i == 1:
        angle_dic['Centre'] = popt_angle[i], np.sqrt(pcov_angle[i,i])#Optimised peak centre and error
    else:
        angle_dic['Sigma'] = popt_angle[i],np.sqrt(pcov_angle[i,i])#Optimised sigma and error
        fwhm_angle = func.FWHM(popt_angle[i])
        angle_dic['FWHM'] = fwhm_angle,np.sqrt(pcov_angle[2,2])/popt_angle[2] * fwhm_angle #Optimsied FWHM and error

#Writing file to csv folder
with open('spdc_g2_csv_files/angle.csv', 'w') as file_angle:
    w = csv.writer(file_angle, delimiter = ',')
    w.writerow(fieldnames)
    for key in angle_dic:
        row = [key] + [angle_dic[key][0]] + [angle_dic[key][1]]
        w.writerow(row)

#Gaussian model data
ydata_angle = func.gaussian(xdata_angle,popt_angle[0],popt_angle[1],popt_angle[2])

#matplotlib plot for angular dependence
fig = plt.figure(figsize = (10,8))
plt.plot(x_mm,coincidence_angle, 'o-', label = 'Data',color = 'black')#Data plot
plt.plot(xdata_angle,ydata_angle, label = 'Gaussian Model', color = 'Red')#Gaussian Model
plt.xlabel(' Displacement [mm]', fontsize = fnt, fontweight = wht)
plt.ylabel('Coincidence Rate', fontsize = fnt, fontweight = wht)
plt.minorticks_on()
plt.ylim(0,7000)
plt.tick_params(labelsize = fnt)
plt.legend(fontsize = fnt)
plt.savefig('spdc_g2_png_files/Angular_Dependence.png')
plt.close()
#plt.show()

#Polarisation Dependence analysis

#Data collected in the quantum lab
polar = [-90,-80,-70,-60,-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90]#Degrees
coincidence_polar = [0,0,5,25,130,470,1160,2210,3200,3600,3400,2660,1624,699,239,48,4,0,0]

#Uncomment the next lines if the file is to be loaded in via a .txt file
#polar, coincidence2 = np.loadtxt('name of file', unpack = 'True', delimiter = 'delimiter in .txt file')

#xdata and inital params for scipy
xdata_polar = np.linspace(polar[0],polar[-1], 1000)
amp_polar = 3600
x0_polar = 0
sd_polar = 0.03*(2*polar[-1])

p_polar = [amp_polar,x0_polar,sd_polar]#Initial guess list for scipy optimise
popt_polar, pcov_polar  = spy.curve_fit(func.gaussian, polar, coincidence_polar, p_polar)

polar_dic = {}

#Gaussian parameters stored in dictionary
for i in range(0,3):
    if i == 0:
        polar_dic['Peak'] = popt_polar[i],np.sqrt(pcov_polar[i,i])#Optimised peak height and error
    elif i == 1:
        polar_dic['Centre'] = popt_polar[i], np.sqrt(pcov_polar[i,i])#Optimised peak centre and error
    else:
        polar_dic['Sigma'] = popt_polar[i],np.sqrt(pcov_polar[i,i])#Optimised sigma and error
        fwhm_polar = func.FWHM(popt_polar[i])
        polar_dic['FWHM'] = fwhm_polar,np.sqrt(pcov_polar[2,2])/popt_polar[2] * fwhm_polar #Optimsied FWHM and error

#Writing file to csv folder
with open('spdc_g2_csv_files/polar.csv', 'w') as file_polar:
    w = csv.writer(file_polar, delimiter = ',')
    w.writerow(fieldnames)
    for key in polar_dic:
        row = [key] + [polar_dic[key][0]] + [polar_dic[key][1]]
        w.writerow(row)

#Gaussian model data
ydata_polar = func.gaussian(xdata_polar,popt_polar[0],popt_polar[1],popt_polar[2])

#matplotlib plot for polarisation dependence
fig = plt.figure(figsize = (10,8))
plt.plot(polar,coincidence_polar, 'o-', label = 'Data',color = 'black')#Data
plt.plot(xdata_polar,ydata_polar, label = 'Gaussian Model', color = 'Red')#Gaussian Model
plt.xlabel(r'$\Delta\Theta$ [$^\circ$]', fontsize = fnt, fontweight = wht)
plt.ylabel('Coincidence Rate', fontsize = fnt, fontweight = wht)
plt.minorticks_on()
plt.tick_params(labelsize = fnt)
plt.legend(fontsize = fnt)
plt.xlim(-90,90)
plt.ylim(0,4000)
plt.savefig('spdc_g2_png_files/Polarisation_Dependence.png')
plt.close()
#plt.show()

#Laser Emission Spectrum

#Loading data from .txt files
wavelength, intensity = np.loadtxt('txt_input_files/Emission.txt', unpack = 'True')

#xdata and inital params for scipy
xdata_emission = np.linspace(770,830, 1000)
amp_emission = 150
x0_emission = 808
sd_emission = 0.03*(2*wavelength[-1])

p_emission = [amp_emission,x0_emission,sd_emission]
popt_emission, pcov_emission  = spy.curve_fit(func.gaussian, wavelength, intensity, p_emission)

emission_dic = {}

#Gaussian parameters stored in dictionary
for i in range(0,3):
    if i == 0:
        emission_dic['Peak'] = popt_emission[i],np.sqrt(pcov_emission[i,i])#Optimised peak height and error
    elif i == 1:
        emission_dic['Centre'] = popt_emission[i], np.sqrt(pcov_emission[i,i])#Optimised peak centre and error
    else:
        emission_dic['Sigma'] = popt_emission[i],np.sqrt(pcov_emission[i,i])#Optimised sigma and error
        fwhm_emission = func.FWHM(popt_emission[i])
        emission_dic['FWHM'] = fwhm_emission,np.sqrt(pcov_emission[2,2])/popt_emission[2] * fwhm_emission #Optimsied FWHM and error

#Writing file to csv folder
with open('spdc_g2_csv_files/emission.csv', 'w') as file_emission:
    w = csv.writer(file_emission, delimiter = ',')
    w.writerow(fieldnames)
    for key in angle_dic:
        row = [key] + [emission_dic[key][0]] + [emission_dic[key][1]]
        w.writerow(row)

#Gaussian model data
ydata_emission = func.gaussian(xdata_emission,popt_emission[0],popt_emission[1],popt_emission[2])

#matplotlib plot for laser
fig = plt.figure(figsize = (10,8))
plt.plot(wavelength,intensity,label = 'Data', color = 'black')
plt.plot(xdata_emission,ydata_emission, label = 'Gaussian Model', linewidth = 3, color = 'Red')
plt.xlabel('$\lambda$ [nm]', fontsize = fnt, fontweight = wht)
plt.ylabel('Intensity [a.u]', fontsize = fnt, fontweight = wht)
plt.minorticks_on()
plt.tick_params(labelsize = fnt)
plt.legend(fontsize = fnt)
plt.savefig('spdc_g2_png_files/Emission.png')
plt.close()
#plt.show()

#Histogram

#Loading data from .txt files
time_diffs, counts = np.loadtxt('txt_input_files/Histogram.txt', unpack = 'True', delimiter = ';')
time_diffs_nm = time_diffs * 1e9

#xdata and inital params for scipy
xdata_hist = np.linspace(0,4, 1000)
amp_hist = 5000
x0_hist = 1.5
sd_hist = 1

p_hist = [amp_hist,x0_hist,sd_hist]
popt_hist, pcov_hist  = spy.curve_fit(func.gaussian, time_diffs_nm, counts, p_hist)

hist_dic = {}

#Gaussian parameters stored in dictionary
for i in range(0,3):
    if i == 0:
        hist_dic['Peak'] = popt_hist[i],np.sqrt(pcov_hist[i,i])#Optimised peak height and error
    elif i == 1:
        hist_dic['Centre'] = popt_hist[i], np.sqrt(pcov_hist[i,i])#Optimised peak centre and error
    else:
        hist_dic['Sigma'] = popt_hist[i],np.sqrt(pcov_hist[i,i])#Optimised sigma and error
        fwhm_hist = func.FWHM(popt_hist[i])
        hist_dic['FWHM'] = fwhm_hist,np.sqrt(pcov_hist[2,2])/popt_hist[2] * fwhm_hist #Optimsied FWHM and error

#Writing file to csv folder
with open('spdc_g2_csv_files/hist.csv', 'w') as file_hist:
    w = csv.writer(file_hist, delimiter = ',')
    w.writerow(fieldnames)
    for key in hist_dic:
        row = [key] + [hist_dic[key][0]] + [hist_dic[key][1]]
        w.writerow(row)

#Gaussian model data
ydata_hist = func.gaussian(xdata_hist,1.45*popt_hist[0],popt_hist[1],popt_hist[2])

#matplotlib plot for histogram
fig = plt.figure(figsize = (10,8))
plt.bar(time_diffs_nm,counts, width = 0.081 , edgecolor = 'black', label = 'Data',color = 'black')# alpha = 0.8 for opacity
#plt.plot(time_diffs_nm,counts, label = 'Raw Data (Midpoints)',color = '#5DFC0A')#Plot the bin centers
plt.plot(xdata_hist,ydata_hist, label = 'Gaussian Model', linewidth = 4, color = 'Red')
plt.xlabel('Time Delay [ns]', fontsize = fnt, fontweight = wht)
plt.ylabel('Coincidences', fontsize = fnt, fontweight = wht)
plt.minorticks_on()
plt.tick_params(labelsize = fnt)
plt.legend(fontsize = fnt)
plt.savefig('spdc_g2_png_files/Histogram.png')
plt.close()
#plt.show()

#g2 heralded and unheralded photons. Styled to mimic output.

#Loading data from .txt files
delay_her, g2_her = np.loadtxt('txt_input_files/Heralded.txt', unpack = 'True')
delay_unher, g2_unher = np.loadtxt('txt_input_files/Unheralded.txt', unpack = 'True')

#matplotlib plot for heralded photon experiment
fig = plt.figure(figsize = (10,8))
#plt.style.use('dark_background')
plt.plot(delay_her,g2_her, 'o', label = 'Heralded', color = 'blue')#Data points
plt.plot(delay_her,g2_her, color = 'black', linewidth = 2)#Connect data with different colours
plt.xlabel(r' $ \tau $ [ns]', fontsize = fnt, fontweight = wht)
plt.ylabel(r'$g^{2}(\tau)$', fontsize = fnt, fontweight = wht)
plt.minorticks_on()
plt.tick_params(labelsize = fnt)
plt.legend(fontsize = fnt)
plt.xlim(-20,20)
plt.ylim(-5,75)
plt.savefig('spdc_g2_png_files/Heralded.png')
plt.close()
#plt.show()

#matplotlib plot for unheralded photon experiment
fig = plt.figure(figsize = (10,8))
#plt.style.use('dark_background')
plt.plot(delay_unher,g2_unher, 'o', label = 'Unhearlded', color = 'blue')
plt.plot(delay_unher,g2_unher, color = 'black', linewidth = 2)
plt.xlabel(r' $ \tau $ [ns]', fontsize = fnt, fontweight = wht)
plt.ylabel(r'$g^{2}(\tau)$', fontsize = fnt, fontweight = wht)
plt.minorticks_on()
plt.tick_params(labelsize = fnt)
plt.legend(fontsize = fnt)
plt.savefig('spdc_g2_png_files/Unheralded.png')
plt.close()
#plt.show()

#Modelling the dip at time delay 0 for heralded photons
Tot = zip(delay_her,g2_her)#Pairing function

#Lists to append into for data selection
g2_value = []
delay_value = []

#Select data close to Gaussian tails. Extreme value not wanted
for i,j in Tot:
    if -15 < i < 15:
        g2_value.append(j)
        delay_value.append(i)

#Gaussian fit to model g2 dip at 0 time delay
xdata_her = np.linspace(-15,15, 1000)
ydata_her = func.g2_func(xdata_her,1.1)

#matplotlib plot for heralded photon Gaussian fitting
fig = plt.figure(figsize = (10,8))
#plt.style.use('dark_background')
plt.plot(delay_value,g2_value, color = 'black', linewidth = 2)
plt.plot(delay_her,g2_her, 'o', label = 'Heralded', color = 'blue')
plt.plot(xdata_her, ydata_her, label = 'Gaussian Model', linewidth = 4, color = 'red')
plt.xlabel(r' $ \tau $ [ns]', fontsize = fnt, fontweight = wht)
plt.ylabel(r'$g^{2}(\tau)$', fontsize = fnt, fontweight = wht)
plt.minorticks_on()
plt.tick_params(labelsize = fnt)
plt.legend(fontsize = fnt)
plt.xlim(-10,10)
plt.ylim(-5,75)
plt.savefig('spdc_g2_png_files/Heralded_fitting.png')
plt.close()
#plt.show()

#Final g2 calculation for heralded and unheralded photons
Tot = zip(delay_her,g2_her)
g2_list = []

#Average value from the small number of events around the dip (possible due to asymptotic N regieme)
for i,j in Tot: 
    if -1 < i < -0.1:
        g2_list.append(j)

#g2 calculation
g2_0 = np.mean(g2_list)
err_g2 = np.std(g2_list)/np.sqrt(len(g2_list))#standard error

tot = zip(delay_unher,g2_unher)#Pairing function for unheralded data
g22 = []

#Average value of time delays between -10 and 30 (ignoring extreme values from graph)
for i,j in tot:
    if -10 < i < 30:
        g22.append(j)

#g2 calculation       
g222 = np.mean(g22)
err_g222 = np.std(g22)/np.sqrt(len(g22))#standard error

with open('spdc_g2_csv_files/g2.csv', 'w') as output:
    w = csv.writer(output, delimiter = ',')
    titles = ['Experiment Condition','Value','Error']
    heralded = ['Heralded',g2_0,err_g2]
    unheralded = ['Unheralded', g222,err_g222]
    w.writerow(titles)
    w.writerow(heralded)
    w.writerow(unheralded)
    
