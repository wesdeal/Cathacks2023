import pygame as pg
import sys
from pygame.locals import *
from config import * # gets all setting constants

pg.init()
vec = pg.math.Vector2 # used for 2 dimensional movement calculations     

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