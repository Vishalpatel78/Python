# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 11:40:03 2023

@author: vishal kurmi
"""


y = [1,2,3,33,23332,444,4,5]
print(sorted(y))
del y[2]
print(y)

#y[2] = 11
#print(y)

x = (3,43,3,244,543,543,33,2544,654)
z = (343,3334,543,53,2,4,2,4)
print("reverse sorted order" ,sorted(x,reverse= True))


print(type(sorted(x)))

print(len(x))
print(min(x))

print(z.count(2))
print(x.index(3))

print(x*2)



