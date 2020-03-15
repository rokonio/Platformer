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
@.....................................
=======.......====================....
:::::::=.....=::::::::::::::::::::==..
::::::::=.0.=:::::::::::::::::::::::==
:::::::::===::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::
"""

# Frame par seconde of the game
FPS = 10 

# The size of blocs in pixels
BLOCK_SIZE = 25

# Bloc traveled by the player when arrow pressed
PLAYER_SPEED = 1/2

# Gravity force, lower when farther to 0 (Need to define better)
GRAVITY_FORCE = 100

# Jump height of player, in bloc of height
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

# Dict of all bloc, keys are the single char in MAP_SOURCE
MAP_CHARS = {
	"." : "void",
	"=" : "ground",
	"@" : "playerspawn",
	"0" : "coin",
	":" : "dirt",
	"+" : "plat"
}

# Color of each bloc, further the entier texture of it
BLOC_TEXTURE = {
	"void" : "light blue",
	"ground" : "green",
	"playerspawn" : "light blue",
	"coin" : "yellow",
	"dirt" : "sienna4",
	"plat" : "black"
}

# List of bloc who have collisions
COLLISION_BLOC = [
	"ground",
	"dirt",
	"plat"
]