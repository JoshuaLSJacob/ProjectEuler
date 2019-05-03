
m = False

a = 138902662
b = 101010103
count = False

while not m:
    if str(b**2)[::2] == '123456789':
        print b
        m = True
    b += 4+2*count
    count ^= True
