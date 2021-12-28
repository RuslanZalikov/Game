import pygame as pg
from button import Button
from controls import Events


black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

def run():
    pg.init()
    screen = pg.display.set_mode((640, 560))
    screen.fill(black)
    pg.display.set_caption("Проверка реакции")
    pg.display.update()
    butnum = 5
    font = pg.font.SysFont('microsofttaile', 32)
    but = Button(screen)

    while True:
        pg.display.update()
        Events(screen, but, butnum, font)
        but.update(screen, butnum)


run()