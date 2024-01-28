import tkinter as tk
from PIL import Image, ImageTk
from graphics import Line, Point
from cell import Cell
import time

class TicTacToe:
    def __init__(self,x1,y1,cell_size_x,cell_size_y,window=None):
        self._x1 = x1
        self._y1 = y1
        self._cell_size_x = int(cell_size_x)
        self._cell_size_y = int(cell_size_y)
        self._win = window
        #self._cell_spacer = (self._win.width / 300) *3

        self._num_rows = 3
        self._num_cols = 3
        self._cells = []

        #image load
        self.image_o = self._load_image("./images/o.png",self._cell_size_x,self._cell_size_y)
        self.image_x = self._load_image("./images/x.jpg",self._cell_size_x,self._cell_size_y)
        self.image_x2 = self._load_image("./images/x2.jpg",self._cell_size_x,self._cell_size_y)

        
        #create game board
        self._create_board()
        #create cells here
        #2D array 3 x 3 cells
        self._create_cells()

    def turn(self, player):
        self._cells[0][0].move("x",self.image_x)
        self._animate()
        print(self._cells[0][0]._xo)

    def _create_board(self):
        #dynamically set from window dimensions
        width = self._win.width
        x1 = int(width / 3)
        x2 = x1 * 2
        height = self._win.height
        y1 = int( height / 3)
        y2 = y1 * 2

        line_width = (width / 300) *3
        radius = line_width/2

        print(f"{x1} {y1} , {x2} {y2}")
        #draw board
        self._win.draw_rounded_line(Line(Point(x1,0+(line_width*3)),Point(x1,height-(line_width*3))), line_width,radius)
        self._win.draw_rounded_line(Line(Point(x2,0+(line_width*3)),Point(x2,height-(line_width*3))), line_width,radius)
        self._win.draw_rounded_line(Line(Point(0+(line_width*3),y1),Point(width-(line_width*3),y1)), line_width,radius)
        self._win.draw_rounded_line(Line(Point(0+(line_width*3),y2),Point(width-(line_width*3),y2)), line_width,radius)

        #test - remove
        # p1 = Point(10, 10)
        # p2 = Point(400, 400)
        # line = Line(p1, p2)
        # self._win.draw_rounded_line(line,line_width=5, radius=line_width/2, fill_colour="red")

    #Create cells for game
    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i,j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return

        cx1 = i * (self._cell_size_x + ((self._win.width / 300)*3)) + (((self._win.width / 300)*3)/2)# line_width)
        cx1 += self._x1
        cy1 = j * (self._cell_size_y + ((self._win.height / 300)*3)) + (((self._win.width / 300)*3)/2)# line_width)
        cy1 += self._y1

        cx2 = cx1 + self._cell_size_x
        cy2 = cy1 + self._cell_size_y

        print(f"{cx1} {cy1} , {cx2} {cy2}")
        self._cells[i][j].draw(cx1,cy1,cx2,cy2)
        self._animate()


    #reset to start over
    def _reset_cells(self):
        pass

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()


    def _load_image(self,filename,x=50,y=50):
        image = Image.open(filename).convert("RGBA")
        image = image.resize((x,y), resample=Image.LANCZOS)
        return ImageTk.PhotoImage(image)
