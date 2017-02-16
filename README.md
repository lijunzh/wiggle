# Wiggle Plot for Seismic Data Section

[![Build Status](https://travis-ci.org/gatechzhu/wiggle.svg?branch=master)](https://travis-ci.org/gatechzhu/wiggle)

## Introduction
The [wiggle](http://wiki.aapg.org/Seismic_data_display) display is an ingenious methodology that displays two dimensional scalar fields on a horizontal plane. 
Originally developed by the geophysical community, the wiggle plot was created to provide a visual analysis of seismic and seismological data, or any other vibration data, in order to help the identification of events that can be stressed out with the coherent alignment of lobes. 
Ultimately those events can be related to geological features and/or can help the determination of the some physical properties of rocks, such as the velocity of P and S waves. 
Before digital displays were standard in the industry the wiggle plot was composed either by oscillatory continuous lines and black filled lobes, both drawn by special plotters on long paper sheets. 
Nowadays, when digital graphical displays are easily available, both elements, the lines and the lobes, are merged into a new one display called wiggle.

Inspired by [wiggle in Matlab](https://www.mathworks.com/matlabcentral/fileexchange/38691-wiggle) function, I created this Python tools to mimic the experience of plotting seismic section data in [Matlab](https://www.mathworks.com/products/matlab.html) with similar user interface. 
Basically one can control the color and direction of the lines, the color of the left and right lobes, among others. 
In order to control these features, a controlling string must be provided as input, in a similar way the function PLOT allows control of the graphical elements. 

Given a d M x N ndarray data matrix D, wiggle decompose it into multiple 
traces. 
Under vertical mode (default), each columns is a seismic trace of size M and 
there are N number of traces. 
When horizontal mode is activated, each row is considered a trace of size N 
and there are M number of traces.


## Dependancy
- [NumPy](http://www.numpy.org/)
- [Matplotlib](http://matplotlib.org/)

## Installation
### From PyPI
```
pip install wiggle
```

### From source file
Download srouce file from [releases page](https://github.com/gatechzhu/wiggle/releases). Under the root directory, type:

```
python setup.py install
```

## Contact

In counter of any trouble, contact *gatechzhu@gmail.com*
