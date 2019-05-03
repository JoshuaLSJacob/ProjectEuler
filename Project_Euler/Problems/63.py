backer = []
for a in range(1,10000):
	matey = False
	x = 0
	while not matey:
		x += 1
		if x == len(str(a**x)):
			print a,x,a**x
			backer.append(a**x)

		if x ==1000:
			break
 
print len(set(backer))