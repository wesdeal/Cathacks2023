import pygame as pg
import sys
import random
from Platform import Platform
from coin import Coin 

from pygame.locals import *
from config import * # gets all setting constants
from player import Player

pg.init()
vec = pg.math.Vector2 # used for 2 dimensional movement calculations    

background = pg.image.load("PyBackground.jpg")

C1 = Coin(300,200)

FPS = pg.time.Clock()
DISPLAYSURF = pg.display.set_mode((WIDTH, HEIGHT))

P1 = Player(K_LEFT, K_RIGHT, "BlueRobot.png", (50, 50))
P2 = Player(K_a, K_d,"RedRobot.png", (WIDTH - 50, 50))

platforms = []
for i in range(random.randint(25,30)): #creates between 18 and 25
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

""" moving_plat = []
for x in range(random.randint(2,6)):
  j = random.randint(0,len(platforms)-1)
  moving_plat.append(platforms[j]) """

moving_platforms = random.sample(platforms, random.randint(2,6))
# Assign a non-zero velocity to each of the selected platforms
for platform in moving_platforms:
  platform.vel = x_speed
  

all_platforms = pg.sprite.Group()
#all_platforms.add(moving_plat)
all_platforms.add(platforms)

game_state = "start"

font = pg.font.SysFont('Arial', 40)
button = font.render('Begin (SPACE)', True, WHITE)
buttonrect = button.get_rect()
buttonrect.center = (WIDTH/2, 200)
blue = font.render('Blue uses Arrow Keys to move', True, BLUE)
bluerect = blue.get_rect()
bluerect.center = (WIDTH/2, 400)
red = font.render('Red uses WASD to move', True, RED)
redrect = red.get_rect()
redrect.center = (WIDTH/2, 600)
# Begin main game loop
while (True):
  # check events first
  for event in pg.event.get():
    if event.type == QUIT:
      sys.exit()
    elif event.type == KEYDOWN:
      if event.key == K_SPACE:
        game_state = "game"
      if event.key == K_UP:
        P1.jump(platforms)
      if event.key == K_w:
        P2.jump(platforms)
    
  
  if game_state == "start":
    DISPLAYSURF.blit(button, buttonrect)
    DISPLAYSURF.blit(blue, bluerect)
    DISPLAYSURF.blit(red, redrect)
    pg.display.update()

  else:
     # update the players

    if(C1.rect.x < 0 or C1.rect.x > WIDTH or C1.rect.y < 0 or C1.rect.y > HEIGHT):
      x = random.randint(20,WIDTH-20)
      y = random.randint(20,HEIGHT-20)


      C1 = Coin(x,y)

      

    if(C1.rect.colliderect(P1)):
              C1.rect.x = -1000
              C1.rect.y = -1000
              P1.score += 1
    if(C1.rect.colliderect(P2)):
              C1.rect.x = -1000
              C1.rect.y = -1000
              P2.score += 1

    
    # update the player
    P1.update(all_platforms)
    P2.update(all_platforms)
    
    # blank out the display surface in preparation for drawing new frame
    DISPLAYSURF.fill(GREY)
    DISPLAYSURF.blit(background,[0,0])

    # draws the platforms to screen
    for platform in platforms:  
        DISPLAYSURF.blit(platform.image, platform.rect)
    
    for g in range(0, len(platforms)):
      platforms[g].rect.x += platforms[g].vel
      DISPLAYSURF.blit(platforms[g].image, platforms[g].rect)
      if platforms[g].rect.right >= 1000 or platforms[g].rect.left <= 0:
        platforms[g].vel *= -1
        
    DISPLAYSURF.blit(P1.image,P1.rect)
    DISPLAYSURF.blit(P2.image, P2.rect)

    DISPLAYSURF.blit(C1.image,C1.rect)


    pg.display.update()
    FPS.tick(FRAMERATE)