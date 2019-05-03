#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 02:01:44 2017

@author: joshuajacob
"""
import math
listy = []
out_of_bounds = []
def is_square(n):
    if n<1:
        return False
    else:
        for i in range(int(n/2)+1):
            if (i*i)==n:
                return True
        return False

for D in range(2,1000):
    solution =False
    if is_square(D):
        continue
    else:
        x = int(D**0.5)-1
        if x < 2:
            x = 2
        while not solution:
            if ((x**2-1)/D)**0.5 % 1 == 0:
                solution = True
                listy.append([x,D])
            else:
                x += 1
                if x%1000000 == 0:
                    solution = True
                    x
                    out_of_bounds.append([x,D])
    if D%25 == 0:
        print(D)

print(sorted(listy))
print(out_of_bounds)
print(len(out_of_bounds))