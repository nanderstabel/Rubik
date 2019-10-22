# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    scramble.py                                        :+:    :+:             #
#                                                      +:+                     #
#    By: nstabel <nstabel@student.codam.nl>           +#+                      #
#                                                    +#+                       #
#    Created: 2019/10/21 00:37:25 by nstabel        #+#    #+#                 #
#    Updated: 2019/10/21 02:18:13 by nstabel       ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

times = {" ": 1, "2": 2, "'": 3}

def this_rubiks(cube, input):
	i = 0
	leng = len(input)
	while i < leng:
		cube.rotate(input[i][0], times[input[i][1]])
		i += 1
	