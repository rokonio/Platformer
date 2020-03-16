from option import *
import tkinter as tk

class Block :
	""" Block class for each block  of the map """
	def __init__(self, x, y, char):
		self.x = x
		self.y = y
		self.char = char
		self.blockType = MAP_CHARS[char]
		self.texture = BLOC_TEXTURE[self.blockType]
		self.collision = self.blockType in COLLISION_BLOC
		self.firstDraw = true   # If the first time of drawing bloc

	def drawBloc(self, canvas):
		if self.firstDraw: # If their is the first draw of the bloc 
			self.display = canvas.create_rectangle(
				self.x*BLOCK_SIZE,
				self.y*BLOCK_SIZE,
				(self.x+1)*BLOCK_SIZE,
				(self.y+1)*BLOCK_SIZE, 
				fill=self.texture)
			self.firstDraw = False
		else :
			canvas.itemconfigure(elf.display, fill=self.texture)