import tkinter as tk
from GUI.frame import BoardFrame


class MyTk(tk.Tk):
    def __init__(self):
        super().__init__()
        self.cnt = 0

    def mainloop(self, n=0):
        print(self.cnt)
        self.cnt += 1


if __name__ == '__main__':
    window = tk.Tk()
    # window = MyTk()
    board = BoardFrame(window)
    board.pack()
    window.mainloop()
