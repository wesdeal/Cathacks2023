import pygame as pg
import sys
from config import *
from pygame.locals import *

vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.surf = pg.Surface((30, 30))
        self.surf.fill(RED)
        self.rect = self.surf.get_rect()

        self.pos = vec((10, 385))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        
    def move(self):
        self.acc = vec(0,0)
        
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
        
        self.rect.midbottom = self.pos
    