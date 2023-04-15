import pygame as pg
import random
from config import *

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.surf = pg.Surface((random.randint(70, 130), 10))
        self.surf.fill(BLACK)
        self.rect = self.surf.get_rect(topleft=(x, y))
        self.rect.x = x
        self.rect.y = y
        self.vel = x_speed