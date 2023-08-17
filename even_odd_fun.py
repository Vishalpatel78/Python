# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 12:48:49 2023

@author: vishal kurmi
"""

def check(a):
    if a%2 == 0:
        return "even"
    else:
        return "odd"
        
a = int(input("enter a"))
check(a)