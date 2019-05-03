#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 15:13:56 2019

@author: joshuajacob
"""
import math
def continued_fraction(D,A = 0, B = 1, n = 0, choices = [0,1,1,0]):
    a_0 = math.floor(D**0.5)
    a = math.floor((a_0+A)/B)
    A = a*B-A
    B = (D - A**2)/B
    n += 1
    choices = [choices[2],choices[3],a*choices[2]+choices[0],a*choices[3]+choices[1]]
    #print(a,choices[2],choices[3])
    return(D,A,B,n,choices)
    
    
#x = continued_fraction(7)
x = 0
'''for a in range(10):
    x =continued_fraction(x[0],x[1],x[2],x[3],x[4])'''
maxy = [0,0]  
for D in range(1,1000):
    if D**0.5 != math.floor(D**0.5):
        x = continued_fraction(D)
        success = False
        while not success:
            x = continued_fraction(x[0],x[1],x[2],x[3],x[4])
            if (x[4][2]**2)-1 == (x[4][3]**2)*D:
                print(x[3])
                if x[4][2] > maxy[0]:
                    maxy = [x[4][2],D]
                success = True

print(maxy[1])