import tkinter as tk

from GUI.frame import BoardFrame
from GUI.Server import Server


class Game:
    def __init__(self, *args):
        self.server = Server(*args)

        self.window = tk.Tk()
        self.board_frame = BoardFrame(self.window)
        self.board_frame.pack()

    def run(self):
        self.window.mainloop()
