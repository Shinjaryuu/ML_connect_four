import numpy as np
from itertools import groupby

class ConnectFourGame:
    """Play a connect 4 game on a board of 6 rows and 7 columns"""

    def __init__(self):
        """Initializes the game by setting the current player and
        setting up the board"""
        self.current_player = 1
        self.board = np.zeros((6,7))

    def _free_slot_in_column(self, column):
        """Returns the first free slot in the column"""
        filled = np.nonzero(self.board[:, column])[0]
        if  filled.size == 0:
            return 0
        else:
            return filled[-1] + 1
    def move(self, column):
        """Attempt to play in the given column. Returns true if it was
        successful, false if the column was full.
        """
        if self.board[5, column] != 0:
            return False
        else:
            first_empty = self._free_slot_in_column(column)
            self.board[first_empty, column] = self.current_player
            self.current_player = -self.current_player
            return True

    def print_board(self):
        """Print the board to standard output in a readable manner"""
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
        print(' 0123456 ')

    def connected_four(self):
        """Return 1 if player 1 won, -1 if player -1 won, 0 if nobody won.
        Assumes legal boardstate (at most one set of 4 connected)
        """
        #check rows
        for row in self.board:
            for p, g in groupby(row):
                if sum(1 for _ in g) > 3 and p!=0:
                    return p
        #check columns
        for col in self.board.T:
            for p, g in groupby(col):
                if sum(1 for _ in g) > 3 and p!=0:
                    return p
        #create and check diagonals
        diags = [self.board.diagonal(offset = i) for i in range(-2,4)]
        for diag in diags:
            for p, g in groupby(diag):
                if sum(1 for _ in g) > 3 and p!=0:
                    return p
        #create and check off diagonals
        off_diags = [self.board[::-1].diagonal(offset = i) for i in range(-2,4)]
        for diag in off_diags:
            for p, g in groupby(diag):
                if sum(1 for _ in g) > 3 and p!=0:
                    return p
        return 0
