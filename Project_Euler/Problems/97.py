b = 1

a = 2**b

while b!=7830457:
    a = a*2
    if b % 5 == 0:
        a = int(str(a)[-10:])
    '''print(a,2**(b+1),b+1)'''
    b += 1
    
print(a,b)

print(str((28433*a)+1)[-10:])

