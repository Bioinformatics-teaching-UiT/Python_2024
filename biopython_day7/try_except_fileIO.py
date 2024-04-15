#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 10:57:57 2023

File IO Exception handling using rainfall exercise:
    
    1. imports the reading function from rainfall module
    2. try to read in the rainfall data 
    3. catch the possible errors here - what is the type 
    the of main error?

@author: yin
"""
from average_rainfall import read_rainfall_to_dict

inputfile = input('Please enter your filename: ')

try:
    rainfall_dict = read_rainfall_to_dict(inputfile)
except Exception as err:
    print(type(err))
    print(err)

# read_rainfall_to_dict(inputfile)
# the correct inputfile is 'rainfall.txt'

# what if you give 'rainfall_nonexistent.txt'?











