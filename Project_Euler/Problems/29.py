powers = []
for a in range(2,101):
	for x in range(2,101):
		powers.append(x**a) 
print(len(set(powers)))
