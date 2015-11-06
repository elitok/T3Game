"""

    This is an implementation of the known pen-and-paper game Tic Tac Toe.
    
    Specification:
        Playground
        +---+---+---+
        | O |   | X |
        +---+---+---+
        |   | O | X |
        +---+---+---+
        |   |   | X |
        +---+---+---+
        
        Field
        +---+    +---+    +---+
        | O |    | X |    |   |
        +---+ or +---+ or +---+
        
        Stone
        O --> CIRCLE (Player X)
        X --> CROSS (Player O)
        
        Game rules
         - in the beginning we have one Playground with 3x3 empty Fields and infinite O and X Stones
         - each player has to set one Stone
         - a player wins the game if he has 3 Stones in a row or diagonal
         - game is over if a player wins or no free Field remains 

    Author: Dr. Erhan Elitok, erhan@elitok.com
    
"""

from t3game.player import *
from t3game.playground import *
from t3game.stone import *

  
class Game(object):
    def __init__(self):
        self.playerX = Player("Erhan")
        self.playerO = Player("Volkan")
        self.playground = Playground()
        self.current_player = self.playerX
        self.winner = None
        print("\n------------------------------")
        print("\n  T I C       Start\n  A O         the\n  C   E       Game")
        print("\n------------------------------\n")

    def set_player_x(self, row, col):
        if self.playground.set_stone_x(col, row):
            if self.winner is None:
                self.winner = self.current_player
        self.current_player = self.playerO

    def set_player_o(self, row, col):
        if self.playground.set_stone_o(col, row):
            if self.winner is None:
                self.winner = self.current_player
        self.current_player = self.playerX

    def __str__(self):
        return str(self.playerO) + " vs. " + str(self.playerX)

