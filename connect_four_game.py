import numpy as np
from itertools import groupby
# muhahaha der uberTroll was here!
#Nein gar nicht
class connect_four_game:

    def __init__(self):
        self.current_player = 1
        self.board = np.zeros((6,7))

    def move(self, column):
        if self.board[5, column] != 0:
            return False
        else:
            filled = np.nonzero(self.board[:, column])[0]
            if  filled.size == 0:
                first_empty = 0
            else:
                first_empty = filled[-1] + 1
            self.board[first_empty, column] = self.current_player
            self.current_player = -self.current_player
            return True

    def print_board(self):
        for row in self.board[::-1, :]:
            line = '|'
            for el in row:
                if el == 0:
                    line += ' '
                elif el == 1:
                    line += 'X'
                else:
                    line += 'O'
            line += '|'
            print(line)

    def connected_four(self):
        """Return 1 if player 1 won, -1 if player -1 won, 0 if nobody won
        """
        #check rows
        for row in self.board:
            for p, g in groupby(row):
                if sum(1 for _ in g) > 3 and p!=0:
                    return p
        for col in self.board.T:
            for p, g in groupby(col):
                if sum(1 for _ in g) > 3 and p!=0:
                    return p
        diags = [self.board.diagonal(offset = i) for i in range(-2,4)]
        for diag in diags:
            for p, g in groupby(diag):
                if sum(1 for _ in g) > 3 and p!=0:
                    return p
        off_diags = [self.board[::-1].diagonal(offset = i) for i in range(-2,4)]
        for diag in off_diags:
            for p, g in groupby(diag):
                if sum(1 for _ in g) > 3 and p!=0:
                    return p
        return 0

class test:
    pass

g = connect_four_game()
while True:
    g.print_board()
    print("Current player: {}".format(g.current_player))
    next_move = int(input())
    if not g.move(next_move):
        print("Dafaq?")
    else:
        winner = g.connected_four()
        if winner != 0:
            print("Congratz! Player {} won!".format(winner))
            break
