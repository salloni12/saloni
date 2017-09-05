# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 11:29:11 2017

@author: Saloni.Kothari
"""
import numpy as np
import inflect 
total=[]
sm=0
p=inflect.engine()
for i in range (1,1001):
    print(p.number_to_words(i))
    #print("count is",len(p.number_to_words(i)))
    total=np.sum(len(x) for x in p.number_to_words(i).replace('-',' ').replace(',',' ').split())
    print(total)
    sm+=total
print(sm)
    