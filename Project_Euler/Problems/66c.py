#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 00:00:16 2019

@author: joshuajacob
"""

import numpy
D = 1
maxy = 1
while D < 100:
    print(D)
    success = False
    if float(D)**0.5 % 1 == 0.0:
        success = True
    y = 2
    while not success:
        x = (float((y**2))*D+1)**0.5
        if x % 1 == 0.0:
            print(x%y,y,x,D)
            if x > maxy:
                maxy = x
            success = True
        else:
            y += 1
    D += 1
    
print(maxy)
''' 947,
 953,
 967,
 971,
 977,
 983,
 991,
 997'''