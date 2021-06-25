"""
Home for global variables describing board state or otherwise.
Maybe I want this as an object - probably eventually, but lets do this quick
and dirty for now, even though it feels awful, this is the first step in
iterative development! Don't commit to a particular object oriented structure
until you know the problem space Aurora!
"""

# Origin of the board is bottom-left-hand corner always.
BOARD_MINIMUM_X = 0
BOARD_MINIMUM_Y = 0

# Set at start so we know how big the board is, and how far is too far
BOARD_MAXIMUM_X = 0
BOARD_MAXIMUM_Y = 0

# Use a dictionary to avoid if/else when determining the change in position
MOVE_LOOKUP = {"left": -1, "right": 1, "up": 1, "down": -1}

# Keep track on if the game is running or not
GAME_ON = False