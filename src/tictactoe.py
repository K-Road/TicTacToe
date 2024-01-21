import tkinter as tk
from PIL import Image, ImageTk
from graphics import Line, Point
from cell import Cell
import time

class TicTacToe:
    def __init__(self,x1,y1,cell_size_x,cell_size_y,window=None):
        self._x1 = x1
        self._y1 = y1
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = window

        self._num_rows = 3
        self._num_cols = 3
        self._cells = []

        #image load
        self.image_o = self._load_image("./images/o.png")
        self.image_x = self._load_image("./images/x.jpg")
        self.image_x2 = self._load_image("./images/x2.jpg")

        
        #create game board
        self._create_board()
        #create cells here
        #2D array 3 x 3 cells
        self._create_cells()

    def _create_board(self):
        width = self._win.width
        x1 = int(width / 3)
        x2 = x1 * 2
        height = self._win.height
        y1 = int( height / 3)
        y2 = y1 * 2
        line_width = (width / 300) *3

       # line = Line(Point(x1,0),Point(x1,height))
        #self._win.draw_line(Line(Point(x1,0),Point(x1,height)),line_width)
        # self._win.draw_line(Line(Point(x2,0),Point(x2,height)),line_width)

        # self._win.draw_line(Line(Point(0,y1),Point(width,y1)),line_width)
        # self._win.draw_line(Line(Point(0,y2),Point(width,y2)),line_width)
        radius = line_width/2
        self._win.draw_rounded_line(Line(Point(x1,0+(line_width*3)),Point(x1,height-(line_width*3))), line_width,radius=line_width/2)
        self._win.draw_rounded_line(Line(Point(x2,0+(line_width*3)),Point(x2,height-(line_width*3))), line_width,radius=line_width/2)
        self._win.draw_rounded_line(Line(Point(0+(line_width*3),y1),Point(width-(line_width*3),y1)), line_width,radius=line_width/2)
        self._win.draw_rounded_line(Line(Point(0+(line_width*3),y2),Point(width-(line_width*3),y2)), line_width,radius=line_width/2)


        p1 = Point(10, 10)
        p2 = Point(400, 400)
        line = Line(p1, p2)
        self._win.draw_rounded_line(line,line_width=5, radius=line_width/2, fill_colour="red")
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

    def _load_image(self,filename,x=50,y=50):
        image = Image.open(filename)
        image = image.resize((x,y), resample=Image.LANCZOS)
        return ImageTk.PhotoImage(image)
