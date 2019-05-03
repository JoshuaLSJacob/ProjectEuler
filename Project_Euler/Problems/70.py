#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 00:31:47 2017

@author: joshuajacob
"""

import numpy
def primes_list(n):
    x = numpy.ones(n, dtype = numpy.bool)
    for i in range(2,int(n**0.5)+1):
        if (i-1)%6 == 0 or (i+1)%6 == 0 or i == 2 or i == 3 and i<n+1:
            x[2*i-1::i] = False
    l = numpy.array(range(1,int(n)+1))
    return(x*l[:n])

x = [x for x in primes_list(30) if x>1]

'''print(x)
y = 0
z = range(10000)
count = 0
listy = [[] for a in x]
for num in range(len(x)):
    for a in range(1,int(1000/x[num])+1):
        count += 1
        if z[a] != 0:
            if z[a] % x[num] == 0:
                z[a] = 0
                listy[y].append(count)
                count = 0
    y+=1
print(listy)'''

bag = []
z = [a for a in range(1,1001)]
print(z)
print(x)
counter = -1
count = 0
for num in x:
    bag.append([num])
    for a in z:
        counter +=1
        count +=1
        if a != 0:
            
            if a%num == 0:
                bag.append(count)
                count = 0
                print(counter)
                z[counter]=0
    print(z)
    counter =-1
    count = 0
            
print(bag)
