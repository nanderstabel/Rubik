# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    rubik.py                                           :+:    :+:             #
#                                                      +:+                     #
#    By: nstabel <nstabel@student.codam.nl>           +#+                      #
#                                                    +#+                       #
#    Created: 2019/10/20 23:28:11 by nstabel        #+#    #+#                 #
#    Updated: 2019/10/22 23:38:52 by nstabel       ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import validity
import build
import scramble
import solve

input = validity.check()
cube = build.Cube()
if input:
	scramble.this_rubiks(cube, input)

ugly = [None] * 50
for i in ugly:
	finished = 0
	while finished == 0:

		list = []
		l = 0
		i = 0
		while i < 3:
			j = 0
			while j < 3:
				k = 0
				while k < 3:
					if cube.subcube[i][j][k].type == 'edge':
						if cube.subcube[i][j][k].x.color == 'white':
							list.append((i, j, k, 'x'))
						if cube.subcube[i][j][k].y.color == 'white':
							list.append((i, j, k, 'y'))
						if cube.subcube[i][j][k].z.color == 'white':
							list.append((i, j, k, 'z'))
					k += 1
				j += 1
			i += 1
		itera = 0
		while itera < 4:
			if list[itera][1] == 2 and list[itera][3] == 'y':
				if list[itera][0] == 0:
					while cube.subcube[0][0][1].y.color == 'white':
						cube.rotate('U', 1)	
					cube.rotate('L', 2)
				elif list[itera][0] == 2:
					while cube.subcube[2][0][1].y.color == 'white':
						cube.rotate('U', 1)
					cube.rotate('R', 2)
				elif list[itera][2] == 0:
					while cube.subcube[1][0][0].y.color == 'white':
						cube.rotate('U', 1)	
					cube.rotate('B', 2)
				elif list[itera][2] == 2:
					while cube.subcube[1][0][2].y.color == 'white':
						cube.rotate('U', 1)	
					cube.rotate('F', 2)
			elif list[itera][1] == 2 and list[itera][3] != 'y':
				if list[itera][3] == 'x' and list[itera][0] == 0:
					while cube.subcube[0][0][1].y.color == 'white':
						cube.rotate('U', 1)
					cube.rotate('L', 3)
					cube.rotate('F', 3)
					cube.rotate('D', 3)
					cube.rotate('F', 1)
					cube.rotate('L', 2)
				elif list[itera][3] == 'z' and list[itera][2] == 0:
					while cube.subcube[1][0][0].y.color == 'white':
						cube.rotate('U', 1)
					cube.rotate('F', 3)
					cube.rotate('R', 3)
					cube.rotate('D', 3)
					cube.rotate('R', 1)
					cube.rotate('F', 2)
				elif list[itera][3] == 'x' and list[itera][0] == 2:
					while cube.subcube[2][0][1].y.color == 'white':
						cube.rotate('U', 1)
					cube.rotate('R', 3)
					cube.rotate('B', 3)
					cube.rotate('D', 3)
					cube.rotate('B', 1)
					cube.rotate('R', 2)
				elif list[itera][3] == 'z' and list[itera][2] == 2:
					while cube.subcube[1][0][2].y.color == 'white':
						cube.rotate('U', 1)
					cube.rotate('B', 3)
					cube.rotate('L', 3)
					cube.rotate('D', 3)
					cube.rotate('L', 1)
					cube.rotate('B', 2)
			elif list[itera][1] == 1:
				if list[itera][0] == 0 and list[itera][2] == 2 and list[itera][3] == 'x':
					while cube.subcube[0][0][1].y.color == 'white':
						cube.rotate('U', 1)	
					cube.rotate('F', 3)
					cube.rotate('D', 3)
					cube.rotate('F', 1)
					cube.rotate('L', 2)
				elif list[itera][0] == 0 and list[itera][2] == 0 and list[itera][3] == 'z':
					while cube.subcube[1][0][0].y.color == 'white':
						cube.rotate('U', 1)
					cube.rotate('R', 3)
					cube.rotate('D', 3)
					cube.rotate('R', 1)
					cube.rotate('F', 2)
				elif list[itera][0] == 2 and list[itera][2] == 0 and list[itera][3] == 'x':
					while cube.subcube[2][0][1].y.color == 'white':
						cube.rotate('U', 1)	
					cube.rotate('B', 3)
					cube.rotate('D', 3)
					cube.rotate('B', 1)
					cube.rotate('R', 2)
				elif list[itera][0] == 2 and list[itera][2] == 2 and list[itera][3] == 'z':
					while cube.subcube[1][0][2].y.color == 'white':
						cube.rotate('U', 1)
					cube.rotate('L', 3)
					cube.rotate('D', 3)
					cube.rotate('L', 1)
					cube.rotate('B', 2)
				elif list[itera][0] == 0 and list[itera][2] == 2 and list[itera][3] == 'z':
					while cube.subcube[1][0][2].y.color == 'white':
						cube.rotate('U', 1)	
					cube.rotate('R', 1)
					cube.rotate('D', 1)
					cube.rotate('R', 3)
					cube.rotate('B', 2)
				elif list[itera][0] == 0 and list[itera][2] == 0 and list[itera][3] == 'x':
					while cube.subcube[0][0][1].y.color == 'white':
						cube.rotate('U', 1)
					cube.rotate('B', 1)
					cube.rotate('D', 1)
					cube.rotate('B', 3)
					cube.rotate('L', 2)
				elif list[itera][0] == 2 and list[itera][2] == 0 and list[itera][3] == 'z':
					while cube.subcube[1][0][0].y.color == 'white':
						cube.rotate('U', 1)	
					cube.rotate('L', 1)
					cube.rotate('D', 1)
					cube.rotate('L', 3)
					cube.rotate('F', 2)
				elif list[itera][0] == 2 and list[itera][2] == 2 and list[itera][3] == 'x':
					while cube.subcube[2][0][1].y.color == 'white':
						cube.rotate('U', 1)
					cube.rotate('F', 1)
					cube.rotate('D', 1)
					cube.rotate('F', 3)
					cube.rotate('R', 2)
			elif list[itera][1] == 0 and list[itera][3] != 'y':
				if list[itera][0] == 0:
					while cube.subcube[0][0][1].y.color == 'white':
						cube.rotate('U', 1)
					cube.rotate('L', 1)
					cube.rotate('U', 3)
					cube.rotate('F', 1)
					cube.rotate('U', 1)
				elif list[itera][0] == 2:
					while cube.subcube[2][0][1].y.color == 'white':
						cube.rotate('U', 1)
					cube.rotate('R', 1)
					cube.rotate('U', 3)
					cube.rotate('B', 1)
					cube.rotate('U', 1)
				elif list[itera][2] == 0:
					while cube.subcube[1][0][0].y.color == 'white':
						cube.rotate('U', 1)
					cube.rotate('F', 1)
					cube.rotate('U', 3)
					cube.rotate('R', 1)
					cube.rotate('U', 1)
				elif list[itera][2] == 2:
					while cube.subcube[1][0][2].y.color == 'white':
						cube.rotate('U', 1)
					cube.rotate('B', 1)
					cube.rotate('U', 3)
					cube.rotate('L', 1)
					cube.rotate('U', 1)
			else:
				finished = 1
			itera += 1

cube.print_flat()
