#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 01:15:54 2019

@author: joshuajacob
"""
import numpy
import math
def rotate(a,frame):
    a = sum([math.factorial(int(x))for x in str(a)])
    if a in frame:
        return(frame)
    else:
        frame.append(a)
        return(rotate(a,frame))

length = 1000000
count = 0
chains = 0

'''z = numpy.ones(length*10,dtype= numpy.bool)
while count < length:
    if z[count]:
        z[rotate(count,[count])] = False
        if len(rotate(count,[count])) == 60:
            chains += 1
    count += 1'''
    

while count < length:
    if len(rotate(count,[count])) == 60:
            chains += 1
    count += 1
print(chains)

 
