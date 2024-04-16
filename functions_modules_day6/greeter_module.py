#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 10:22:27 2024

Module containing two functions to greet a user

1. take arbitrary number of names, print out a message

2. take arbitrary number of names and messages, print these out


def somefunc(*args, **kwargs):
    ...

@author: yin
"""

def greeter_names(*names, msg = 'Welcome to week 2!'):
    """
    Function that takes in as many names as you choose,
    prints out a message per name
    
    :param *names: tuple of strings, each string is a name
    :param msg: default string, message to print
    
    :return None:
    """
    for name in names:
        print(msg, name)
    

def greeter_names_messages(*names, **messages):
    """
    Function that takes in as many names and messages
    as you choose, prints out each message per name
    
    :param *names: tuple of strings, each string is a name
    :param **messages: dict of str, each string is a message
    
    :return None:
    """
    for name in names:
        for msglabel, msg in messages.items():
            print(f'{msglabel}: {msg} {name}')

if __name__ == '__main__':
    greeter_names('Harry', 'Hermione')
    greeter_names_messages('Harry', 'Hermione', msg = 'Hogwarts students')











