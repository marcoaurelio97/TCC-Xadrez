from chessboard import *
from functions import *
from minimax import *
import time


class Game:
    chessboard = None
    black_score = None
    white_score = None

    def __init__(self):
        self.chessboard = Chessboard()
        self.black_score = 0
        self.white_score = 0

    def run(self):
        while not self.endgame():
            self.chessboard.print_board()
            y_curr, x_curr, y_next, x_next = get_player_move()
            self.chessboard.move(x_curr, y_curr, x_next, y_next)

            self.chessboard.print_board()
            y_curr, x_curr, y_next, x_next = Minimax().get_minimax_move(self.chessboard)
            self.chessboard.move(x_curr, y_curr, x_next, y_next)

    def endgame(self):
        return False
