#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 01:40:24 2019

@author: joshuajacob
"""

import numpy
import timeit
def primes_list_a(n):
    x = numpy.ones(n, dtype = numpy.bool)
    i = 2
    x[0] = x[1] = False
    while i<int((n**0.5)+1):
        if x[i]:
            x[2*i::i] = False
        i += 1
    return(x)

def denom_a(n,primes):
    x = numpy.array(range(n))
    x = numpy.array([float(a) for a in x])
    i = 2
    x[0] = 0
    x[1] = 0
    while i<n:
        if primes[i]:
            x[i::i] *= (i-1)/i
        i += 1
    return(x)

maxy = 1000000 
print(sum(denom_a(maxy+1,primes_list_a(maxy+1))))
