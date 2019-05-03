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
    return([a for a in x*l[:n] if a and frequency_checker(a) > 2]) #is prime and has a repeated number of min 3 repeats

z = primes_list(1000000)

def five_digit(n,primes) :
    bands = [1110, 10110, 11010, 11100]
    for x in bands:
        count = 0
        for y in range(1,10):
            if y*x+n not in primes or len(str(y*x+n)) != len(str(n)):
                count+= 1
        if count < 3:
            success = True
            return(True)
    return(False)
    
def five_digit_end(n,primes) :
    bands = [1110, 10110, 11010, 11100]
    for x in bands:
        count = 0
        for y in range(1,10):
            if y*x+n not in primes or len(str(y*x+n)) != len(str(n)):
                count+= 1
        if count < 3:
            success = True
            return([a*x+n for a in range(1,10)])
    return(False)
    
    

def six_digit(n,primes):
    bands = [1110, 10110, 11010, 11100, 100110, 101010, 101100, 110010, 110100, 111000]
    for x in bands:
        count = 0
        for y in range(1,10):
            if y*x+n not in primes or len(str(y*x+n)) != len(str(n)):
                count+= 1
        if count < 3:
            success = True
            return(True)
    return(False)

def six_digit_end(n,primes):
    bands = [1110, 10110, 11010, 11100, 100110, 101010, 101100, 110010, 110100, 111000]
    for x in bands:
        count = 0
        for y in range(1,10):
            if y*x+n not in primes or len(str(y*x+n)) != len(str(n)):
                count+= 1
        if count < 3:
            success = True
            return([a*x+n for a in range(1,10)])
    return(False)
    
    
for x in z:
    if len(str(x)) == 5:
        if five_digit(x,z):
            print(x)
            print(five_digit_end(x,z))
    if len(str(x)) == 6:
        if six_digit(x,z):
            print(x)
            print(six_digit_end(x,z))

    


