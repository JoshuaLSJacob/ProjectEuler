
def prime_checker(x): #where x is the number we want to check
	prime = True
	for a in range(2,int(0.5+x**0.5)):
		if x%a == 0:
			prime = False
			break
	return prime

z = ''
for a in range(101,151,2):
	for b in range(len(str(a))):
		print int(z.join([str(a)[x-b] for x in range(len(str(a)))]))

