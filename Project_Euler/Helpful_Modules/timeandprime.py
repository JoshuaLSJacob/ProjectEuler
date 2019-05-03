#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 11:35:35 2018

@author: joshuajacob
"""

from prime_sieve_june import primes_a as pa
import timeit

def primes_a(n):
    import numpy
    x = numpy.ones(n, dtype = numpy.bool)
    i = 2
    x[0] = x[1] = False
    while i<int((n**0.5)+1):
        if x[i]:
            x[2*i::i] = False
        i += 1
    return([j for j in x*[k for k in range(n)] if j])

x = timeit.Timer('primes_a(100)', 'from __main__ import primes_a')

print(x.timeit())
