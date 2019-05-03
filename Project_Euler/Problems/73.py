#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 17:57:41 2019

@author: joshuajacob
"""

def co_prime(a,b):
    if b == 0:
        return(False)
    elif b == 1:
        return(True)
    else:
        return(co_prime(b, a%b))

a = 100
b = 670
if co_prime(a,b):
    print('yes')
elif not co_prime(a,b):
    print('no')

counter = 0
for a in range(1,6001):
    for b in range(2*a+1,3*a):
        if co_prime(a,b):
            if b < 12001:
                counter += 1

print(counter)
#shit brute force code - sorry

