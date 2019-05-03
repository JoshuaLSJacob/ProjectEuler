a = 2^30
b = 30
while b<7830457:
    a = int(str(a*2)[-10:])
    b += 1

print(a)
