import numpy as np
import copy

from typing import *


WIDTH, HEIGHT = 11, 11

BLACK = 1
WHITE = -1
EMPTY = 0
OUT = -2

BLACK_CHR = 'X'
WHITE_CHR = 'O'
EMPTY_CHR = '.'

RULE_GOMOKU = 1
RULE_RENJU = 2

GUI = 1
HEADLESS = 2

processes = 4


class MoveProbPair:
    def __init__(self, move: int, prob):
        self.move = move
        self.prob = prob


def move_int2xy(move_int: int) -> Tuple[int, int]:
    return move_int // WIDTH, move_int % WIDTH

def move_xy2int(x: int, y: int) -> int:
    return x * WIDTH + y

def vector(*args, dtype=None):
    if dtype is None:
        return np.array(args)
    return np.array(args, dtype=dtype)

directions = vector(
    (1, 1),
    (0, 1),
    (-1, 1),
    (-1, 0),
)

