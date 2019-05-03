from prime_checker import prime_checker as pc
success = False
a = 5
while not success:
	if not pc(a):
		sub_success = False
		for b in range(a):
			if pc(b):
				if (float(a-b)/2)**0.5 % 1 == 0:
					sub_success = True
					break
		if not sub_success:
			print a
			exit()
	a += 2
				
					

