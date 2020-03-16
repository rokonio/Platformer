from map_and_player import *
from math import ceil, floor

def underBlock(gMap, player):
	beetweenBlock = [ceil(player.x), floor(player.x)]
	heighterBlock = gMap[-1][-1]
	for y in range(ceil(player.y), len(gMap)):
		for x in beetweenBlock:
			try :
				if gMap[y][x].y < heighterBlock.y and gMap[y][x].collision:
					heighterBlock = gMap[y][x]
			except IndexError :
				if gMap[len(gMap)-1][x].y < heighterBlock.y and gMap[len(gMap)-1][x].collision:
					heighterBlock = gMap[len(gMap)-1][x]
	return heighterBlock