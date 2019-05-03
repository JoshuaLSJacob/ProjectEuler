
count = 0
b = -1		#for c in options:
while b < 201:
	print b
	c = -1
	b += 1
	while c < 101:
		if b*1+c*2 > 200:
			break
		d = -1
		c += 1
		while d <41:
			if b*1+c*2+d*5 > 200:
				break
			e = -1
			d += 1
			while e <21:
				if b*1+c*2+d*5+e*10 > 200:
					break
				f = -1
				e += 1
				while f <11:
					if b*1+c*2+d*5+e*10+f*20 > 200:
						break
					g = -1
					f += 1
					while g <5:
						if b*1+c*2+d*5+e*10+f*20+g*50 > 200:
							break
						h = -1
						g += 1
						while h < 3:
							h += 1
							if b*1+c*2+d*5+e*10+f*20+g*50+h*100 == 200:
								count += 1
print count