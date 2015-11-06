from tkinter import *


class Board(Canvas):
    STEP=100
    PAD = 20
    PADS= 5
    THICKNESS=6

    def __init__(self, master=None, game=None):
        Canvas.__init__(self, master=master, width=300, height=300)
        self.pack()

        self.game = game

        self.bind("<Button-1>", self.click)

        for y in range(3):
            for x in range(3):
                xa = x*self.STEP+self.PADS
                ya = y*self.STEP+self.PADS
                xb = x*self.STEP+self.STEP-self.PADS
                yb = y*self.STEP+self.STEP-self.PADS
                self.create_rectangle(xa, ya, xb, yb, outline='', fill='#eee', width=2)

        self.create_line(self.STEP, self.PADS, self.STEP, 3*self.STEP-self.PADS, fill='#000', width=2)
        self.create_line(self.STEP*2, self.PADS, self.STEP*2, 3*self.STEP-self.PADS, fill='#000', width=2)
        self.create_line(self.PADS, self.STEP, 3*self.STEP-self.PADS, self.STEP, fill='#000', width=2)
        self.create_line(self.PADS, self.STEP*2, 3*self.STEP-self.PADS, self.STEP*2, fill='#000', width=2)

    def cross(self, x, y):
        xa = x*self.STEP+self.PAD
        ya = y*self.STEP+self.STEP-self.PAD
        xb = x*self.STEP+self.STEP-self.PAD
        yb = y*self.STEP+self.PAD
        self.create_line(xa, ya, xb, yb, fill='#f00', width=self.THICKNESS)
        self.create_line(xa, yb, xb, ya, fill='#f00', width=self.THICKNESS)

    def circle(self, x, y):
        xa = x*self.STEP+self.PAD
        ya = y*self.STEP+self.PAD
        xb = (x+1)*self.STEP-self.PAD
        yb = (y+1)*self.STEP-self.PAD
        self.create_oval(xa, ya, xb, yb, outline='#00f', fill='', width=self.THICKNESS)

    def click(self, event):
        a = self.find_withtag(CURRENT)[0]-1
        if a in range(9):
            if self.game.current_player is self.game.playerX:
                self.cross(a % 3, a//3)
                self.game.set_player_x(a % 3, a//3)
            else:
                self.circle(a % 3, a//3)
                self.game.set_player_o(a % 3, a//3)
        if self.game.winner is not None:
            print("Winner is ", self.game.winner)