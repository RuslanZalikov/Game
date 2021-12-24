import random

import pygame as pg
from button import Button
import time

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

def run():
    pg.init()
    screen = pg.display.set_mode((640, 360))
    screen.fill(black)
    pg.display.set_caption("Проверка реакции")
    pg.display.update()

    gamerun = True
    but = Button(screen)
    k = True

    while gamerun:
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                gamerun = False
            if k:
                time.sleep(random.randint(1, 5))
                start = time.time()
                but.draw()
                pg.display.update()
                k = False
            if event.type == pg.MOUSEBUTTONDOWN and (pg.mouse.get_pos()[0] - but.posold[0])**2 + (pg.mouse.get_pos()[1] - but.posold[1])**2 <= 1225:
                print("Nice:", int(1000*(time.time() - start)), "ms")
                pg.draw.circle(screen, green, but.posold, 35)
                pg.display.update()
                time.sleep(1)
                pg.draw.circle(screen, black, but.posold, 35)
                pg.display.update()
                k = True
            elif event.type == pg.MOUSEBUTTONDOWN and (pg.mouse.get_pos()[0] - but.posold[0])**2 + (pg.mouse.get_pos()[1] - but.posold[1])**2 > 1225:
                print("Lose")
                pg.draw.circle(screen, red, but.posold, 35)
                pg.display.update()
                time.sleep(1)
                pg.draw.circle(screen, black, but.posold, 35)
                pg.display.update()
                k = True

run()
