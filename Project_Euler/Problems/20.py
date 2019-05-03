number = 100
x = 1
y = 0
for a in range(number):
	x *= (a+1)

for a in str(x):
	y += int(a)

print(y)
