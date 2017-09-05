# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 17:56:45 2017

@author: Saloni.Kothari
"""


for a in range (50):
    for b in range(50):
        for c in range (50):
            if a*b*c==50:
                print("a is %s b is %s c is %s  " % (a,b,c))
                break
a+=1
b+=1
c+=1
            
            