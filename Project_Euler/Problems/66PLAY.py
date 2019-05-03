import math 
from decimal import *



maxy = [0,1]


def p_f(y):
    prime = False
    factors = []
    while not prime:
            a = 1
            for a in range(2,y+1):
                if y%a == 0:
                    break
            if y/a == 1:
                prime = True
                factors.append(a)
            else:
                factors.append(a)
                y = int(y/a)

    return(factors)
    
    
'''success = False
x = 2
while not success:
    y = ((float((x**2)-1))/D)**0.5
    if math.gcd(x,D) == 1 and ((float((x**2)-1))/D)**0.5 % 1 == 0.0:
        print(D,p_f(D))
        print(y,p_f(int(y)))
        print(x,p_f(int(x)))
        if x > 1000000:
            success = True
    x += 1'''


D=1
while D < 62:
    success = False
    if math.sqrt(float(D)) % 1 == 0.0:
        success = True
    adder = 1
    
    if D%2 == 0:
            if D%8 != 0:
                adder = 2     
    
    y = adder
    
    while not success:
        if ((Decimal(y)**Decimal(2))*Decimal(D)+Decimal(1))**Decimal(0.5) % Decimal(1) == Decimal(0.0):
            if ((Decimal(y)**Decimal(2))*Decimal(D)+Decimal(1))**Decimal(0.5) > maxy[1]:
                maxy = [D, ((Decimal(y)**Decimal(2))*Decimal(D)+Decimal(1))**Decimal(0.5)]
                print('maxy:')
            print('D',D,p_f(D))
            print('y',y,p_f(int(y)))
            print('x',((Decimal(y)**Decimal(2))*Decimal(D)+Decimal(1))**Decimal(0.5),p_f(int(math.sqrt(Decimal(float((y**2)*D)+1)))))
            success = True
        
        y += adder
    D += 1
    
'''y 42912791 [42912791]
x 335159612.0 [2, 2, 29, 101, 28607]'''