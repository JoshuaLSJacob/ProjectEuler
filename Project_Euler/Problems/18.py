import csv

triangle = []
with open('/Users/joshuajacob/Library/Mobile Documents/com~apple~TextEdit/Documents/trianglebig.txt') as triangle1:
    for row in csv.reader(triangle1):
        triangle.append([int(x) for x in row[0].split()])

triangle2 = []

for a in triangle:
	triangle2.append([[y,x,y,[x]] for x,y in enumerate(a)])

#print triangle



for x in triangle2:
	
	for b in x:
		
		if len(x) == 1:
			
			break
		if b[1] == 0:										#left edge of the triangle
			R = triangle2[len(x)-2][b[1]]
			
			b[3].append(R[3][0])										
			b[2] += R[2]
			
		elif b[1] == len(x)-1:								#right edge of triangle
			L = triangle2[len(x)-2][b[1]-1]
			b[3].append(L[3][0]) 								
			b[2] += L[2] 
		else:
			L = triangle2[len(x)-2][b[1]-1]
			R = triangle2[len(x)-2][b[1]]
			if L[2] > R[2]:												#route from up to the left > route from up to the right:
				for c in L[3]:
					b[3].append(c)
																#make the route to b come from the left; by adding the route it had saved
				b[2] += L[2] 											#add the value of b to the route value
			else:
				for c in R[3]:
					b[3].append(c)
														#make the route to b come form the right; by adding the route L had saved
				b[2] += R[2]	
												#add the value of b to the route value


zebra = []
for lot in triangle2[-1]:
	zebra.append(lot[2])
print(max(zebra))
print(triangle2[-1][0][3])


