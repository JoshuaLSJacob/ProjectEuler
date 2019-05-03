#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 13:24:41 2018

@author: joshuajacob
"""
import numpy

def frequency_checker(num):
    a = [0,0,0,0,0,0,0,0,0,0]
    for x in str(num)[:-1]:
        a[int(x)] += 1
    return(max(a))
    
    
def primes_list(n):
    x = numpy.ones(n, dtype = numpy.bool)
    i = 2
    x[0] = x[1] = False
    while i<n:
        if x[i]:
            x[2*i::i] = False
            
        i += 1
    l = numpy.array(range(int(n)+1))
    return([a for a in x*l[:n] if a and frequency_checker(a) > 2])

z = primes_list(10000000)


            


