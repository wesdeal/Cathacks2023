import pygame as pg
import sys
from player import Player
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

HEIGHT = 450
WIDTH = 400
displaysurface = pg.display.set_mode((WIDTH, HEIGHT))

P1 = Player()

# Begin main game loop
while (True):
  # code codity code hot sausage and mustard
  for event in pg.event.get():
    if event.type == QUIT:
      sys.exit()
  displaysurface.fill((0,0,0))
  displaysurface.blit(P1.surf,P1.rect)
  P1.update()
  P1.move()
  pg.display.update()
  FPS.tick(FRAMERATE)