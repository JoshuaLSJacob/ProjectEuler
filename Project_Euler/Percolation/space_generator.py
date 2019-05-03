def coords_creator(max_x,min_x=0,min_y=None,max_y=None, min_z=None, max_z=None, _frequency = 20):
	from random import randrange
	if min_y == None:
		min_y = min_x
	if max_y == None:
		max_y = max_x
	if min_z == None:
		min_z = min_x
	if max_z == None:
		max_z = max_x
	coords = [[randrange(min_x,max_x) for x in range(_frequency)],[randrange(min_y,max_y) for y in range(_frequency)],[randrange(min_z,max_z) for x in range(_frequency)]]
	return coords

import matplotlib.pyplot as plt
import pylab
from mpl_toolkits.mplot3d import Axes3D
fig = pylab.figure()
ax = Axes3D(fig)
limit = 200
coords = coords_creator(limit, _frequency = 400)
ax.scatter3D(coords[0],coords[1],coords[2],s=100,c='b') #I can create an array of the colours to represent percolation.
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_xbound(0,limit)
ax.set_ybound(0,limit)
ax.set_zbound(0,limit)
ax.mouse_init()
plt.show()

