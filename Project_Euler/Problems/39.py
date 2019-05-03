numbers = [a for a in range(1,1001)]
results = []
for a in numbers:
	for b in numbers:
		c = (a**2 + b**2)**0.5
		if c % 1 == 0:
			p = a + b + c
			if p < 1001:
				results.append(p)
max_count = [0.0]
for a in sorted(results):
	if a == b:
		count+= 1
	else:
		count = 1
	b = a
	if count > max_count[0]:
		max_count = [count,a]

print max_count


			