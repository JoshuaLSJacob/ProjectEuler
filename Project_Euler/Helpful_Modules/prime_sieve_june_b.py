#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 12:39:43 2018

@author: joshuajacob
"""
import numpy
import timeit

    
def primes_list_b(n):
    x = numpy.ones(n, dtype = numpy.bool)
    i = 2
    x[0] = x[1] = False
    while i<int((n**0.5)+1):
        if x[i]:
            x[2*i::i] = False
        i += 1
    l = numpy.array(range(int(n)+1))
    return([a for a in x*l[:n] if a]) #is prime and has a repeated number of min 3 repeats
  

primes_list_b(1000)

