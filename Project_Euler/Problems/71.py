#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 00:32:30 2017

@author: joshuajacob
"""
'''import numpy
def primes_list(n):
    x = numpy.ones(n, dtype = numpy.bool)
    for i in range(2,int(n**0.5)+1):
        if (i-1)%6 == 0 or (i+1)%6 == 0 or i == 2 or i == 3 and i<n+1:
            x[2*i-1::i] = False
    l = numpy.array(range(1,int(n)+1))
    return([k for k in x*l[:n] if k > 1])


n = int(1000000/7)
x = primes_list(n)[-50::1]

denom = 100
numer = 50

for a in range(1,len(x)):
    if abs(x[a-1]/x[a] - 1) < abs((numer/denom) - 1):
        numer = x[a-1]
        denom = x[a]
print(numer*3,denom*7)'''

numer = 428361 
denom = 999523
for number_1 in range(999523,1000001):
    #print(int(number_1*numer/denom),int((number_1*3/7)+1))
    for number_2 in range(int(number_1*numer/denom),int(number_1*3/7)+1):
        if abs(number_2 / number_1 - (3/7)) < abs(numer/denom -(3/7)):
            numer = number_2
            denom = number_1
            print(numer,denom)
    
