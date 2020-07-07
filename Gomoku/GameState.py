from common import *

from Gomoku.Board import Board


class GameState:
    def __init__(self):
        self.current_player = BLACK
        self.available = set(range(WIDTH * HEIGHT))
        self.moved: List[int] = []
        self.state = Board()
        self.last_move: int = None

    def copy(self):
        return copy.deepcopy(self)

    def is_empty(self) -> bool:
        return len(self.moved) == 0

    def play(self, move: int) -> bool:
        if not self.state.check_valid(*move_int2xy(move), self.current_player):
            return False

        self.state.set(*move_int2xy(move), self.current_player)
        self.available.remove(move)
        self.moved.append(move)
        self.last_move = move
        self.change_player()

        return True

    def undo(self) -> bool:
        if len(self.moved) == 0:
            return False

        self.state.set(*move_int2xy(self.last_move), EMPTY)
        self.available.add(self.last_move)
        self.moved.pop()
        if len(self.moved) == 0:
            self.last_move = EMPTY
        else:
            self.last_move = self.moved[-1]
        self.change_player()

        return True

    def change_player(self):
        self.current_player = WHITE if self.current_player == BLACK else BLACK

    def check_winner(self) -> Tuple[bool, int]:
        # must be called right after every moves
        winner = self.state.check_winner(*move_int2xy(self.last_move))
        if len(self.available) == 0 and winner == EMPTY:
            return True, EMPTY
        if winner == BLACK:
            return True, BLACK
        if winner == WHITE:
            return True, WHITE
        return False, EMPTY

    def show(self):
        char = {
            BLACK: 'X',
            WHITE: 'O',
            EMPTY: '.'
        }

        print('   ', end='')
        for x in range(WIDTH):
            print(chr(x + 97), end=' ')
        print('\n', end='')
        for y in range(HEIGHT):
            if y > 9:
                print(y, end=' ')
            else:
                print(y, end='  ')
            for x in range(WIDTH):
                print(char[self.state.get(x, y)], end=' ')
            print('\n', end='')


