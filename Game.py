import pygame as pg
from tkinter import *
from button import ButtonPG
from controls import Events
from setting import Setting


black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

window = Tk()
window.title("Добро пожаловать!")

setting = Setting(window)
setting.Buttons()

def run():
    pg.init()
    screen = pg.display.set_mode((640, 560))
    screen.fill(black)
    pg.display.set_caption("Проверка реакции")
    pg.display.update()
    butnum = 5
    font = pg.font.SysFont('microsofttaile', 32)
    but = ButtonPG(screen)

    while True:
        pg.display.update()
        Events(screen, but, butnum, font)
        but.update(screen, butnum)


run()