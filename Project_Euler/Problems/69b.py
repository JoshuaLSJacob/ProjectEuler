#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 02:33:09 2017

@author: joshuajacob
"""

def primes_list(n):
    x = numpy.ones(n, dtype = numpy.bool)
    for i in range(2,int(n**0.5)+1):
        if (i-1)%6 == 0 or (i+1)%6 == 0 or i == 2 or i == 3 and i<n+1:
            x[2*i-1::i] = False
    l = numpy.array(range(1,int(n)+1))
    return([z for z in x*l[:n] if z > 1])



def prime_factors(n,pl):
    a = 0
    p_fs = []
    
    while pl[a] < int(n**0.5)+1:
        if n in pl:
            p_fs.append(int(n))
            break
        if n%pl[a] == 0:
            p_fs.append(pl[a])
            n = n/pl[a]
            a = 0
        else:
            a += 1
    return(sorted(p_fs))
    
num = 1000000
pl = primes_list(num)
print(prime_factors(num,pl))
oops = []
for a in range(num):
    oops.append(prime_factors(a,pl))
    if a%100 == 0:
        print(a)


'''
if n%a == 0:
    x.append(a)
    n = a
    a = 1
'''
'''
z = 1
n = 0
l = []
x = primes_list(1000)
while z < 1000000:
    z *= x[n]
    l.append(x[n])
    n += 1

print(z/x[n-1])
print(l[:-1:])
print()
'''
