import tkinter as tk
from graphics import Window, Line, Point
from cell import Cell
from tictactoe import TicTacToe

def main():
    win = Window(300,300)
    margin = 1
    line_width = 3

    #dont need these here. will revise
    cell_size_x = ((win.width) / 3) - (line_width)
    cell_size_y = ((win.height) / 3) - (line_width)


    t = TicTacToe(0,0,cell_size_x,cell_size_y,win)
    t.turn("player1")
    win.wait_for_close()

if __name__ == "__main__":
    main()