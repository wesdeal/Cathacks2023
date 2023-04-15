import pygame as pg
import sys
from pygame.locals import *

vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.surf = pg.Surface((30, 30))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect()

        self.pos = vec((10, 385))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
    def move(self):
        self.acc = vec(0,0)
        
        self.acc.x += self.vel.x * -0.12
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

    def update(self):
        pressed_keys = pg.key.get_pressed()
                
        if pressed_keys[K_LEFT]:
            self.acc.x = -0.5
        if pressed_keys[K_RIGHT]:
            self.acc.x = 0.5  
        if self.pos.x > 400:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = 400
        
        self.rect.midbottom = self.pos
    