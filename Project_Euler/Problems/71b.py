#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 02:17:58 2017

@author: joshuajacob
"""
import numpy
def primes_list(n):
    x = numpy.ones(n, dtype = numpy.bool)
    for i in range(2,int(n**0.5)+1):
        if (i-1)%6 == 0 or (i+1)%6 == 0 or i == 2 or i == 3 and i<n+1:
            x[2*i-1::i] = False
    l = numpy.array(range(1,int(n)+1))
    return([k for k in x*l[:n] if k > 1])
    
l = primes_list(1000)
numer = 428361
denom = 999523
for number_1 in range(1,1000001):
    if number_1%10000 ==0:
        print(number_1)
    for number_2 in range(int(number_1*numer/denom)+1,int(number_1*3/7)+2):
        coprime = True
        for prime in l:
            if number_2%prime == 0 and number_1%prime ==0:
                coprime = False
        if coprime:
            if number_2/number_1<3/7:
                numer = number_2
                denom = number_1
print(numer,denom)