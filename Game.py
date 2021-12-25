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

    while gamerun:
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT: #выход
                gamerun = False
            if but.rg: #запускаем 5 точек
                but.rgp = 0
                time.sleep(random.randint(1, 5))
                but.draw()
                pg.display.update()
                but.rg = False
            if but.rg == False and event.type == pg.MOUSEBUTTONDOWN: #узнаем по каким попали и сколько раз нажали
                    but.exam(screen)
                    but.rgp += 1
            if but.rgp == 5: #как только нажали 5 раз, красим в красный оставшийся и выводим время, чутка ждем и очищаем
                    but.rg = True
                    but.colred(screen)
                    but.times()
                    time.sleep(3)
                    but.kill(screen)


run()
