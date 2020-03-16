from map_and_player import *
from math import ceil, floor

def underBloc(gMap, player):
	beetweenBlock = [ceil(player.x), floor(player.x)]
	heighterBlock = gMap[-1][-1]
	for y in range(ceil(player.y), len(gMap)):
		for x in beetweenBlock:
			if gMap[y][x].y < heighterBlock.y and gMap[y][x].collision:
				heighterBlock = gMap[y][x]
	return heighterBlock