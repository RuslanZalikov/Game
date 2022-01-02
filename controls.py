import sys
import pygame as pg
import time, random

def Events(screen, but, butnum, font):
    for event in pg.event.get():
        if event.type == pg.QUIT:  # выход
            sys.exit()
        if but.rg:  # запускаем 5 точек
            but.rgp = 0
            pg.time.delay(random.randint(1, 2))
            but.draw(butnum) #speed = 2n
            pg.display.update()
            but.rg = False
        if but.rg == False and event.type == pg.MOUSEBUTTONDOWN:  # узнаем по каким попали и сколько раз нажали
            but.exam(butnum) #speed = n
            but.rgp += 1
        if but.rgp == butnum:  # как только нажали 5 раз, красим в красный оставшийся и выводим время, чутка ждем и очищаем
            but.rg = True
            but.colred(butnum) #speed = n
            but.times(screen, font) #speed = n
            pg.time.delay(2000)
            but.kill(screen,butnum) #speed = n