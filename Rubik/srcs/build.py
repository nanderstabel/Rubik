# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    build.py                                           :+:    :+:             #
#                                                      +:+                     #
#    By: nstabel <nstabel@student.codam.nl>           +#+                      #
#                                                    +#+                       #
#    Created: 2019/10/19 15:53:35 by nstabel        #+#    #+#                 #
#    Updated: 2019/10/22 19:03:48 by nstabel       ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import blueprint
import colform

types = ('corner', 'edge', 'center', 'core')

def get_subcubes():
	subcubes = [[[None] * 3, [None] * 3, [None] * 3],
				[[None] * 3, [None] * 3, [None] * 3],
				[[None] * 3, [None] * 3, [None] * 3]]
	i = 0
	while i <= 2:
		j = 0
		while j <= 2:
			k = 0
			while k <= 2:
				subcubes[i][j][k] = Subcube(i, j, k)
				k += 1
			j += 1
		i += 1
	return subcubes

faces = {	'F': ['z', [[0, 0, 0], [1, 0, 0], [2, 0, 0], [0, 1, 0], [1, 1, 0], [2, 1, 0], [0, 2, 0], [1, 2, 0], [2, 2, 0]]],
		 	'R': ['x', [[2, 0, 0], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]],
			'U': ['y', [[0, 0, 2], [1, 0, 2], [2, 0, 2], [0, 0, 1], [1, 0, 1], [2, 0, 1], [0, 0, 0], [1, 0, 0], [2, 0, 0]]], 
			'B': ['z', [[2, 0, 2], [1, 0, 2], [0, 0, 2], [2, 1, 2], [1, 1, 2], [0, 1, 2], [2, 2, 2], [1, 2, 2], [0, 2, 2]]],
			'L': ['x', [[0, 0, 2], [0, 0, 1], [0, 0, 0], [0, 1, 2], [0, 1, 1], [0, 1, 0], [0, 2, 2], [0, 2, 1], [0, 2, 0]]],
			'D': ['y', [[0, 2, 0], [1, 2, 0], [2, 2, 0], [0, 2, 1], [1, 2, 1], [2, 2, 1], [0, 2, 2], [1, 2, 2], [2, 2, 2]]]}

layers = {	'F': ['z', [[0, 0, 0], [1, 0, 0], [2, 0, 0], [2, 1, 0], [2, 2, 0], [1, 2, 0], [0, 2, 0], [0, 1, 0]]],
		 	'R': ['x', [[2, 2, 2], [2, 2, 1], [2, 2, 0], [2, 1, 0], [2, 0, 0], [2, 0, 1], [2, 0, 2], [2, 1, 2]]],
			'U': ['y', [[0, 0, 2], [1, 0, 2], [2, 0, 2], [2, 0, 1], [2, 0, 0], [1, 0, 0], [0, 0, 0], [0, 0, 1]]], 
			'B': ['z', [[0, 2, 2], [1, 2, 2], [2, 2, 2], [2, 1, 2], [2, 0, 2], [1, 0, 2], [0, 0, 2], [0, 1, 2]]],
			'L': ['x', [[0, 0, 2], [0, 0, 1], [0, 0, 0], [0, 1, 0], [0, 2, 0], [0, 2, 1], [0, 2, 2], [0, 1, 2]]],
			'D': ['y', [[0, 2, 2], [0, 2, 1], [0, 2, 0], [1, 2, 0], [2, 2, 0], [2, 2, 1], [2, 2, 2], [1, 2, 2]]]}

def rotate(cube, layer, axis):
	color_list = [None] * 24
	i = 0
	while i < 8:
		if axis == 'z':
			color_list[i * 3 + 1] = cube.subcube[layer[i][0]][layer[i][1]][layer[i][2]].x.color
			color_list[i * 3] = cube.subcube[layer[i][0]][layer[i][1]][layer[i][2]].y.color
			color_list[i * 3 + 2] = cube.subcube[layer[i][0]][layer[i][1]][layer[i][2]].z.color
		if axis == 'x':
			color_list[i * 3] = cube.subcube[layer[i][0]][layer[i][1]][layer[i][2]].x.color
			color_list[i * 3 + 2] = cube.subcube[layer[i][0]][layer[i][1]][layer[i][2]].y.color
			color_list[i * 3 + 1] = cube.subcube[layer[i][0]][layer[i][1]][layer[i][2]].z.color
		if axis == 'y':
			color_list[i * 3 + 2] = cube.subcube[layer[i][0]][layer[i][1]][layer[i][2]].x.color
			color_list[i * 3 + 1] = cube.subcube[layer[i][0]][layer[i][1]][layer[i][2]].y.color
			color_list[i * 3] = cube.subcube[layer[i][0]][layer[i][1]][layer[i][2]].z.color				
		i += 1
	color_list = color_list[18:] + color_list[:18]
	i = 0
	while i < 8:
		cube.subcube[layer[i][0]][layer[i][1]][layer[i][2]].x.color = color_list[i * 3]
		cube.subcube[layer[i][0]][layer[i][1]][layer[i][2]].y.color = color_list[i * 3 + 1]
		cube.subcube[layer[i][0]][layer[i][1]][layer[i][2]].z.color = color_list[i * 3 + 2] 
		i += 1

class Cube:
	
	def __init__(self):
		self.subcube = get_subcubes()
	def rotate(self, rotation, n):
		while n:
			rotate(self, layers[rotation][1], layers[rotation][0])
			n -= 1
	def print_flat(self):
		formlist = colform.get_colform(self)
		output = blueprint.output.format(*formlist)
		print output

class Subcube:

	def __init__(self, x, y, z):
		self.type = types[[x, y, z].count(1)]
		self.x = Dimension(x, ('orange', None, 'red')[x])
		self.y = Dimension(y, ('white', None, 'yellow')[y])
		self.z = Dimension(z, ('green', None, 'blue')[z])

class Dimension:

	def __init__(self, value, color):
		self.value = value
		self.color = color
