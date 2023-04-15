import pygame as pg
import sys, random
from pygame.locals import *
from config import *

class Coin(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__() 
        self.surf = pg.Surface((20, 20))
        self.surf.fill((212,175,55))
        self.rect = self.surf.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        