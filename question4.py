# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 14:54:02 2023

@author: vishal kurmi
"""

d = { "vishal" : 90, "shrey": 40, "vivek": 95}
print(d)
d["nitin"] = 85
print(d)
p = d.values()
print(p)
for i in p:
    if (i > 89):
        print(i)
        