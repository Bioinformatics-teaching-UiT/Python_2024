# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 19:24:33 2024

@author: andre

Replace within string: Take in a string with words separated by commas and replace the commas
with spaces, then print out the resulting string.

"""
# Define string with words seperated by commas
comma_str = "Hi,it,is,nice,to,see,you!"

# Replace commas with spaces
spaces_str = comma_str.replace(',', ' ')

# Print new string
print(f"Here is the new string: {spaces_str}")

# Count how many commas are in string
ncommas = comma_str.count(',')

# Print comma count
print(ncommas, 'commas were replaced with spaces')