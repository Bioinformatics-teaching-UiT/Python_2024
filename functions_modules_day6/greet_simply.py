#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 12:48:06 2024

Script that greets a user given the users name

Requires the module_demo module

@author: yin
"""

import module_demo 

module_demo.sayhello('Yin')

module_demo.saygoodbye('Yin')

import module_demo as md

md.sayhello('Yin')

md.saygoodbye('Yin')

from module_demo import *

sayhello('Bob')
saygoodbye('Bob')









