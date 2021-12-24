import pygame as pg
from random import randint


class Button:
    def __init__(self, screen):
        self.screen = screen
    def draw(self):
        self.pos = (randint(35, 605), randint(35, 325))
        self.posold = self.pos
        pg.draw.circle(self.screen, (255, 255, 255), self.pos, 35)
