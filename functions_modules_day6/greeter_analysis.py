#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 10:36:03 2024

Imports from greeter_module and runs greeter functions

@author: yin
"""
from greeter_module import greeter_names, greeter_names_messages

# from greeter_module import *

# greet some people
greeter_names('yin', 'ines')
greeter_names('yin', 'ines', msg = 'done with week 1')
greeter_names()

# greet some people with multiple messages
greeter_names_messages('yin', 'ines', msg1 = 'hello', msg2 = 'bye')