import pygame as pg

class Move:
    def __init__(self, button):
        self.but = button
    def move(self):
        for i in range(5):
            self.but.pos[i] += self.but.direction

