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
			print('uhoh')
			exit()

	num[num.index(l)] = k
	num[num.index(k)] = l
	num[num.index(l)+1::1] = num[:num.index(l):-1]

	return num
print
