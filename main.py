import pygame as pg
import sys
from pygame.locals import QUIT
pg.init()

WINDOWSIZE = (400,400)
DISPLAYSURF = pg.display.set_mode(WINDOWSIZE)
FPS = pg.time.Clock()
FRAMERATE = 60
BLACK = pg.Color(0, 0, 0)         
WHITE = pg.Color(255, 255, 255)   
GREY = pg.Color(128, 128, 128)   
RED = pg.Color(255, 0, 0)       

# Begin main game loop
while (True):
  # code codity code hot sausage and mustard
  for event in pg.event.get():
    if event.type == QUIT:
      sys.exit()
  pg.display.update()
  FPS.tick(FRAMERATE)