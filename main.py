from map_and_player import *
from option import *
from landing_block import *
import tkinter as tk

gMap = MapParser(MAP_SOURCE)
player = Player(gMap)

def update():
	global gMap, player, can
	undrBlc = underBloc(gMap, player)
	for y in range(len(gMap)):
		for x in range(len(gMap[0])):
			if gMap[y][x] == undrBlc:
				gMap[y][x].texture = "red"
			else :
				gMap[y][x].texture = BLOC_TEXTURE[gMap[y][x].blockType]
	gMap.draw(can)
	player.drawPlayer(can)

	can.after(1000//FPS, update)

def pRight(event):
	global player
	player.x += PLAYER_SPEED

def pLeft(event):
	global player
	player.x -= PLAYER_SPEED

def quitAll(event):
	root.quit()

root = tk.Tk()
can = tk.Canvas(height=len(gMap)*BLOCK_SIZE, width=len(gMap[0])*BLOCK_SIZE)
can.pack()

root.bind("<Left>", pLeft)
root.bind("<Right>", pRight)
root.bind("<Escape>", quitAll)
update()

root.mainloop()