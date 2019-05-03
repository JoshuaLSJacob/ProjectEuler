def coords_creator(min_x,max_x,min_y=None,max_y=None, _frequency = 20):
	from random import randrange
	if min_y == None:
		min_y = min_x
	if max_y == None:
		max_y = max_x
	coords = [[randrange(min_x,max_x),randrange(min_y,max_y)] for x in range(_frequency)]
	return coords
coords_list = coords_creator(0,100,_frequency=5)
print coords_list