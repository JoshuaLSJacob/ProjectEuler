
def splat(a):
            return sum([int(x)**2 for x in str(a)])
length = 1000
x = [a for a in range(1,length)]

for a in range(1,length):
    b = a
    done = False
    while not done:
        if b == 89 or b == 1:
            x[a-1] = b
            done = True
        b = splat(b)

print(x.count(89))
'''
m = length

while m>length:
    m = splat(m)
x.append(x[m-1]'''
