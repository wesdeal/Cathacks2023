import pygame as pg
import sys, random
from pygame.locals import *
from config import *

class Coin(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__() 
        self.image = pg.image.load("CoinMoney.png")
        self.surf = pg.Surface((40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        