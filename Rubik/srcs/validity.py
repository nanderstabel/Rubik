# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    validity.py                                        :+:    :+:             #
#                                                      +:+                     #
#    By: nstabel <nstabel@student.codam.nl>           +#+                      #
#                                                    +#+                       #
#    Created: 2019/10/20 23:37:34 by nstabel        #+#    #+#                 #
#    Updated: 2019/10/22 18:35:56 by nstabel       ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import sys

valid_list = ["F", "F2", "F'", "R", "R2", "R'", "U", "U2", "U'", "B", "B2", "B'", "L", "L2", "L'", "D", "D2", "D'"]
usage = 'usage: python rubik.py "<arg1> <arg2> ... <argn>"\nargs should contain one of the following:\n[%s]' % ', '.join(map(str, valid_list)) + '\n'

def check():
	if len(sys.argv) > 2:
		print usage
		exit()
	if len(sys.argv) == 2:
		input = sys.argv[1].split()
		if set(input).issubset(valid_list):
			input = [item + ' ' for item in input]
			return input
		else:
			print usage
			exit()
