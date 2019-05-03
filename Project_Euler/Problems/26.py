def remainder(r,a):
	return (10*r)%a
	
stop = False
max_cycle = [0,0]
for a in range(2, 1000):
	stop = False
	r = 1
	remainders = [0]
	while not stop:
		if remainder(r,a) not in remainders:
			remainders.append(remainder(r,a))
			r = remainder(r,a)
		else:
			if len(remainders) > max_cycle[0] and remainder(r,a) != 0:
				max_cycle = [len(remainders),a]
			stop = True
print max_cycle


