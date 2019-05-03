import math
a = 3
while a<10000000:
	summer = 0
	for b in str(a):
		summer += math.factorial(int(b))
	if summer == a:
		print a
	a += 1
