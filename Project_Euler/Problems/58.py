from prime_checker import prime_checker as pc
count1 = 1
count2 = 0 
n = float(0)
d = float(1)
x = 1
while  n > 0.4*d or n == 0:
	count2 +=1 
	for a in range(4):
		x = x+count2*2
		if pc(x):
			n += 1
			print x
		else:
			print x, 'NOPE'
		d += 1
print n/d, n, d, 1+count2*2 