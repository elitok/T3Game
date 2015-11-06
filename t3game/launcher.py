from t3game.board import *
from t3game.game import *
from tkinter import font
from threading import Timer


class Launcher(Frame):
    def __init__(self, master=None, game=None):
        Frame.__init__(self, master)
        self.pack()

        self.game = game

        self.banner = Label(self)
        self.banner.config(text=str(self.game), height=2, font=font.Font(family='Helvetica', size=16, weight='bold'))
        self.banner.pack(side="top")

        self.board = Board(self, self.game)

        self.gameover = Timer(0.1, self.game_over)
        self.gameover.run()

    def game_over(self):
        if self.game.winner is not None:
            print("GAME OVER")
        else:
            print("Continue to play")


TITLE = "Tic Tac Toe"

root = Tk()
root.title(TITLE)
t3 = Launcher(master=root, game=Game())

t3.mainloop()