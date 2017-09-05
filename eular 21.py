# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 16:36:35 2017

@author: Saloni.Kothari
"""

value=1184
import numpy as np
def get_divisors(num):
    divisors = []
    for i in range(1,num):
        if num % i == 0:
            divisors.append(i)
   # divisors.append(num)
    return divisors
divisors = get_divisors(value)
print(divisors)
total=np.sum(divisors)
print(total)
againdiv=get_divisors(total)
print(againdiv)
total1=np.sum(againdiv)
print(total1)

if value == total1:
    print("amicable")
else:
    print("not amicable")
'''for i in range(1,10000):
    sum=sum+i
    print(sum," :",end='')
    divisors=get_divisors(sum)
    #print(divisors,"\t",end='')
   # if len(divisors)<500:
       # break
    #print(sum)'''
    

def sum_divisors(n):
    s = 0
    for i in range(1,n):
        if n % i == 0: s += i
    return s
 
def amicable_pairs_xrange(low,high):
    L = [sum_divisors(i) for i in range(low,high + 1)]
    pairs = []
    for i in range(high - low + 1):
        ind = L[i]
        if i + low < ind and low <= ind and ind <= high and L[ind - low] == i + low:
            pairs.append([i+low,ind])
    return pairs
 
def sum_pairs(pairs):
    return sum([sum(pair) for pair in pairs])
 

 
ans = sum_pairs(amicable_pairs_xrange(1,10000))
 

print(ans)
