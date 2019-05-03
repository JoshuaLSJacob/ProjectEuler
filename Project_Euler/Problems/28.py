sum = 0
last = 1
gap = 2
sub_count = 0
a = 1
while a < 1001**2+1:
	sum += a
	a += gap
	sub_count += 1
	if sub_count == 4:
		gap += 2
		sub_count = 0
print sum