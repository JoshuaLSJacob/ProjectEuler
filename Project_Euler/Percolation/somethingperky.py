import matplotlib.pyplot as plt
import pylab
import math
from mpl_toolkits.mplot3d import Axes3D
fig = pylab.figure()
ax = Axes3D(fig)
limit = 200
size_in_points = ax.transData.transform([2,0])-ax.transData.transform([1,0])
print size_in_points[0]
print ax.transData.transform([1,0])

coords = [[1,3,5]]
ax.scatter3D([0,100],[100,0],s=(math.sqrt(27000)/50)**2,c='b') #I can create an array of the colours to represent percolation.
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_xbound(0,limit)
ax.set_ybound(0,limit)
ax.set_zbound(0,limit)
ax.mouse_init()
plt.show()