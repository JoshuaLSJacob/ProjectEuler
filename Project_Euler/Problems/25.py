x = 1
x1 = 1
count = 2

while len(str(x)) < 1000:
	x = x + x1
	x1 = x - x1
	count += 1

print(count)	