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
		self.firstDraw = True   # If the first time of drawing bloc

	def drawBloc(self, canvas):
		if self.firstDraw: # If their is the first draw of the bloc 
			self.display = canvas.create_rectangle(
				self.x*BLOCK_SIZE,
				self.y*BLOCK_SIZE,
				(self.x+1)*BLOCK_SIZE,
				(self.y+1)*BLOCK_SIZE, 
				fill=self.texture,
				width=0)
			self.firstDraw = False
		else :
			canvas.itemconfigure(self.display, fill=self.texture)


class MapParser:
	def __init__(self, source):
		self.lines = source.split('\n') # List of all the lines
		self._grid = [] # 2D array who contain the bloc

		# Filter the void line
		for line in range(len(self.lines)-1):
			if self.lines[line] in ["", "\n", " ", "\t"]:
				del self.lines[line]

		# Making the map in self._grid
		for y,line in enumerate(self.lines):
			self._grid.append([])
			for x,char in enumerate(line):
				self._grid[y].append(Block(x, y, char))

		del self.lines

	def draw(self, canvas):
		for y in range(len(self._grid)):
			for x in range(len(self._grid[y])):
				self._grid[y][x].drawBloc(canvas)

	def __getitem__(self, index):
		return self._grid[index]

	def __len__(self):
		return len(self._grid)

if __name__ == '__main__':
	mape = MapParser(MAP_SOURCE)
	
	root = tk.Tk()
	can = tk.Canvas(height=len(mape)*BLOCK_SIZE, width=len(mape[0])*BLOCK_SIZE)
	can.pack()
	
	mape.draw(can)

	root.mainloop()