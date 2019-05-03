from prime_checker import prime_checker as pc
primes = []
for a in range(1000,10000):
	if pc(a):
		primes.append(a)

for a in primes:
	count = 1
	for b in primes:
		if a < b:
			if sorted(str(a)) == sorted(str(b)):
				count += 1
				if count == 2:
					x2 = b
				if count == 3:
					if x2 -a == b - x2:
						print a-x2, b-x2
						print str(a)+str(x2)+str(b)
						exit()
		
