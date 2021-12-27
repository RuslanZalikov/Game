import pygame as pg
import time, random

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)


def run():
    pg.init()
    screen = pg.display.set_mode((640, 360))
    pg.display.set_caption("Test")
    pg.display.update()
    runGame = True
    while runGame:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                runGame = False


run()