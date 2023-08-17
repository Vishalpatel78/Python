# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 13:31:44 2023

@author: vishal kurmi
"""
d = [1,22,43,4,23,54,3223,4,32,2]
even = 0
odd = 0
for i in d:
    if(i%2==0):
        odd = odd +1
    else:
        even = even +1

print(even)
print(odd)