
def prime_checker(x): #where x is the number we want to check
	prime = True
	for a in range(2,int(0.5+x**0.5)):
		if x%a == 0:
			prime = False
			break
	return prime

z = ''
count = 0
for a in range(2,1000000,2):
	prime = True
	for b in range(len(str(a))):
		if not prime_checker(int(z.join([str(a)[x-b] for x in range(len(str(a)))]))):
			prime = False
	if prime:
		count += 1
		print count