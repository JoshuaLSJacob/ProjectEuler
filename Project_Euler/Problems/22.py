import csv
import string
names_list = []
with open('/Users/joshuajacob/Desktop/Project Euler/names.txt') as names:
    for a in csv.reader(names):
    	names_list = [[y,x] for x,y in enumerate(sorted(a))]


'''for e in names_list:
	for f in e[0]:
		print f'''

for b in names_list:
	c = 0
	for d in b[0]:
		c += 1+string.uppercase.index(d)
	b.append(c)

g = 0       
for h in names_list:
	g += (h[1]+1)*h[2]

print(names_list)
print(g)