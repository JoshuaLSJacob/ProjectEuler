# -*- coding: utf-8 -*-
import numpy
def primes_list(n):
    import numpy
    x = numpy.ones(n, dtype = numpy.bool)
    i = 2
    x[0] = x[1] = False
    while i<int((n**0.5)+1):
        if x[i]:
            x[2*i::i] = False
        i += 1
    return([j for j in x*[k for k in range(n)] if j])

def primes_a(n):
    import numpy
    x = numpy.ones(n, dtype = numpy.bool)
    i = 2
    x[0] = x[1] = False
    while i<int((n**0.5)+1):
        if x[i]:
            x[2*i::i] = False
        i += 1
    return(x)
    
def prime_checker(x): #where x is the number we want to check
    prime = True
    if x == 1 or x==0:
            prime = False
    a = 2
    while a < 1+(x**0.5):
        if x%a == 0 and x != a:
            prime = False
            a = x
    return prime

n = 10000

primes = primes_list(n)
'''primes_big = primes_a(int(str(n)+str(n)))'''

matrix = numpy.zeros((len(primes),len(primes)), dtype = numpy.bool)

counter_1 = 0

while counter_1 < len(primes):
    counter_2 = 0
    while counter_2 < len(primes):
        if  primes_big[int(str(primes[counter_1])+str(primes[counter_2]))]:
            matrix[counter_1][counter_2] = True
        counter_2 += 1
    counter_1 += 1

matrix = numpy.transpose(matrix)*matrix

counter = 0

while counter < len(matrix):
    if sum(matrix[counter]) < 4:
        matrix[counter] = False
        
    counter += 1

matrix = numpy.transpose(matrix)
counter = 0

while counter < len(matrix):
    if sum(matrix[counter]) < 4:
        matrix[counter] = False
        
    counter += 1




primes = [x for x in numpy.array([any(x) for x in matrix])*primes if x]
matrix = numpy.array([x for x in matrix if any(x)])
matrix = numpy.transpose(matrix)
matrix = numpy.array([x for x in matrix if any(x)])
matrix_2 = numpy.dot(1*matrix,1*matrix)

print(len(primes))


counter_1 = 0
counter_2 = 0
while counter_1 < len(primes):
    counter_2 = counter_1
    while counter_2 < len(primes):
        if matrix_2[counter_1][counter_2] < 3:
            if matrix[counter_1][counter_2] == True:
                matrix[counter_1][counter_2] = False
                if counter_1 == 0 and counter_2 == 1:
                    print('yes')
        counter_2 += 1
    counter_1 += 1

matrix = numpy.transpose(matrix)*matrix
primes = [x for x in numpy.array([any(x) for x in matrix])*primes if x]
matrix = numpy.array([x for x in matrix if any(x)])
matrix = numpy.transpose(matrix)
matrix = numpy.array([x for x in matrix if any(x)])

counter = 0

while counter < len(matrix):
    if sum(matrix[counter]) < 4:
        matrix[counter] = False
        
    counter += 1

matrix = numpy.transpose(matrix)
counter = 0

while counter < len(matrix):
    if sum(matrix[counter]) < 4:
        matrix[counter] = False
        
    counter += 1

matrix = numpy.transpose(matrix)*matrix
primes = [x for x in numpy.array([any(x) for x in matrix])*primes if x]
matrix = numpy.array([x for x in matrix if any(x)])
matrix = numpy.transpose(matrix)
matrix = numpy.array([x for x in matrix if any(x)])
matrix_2 = numpy.dot(1*matrix,1*matrix)

print(len(primes))


counter_1 = 0
counter_2 = 0
while counter_1 < len(primes):
    counter_2 = counter_1
    while counter_2 < len(primes):
        if matrix_2[counter_1][counter_2] < 3:
            if matrix[counter_1][counter_2] == True:
                matrix[counter_1][counter_2] = False
                if counter_1 == 0 and counter_2 == 1:
                    print('yes')
        counter_2 += 1
    counter_1 += 1

matrix = numpy.transpose(matrix)*matrix
primes = [x for x in numpy.array([any(x) for x in matrix])*primes if x]
matrix = numpy.array([x for x in matrix if any(x)])
matrix = numpy.transpose(matrix)
matrix = numpy.array([x for x in matrix if any(x)])

counter = 0

while counter < len(matrix):
    if sum(matrix[counter]) < 4:
        matrix[counter] = False
        
    counter += 1

matrix = numpy.transpose(matrix)
counter = 0

while counter < len(matrix):
    if sum(matrix[counter]) < 4:
        matrix[counter] = False
        
    counter += 1

matrix = numpy.transpose(matrix)*matrix
primes = [x for x in numpy.array([any(x) for x in matrix])*primes if x]
matrix = numpy.array([x for x in matrix if any(x)])
matrix = numpy.transpose(matrix)
matrix = numpy.array([x for x in matrix if any(x)])
matrix_2 = numpy.dot(1*matrix,1*matrix)

print(len(primes))


counter_1 = 0
counter_2 = 0
while counter_1 < len(primes):
    counter_2 = counter_1
    while counter_2 < len(primes):
        if matrix_2[counter_1][counter_2] < 3:
            if matrix[counter_1][counter_2] == True:
                matrix[counter_1][counter_2] = False
                if counter_1 == 0 and counter_2 == 1:
                    print('yes')
        counter_2 += 1
    counter_1 += 1

matrix = numpy.transpose(matrix)*matrix
primes = [x for x in numpy.array([any(x) for x in matrix])*primes if x]
matrix = numpy.array([x for x in matrix if any(x)])
matrix = numpy.transpose(matrix)
matrix = numpy.array([x for x in matrix if any(x)])

counter = 0

while counter < len(matrix):
    if sum(matrix[counter]) < 4:
        matrix[counter] = False
        
    counter += 1

matrix = numpy.transpose(matrix)
counter = 0

while counter < len(matrix):
    if sum(matrix[counter]) < 4:
        matrix[counter] = False
        
    counter += 1

matrix = numpy.transpose(matrix)*matrix
primes = [x for x in numpy.array([any(x) for x in matrix])*primes if x]
matrix = numpy.array([x for x in matrix if any(x)])
matrix = numpy.transpose(matrix)
matrix = numpy.array([x for x in matrix if any(x)])
matrix_2 = numpy.dot(1*matrix,1*matrix)

print(primes)
print(matrix)




            

