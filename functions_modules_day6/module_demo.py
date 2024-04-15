#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 12:34:29 2024

Basic module to say hello and goodbye

@author: yin
"""

def sayhello(name):
    """Function that takes in a string and says hello"""
    print(f'Hello {name}!')


def saygoodbye(name):
    """Function that takes in a string and says goodbye"""
    print(f'Goodbye {name}!')
    
def sayhello_multiple(*name):
    for item in name:
        print(f'Hello {item}')

def print_message(*name, **messages):
    for item in name:
        for msgname, msg in messages.items():
            print(f'{msgname}: {msg} {item}!')
    

# if __name__ == '__main__': # if you are running this current script
#     sayhello('Yin')
    
    
