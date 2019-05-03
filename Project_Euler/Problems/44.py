pents = []
for a in range(1,10000):
	pents.append(a*(3*a-1)*0.5)
minnie = [10000000000]
print 'go'
for x in pents:
	for b in pents:
		if b != x:
			if (float(1)/6)*(1+(24*(x+b)+1)**0.5) % 1 == 0:

				if (float(1)/6)*(1+(24*abs(x-b)+1)**0.5) % 1 == 0:
					print x,b
					if abs(x-b) < minnie[0]:
						minnie = [abs(x-b),x, b, x+b]
						print minnie
print minnie
print (1/6)*(1+(minnie[-1]+1)**0.5)%1

