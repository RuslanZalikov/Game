import pygame as pg
from random import randint, randrange
import time

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

class ButtonPG: # speed = 1
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pg.image.load('images/pixil-frame-0.png')
        self.image2 = pg.image.load('images/pixil-frame-0 (1).png')
        self.image3 = pg.image.load('images/pixil-frame-0 (2).png')
        self.image_rect = self.image.get_rect()
        self.image2_rect = self.image2.get_rect()
        self.image3_rect = self.image3.get_rect()
        self.rg = True
        self.rgp = 0
        self.pos = []
        self.ftime = []
        self.ftime = []
        self.direction = []
        self.flag = []
        self.y = 380
        self.x = 15
        """self.boom = [[],[],[],[],[],[]]
        for i in range():
            self.boom[i] = pg.image.load(self.boom[i])
            self.boom[i] = self.boom[i].get_rect()"""
    def draw(self, butnum): #функция для рисования 5 точек и проверка чтобы не накладывались #speed = 2n
        self.flag.clear()
        for i in range(butnum): #speed = n
            self.pos.insert(i, [randint(i*(640//butnum) + 50, (i+1)*(640//butnum) - 50), randint(50,310)])
            self.direction.insert(i, [randrange(-1,1,2), randrange(-1,1,2)])
            self.flag.insert(i, False) #если true то попал
        self.start = time.time()
        for i in range(butnum): #рисуем 5 белых точек #speed = n
            self.image_rect.center = self.pos[i]
            self.screen.blit(self.image, self.image_rect)
            pg.display.update()
    def exam(self, butnum): #проверка на попадание speed = n
        for i in range(butnum): #после нажатия проверят каждую точку, попал ли speed = n
            r = (pg.mouse.get_pos()[0] - self.pos[i][0])**2 + (pg.mouse.get_pos()[1] - self.pos[i][1])**2
            if r <= 2500:
                self.flag[i] = True
                self.image2_rect.center = self.pos[i]
                self.screen.blit(self.image2, self.image2_rect)
                pg.display.update()
                pg.time.delay(200)
                self.pos[i] = [ -10000, -10000]
        self.time = time.time() - self.start
    def colred(self, butnum): #закрашивание всех непопавших точек в красный speed = n
        for i in range(butnum):
            if self.flag[i] == False:
                self.image3_rect.center = self.pos[i]
                self.screen.blit(self.image3, self.image3_rect)
        pg.display.update()
    def kill(self, screen,butnum): #очищение #speed = n
        for i in range(butnum):
            pg.draw.circle(screen, black, self.pos[i], 50)
            self.pos[i] = [-10000, -10000]
        pg.display.update()
    def times(self, screen, font): #вывод времени #speed = n
        if False in self.flag:
            text = font.render("Lose: " + str(int(1000 * self.time)) + "ms", 1, white)
            print("Lose: ", int(1000 * self.time), "ms")
        else:
            text = font.render("Nice: " + str(int(1000 * self.time)) + "ms", 1, white)
            print("Nice: ", int(1000 * self.time), "ms")
        if self.y >= 530:
            self.x += 175
            self.y = 380
        if self.x > 190:
            self.x = 15
            self.screen.fill(black)
        screen.blit(text, (self.x, self.y))
        pg.display.update()
        self.y += 34
    def update(self, screen, butnum): #обновление движения #speed = n**2
        pg.draw.rect(screen, black, ((0,0), (640,360)))
        pg.draw.rect(screen, white, (0, 0, 640, 360), 1)
        pg.draw.rect(screen, white, (0, 360, 640, 200), 1)
        pg.draw.rect(screen, white, (175, 360, 175, 200), 1)
        for i in range(butnum):
            if self.pos[i][0] + 50 >= 640 or self.pos[i][0] - 50 <= 0: #проверка каждой точки на пересечение с границей
                self.direction[i][0] *= -1
            if self.pos[i][1] + 50 >= 360 or self.pos[i][1] - 50 <= 0:
                self.direction[i][1] *= -1
            self.pos[i][0] += self.direction[i][0]
            self.pos[i][1] += self.direction[i][1]
            j = i
            while j < butnum: #проверка точек на пересечение друг с другом
                r = (self.pos[i][0] - self.pos[j][0]) ** 2 + (self.pos[i][1] - self.pos[j][1]) ** 2
                if r <= 10000 and r != 0:
                    self.direction[i][0] *= -1
                    self.direction[i][1] *= -1
                    self.direction[j][0] *= -1
                    self.direction[j][1] *= -1
                j += 1
            self.pos[i][0] += self.direction[i][0]
            self.pos[i][1] += self.direction[i][1]
            self.image_rect.center = self.pos[i]
            if self.flag[i] == False:
                self.screen.blit(self.image, self.image_rect)




