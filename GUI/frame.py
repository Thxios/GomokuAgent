import tkinter as tk

from common import *
from Gomoku.Board import Board


class BoardCanvas(tk.Canvas):
    def __init__(self, master=None, height=0, width=0):
        tk.Canvas.__init__(self, master, height=height, width=width)
        self.turn = 1
        self.game = Board()
        self.draw_board()
        self.previous_action = []

    def draw_board(self):
        # 15 horizontal lines
        for i in range(15):
            start_pixel_x = (i + 1) * 30
            start_pixel_y = (0 + 1) * 30
            end_pixel_x = (i + 1) * 30
            end_pixel_y = (14 + 1) * 30
            self.create_line(start_pixel_x, start_pixel_y, end_pixel_x, end_pixel_y)

        # 15 vertical lines
        for j in range(15):
            start_pixel_x = (0 + 1) * 30
            start_pixel_y = (j + 1) * 30
            end_pixel_x = (14 + 1) * 30
            end_pixel_y = (j + 1) * 30
            self.create_line(start_pixel_x, start_pixel_y, end_pixel_x, end_pixel_y)

        # place a "star" to particular intersections
        self.draw_star(3, 3)
        self.draw_star(11, 3)
        self.draw_star(7, 7)
        self.draw_star(3, 11)
        self.draw_star(11, 11)

    def draw_star(self, x, y):
        start_pixel_x = (x + 1) * 30 - 2
        start_pixel_y = (y + 1) * 30 - 2
        end_pixel_x = (x + 1) * 30 + 2
        end_pixel_y = (y + 1) * 30 + 2

        self.create_oval(start_pixel_x, start_pixel_y, end_pixel_x, end_pixel_y, fill='black')

    def draw_stone(self, x, y, turn):
        inner_start_x = (x + 1) * 30 - 4
        inner_start_y = (y + 1) * 30 - 4
        inner_end_x = (x + 1) * 30 + 4
        inner_end_y = (y + 1) * 30 + 4

        outer_start_x = (x + 1) * 30 - 6
        outer_start_y = (y + 1) * 30 - 6
        outer_end_x = (x + 1) * 30 + 6
        outer_end_y = (y + 1) * 30 + 6

        start_pixel_x = (x + 1) * 30 - 10
        start_pixel_y = (y + 1) * 30 - 10
        end_pixel_x = (x + 1) * 30 + 10
        end_pixel_y = (y + 1) * 30 + 10

        if turn == BLACK:
            self.create_oval(start_pixel_x, start_pixel_y, end_pixel_x, end_pixel_y, fill='black')
            self.create_oval(outer_start_x, outer_start_y, outer_end_x, outer_end_y, fill='white')
            self.create_oval(inner_start_x, inner_start_y, inner_end_x, inner_end_y, fill='black')
        elif turn == WHITE:
            self.create_oval(start_pixel_x, start_pixel_y, end_pixel_x, end_pixel_y, fill='white')
            self.create_oval(outer_start_x, outer_start_y, outer_end_x, outer_end_y, fill='black')
            self.create_oval(inner_start_x, inner_start_y, inner_end_x, inner_end_y, fill='white')

    def draw_prev_stone(self, x, y, turn):
        start_pixel_x = (x + 1) * 30 - 10
        start_pixel_y = (y + 1) * 30 - 10
        end_pixel_x = (x + 1) * 30 + 10
        end_pixel_y = (y + 1) * 30 + 10

        if turn == BLACK:
            self.create_oval(start_pixel_x, start_pixel_y, end_pixel_x, end_pixel_y, fill='black')
        elif turn == WHITE:
            self.create_oval(start_pixel_x, start_pixel_y, end_pixel_x, end_pixel_y, fill='white')

    def put_stone(self, x, y, turn):
        if not self.game.check_valid(x, y, turn):
            print('invalid action')
            return False

        self.game.set(x, y, turn)
        self.draw_stone(x, y, turn)

        if len(self.previous_action):
            pre_x, pre_y, pre_turn = self.previous_action[-1]
            self.draw_prev_stone(pre_x, pre_y, pre_turn)

        self.previous_action.append((x, y, turn))
        return True

    def on_board_clicked(self, event):
        clicked_x, clicked_y = (event.x - 15) // 30, (event.y - 15) // 30
        error_x, error_y = event.x - (clicked_x + 1) * 30, event.y - (clicked_y + 1) * 30
        if abs(error_x) > 10 or abs(error_y) > 10:
            return 0

        if self.put_stone(clicked_x, clicked_y, self.turn):
            self.change_turn()

    def change_turn(self):
        if self.turn == BLACK:
            self.turn = WHITE
        elif self.turn == WHITE:
            self.turn = BLACK


class BoardFrame(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.board_canvas = BoardCanvas(height=550, width=480)
        self.board_canvas.bind('<Button-1>', self.board_canvas.on_board_clicked)
        self.board_canvas.pack()
