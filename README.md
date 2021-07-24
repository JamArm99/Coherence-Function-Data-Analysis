
<img src="https://drive.google.com/uc?export=view&id=1QspeLL4wVjzzIGHuyYVMfy2-77yHECNT" width = "350" height="150">

# Coherence-Function-Data-Analysis 
This analysis aims to calculate various parameters about an SPDC crystal and the second-order coherence function g<sup>2</sup>(τ) for both heralded and unheralded photons. Crystal angle and polarisation dependence are inputted and modelled as Gaussian distributions to calculate the crystal width and SPDC type. In addition, g<sup>2</sup>(τ) is calculated by importing data from the coincidence counting units to observe the quantum nature of light. For more information on the theory and results, please see my third-year dissertation, which can be found [here](https://drive.google.com/file/d/15I74rcw3ZxaHnSUxd7CdCN3ogJRqTsIW/view?usp=sharing).

## Prerequisites 
Python modules utilised in this analysis:
- numpy
- os
- matplotlib
- scipy
- csv
- unittest

To install any missing modules excecute
```
$ python3 -m pip install missing-moduule-name
```
or
```
$ pip3 install missing-module-name
```
## Download
To download this analysis just clone this repository and then move to that directory to excecute.
```
$ git clone https://github.com/JamArm99/Coherence-Function-Data-Analysis.git
$ cd Coherence-Function-Data-Analysis
```

## Excecute
### Spdc_g2.py
This script conducts the primary analysis. It takes input from text files in the **_txt_input_files_** directory and uses this data to perform a series of calculations. Gaussian modelling is used for angle and polarisation dependence, laser emission spectra, and coincidence time window analysis. All the Gaussian parameters such as peak height, centre and width are computed along with their error. g<sup>2</sup>(τ) is determined for both heralded and unheralded experiments by averaging data around specific regions. 
```
$ python3 spdc_g2.py
```

### test_spdc_g2.py
This script is designed to run tests on the functions defined in **_func.py_**. The essential functions are the Gaussian and Full Width and Half-Maximum (FWHM) functions. Using unittest, these functions can be tested to ensure the desired result when called upon in the main script. The Gaussian function can be tested by ensuring it returns a normal distribution when passing data using the Shapiro-Wilk test. In addition, the correct errors are received when passing unphysical arguments into the function.
```
$ python3 -m unittest test_spdc_g2.py
```
or
```
$ python3 test_spdc_g2.py
```
## Outputs
Two folders are either created or overwritten when the primary analysis is executed. csv files are created for each of the Gaussian modelling sub-analyses and the g<sup>2</sup>(τ) analysis. In order to keep the working directory clear, these files are stored in the folder **_ spdc_g2_csv_files_**. Image files are also produced for each analysis and are stored in the folder **_ spdc_g2_png_files _**. 
