from common import *

from Gomoku.GameState import GameState


class Agent:
    manual = False

    def __init__(self, color):
        self.color = color

    def get_action(self, state: GameState) -> int:
        raise NotImplementedError('cannot get action')


class HumanPlayer(Agent):
    manual = True

    def get_action(self, state: GameState) -> int:
        state.show()
        while True:
            raw = input('action to move : ').lower().strip().replace(' ', '')
            try:
                x = ord(raw[0]) - 97
                y = int(raw[1:])
            except ValueError:
                print('invalid input format', raw)
                continue

            if x >= WIDTH or y >= HEIGHT or x < 0 or y < 0:
                print('invalid input range:', (x, y))
                continue

            if state.state.check_valid(x, y, self.color):
                return move_xy2int(x, y)
            else:
                print('invalid action:', (x, y))
                continue


