from common import *
import config
from Gomoku.validation import ThreeChecker, FourChecker, FiveChecker, SixChecker


class Board:
    def __init__(self):
        self.array = np.ones((WIDTH, HEIGHT), dtype=np.int) * EMPTY

    def get(self, x, y):
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            return EMPTY
        return self.array[x, y]

    def set(self, x, y, player):
        self.array[x, y] = player

    def check_valid(self, x, y, player):
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            return False
        if self.get(x, y) != EMPTY:
            return False

        if player == BLACK and config.RULE == RULE_RENJU:
            lines = self._get_direction_lines(x, y, player)
            _six = SixChecker.check(lines, player)
            _five = FiveChecker.check(lines, player)
            if _five > _six:
                return True
            if _six:
                return False
            if ThreeChecker.check(lines, player) >= 2:
                return False
            if FourChecker.check(lines, player) >= 2:
                return False

        return True

    def check_winner(self, x, y) -> int:
        lines = self._get_direction_lines(x, y)
        if FiveChecker.check(lines, BLACK):
            return BLACK
        if FiveChecker.check(lines, WHITE):
            return WHITE
        return EMPTY

    def copy(self):
        return copy.deepcopy(self)

    def _get_direction_lines(self, x, y, put=None):
        origin = vector(x, y)
        lines = np.array([[self.get(*(i * direction + origin)) for i in range(-4, 5)] for direction in directions])
        if put is not None:
            for line in lines:
                line[4] = put
        return lines
