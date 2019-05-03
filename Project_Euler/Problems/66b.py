import math 
D = 1
maxy = 1
while D < 100:
    success = False
    if float(D)**0.5 % 1 == 0.0:
        success = True
    x = 2
    while not success:
        if math.gcd(x,D) == 1 and ((float((x**2)-1))/D)**0.5 % 1 == 0.0:
            print (x,D)
            if x > maxy:
                maxy = x
            success = True
        else:
            print 
            x += 1
    D += 1
print(maxy)
'''983,
 991,
 997'''
 
 