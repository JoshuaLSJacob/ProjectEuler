from Sum_of_divisors import prime_divisors as div 
success = False
a = 1
while not success:
	if len(div(a)) == 4:
		count += 1
	else:
		count = 0
	if count == 4:
		print(a-3,a-2,a-1,a)
		exit()

	a += 1

