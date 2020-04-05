# This file is the  of option of the platformer

# The map, draw with multi-line string
MAP_SOURCE = """
......................................
......................................
......................................
......................................
......................................
......................................
......................................
......................................
......................................
.....................+................
....................+0+...0...........
.....................+....0...........
................<++++++++++...........
@................0....+...............
++...............0....+...............
.....................+................
....................+.+...............
...................+...+..............
======================================
::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
"""

# Frame par seconde of the game
FPS = 60

# The size of blocks in pixels
BLOCK_SIZE = 25

# block traveled by the player when arrow pressed
PLAYER_SPEED = 1 / 2

# Gravity force, lower when farther to 0 (Need to define better)
GRAVITY_FORCE = 80

# Jump height of player, in block of height
JUMP_HEIGHT = 5

# Option of the windows
WIN_OPT = {
    # Title of the windows
    "Title": "Snake game in tkinter 1.0.0",
    # Size of windows, type "{}x{}" for not-defined, or else "800x700"
    # for windows of size 800 by 700
    "Size": "{}x{}",
}

# Color of the player in hexadecimal or simple name of color. List of
# color defined here: http://www.tcl.tk/man/tcl8.6/TkCmd/colors.htm
PLAYER_COLOR = "Blue"

# Dict of all block, keys are the single char in MAP_SOURCE
MAP_CHARS = {
    ".": "void",
    "=": "ground",
    "@": "playerspawn",
    "0": "coin",
    ":": "dirt",
    "+": "plat",
    "U": "bouncer",
    "<": "rBorder",
    "Q": "stone",
}

# Texture for each block :
# 	The dict contain all the texture for all block
# 	 	The list contain all the texture for one block :
# 			Each list in it contain one texture for block :
# 				* The type of texture :
# 					* "rect" for rectangle
# 					* "oval" for oval
# 				* The two first digit are the coords of the first drawing point
# 				* The third and fourth are the coords of the second point
# 				* The last string is the color of the texture :
# 					* The avaible color is the link at line 48
# For polygon:
# 	 * The first string must be "polygone"
# 	 * The seconde is a list of tuple of point like this: [(0,0),(1,1),(0,1)]
# 	 * The last is the color
#
#
# Exemple :
# 		"coin" : [["rect",0,0,1,1,"light blue"],
# 				  ["oval",0,0,1,1,"yellow"]]
# 	 The first list is the sky on background :
# 		Rectangle, the first drawing point is (0,0) and the second is (1,1).
# 		The color is light blue for the sky
# 	 The second is the coin :
# 		Oval the first drawing point is (0,0) and the second is (1,1).
# 		The color is yellow like a coin

BLOCK_TEXTURE = {
    "void": [["rect", 0, 0, 1, 1, "light blue"]],
    "ground": [["rect", 0, 0, 1, 1 / 5, "green"], ["rect", 0, 1 / 5, 1, 1, "sienna4"]],
    "playerspawn": [["rect", 0, 0, 1, 1, "light blue"]],
    "coin": [["rect", 0, 0, 1, 1, "light blue"], ["oval", 0, 0, 1, 1, "yellow"]],
    "dirt": [["rect", 0, 0, 1, 1, "sienna4"]],
    "plat": [["rect", 0, 0, 1, 1, "black"]],
    "bouncer": [
        ["rect", 0, 0, 1, 1, "light blue"],
        ["rect", 2 / 5, 2 / 5, 3 / 5, 3 / 5, "red"],
        ["rect", 0, 3 / 5, 1, 1, "red"],
    ],
    "rBorder": [
        ["rect", 0, 0, 1, 1, "light blue"],
        ["polygone", [(1 / 3, 0), (1, 1), (1, 0)], "black"],
    ],
    "stone": [["rect", 0, 0, 1, 1, "grey"]],
}

# List of block who have collisions
COLLISION_BLOCK = ["ground", "dirt", "plat", "rBorder", "stone"]

INTERACTIVE_BLOCK = {"bouncer": ["bounce"], "coin": ["pop", "score+1"]}
