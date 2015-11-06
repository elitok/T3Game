from t3game.field import *


class Playground:
    def __init__(self):
        print("Init Playground")
        self.playground = [[Field() for col in range(3)] for row in range(3)]

    def __str__(self):
        result = "+---+---+---+\n"
        for row in self.playground:
            for col in row:
                result += "| "+str(col.stone)+" "
            result += "|\n+---+---+---+\n"
        return result

    def set_stone_x(self, row, col):
        self.playground[row][col].set_x()
        return self.check_pos(row, col)

    def set_stone_o(self, row, col):
        self.playground[row][col].set_o()
        return self.check_pos(row, col)

    def check_pos(self, x, y):
        v = (self.playground[x][0].stone == self.playground[x][1].stone) \
            and (self.playground[x][1].stone == self.playground[x][2].stone) \
            and (self.playground[x][2].stone != Stone.EMPTY)
        h = (self.playground[0][y].stone == self.playground[1][y].stone) \
            and (self.playground[1][y].stone == self.playground[2][y].stone) \
            and (self.playground[2][y].stone != Stone.EMPTY)
        d1 = (self.playground[0][0].stone == self.playground[1][1].stone) \
             and (self.playground[1][1].stone == self.playground[2][2].stone) \
             and (self.playground[2][2].stone != Stone.EMPTY)
        d2 = (self.playground[2][0].stone == self.playground[1][1].stone) \
             and (self.playground[1][1].stone == self.playground[0][2].stone) \
             and (self.playground[0][2].stone != Stone.EMPTY)

        print(self.playground[x][0].stone, v, h, d1, d2)

        return v or h or d1 or d2
