# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 15:10:29 2023

@author: vishal kurmi
"""

def add(farg,*args):
    print("formal arguments = ", farg)
    sum = 0
    for i in args:
        sum+=i
    print("sum of all arguments :", (farg+sum))
add(10,20)
add(10,20,30)