max_sum =[0,0,0]
for a in range(1,101):
	for b in range(1,101):
		if sum([int(x) for x in str(a**b)]) > max_sum[0]:
			max_sum = [sum([int(x) for x in str(a**b)]),a,b]
print max_sum
