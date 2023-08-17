# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 13:09:43 2023

@author: vishal kurmi
"""
x = int(input("enter"))
try:
    assert x>0,"wrong no,entered"
    print("Entered no is ",x)
except AssertionError:
    print("wrong no entered")