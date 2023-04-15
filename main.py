import pygame as pg
import sys
from pygame.locals import *

pg.init()
vec = pg.math.Vector2 # used for 2 dimensional movement calculations

# Game performance/display settings
WIDTH = 500 
HEIGHT = 500
FRAMERATE = 60

# Constants for movement to fine tune how it works
ACC = 0.5
# Comment this line out for !!FUN!!
# Also don't make it less than -1 or it also gets !!FUN!!
FRIC = -0.12

# colors predefined for easy use
BLACK = pg.Color(0, 0, 0)         
WHITE = pg.Color(255, 255, 255)   
GREY = pg.Color(128, 128, 128)   
RED = pg.Color(255, 0, 0)      

FPS = pg.time.Clock()
DISPLAYSURF = pg.display.set_mode((WIDTH, HEIGHT))

# Begin main game loop
while (True):
  # check events first
  for event in pg.event.get():
    if event.type == QUIT:
      sys.exit()
  
  # blank out the display surface in preparation for drawing new frame
  DISPLAYSURF.fill(WHITE)

  pg.display.update()
  FPS.tick(FRAMERATE)