import pygame as pg
from config import *

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.surf = pg.Surface((50, 10))
        self.surf.fill(BLACK)
        self.rect = self.surf.get_rect()
        self.rect.x = x
        self.rect.y = y




        

        