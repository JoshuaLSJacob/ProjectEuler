#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 03:05:22 2017

@author: joshuajacob
"""

import numpy
def primes_list(n):
    x = numpy.ones(n, dtype = numpy.bool)
    for i in range(2,int(n**0.5)+1):
        if (i-1)%6 == 0 or (i+1)%6 == 0 or i == 2 or i == 3 and i<n+1:
            x[2*i-1::i] = False
    l = numpy.array(range(1,int(n)+1))
    return([k for k in x*l[:n] if k > 1])

num = 30
l = primes_list(num)
count = 0
buffer = numpy.ones(num**2,dtype = bool)

for number_1 in range(1,num + 1 ):
    if number_1%1000 ==0:
        print(number_1)
    for number_2 in range(int(number_1*1/3),int(number_1*1/2)+3):
        coprime = True
        prime = 0
        while l[prime] < number_1**0.5 + 1:
            if number_2%l[prime] == 0 and number_1%l[prime] ==0:
                coprime = False
                break
            prime += 1
        if coprime:
            if number_2/number_1<1/2 and number_2/number_1>1/3 :
                #print(number_1,number_2)
                print([number_2,number_1])
                count += 1
print(count)

