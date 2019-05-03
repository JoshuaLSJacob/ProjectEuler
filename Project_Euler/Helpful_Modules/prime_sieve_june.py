#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 12:39:43 2018

@author: joshuajacob
"""


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
    
def primes_b(n):
    import numpy
    x = numpy.ones(n, dtype = numpy.bool)
    i = 2
    x[0] = x[1] = False
    while i<int((n**0.5)+1):
        if x[i]:
            x[2*i::i] = False
        i += 1
    l = numpy.array(range(int(n)+1))
    return([a for a in x*l[:n] if a])

#is prime and has a repeated number of min 3 repeats

print(len(primes_b(1000)))

def primes_c(n):
    import numpy
    x = numpy.ones(n, dtype = numpy.bool)
    i = 2
    x[0] = x[1] = False
    while i<int((n**0.5)+1):
        if x[i]:
            x[2*i::i] = False
        i += 1
    l = numpy.array(range(int(n)+1))
    return([x*l[x] for a in x*l[:n] if a])

import timeit

print(timeit.timeit('primes_a(10)','from __main__ import primes_a', number = 1))
print(timeit.timeit('primes_b(10)','from __main__ import primes_b', number = 1))

