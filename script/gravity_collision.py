from landing_block import *
from math import ceil, floor

def applyGravity(gMap, player):
	dist =  underBlock(gMap, player).y - player.y - 1
	if dist > 0:
		player.velocity += GRAVITY_FORCE/1000
	if player.velocity > dist:
		player.velocity = dist
	player.y += player.velocity

def applyCollision(gMap, player, direction):
	betweenBlock = [ceil(player.x), floor(player.x)]
	betweenBlock2 = [ceil(player.y), floor(player.y)]
	for y in range(len(gMap)) :
		for x in range(len(gMap[0])) :
			if gMap[y][x].x in betweenBlock and\
					y in betweenBlock2 and\
					gMap[y][x].blockType in COLLISION_BLOCK:
				player.x += direction*PLAYER_SPEED
			elif gMap[y][x].x in betweenBlock and\
					y in betweenBlock2 and\
					gMap[y][x].blockType in INTERACTIVE_BLOCK.keys():
				for effect in INTERACTIVE_BLOCK[gMap[y][x].blockType]:
					if effect == "bounce":
						player.velocity = -130/GRAVITY_FORCE
					elif effect == "pop":
						gMap[y][x] = Block(x, y, ".")
						player.score += 1
			if gMap[y][x].y == betweenBlock2[1] and\
					gMap[y][x].x in betweenBlock and\
					gMap[y][x].blockType in COLLISION_BLOCK:
				player.velocity = 0.25