#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 10:54:39 2024

Error handling

Throwing exception
Raising exception

@author: yin
"""

# function to divide two integers
# error is division by zero

def divide_two_nums(num1, num2):
    """Function to divide two numbers, can be int or float"""
    result = num1/num2
    return result

# catch a division by zero error
try:
    res = divide_two_nums(4,0)
except:
    print('You cannot divide by zero')

# catch specific errors
entry1 = 4
entry2 = 0
try:
    res = divide_two_nums(entry1, entry2)
except ZeroDivisionError:
    print('You cannot divide by zero')
except TypeError:
    print('You entered invalid or no input')

# catch all errors, output something meaningful
entry1 = 'b'
entry2 = 'a'
try:
    res = divide_two_nums(entry1, entry2)
except Exception as error:
    print(error)
    print(type(error))

# add else and finally clauses
entry1 = 1
entry2 = 0
try:
    res = divide_two_nums(entry1, entry2)
except Exception as error:
    print(error)
    print(type(error))
else:
    print('You are good at math!')
finally:
    print('Always do this.')












