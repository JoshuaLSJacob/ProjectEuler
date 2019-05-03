#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 16:26:06 2019

@author: joshuajacob
"""

import numpy

def factors_list(n):
    x = numpy.ones(n, dtype = numpy.int)
    i = 2
    while i<n:
        x[2*i-1::i] += 1
        i += 1
    return(x)
    
print(factors_list(10)-1)

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
    return([j for j in x*[k for k in range(n)] if j])
    