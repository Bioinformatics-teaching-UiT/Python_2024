#!/usr/bin/python

import pytest
from random import randint


def average(item_list):
    # if len(item_list) == 0:
    #    raise(ValueError, 'Passed list is empty')
    total = 0
    for element in item_list:
        total += element
    n_elements = len(item_list)
    return total / n_elements


def test_average_1():
    assert average([1, 1, 1]) == 1
    
    
def test_average_mixed():
    assert average([1, 2, 5, 7, 10]) == 5
 
    
def test_average_zero_division():
    pass
    with pytest.raises(ZeroDivisionError):
        average([])

# a = [randint(0,100) for x in range(1000)]
# print(average(a))
