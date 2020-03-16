from landing_block import *

def applyGravity(gMap, player):
	dist =  underBlock(gMap, player).y - player.y - 1
	if dist > 0:
		player.velocity += GRAVITY_FORCE/1000
	else :
		if player.velocity > 0:
			player.velocity = 0

	player.y += player.velocity