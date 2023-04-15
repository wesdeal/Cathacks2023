import pygame as pg
import sys
from Platform import Platform

from pygame.locals import *
from config import * # gets all setting constants
from player import Player

pg.init()
vec = pg.math.Vector2 # used for 2 dimensional movement calculations     

FPS = pg.time.Clock()
DISPLAYSURF = pg.display.set_mode((WIDTH, HEIGHT))

HEIGHT = 450
WIDTH = 400

P1 = Player()

platform = Platform(x=100, y=200)

# Begin main game loop
while (True):
  # check events first
  for event in pg.event.get():
    if event.type == QUIT:
      sys.exit()
  
  # blank out the display surface in preparation for drawing new frame
  DISPLAYSURF.fill(WHITE)
  DISPLAYSURF.blit(P1.surf,P1.rect)
  DISPLAYSURF.blit(platform.surf, platform.rect)
  P1.update()
  P1.move()

  pg.display.update()
  FPS.tick(FRAMERATE)