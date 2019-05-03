def prime_checker(x): #where x is the number we want to check
	prime = True
	for a in range(2,int(1+abs(x)**0.5)):
		if x%a == 0:
			prime = False
			break
	return prime

def divisors(number):
	x = []
	for a in range(0,int(1+(abs(number)**0.5))):
		if (a+1)**2 == number or (a+1) ==1:
			x.append(a+1)
		elif a+1 == 0:
			continue
		elif number%(a+1) == 0:
			x.append(a+1)
			x.append(number/(a+1))
	return sorted(x)

def quadratic_checker(a,b,lower_limit,upper_limit):
	max_count = [0,0]
	count = 0
	for x in range(lower_limit,upper_limit):
		if prime_checker(x**2+a*x+b):
			count  += 1
		else:
			if count > max_count[0]:
				max_count = [count,x]
			break
	return max_count

'''	a and b must both be odd
	they shouldn't share any factors, smaller than the largest run of primes found'''


upper_limit = 1000
lower_limit = 0

primes = []

'''for a in range(-10000,10000):
	if prime_checker(a):
		primes.append(a)
golden_duck = [0,0,0,0]
for a in primes:
	for b in primes:
		runner = quadratic_checker(a,b,lower_limit,upper_limit)
		if golden_duck[0] < runner[0]:
			golden_duck = [runner[0],runner[1],a,b]
		elif golden_duck == runner:
			print [runner[0],runner[1],a,b]
		else:
			continue
	print golden_duck,a '''


golden_duck = [0,0,0,0]


for a in range(-1000,1000):
	for b in range(-1000,1001):
		small_common_factor = False
		runner = quadratic_checker(a,b,lower_limit,upper_limit)
		if golden_duck[0] < runner[0]:
			golden_duck = [runner[0],runner[1],a,b]
		elif golden_duck == runner:
			print [runner[0],runner[1],a,b]
	print golden_duck,a
	


