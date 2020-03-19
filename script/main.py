from map_and_player import *
from gravity_collision import *
from option import *
from landing_block import *
import tkinter as tk

gMap = MapParser(MAP_SOURCE)
player = Player(gMap)
game = True

def update():
	global gMap, player, can, lab, game
	if game :
		undrBlc = underBlock(gMap, player)
		for y in range(len(gMap)):
			for x in range(len(gMap[0])):
				if gMap[y][x] == undrBlc:
					gMap[y][x].texture = [["rect", 0,0,1,1, "red"]]
				else :
					gMap[y][x].texture = BLOCK_TEXTURE[gMap[y][x].blockType]
		applyGravity(gMap, player)
		applyCollision(gMap, player, 0)
		gMap.draw(can)
		player.drawPlayer(can)
		lab["text"] = player.score
		try :
			can.tag_raise(player.display, can.find_all()[-1])
		except :
			pass
	can.after(1000//FPS, update)

def pRight(event):
	global player, game
	if game :
		applyCollision(gMap, player, -1)
		player.x += PLAYER_SPEED

def pLeft(event):
	global player
	if game:
		applyCollision(gMap, player, 1)
		player.x -= PLAYER_SPEED

def pJump(event):
	global player, game
	if (underBlock(gMap, player).y - player.y - 1) <= 0 and game:
		player.velocity -= JUMP_HEIGHT*20/GRAVITY_FORCE

def quitAll(event):
	root.destroy()

def pause(event):
	global game
	if game:
		game=False
	else :
		game=True

root = tk.Tk()
lab = tk.Label(root, text=player.score, font=("Helvetica",25))
lab.pack()
can = tk.Canvas(root, height=len(gMap)*BLOCK_SIZE, width=len(gMap[0])*BLOCK_SIZE)
can.pack()

root.bind("<Left>", pLeft)
root.bind("<Right>", pRight)
root.bind("<Escape>", quitAll)
root.bind("<space>", pJump)
root.bind("<w>", pause)
update()

root.mainloop()