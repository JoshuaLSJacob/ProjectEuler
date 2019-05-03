def sum_of_divisors(number):
	x = 0
	for a in range(int(0.5+(number**0.5))):
		if (a+1)**2 == number or (a+1) ==1:
			x += (a+1)
		elif number%(a+1) == 0:
			x += (a+1)
			x += number/(a+1)
	return x
abundants = []
for a in range(1,49):
	b = sum_of_divisors(a)
	
	if b>a:
		abundants.append(a)
		print(b,a)
print abundants
sums = []
for c in range(1,60):
	if c % 100 == 0 :
			print(c)
	for d in abundants:
		if d > c:
			print([c,'no'])
			break
		if c - d in abundants:
			sums.append(c)
			print([c,'yes'])
			break

'''
print(sums)
f = 0
for e in range(1,28124):
	if e not in sums:
		f+=e
		print e
print f'''