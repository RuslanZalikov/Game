from tkinter import *

class Setting:
    def __init__(self, window):
        self.window = window
        self.k = 0
    def Buttons(self):
        self.btn = []
        for self.k in range(10):
            self.btn.insert(self.k, Button(self.window, text=str(self.k)))
            self.btn[self.k].grid(column=self.k%5, row=self.k//5)
        self.window.mainloop()
        for i in range(10):
            self.btn[i] = Button(self.window, text=str(self.k), command=self.examBut)
    def examBut(self):
        print(self.k)