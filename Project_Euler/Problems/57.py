d= 2
n = 1
z = 0
for x in range(1001):
	if len(str(d+n)) > len(str(d)):
		z += 1
	hanger = d
	d = n+2*d
	n = hanger
print z
