# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 14:28:25 2023

@author: vishal kurmi
"""

a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = a/b
try:
    print("division:",a/b)
    
except ValueError:
    print("value error")
