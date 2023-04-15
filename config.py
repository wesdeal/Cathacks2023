import pygame as pg

# This file just defines constants used across the whole game
# Window width and height
WIDTH = 500
HEIGHT = 500

FRAMERATE = 60

# Movement constants
# NOTE: Do not set FRIC outside [-1, 0) unless you want !!FUN!!
FRIC = -0.12
ACC = 0.5

# Some predefined colors for easy use
BLACK = pg.Color(0, 0, 0)         
WHITE = pg.Color(255, 255, 255)   
GREY = pg.Color(128, 128, 128)   
RED = pg.Color(255, 0, 0) 
