from common import *


class _LineChecker:
    def __init__(self, multiply, compare):
        self.mul = multiply
        self.comp = compare

        self._str = ''
        for i in range(9):
            if self.mul[i] == 0:
                self._str += '?'
            else:
                if self.comp[i] == 0:
                    self._str += '.'
                elif self.comp[i] == 1:
                    self._str += 'X'
        #     self._str += ' '
        # self._str = self._str[:-1]

    def __str__(self):
        return self._str

    def check(self, line: np.ndarray, player: int):
        # print(line * self.mul == self.comp)
        # print(line * self.mul)
        return np.all(line * self.mul == self.comp * player) or \
               np.all(np.flip(line) * self.mul == self.comp * player)

    @staticmethod
    def from_str(pattern):
        mul = np.zeros((9,), dtype=np.int)
        comp = np.zeros((9,), dtype=np.int)
        for i in range(9):
            if pattern[i] != '?':
                mul[i] = 1
                if pattern[i] == 'X':
                    comp[i] = 1
        return _LineChecker(mul, comp)


class _Checker:
    checker: List[_LineChecker]

    def check(self, lines, player):
        cnt = 0
        for line in lines:
            for checker in self.checker:
                if checker.check(line, player):
                    # print(checker)
                    cnt += 1
                    break
        return cnt


class ThreeChecker(_Checker):
    checker = [
        _LineChecker.from_str('???.XX.X.'),
        _LineChecker.from_str('???.X.XX.'),
        _LineChecker.from_str('???.XXX..'),
        _LineChecker.from_str('??..XXX.?'),

        _LineChecker.from_str('??.XXX..?'),
        _LineChecker.from_str('??.XX.X.?'),
        _LineChecker.from_str('?.X.XX.??'),
    ]


class FourChecker(_Checker):
    checker = [
        _LineChecker.from_str('???.XXXX?'),
        _LineChecker.from_str('??.XXXX??'),
        _LineChecker.from_str('????XXXX.'),
        _LineChecker.from_str('???XXXX.?'),

        _LineChecker.from_str('????XX.XX'),
        _LineChecker.from_str('???XX.XX?'),
    ]


class FiveChecker(_Checker):
    checker = [
        _LineChecker.from_str('????XXXXX'),
        _LineChecker.from_str('???XXXXX?'),
        _LineChecker.from_str('??XXXXX??'),
    ]


class SixChecker(_Checker):
    checker = [
        _LineChecker.from_str('???XXXXXX'),
        _LineChecker.from_str('??XXXXXX?'),
    ]


ThreeChecker = ThreeChecker()
FourChecker = FourChecker()
FiveChecker = FiveChecker()
SixChecker = SixChecker()
