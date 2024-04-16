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

# read_rainfall_to_dict(inputfile)

#inputfile = input('Please enter your filename: ')
inputfile = 'rainfall.tx'

# the correct inputfile is 'rainfall.txt'
# what if you give 'rainfall_nonexistent.txt'?

try:
    rainfalldict = read_rainfall_to_dict(inputfile)
except FileNotFoundError as fnferror:
    print('File does not exist')
except Exception as error:
    print(f'Your error is of type: {type(error)}')
    print(f'Error message: {error}')
else:
    print(rainfalldict)


# def rainfall_analysis(inputfile):
#     try:
#         rainfalldict = read_rainfall_to_dict(inputfile)
#     except FileNotFoundError as fnferror:
#             print(fnferror)
#             inputfile = input('Please give a file that exists: ')
#     else:
#         ....








