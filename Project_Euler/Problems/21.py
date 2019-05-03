def sum_of_divisors(number):
	x = 0
	for a in range(int(0.5+(number**0.5))):
		if (a+1)**2 == number or (a+1) ==1:
			x += (a+1)
		elif number%(a+1) == 0:
			x += (a+1)
			x += number/(a+1)
	return x

list_of_bits = []
for a in range(1,10001):
		list_of_bits.append([a,sum_of_divisors(a)])

amicable_numbers = []

for b in list_of_bits:
	if b[1] <10000:
		if b[0] == list_of_bits[b[1]-1][1]:
			if b[0] != b[1]:
				for c in b:
					if c not in amicable_numbers:
						amicable_numbers.append(c)

print(sum(amicable_numbers))