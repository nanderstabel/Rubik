# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    colform.py                                         :+:    :+:             #
#                                                      +:+                     #
#    By: nstabel <nstabel@student.codam.nl>           +#+                      #
#                                                    +#+                       #
#    Created: 2019/10/20 21:37:01 by nstabel        #+#    #+#                 #
#    Updated: 2019/10/20 21:41:23 by nstabel       ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

WHITE = u'\u001b[38;5;15m'
ORANGE = u'\u001b[38;5;208m'
GREEN = u'\u001b[38;5;82m'
RED = u'\u001b[38;5;196m'
BLUE = u'\u001b[38;5;33m'
YELLOW = u'\u001b[38;5;226m'
ENDC = '\033[0m'

colors = {'white': WHITE, 'orange': ORANGE, 'green': GREEN, 'red': RED, 'blue': BLUE, 'yellow': YELLOW}

def colorcode(color):
	return color[0].capitalize()

def get_colform(cube):
	colform = []
	colform.append(colors[cube.subcube[0][0][2].y.color] + colorcode(cube.subcube[0][0][2].y.color) + ENDC)
	colform.append(colors[cube.subcube[1][0][2].y.color] + colorcode(cube.subcube[1][0][2].y.color) + ENDC)
	colform.append(colors[cube.subcube[2][0][2].y.color] + colorcode(cube.subcube[2][0][2].y.color) + ENDC)
	colform.append(colors[cube.subcube[0][0][1].y.color] + colorcode(cube.subcube[0][0][1].y.color) + ENDC)
	colform.append(colors[cube.subcube[1][0][1].y.color] + colorcode(cube.subcube[1][0][1].y.color) + ENDC)
	colform.append(colors[cube.subcube[2][0][1].y.color] + colorcode(cube.subcube[2][0][1].y.color) + ENDC)
	colform.append(colors[cube.subcube[0][0][0].y.color] + colorcode(cube.subcube[0][0][0].y.color) + ENDC)
	colform.append(colors[cube.subcube[1][0][0].y.color] + colorcode(cube.subcube[1][0][0].y.color) + ENDC)
	colform.append(colors[cube.subcube[2][0][0].y.color] + colorcode(cube.subcube[2][0][0].y.color) + ENDC)

	colform.append(colors[cube.subcube[0][0][2].x.color] + colorcode(cube.subcube[0][0][2].x.color) + ENDC)
	colform.append(colors[cube.subcube[0][0][1].x.color] + colorcode(cube.subcube[0][0][1].x.color) + ENDC)
	colform.append(colors[cube.subcube[0][0][0].x.color] + colorcode(cube.subcube[0][0][0].x.color) + ENDC)
	colform.append(colors[cube.subcube[0][0][0].z.color] + colorcode(cube.subcube[0][0][0].z.color) + ENDC)
	colform.append(colors[cube.subcube[1][0][0].z.color] + colorcode(cube.subcube[1][0][0].z.color) + ENDC)
	colform.append(colors[cube.subcube[2][0][0].z.color] + colorcode(cube.subcube[2][0][0].z.color) + ENDC)
	colform.append(colors[cube.subcube[2][0][0].x.color] + colorcode(cube.subcube[2][0][0].x.color) + ENDC)
	colform.append(colors[cube.subcube[2][0][1].x.color] + colorcode(cube.subcube[2][0][1].x.color) + ENDC)
	colform.append(colors[cube.subcube[2][0][2].x.color] + colorcode(cube.subcube[2][0][2].x.color) + ENDC)
	colform.append(colors[cube.subcube[2][0][2].z.color] + colorcode(cube.subcube[2][0][2].z.color) + ENDC)
	colform.append(colors[cube.subcube[1][0][2].z.color] + colorcode(cube.subcube[1][0][2].z.color) + ENDC)
	colform.append(colors[cube.subcube[0][0][2].z.color] + colorcode(cube.subcube[0][0][2].z.color) + ENDC)

	colform.append(colors[cube.subcube[0][1][2].x.color] + colorcode(cube.subcube[0][1][2].x.color) + ENDC)
	colform.append(colors[cube.subcube[0][1][1].x.color] + colorcode(cube.subcube[0][1][1].x.color) + ENDC)
	colform.append(colors[cube.subcube[0][1][0].x.color] + colorcode(cube.subcube[0][1][0].x.color) + ENDC)
	colform.append(colors[cube.subcube[0][1][0].z.color] + colorcode(cube.subcube[0][1][0].z.color) + ENDC)
	colform.append(colors[cube.subcube[1][1][0].z.color] + colorcode(cube.subcube[1][1][0].z.color) + ENDC)
	colform.append(colors[cube.subcube[2][1][0].z.color] + colorcode(cube.subcube[2][1][0].z.color) + ENDC)
	colform.append(colors[cube.subcube[2][1][0].x.color] + colorcode(cube.subcube[2][1][0].x.color) + ENDC)
	colform.append(colors[cube.subcube[2][1][1].x.color] + colorcode(cube.subcube[2][1][1].x.color) + ENDC)
	colform.append(colors[cube.subcube[2][1][2].x.color] + colorcode(cube.subcube[2][1][2].x.color) + ENDC)
	colform.append(colors[cube.subcube[2][1][2].z.color] + colorcode(cube.subcube[2][1][2].z.color) + ENDC)
	colform.append(colors[cube.subcube[1][1][2].z.color] + colorcode(cube.subcube[1][1][2].z.color) + ENDC)
	colform.append(colors[cube.subcube[0][1][2].z.color] + colorcode(cube.subcube[0][1][2].z.color) + ENDC)

	colform.append(colors[cube.subcube[0][2][2].x.color] + colorcode(cube.subcube[0][2][2].x.color) + ENDC)
	colform.append(colors[cube.subcube[0][2][1].x.color] + colorcode(cube.subcube[0][2][1].x.color) + ENDC)
	colform.append(colors[cube.subcube[0][2][0].x.color] + colorcode(cube.subcube[0][2][0].x.color) + ENDC)
	colform.append(colors[cube.subcube[0][2][0].z.color] + colorcode(cube.subcube[0][2][0].z.color) + ENDC)
	colform.append(colors[cube.subcube[1][2][0].z.color] + colorcode(cube.subcube[1][2][0].z.color) + ENDC)
	colform.append(colors[cube.subcube[2][2][0].z.color] + colorcode(cube.subcube[2][2][0].z.color) + ENDC)
	colform.append(colors[cube.subcube[2][2][0].x.color] + colorcode(cube.subcube[2][2][0].x.color) + ENDC)
	colform.append(colors[cube.subcube[2][2][1].x.color] + colorcode(cube.subcube[2][2][1].x.color) + ENDC)
	colform.append(colors[cube.subcube[2][2][2].x.color] + colorcode(cube.subcube[2][2][2].x.color) + ENDC)
	colform.append(colors[cube.subcube[2][2][2].z.color] + colorcode(cube.subcube[2][2][2].z.color) + ENDC)
	colform.append(colors[cube.subcube[1][2][2].z.color] + colorcode(cube.subcube[1][2][2].z.color) + ENDC)
	colform.append(colors[cube.subcube[0][2][2].z.color] + colorcode(cube.subcube[0][2][2].z.color) + ENDC)

	colform.append(colors[cube.subcube[0][2][0].y.color] + colorcode(cube.subcube[0][2][0].y.color) + ENDC)
	colform.append(colors[cube.subcube[1][2][0].y.color] + colorcode(cube.subcube[1][2][0].y.color) + ENDC)
	colform.append(colors[cube.subcube[2][2][0].y.color] + colorcode(cube.subcube[2][2][0].y.color) + ENDC)
	colform.append(colors[cube.subcube[0][2][1].y.color] + colorcode(cube.subcube[0][2][1].y.color) + ENDC)
	colform.append(colors[cube.subcube[1][2][1].y.color] + colorcode(cube.subcube[1][2][1].y.color) + ENDC)
	colform.append(colors[cube.subcube[2][2][1].y.color] + colorcode(cube.subcube[2][2][1].y.color) + ENDC)
	colform.append(colors[cube.subcube[0][2][2].y.color] + colorcode(cube.subcube[0][2][2].y.color) + ENDC)
	colform.append(colors[cube.subcube[1][2][2].y.color] + colorcode(cube.subcube[1][2][2].y.color) + ENDC)
	colform.append(colors[cube.subcube[2][2][2].y.color] + colorcode(cube.subcube[2][2][2].y.color) + ENDC)
	return colform
