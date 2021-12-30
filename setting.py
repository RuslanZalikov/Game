from tkinter import *

class Setting:
    def __init__(self, window):
        self.window = window
        self.k = 0
    def Buttons(self):
        self.btn = []
        for i in range(10):
            self.k += 1
            self.btn.insert(i, Button(self.window, text=str(i), command=self.examBut))
            self.btn[i].grid(column=i%5, row=i//5)
        self.window.mainloop()
    def examBut(self):
        print(self.k)