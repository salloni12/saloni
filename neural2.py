# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 17:01:06 2017

@author: Saloni.Kothari
"""

import theano
import theano.tensor as T
from theano.ifelse import ifelse
import numpy as np

#Define variables:
x = T.vector('x')
w = T.vector('w')
b = T.scalar('b')

#w = theano.shared(np.array([1,1]))
#b = theano.shared(-1.5)

#Define mathematical expression:
z = T.dot(x,w)+b
a = ifelse(T.lt(z,0),0,1)

#neuron = theano.function([x],a)
neuron = theano.function([x,w,b],a)
#Define inputs and weights
inputs = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]
weights = [ 20, 20]
bias = -10
#Iterate through all inputs and find outputs:
'''for i in range(len(inputs)):
    t = inputs[i]
    out = neuron(t)
    print ('x1=%d and x2=%d  %d' % (t[0],t[1],out))'''
for i in range(len(inputs)):
    t = inputs[i]
    out = neuron(t,weights,bias)
    print (' x1=%d and x2=%d  %d' % (t[0],t[1],out))