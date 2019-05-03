product = [1,1]
for a in range(10,100):
	for b in range(10,100):
		if a >b:
			if a != b and not (a%10 ==0 and b%10 == 0):
				for c in str(a):
					if c in str(b):
						for d in str(a):
							for e in str(b):
								if d != c and e != c and d != str(0) and e != str(0):
									if float(d)/float(e) == float(a)/b:
										product[0] *= float(d)
										product[1] *= float(e)
print product