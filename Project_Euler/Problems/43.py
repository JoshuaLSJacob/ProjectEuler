from prime_checker import prime_checker as pc

def permute(num):	
	ay = False
	for a in num[-2::-1]:
		for b in num[:num.index(a):-1]:
			if b > a:
				k = a
				ay = True
				break
		if ay:
			break

	for a in num[:num.index(k):-1]:
		if a > k:
			l = a
			break
		elif a == b:
			print 'uhoh'
			exit()

	num[num.index(l)] = k
	num[num.index(k)] = l
	num[num.index(l)+1::1] = num[:num.index(l):-1]

	return num

primes = [x for x in range(1,20) if pc(x)]
num = [0,1,2,3,4,5,6,7,8,9]
x = 1
for z in num:
	x *= z+1
count = 0
for a in range(x-1):
	num = permute(num)
	success = True
	for b in range(1,8):
		if float(num[b]*100+num[1+b]*10+num[2+b]) % primes[b-1] != 0:
			success = False
			break

	if success:
		print int(''.join([str(x) for x in num]))
		count += int(''.join([str(x) for x in num]))

print count


