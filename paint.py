#creacion de un paint
from tkinter import *

class Paint:
    def __init__(self):
        self.root=Tk()
        self.root.title("Paint Windows")
        self.root.resizable(0,0)
        self.root.geometry("800x800")
        self.root.mainloop()
if __name__ == '__main__':
    apppaint=Paint()

