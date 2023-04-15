import pygame as pg
import sys
import random
from Platform import Platform

from pygame.locals import *
from config import * # gets all setting constants
from player import Player


""" def movingRect():
  moving_plat.x += x_speed
  pg.draw.rect(DISPLAYSURF, (0,255,0), moving_plat) """

pg.init()
vec = pg.math.Vector2 # used for 2 dimensional movement calculations     

FPS = pg.time.Clock()
DISPLAYSURF = pg.display.set_mode((WIDTH, HEIGHT))

P1 = Player()




platforms = []
#def PlatformGen():
for i in range(random.randint(20,25)): #creates between 18 and 25
  while True:
    x = random.randint(15,985)
    y = random.randint(75,775)
    new_platform = Platform(x,y)

    overlap = False
    for platform in platforms:
      if (abs(x - platform.rect.x) < PLAT_PADDING_X and abs(y - platform.rect.y) < PLAT_PADDING_Y):
        overlap = True
        break

    if not overlap:
      platforms.append(new_platform)
      break

moving_plat = []
for x in range(random.randint(2,6)):
  j = random.randint(0,len(platforms)-1)
  moving_plat.append(platforms[j])

#check if any moving rect hits static platform, if so, delete static plat if poss

#new_platforms = []
# Begin main game loop
while (True):
  # check events first
  for event in pg.event.get():
    if event.type == QUIT:
      sys.exit()
  
  # blank out the display surface in preparation for drawing new frame
  DISPLAYSURF.fill(WHITE)
  DISPLAYSURF.blit(P1.surf,P1.rect)

  
  #new_platforms = []

  """ for i in range(len(platforms)):
    for j in range(len(moving_plat)):
      if abs(moving_plat[j].rect.y-platforms[i].rect.y) > 30:
        break #skips adding this platform to new platform array
      else:
        new_platforms.append(moving_plat[j]) """

  for platform in platforms:  
      DISPLAYSURF.blit(platform.surf, platform.rect)
  
  #platforms = new_platforms #updates old platforms array to only oens that dont collide
  #for platform in platforms:  
  #    DISPLAYSURF.blit(platform.surf, platform.rect)

  

  for g in range(0, len(moving_plat)):
    moving_plat[g].rect.x += moving_plat[g].vel
    DISPLAYSURF.blit(moving_plat[g].surf, moving_plat[g].rect)
    if moving_plat[g].rect.right >= 1000 or moving_plat[g].rect.left <= 0:
      moving_plat[g].vel *= -1


  
  #coinPlatform = platforms[random.randint(0,len(platforms))]

  #movingRect()
  P1.update()
  P1.move()

  pg.display.update()
  FPS.tick(FRAMERATE)