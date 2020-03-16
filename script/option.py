# This file is the  of option of the platformer

# The map, draw with multi-line string
MAP_SOURCE = """
......................................
......................................
..............+++++..............++...
......................................
+++++................+++++++..........
.........0.......................0....
......++++++....................++++..
......................................
......................................
@.............................U.......
=======.......====================....
:::::::=.....=::::::::::::::::::::==..
::::::::=.0.=:::::::::::::::::::::::==
:::::::::===::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::
"""

# Frame par seconde of the game
FPS = 60 

# The size of blocks in pixels
BLOCK_SIZE = 25

# block traveled by the player when arrow pressed
PLAYER_SPEED = 1/2

# Gravity force, lower when farther to 0 (Need to define better)
GRAVITY_FORCE = 80

# Jump height of player, in block of height
JUMP_HEIGHT = 5

# Option of the windows
WIN_OPT = {
	# Title of the windows
	"Title" : "Snake game in tkinter 1.0.0",

	# Size of windows, type "{}x{}" for not-defined, or else "800x700"
	# for windows of size 800 by 700
	"Size" : "{}x{}"
}

# Color of the player in hexadecimal or simple name of color. List of
# color defined here: http://www.tcl.tk/man/tcl8.6/TkCmd/colors.htm
PLAYER_COLOR = "Blue"

# Dict of all block, keys are the single char in MAP_SOURCE
MAP_CHARS = {
	"." : "void",
	"=" : "ground",
	"@" : "playerspawn",
	"0" : "coin",
	":" : "dirt",
	"+" : "plat",
	"U" : "bouncer"
}

# Color of each block, further the entier texture of it
BLOCK_TEXTURE = {
	"void" : "light blue",
	"ground" : "green",
	"playerspawn" : "light blue",
	"coin" : "yellow",
	"dirt" : "sienna4",
	"plat" : "black",
	"bouncer" : "red"
}

# List of block who have collisions
COLLISION_BLOCK = [
	"ground",
	"dirt",
	"plat"
]

INTERACTIVE_BLOCK = {
	"bouncer" : ["bounce"],
	"coin" : ["pop", "score+1"]
}