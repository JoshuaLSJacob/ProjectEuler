import timeit
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

def prime_list_maker_1(upper):
    prime_list = []
    x = 2
    while x <= upper:
        prime = True
        if x == 1 or x==0:
                prime = False
        for a in prime_list:
            if a < int(0.5+x**0.5)+1:
                if x%a == 0 and x != a:
                    prime = False
                    break
        if prime:
            prime_list.append(x)
        x += 1
        
    return prime_list

def prime_list_maker_2(upper):
    prime_list = []
    x = 2
    while x <= upper:
        prime = True
        if x == 1 or x==0:
            prime = False
        for a in range(2,int(0.5+x**0.5)+1):
            if x%a == 0 and x != a:
                    prime = False
                    break
        if prime:
            prime_list.append(x)
        x += 1
    return prime_list

x = (prime_list_maker_2(1000000))



