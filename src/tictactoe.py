import tkinter as tk
from PIL import Image, ImageTk
from graphics import Line, Point
from cell import Cell
import time

class TicTacToe:
    def __init__(self,root):
        self.root = root
        self.root.title("Tic Tac Toe")

        #image load
        self.image_o = self._load_image("./images/o.png")
        self.image_x = self._load_image("./images/x.jpg")
        self.image_x2 = self._load_image("./images/x2.jpg")

        #create cells here
        #2D array 3 x 3 cells

    #Create cells for game
    def _create_cells(self):
        pass

    def _draw_cells(self, i, j):
        pass


    #reset to start over
    def _reset_cells(self):
        pass

    def _animate(self):
        pass

    def _load_image(self,filename):
        image = Image.open(filename)
        image = image.resize((50,50), Image.ANTIALIAS)
        return ImageTk.PhotoImage(image)
