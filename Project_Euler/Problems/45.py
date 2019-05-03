count = 0
second = False
a = 143
while not second:
	b = a*(2*a-1)
	if ((float(1)/6)*(1+(24*b+1)**0.5))%1 == 0:
		print ((float(1)/6)*(1+(24*b+1)**0.5))
		if ((float(1)/2)*(1+(24*b+1)**0.5))%1 == 0:
			print ((float(1)/2)*(-1+(8*b+1)**0.5))
			count += 1
			if count == 2:
				print b
				exit()
	a+= 1
			

