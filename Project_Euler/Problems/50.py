from prime_checker import prime_checker as pc
summer = []
maxy = [0,0,0]
for a in range(1,2000):
	sub_max = [0,0,0]
	summer = []
	while sum(summer)<1000000:
		if pc(a):
			summer.append(a)
			if pc(sum(summer)):
				sub_max = [sum(summer),summer[-1], len(summer)]
		a += 1
	if sub_max[2] > maxy[2]:
		maxy = sub_max
		print maxy
	elif sub_max[2] < 500:
		exit()
