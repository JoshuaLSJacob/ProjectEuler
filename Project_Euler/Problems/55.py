lychrel = 0
for a in range(1,10000):
	count = 0
	success = False
	b = a
	while success == False:
		b += int(str(b)[::-1])
		if b == int(str(b)[::-1]):
			break
			success = True 
		elif count < 51:
			count += 1
		else:
			lychrel +=1
			success = True
			if str(a)[::-1] == str(a):
				print a,b,count


print lychrel