
setty = sorted([str(x) for x in range(1,10)])
summer = []

print 987654321**0.25
for a in range(2,10000):
 	for b in range(2,100):
 		if len(str(a*b))+len(str(a))+len(str(b)) == 9:
			if sorted(set(str(a)+str(b)+str(a*b))) == setty:
 				if a*b not in summer:
 					summer.append(a*b)
					print a,b,a*b
print sum(summer)
