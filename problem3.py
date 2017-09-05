# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 17:52:15 2017

@author: Saloni.Kothari
"""
'''print(sorted([5,3,5,1,0,9]))
a=[3,0,1,7,4,8,9]
a.sort()
print(a)
def square(num):
    return num**3
print(square(2))
print(square(13))

print(abs.__doc__)
print(int.__doc__)
print(sorted.__doc__)'''

'''class American(object):
    @staticmethod
    def printNationality():
        print ("America")

anAmerican = American()
anAmerican.printNationality()
American.printNationality()'''

class American(object):
    pass

class NewYorker(American):
    pass

anAmerican = American()
aNewYorker = NewYorker()
print (anAmerican)
print (aNewYorker)