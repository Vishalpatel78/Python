# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 12:49:30 2023

@author: vishal kurmi
"""

dis = {'vishal' : 8 , 'vivek' : 7 , 'shrey': 9}
avg = 0
sum = 0
l = len(dis)
for i in dis.values() :
    sum = sum + i
print("avg is :",sum/l)