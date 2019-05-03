#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 12:58:24 2019

@author: joshuajacob
"""
import numpy
x = numpy.zeros(1500001, dtype = numpy.bool)
y = []
c= 1
n= 1
while c < 1500000:
    n = 2-c%2
    while n < c:
        if (c**2 - n**2) % (2*n) == 0:
            if int((2*(c**2 - n**2) / (2*n)) + c + n) < 1500001:
                if x[int((2*(c**2 - n**2) / (2*n)) + c + n)]:
                    y.append(2*((c**2 - n**2) / (2*n)) + c + n)
                else:
                    x[int((2*(c**2 - n**2) / (2*n)) + c + n)::int((2*(c**2 - n**2) / (2*n)) + c + n)] = True
        n += 2
    c += 1

