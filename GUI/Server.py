from common import *

from Gomoku.Player import HumanPlayer
from Gomoku.GameState import GameState
from MCTS.Agent import MCTSAgent


class Server:

    def __init__(
            self,
            player1: Union[HumanPlayer, MCTSAgent],
            player2: Union[HumanPlayer, MCTSAgent],
            mode=GUI
    ):
        self.board = GameState()

        self.player1 = player1
        self.player2 = player2
        self.mode = mode

        if self.player1.color == self.player2.color:
            raise ValueError('two players have same color')

        self.player = {
            self.player1.color: self.player1,
            self.player2.color: self.player2
        }

        self.playing = False
        self.winner = EMPTY

    @property
    def current_player(self):
        return self.player[self.board.current_player]

    @property
    def is_human_turn(self):
        return self.current_player.manual

    def start_game(self):
        self.playing = True

        if self.mode == HEADLESS:
            self._headless_play()
        elif self.mode == GUI:
            self._gui_play()

    def headless_player_turn(self):
        action = self.current_player.get_action(self.board)
        self.board.play(action)

        is_end, winner = self.board.check_winner()
        if is_end:
            self.playing = False
            self.winner = winner

    def gui_human_turn(self, move):
        if not self.is_human_turn:
            return

        valid = self.board.play(move)
        if not valid:
            print('Invalid move')
            return

        is_end, winner = self.board.check_winner()
        if is_end:
            self.playing = False
            self.winner = winner

        if not self.is_human_turn:
            self.headless_player_turn()

    def _headless_play(self):
        while self.playing:
            self.headless_player_turn()

    def _gui_play(self):
        if self.is_human_turn:
            return
        else:
            self.headless_player_turn()




