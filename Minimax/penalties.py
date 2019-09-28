import numpy as np


class PsqtBonus:
    pawns = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, -5, 10, 13, 21, 17, 6, -3],
        [-11, -10, 15, 22, 26, 28, 4, -24],
        [-9, -18, 8, 22, 33, 25, -4, -16],
        [6, -3, -10, 1, 12, 6, -12, 1],
        [-6, -8, 5, 11, -14, 0, -12, -14],
        [-10, 6, -5, -11, -2, -14, 12, -1],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ])

    knights = np.array([
        [-169, -96, -80, -79],
        [-79, -39, -24, -9],
        [-64, -20, 4, 19],
        [-28, 5, 41, 47],
        [-29, 13, 42, 52],
        [-11, 28, 63, 55],
        [-67, -21, 6, 37],
        [-200, -80, -53, -32]
    ])

    bishop = np.array([
        [-44, -4, -11, -28],
        [-18, 7, 14, 3],
        [-8, 24, -3, 15],
        [1, 8, 26, 37],
        [-7, 30, 23, 28],
        [-17, 4, -1, 8],
        [-21, -19, 10, -6],
        [-48, -3, -12, -25]
    ])

    rook = np.array([
        [-24, -13, -7, 2],
        [-18, -10, -5, 9],
        [-21, -7, 3, -1],
        [-13, -5, -4, -6],
        [-24, -12, -1, 6],
        [-24, -4, 4, 10],
        [-8, 6, 10, 12],
        [-22, -24, -6, 4]
    ])

    queen = np.array([
        [3, -5, -5, 4],
        [-3, 5, 8, 12],
        [-3, 6, 13, 7],
        [4, 5, 9, 8],
        [0, 14, 12, 5],
        [-4, 10, 6, 8],
        [-5, 6, 10, 8],
        [-2, -2, 1, -2]
    ])

    king = np.array([
        [272, 325, 273, 190],
        [277, 305, 241, 183],
        [198, 253, 168, 120],
        [169, 191, 136, 108],
        [145, 176, 112, 69],
        [122, 159, 85, 36],
        [87, 120, 64, 25],
        [64, 87, 49, 0]
    ])

    @staticmethod
    def get_score_by_piece(piece, x, y):
        score = 0

        if piece.islower():
            y = 7 - y

        if piece.lower() == 'p':
            score = PsqtBonus().pawns[y][min((7 - x), x)]
        if piece.lower() == 'b':
            score = PsqtBonus().bishop[y][min((7 - x), x)]
        if piece.lower() == 'n':
            score = PsqtBonus().knights[y][min((7 - x), x)]
        if piece.lower() == 'r':
            score = PsqtBonus().rook[y][min((7 - x), x)]
        if piece.lower() == 'q':
            score = PsqtBonus().queen[y][min((7 - x), x)]
        if piece.lower() == 'k':
            score = PsqtBonus().king[y][min((7 - x), x)]

        return score