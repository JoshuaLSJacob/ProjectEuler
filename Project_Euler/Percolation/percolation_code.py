r = 4
import math
frequency = 10000
scale_limit = [0,200]

def percolation_checker(a,b,r):
	import math
	if math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2+(a[2]-b[2])**2) < 2*r :
		return True
	else:
		return False

def coords_creator(max_x=100,min_x=0,min_y=None,max_y=None, min_z=None, max_z=None, _frequency = 20):
	from random import randrange
	if min_y == None:
		min_y = min_x
	if max_y == None:
		max_y = max_x
	if min_z == None:
		min_z = min_x
	if max_z == None:
		max_z = max_x
	return [[randrange(min_x,max_x) for x in range(_frequency)],[randrange(min_y,max_y) for y in range(_frequency)],[randrange(min_z,max_z) for z in range(_frequency)],['b' for colour in range(_frequency)],[x for x in range(_frequency)]]

coords_list = coords_creator(scale_limit[1],_frequency=frequency) #clean/more dynamic range  option

for a in range(frequency):
	for b in range(frequency):
		if percolation_checker([coords_list[0][a],coords_list[1][a],coords_list[2][a]],[coords_list[0][b],coords_list[1][b],coords_list[2][b]],r):
			for c in coords_list[4]:
				if coords_list[4][c] == coords_list[4][a] and c != a:
					coords_list[4][c] = coords_list[4][b]
			coords_list[4][a] = coords_list[4][b]
b = sorted(coords_list[4])
prev = frequency


current_count = 0
max_count = [0,0]
for item in b:
	if item == prev:
		current_count += 1
		if current_count > max_count[1]:
			max_count[0] = item
			max_count[1] = current_count

	else:
		current_count = 0
	prev = item


for a in range(frequency):
	if coords_list[4][a] == max_count[0]:
		coords_list[3][a] = 'r'


import matplotlib.pyplot as plt
import pylab
from mpl_toolkits.mplot3d import Axes3D
import numpy
fig = pylab.figure()
ax = Axes3D(fig)
size_in_points = ax.transData.transform([2,0])-ax.transData.transform([1,0])
limit = scale_limit[1]
ax.scatter3D(coords_list[0],coords_list[1],coords_list[2],s=(80/9)*(r**2),c=coords_list[3]) #I can create an array of the colours to represent percolation.
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_xbound(0,limit)
ax.set_ybound(0,limit)
ax.set_zbound(0,limit)
ax.mouse_init()
plt.show()





