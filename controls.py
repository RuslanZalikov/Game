import sys
import pygame as pg
import time, random

def Events(screen, but):
    for event in pg.event.get():
        if event.type == pg.QUIT:  # выход
            sys.exit()
        if but.rg:  # запускаем 5 точек
            but.rgp = 0
            time.sleep(random.randint(1, 5))
            but.draw()
            pg.display.update()
            but.rg = False
        if but.rg == False and event.type == pg.MOUSEBUTTONDOWN:  # узнаем по каким попали и сколько раз нажали
            but.exam(screen)
            but.rgp += 1
        if but.rgp == 5:  # как только нажали 5 раз, красим в красный оставшийся и выводим время, чутка ждем и очищаем
            but.rg = True
            but.colred(screen)
            but.times()
            time.sleep(3)
            but.kill(screen)