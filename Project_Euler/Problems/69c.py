#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 14:29:22 2017

@author: joshuajacob
"""
import numpy


def primes_list(n):
    x = numpy.ones(n, dtype = numpy.bool)
    for i in range(2,int(n**0.5)+1):
        if (i-1)%6 == 0 or (i+1)%6 == 0 or i == 2 or i == 3 and i<n+1:
            x[2*i-1::i] = False
    l = numpy.array(range(1,int(n)+1))
    return([z for z in x*l[:n] if z > 1])
    
def prime_factor_list(n):
    x = [[] for x in range(n)]
    a = 2
    for i in range(1,n):
        if i != 1:
            while a*i < n:
                x[a*i-1].append(i)
                a += 1
            a = 2
    return(x)

num = 1000
    
z = prime_factor_list(num)
print(z)

y = [len(x) for x in z]
u = []
m = 0
while m  < num:
    u.append([m+1,y[m]])
    m += 1
print(u)
print(u[:][:][0])
