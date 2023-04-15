import pygame as pg
import sys
from pygame.locals import *
from config import * # gets all setting constants
from player import Player

pg.init()
vec = pg.math.Vector2 # used for 2 dimensional movement calculations     

FPS = pg.time.Clock()
DISPLAYSURF = pg.display.set_mode((WIDTH, HEIGHT))

HEIGHT = 450
WIDTH = 400
displaysurface = pg.display.set_mode((WIDTH, HEIGHT))

P1 = Player()

# Begin main game loop
while (True):
  # check events first
  for event in pg.event.get():
    if event.type == QUIT:
      sys.exit()
  
  # blank out the display surface in preparation for drawing new frame
  DISPLAYSURF.fill(WHITE)
  displaysurface.blit(P1.surf,P1.rect)
  P1.update()
  P1.move()

  pg.display.update()
  FPS.tick(FRAMERATE)