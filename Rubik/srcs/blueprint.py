# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    blueprint.py                                       :+:    :+:             #
#                                                      +:+                     #
#    By: nstabel <nstabel@student.codam.nl>           +#+                      #
#                                                    +#+                       #
#    Created: 2019/10/19 20:04:31 by nstabel        #+#    #+#                 #
#    Updated: 2019/10/20 23:20:16 by nstabel       ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

nl = '\n'
skip =		'       ' * 3
upper =		' _____ ' * 3
middle =	'|     |' * 3
param =		'|  {0}  |'
lower =		'|_____|' * 3

uno = skip + upper + skip * 2 + nl + skip + middle + skip * 2 + nl + skip + param.format('{0}') + param.format('{1}') + param.format('{2}') + nl + skip + lower + skip * 2 + nl
quatro = upper * 4 + nl + middle * 4 + nl + param.format('{0}') + param.format('{1}') + param.format('{2}') + param.format('{3}') + param.format('{4}') + param.format('{5}') + \
			param.format('{6}') + param.format('{7}') + param.format('{8}') + param.format('{9}') + param.format('{10}') + param.format('{11}') + nl + lower * 4 + nl

output =					uno.format('{0}' , '{1}' , '{2}') + \
							uno.format('{3}' , '{4}' , '{5}') + \
							uno.format('{6}' , '{7}' , '{8}') + \
quatro.format('{9}' , '{10}', '{11}', '{12}', '{13}', '{14}', '{15}', '{16}', '{17}', '{18}', '{19}', '{20}') + \
quatro.format('{21}', '{22}', '{23}', '{24}', '{25}', '{26}', '{27}', '{28}', '{29}', '{30}', '{31}', '{32}') + \
quatro.format('{33}', '{34}', '{35}', '{36}', '{37}', '{38}', '{39}', '{40}', '{41}', '{42}', '{43}', '{44}') + \
						   uno.format('{45}', '{46}', '{47}') + \
						   uno.format('{48}', '{49}', '{50}') + \
						   uno.format('{51}', '{52}', '{53}')
