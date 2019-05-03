def sum_of_divisors(number):
	x = 0
	for a in range(int(0.5+(number**0.5))):
		if (a+1)**2 == number or (a+1) ==1:
			x += (a+1)
		elif number%(a+1) == 0:
			x += (a+1)
			x += number/(a+1)
	return x

abundants = [a for a in range(1,28124) if a < sum_of_divisors(a)]
abundants2 = []
length = len(abundants)
print(length)
for a in range(length):
	for b in range(length):
		if abundants[a]+abundants[b] < 28124:
			abundants2.append(abundants[a]+abundants[b])



print('1')

abundants2 = sorted(list(set(abundants2)))
print(abundants2)

print('2')

print((28124*28123/2)-sum(abundants2))









