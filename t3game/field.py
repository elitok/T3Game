from t3game.stone import *


class Field(object):
    def __init__(self, stone=Stone.EMPTY):
        self.stone = stone

    def set_o(self):
        self.stone = Stone.CIRCLE

    def set_x(self):
        self.stone = Stone.CROSS

    def __str__(self):
        return self.stone
