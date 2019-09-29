from Minimax.state import State
from math import inf as infinite

EMPTY_STATE = '.'

MINIMAZING_PLAYER = -1
MAXIMAZING_PLAYER = 1

evaluated_states = 0

class Minimax:

    def __init__(self, depth):
        self.depth = depth
        self.evaluated_states = 0

    def get_minimax_move(self, chessboard, player):
        initial_state = State(chessboard.board)

        best_state, _ = Minimax.search(initial_state, self.depth, player, -infinite, infinite)

        if best_state:
            global evaluated_states
            next_move = best_state.initial_y, best_state.initial_x, best_state.final_y, best_state.final_x, evaluated_states

            return next_move
        else:
            for move in initial_state.children:
                print("Score: {}".format(move.score))
            raise Exception("Sorry but we could'n find the best move for this case!")

    @staticmethod
    def search(state, depth, player, alpha, beta):
        global evaluated_states

        if depth == 0:
            return '', state.get_score()

        state.generate_children(player)
        best_value = -infinite if player == MAXIMAZING_PLAYER else infinite

        for child in state.children:
            eval_state, eval_value = Minimax.search(child, depth-1, -player, alpha, beta)

            evaluated_states += 1
            if player == MAXIMAZING_PLAYER and best_value < eval_value:
                best_value = eval_value
                best_state = child
                alpha = max(alpha, best_value)
                if beta <= alpha:
                    break

            elif player == MINIMAZING_PLAYER and best_value > eval_value:
                best_value = eval_value
                best_state = child
                beta = min(beta, best_value)
                if beta <= alpha:
                    break

        return best_state, best_value
