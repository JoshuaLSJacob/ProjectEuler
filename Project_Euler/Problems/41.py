from prime_checker import prime_checker as pc
a = 987654321
z = set([str(x) for x in range(1,len(str(a))+1)])
print pc(11)
while a > 0:
	if len(str(a)) < len(str(a+2)):
		z = set([str(x) for x in range(1,len(str(a))+1)])
	if (a+1)%1000000 == 0:
		print a
	if set(str(a)) == z:
		if pc(a):
			print a
			exit()
	a -= 9
	
'''horrible code!!!!!'''