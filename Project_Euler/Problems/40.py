a = 0
b = ''
c = 0
product = 1
while a < 1000001:
	a+= 1
	for num in str(a):
		b += num
		if len(b) == 10**c:
			product *= int(b[-1])
			c += 1
			print b[-1]
print product
