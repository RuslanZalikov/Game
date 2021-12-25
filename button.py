import pygame as pg
from random import randint
import time

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

class Button:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.rg = True
        self.rgp = 0
    def draw(self): #функция для рисования 5 точек и проверка чтобы не накладывались
        self.pos = [[-35, -35], [-35, -35], [-35, -35], [-35, -35], [-35, -35]] #координаты точек
        self.ftime = [[-35, -35], [-35, -35], [-35, -35], [-35, -35], [-35, -35]] #временный список чтобы проверять накладку точек друг на друга
        self.flag = [False, False, False, False, False] #если true то попал
        self.start = time.time()
        z = 0
        while z < 25: #проверка накладности, точек 5 и при проверке каждой с каждой 5**2 = 25
            for k in range(5):
                l = (randint(35, 605), randint(35, 325))
                self.ftime[k] = l
            for k in range(5):
                for j in range(5):
                    if (self.ftime[k][0] - self.ftime[j][0])**2 + (self.ftime[k][1] - self.ftime[j][1])**2 > 4900 or (self.ftime[k][0] - self.ftime[j][0])**2 + (self.ftime[k][1] - self.ftime[j][1])**2 == 0:
                        z += 1
                    else:
                        z = 0
        self.pos = self.ftime
        for i in range(5): #рисуем 5 белых точек
            pg.draw.circle(self.screen, white, self.pos[i], 35)
    def exam(self, screen): #проверка на попадание
        for i in range(5): #после нажатия проверят каждую точку, попал ли
            r = (pg.mouse.get_pos()[0] - self.pos[i][0])**2 + (pg.mouse.get_pos()[1] - self.pos[i][1])**2
            if r <= 1225:
                self.flag[i] = True
                pg.draw.circle(screen, green, self.pos[i], 35)
                pg.display.update()
        self.time = time.time() - self.start
    def colred(self, screen): #закрашивание всех непопавших точек в красный
        for i in range(5):
            if self.flag[i] == False:
                pg.draw.circle(screen, red, self.pos[i], 35)
        pg.display.update()
    def kill(self, screen): #очищение
        for i in range(5):
            pg.draw.circle(screen, black, self.pos[i], 35)
        pg.display.update()
    def times(self): #вывод времени
        if False in self.flag:
            print("Lose: ", int(1000 * self.time), "ms")
        else:
            print("Nice: ", int(1000 * self.time), "ms")



