# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 15:10:05 2023

@author: vishal kurmi
"""

p = [4,3,6,32,7,3,5]
s1 = set(p)
q = [33,544,876,3,4,3]
s2 = set(q)

print("union is ",s1.union(s2))
print("intersection is ",s1.intersection(s2))
print("difference is :",s1.difference(s2))