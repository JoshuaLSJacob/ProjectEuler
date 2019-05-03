import numpy as np
a = [1.0,2.0,1.0]
x = 0
while len(a) < 101:
	a.append(0)
	b = a[::-1]
	a =(np.array(a)+np.array(b)).tolist()
	for c in a:
		if c > 1000000:
			x += 1
	print a
			#a[a.index(c)] =1000000
print x