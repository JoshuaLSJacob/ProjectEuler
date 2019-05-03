#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 12:39:43 2018

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
    return([j for j in x*[k for k in range(n)] if j])
    
primes_list_a(1000)



