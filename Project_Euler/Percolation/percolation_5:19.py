#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  3 16:52:31 2019

@author: joshuajacob
"""

def percolation_checker(a,b,r):

	if (a[0]-b[0])**2+(a[1]-b[1])**2+(a[2]-b[2])**2 < 4*r**2 :
		return True
	else:
		return False

def limit_checker(a,limit,r):
    if (a-limit)**2 <= r**2:
        return True
    else:
        return False

def recursive_percolation_checker(points, r, base_point, bubble, duds, limits, success = False):
    b = 0
    while b < len(points):
        if b not in bubble and b not in duds and percolation_checker(points[base_point],points[b],r):
            bubble += [b]
            if limit_checker(points[b][0],limits[1],r):
                success = True
                b = len(points)
            else:
                bubble,success = recursive_percolation_checker(points, r, b, bubble, duds, limits)
                if success:
                    b = len(points)
        b += 1
    return bubble,success

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
	return [[randrange(min_x,max_x),randrange(min_y,max_y),randrange(min_z,max_z)] for x in range(_frequency)]




#go through all starting points i.e. points that hit the LHS
r = 4

frequency = 400
scale_limit = [0,50]

points = coords_creator(scale_limit[1],_frequency=frequency)
#print(points[0]) #clean/more dynamic range  option

duds = []
a = 0
while a < len(points):
    if a not in duds and limit_checker(points[a][0],scale_limit[0],r):
        bubble, success = recursive_percolation_checker(points,r, a,[a],duds,scale_limit)
        if success == True:
            a = len(points)
            print(bubble)
        else:
            duds += bubble
            
    a += 1

if success:
    import matplotlib.pyplot as plt
    import pylab
    from mpl_toolkits.mplot3d import Axes3D
    fig = pylab.figure()
    ax = Axes3D(fig)
    size_in_points = ax.transData.transform([2,0])-ax.transData.transform([1,0])
    limit = scale_limit[1]
    ax.scatter3D([points[a][0] for a in bubble] ,[points[a][1] for a in bubble],[points[a][2] for a in bubble],s=40*(r**2),c='r') #I can create an array of the colours to represent percolation.
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_xbound(0,scale_limit[1])
    ax.set_ybound(0,scale_limit[1])
    ax.set_zbound(0,scale_limit[1])
    ax.mouse_init()
    plt.show()

fig = pylab.figure()
ax = Axes3D(fig)
size_in_points = ax.transData.transform([2,0])-ax.transData.transform([1,0])
limit = scale_limit[1]
ax.scatter3D([points[a][0] for a in range(len(points))] ,[points[a][1] for a in range(len(points))],[points[a][2] for a in range(len(points))],s=40*(r**2),c='b') #I can create an array of the colours to represent percolation.
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_xbound(0,scale_limit[1])
ax.set_ybound(0,scale_limit[1])
ax.set_zbound(0,scale_limit[1])
ax.mouse_init()
plt.show()