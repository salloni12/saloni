# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 15:15:44 2017

@author: Saloni.Kothari
"""

'''def solve(numheads,numlegs):
    ns='No solutions!'
    for i in range(numheads+1):
        j=numheads-i
        if 2*i+4*j==numlegs:
            return i,j
    return ns,ns

numheads=35
numlegs=94
solutions=solve(numheads,numlegs)
print (solutions)'''
#reverse the string and number
'''s=input()
s=s[::-1]
print(s)'''
#permutation of numbers
'''import itertools
ls=[1,2,3]
print(list(itertools.permutations(ls)))'''
#solution 2

'''lst = [3, 3, 4]
import itertools
print(set(itertools.permutations(lst)))'''
#Please write a program which count and print the numbers of each character in a string input by console.
'''import collections
letters = collections.Counter(input())
print(letters)'''
'''dic = {}
s=input()
for s in s:
    dic[s] = dic.get(s,0)+1
print ('\n'.join(['%s,%s' % (k, v) for k, v in dic.items()]))'''
#remove duplicates
'''s=input()
print(set(s))'''
#shuffle
'''from random import shuffle
li = [3,6,7,8]
print(shuffle(li))'''
import zlib
s = 'hello world!hello world!hello world!hello world!'
t = zlib.compress(s)
print(t)
print (zlib.decompress(t))
