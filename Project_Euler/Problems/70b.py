#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 12:23:40 2017

@author: joshuajacob
"""

import numpy
def primes_list(n):
    x = numpy.ones(n)
    for i in range(2,int(n**0.5)+1):
        if (i-1)%6 == 0 or (i+1)%6 == 0 or i == 2 or i == 3 and i<n+1:
            x[2*i-1::i] += 1
    return(x)
    
m = []
z = primes_list(30)
for a in range(len(z)):
    m.append([a+1,z[a]])
print(m)

