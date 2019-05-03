z = 0
for a in range(1,10000000):
	if sum([int(x)**5 for x in str(a)]) == a and a != 1:
		z += a
		print z

