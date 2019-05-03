num = 100
def creator(num):           
    k=num-1   

    numerator = 1
    denominator = 1

    if (k+1) % 3 == 0:
        a = (k+1)*2/3      
    else:
        a = 1

    denominator = a   

    k -= 1    
    
    while k>0: 

        if (k+1) % 3 == 0:  
            a = (k+1)*2/3      
        else:
            a = 1   




        denominator, numerator = a*denominator+numerator,denominator

        k -= 1
        

    numerator += 2*denominator

    return(numerator)
x = 0
z = creator(num)
print(z)
print(str(z))
for a in str(int(z)):
    x += int(a)
    print(int(a))
print(x)
    
    

    




