# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 10:16:13 2023

@author: vishal kurmi
"""

p = "vishal"
b = " vishal "

if(p == b.rstrip()):
    print("string is same")
else:
   print("string is not same")
    
   
if(p == b.strip()):
    print("string is same")
else:
   print("string is not same")
    