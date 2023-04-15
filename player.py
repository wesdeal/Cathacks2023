import pygame as pg
import sys
from config import *
from pygame.locals import *

vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.width = 30
        self.height = 30
        self.surf = pg.Surface((self.width, self.height))
        self.surf.fill(RED)
        self.rect = self.surf.get_rect()
        self.jumping = False

        # self.pos corresponds to the center of the Player's rect
        self.pos = vec((50, 0))
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def move(self):
        self.acc = vec(0,GRAV) # By default it's going down
        
        pressed_keys = pg.key.get_pressed()
        if pressed_keys[K_LEFT]:
            self.acc.x = -0.5
        if pressed_keys[K_RIGHT]:
            self.acc.x = 0.5  

        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc # 0.5 is from kinematics eqn

        # quick way to allow screen wrapping
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        if self.pos.y > HEIGHT:
            self.pos.y = HEIGHT
        if self.pos.y < 0:
            self.pos.y = HEIGHT
        
        self.rect.center = self.pos
        
    # used to check for collisions with all the platforms
    def check_platform_collide(self, platforms):
        hits = pg.sprite.spritecollide(self, platforms, False)
        if hits:

          # Make sure we don't cancel the effect of jump() (only stop if there's already downward velocity)
          if self.vel.y > 0:
              self.pos.y = hits[0].rect.top - self.height / 2
              self.vel.y = 0

          # check to make sure we aren't hitting bottom of a platform
          if abs(hits[0].rect.bottom - self.rect.top) < 10:
            self.pos.y = hits[0].rect.bottom + self.height / 2
            self.vel.y = 0

          # check for player collision on the right of player
          if abs(hits[0].rect.left - self.rect.right) < 10:
            self.pos.x = hits[0].rect.left - self.width / 2
            self.vel.x = 0

          # check for player collision on the left ofnlayer
          if abs(hits[0].rect.right - self.rect.left) < 10:
            self.pos.x = hits[0].rect.right + self.width / 2
            self.vel.x = 0
            

    
    # Requires platform group to be passed in
    def jump(self, platforms):
      hits = pg.sprite.spritecollide(self, platforms, False)
      if hits: # only allow jumping if you're actually on a platform
        self.vel.y = -15
        self.jumping = True

  