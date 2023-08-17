# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 11:01:06 2023

@author: vishal kurmi
"""

a = int(input("Enter first input"))
b = int(input("Enter second input"))
sum = 0
count = 0
for i in range(a, b):
    if i % 2 == 0:
        sum = sum +i
        count = count +1
print("total sum of even number is : ",sum)
print("total count of even numbers is :",count)
