# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 16:28:25 2017

@author: Saloni.Kothari
"""

def is_prime(num):
    for i in range(2,num):
        if num%i == 0:
            return False
    return True


primes = []
for num in range(2,2000000):
    if is_prime(num):
        primes.append(num) 
        total=sum(num for num in primes)
     
print(total)