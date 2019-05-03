from prime_checker import prime_checker as pc


def recurrsive_lr_pc(x):
	prime = True
	if x > 0:
		if pc(x):
			prime = recurrsive_lr_pc(x-int(str(x)[0])*10**(len(str(x))-1))
		else:
			prime = False
	return prime

def recurrsive_rl_pc(x):
	prime = True
	if x > 0:
		if pc(x):
			prime = recurrsive_rl_pc((x-int(str(x)[-1]))/10)
		else:
			prime = False
	return prime


count = 0
for num in range(10,10000000):
	if recurrsive_lr_pc(num):
		if recurrsive_rl_pc(num):
			print num
			count += num
			print count


