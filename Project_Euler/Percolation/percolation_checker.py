def percolation_checker(a,b,r):
	import math
	if math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2+(a[2]-b[2])**2) < 2*r :
		print 'Yes'
		return True
	else:
		print 'No'
		return False

percolation_checker([1,2,3],[3,2,1],1)
cluster_1 = []





