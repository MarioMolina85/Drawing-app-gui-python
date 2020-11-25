#creacion de un paint
from tkinter import *

class Paint:
    def __init__(self):
        self.root=Tk()
        self.root.title("Paint Windows")
        self.root.resizable(0,0)
        self.root.geometry("700x600")
        #trabajando con canvas
        self.w=600
        self.h=400
        self.my_canva=Canvas(self.root, width=self.w,height=self.h, bg="white")
        self.my_canva.pack(pady=20)
        self.x1=0
        self.y1=100

        self.x2=300
        self.y2=100
        #self.my_canva.create_line(self.x1, self.y1, self.x2, self.y2, fill="red")
        #self.my_canva.create_line(150, 100, 100, 300, fill="green")
        self.my_canva.bind('<B1-Motion>', self.paint)
        self.root.mainloop()

    def paint(self, e):
        x1=e.x
        y1=e.y
        x2 = e.x+1
        y2= e.y+1
        self.my_canva.create_line(x1, y1, x2, y2, fill="red")
if __name__ == '__main__':
    apppaint=Paint()

