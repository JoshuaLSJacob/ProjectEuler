success = False
a = 1
while not success:
	'''if set(str(a)) == set(str(2*a)) and set(str(a)) == set(str(3*a)) and set(str(a)) == set(str(4*a)) and set(str(a)) == set(str(5*a)) and set(str(a)) == set(str(6*a)):'''
	if set(str(a)) == set(str(2*a)) == set(str(3*a)) == set(str(4*a)) == set(str(5*a)) == set(str(6*a)):
		print a
		exit()
	a += 1