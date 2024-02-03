import tkinter as tk
from PIL import Image, ImageTk
from graphics import Line, Point, Window
from cell import Cell
import time
import random
from tkinter import messagebox

class TicTacToe:
    def __init__(self,x1,y1,cell_size_x,cell_size_y,window=None):
        self._x1 = x1
        self._y1 = y1
        self._cell_size_x = int(cell_size_x)
        self._cell_size_y = int(cell_size_y)
        self._win = window
        #self._cell_spacer = (self._win.width / 300) *3
        self._playing = False
        self._num_rows = 3
        self._num_cols = 3
        self._cells = []
        self.turn = 0

        #image load
        self.image_o = self._load_image("./images/o.png",self._cell_size_x,self._cell_size_y)
        self.image_x = []
        self.image_x.append(self._load_image("./images/x.jpg",self._cell_size_x,self._cell_size_y))
        self.image_x.append(self._load_image("./images/x2.jpg",self._cell_size_x,self._cell_size_y))

        #create game board
        self._create_board()
        #create cells here
        #2D array 3 x 3 cells
        self._create_cells()



    def _turn(self, cell, player):
        if player == 1:
            cell.move("o",self.image_o)
        else:
            cell.move("x",random.choice(self.image_x))
        self._animate()

    def play(self):

        self.turn = 0
        while self.turn < 9:
            cell = None
            while cell is None:
                input = self._win.wait_input()
                cell,x,y = self.get_cell(input)
            
            player = 1 if self.turn % 2 == 0 else 2
            self._turn(cell,player)

            if self._check_win_condition(player,x,y):
                result = player
                break
            self.turn += 1

        if self.turn == 9:
            result = 0

        if self._play_again(result):
            self._reset_cells()
        
    def _play_again(self,status):
        if status == 0:
            result = tk.messagebox.askyesno("Game tied", "Do you want to play again?")
        else:
            result = tk.messagebox.askyesno(f"Player {status} wins!", "Do you want to play again?")
        if result:
            return True
        return False
    
    def get_cell(self, input):
        x = input[0]//self._cell_size_x
        y = input[1]//self._cell_size_y
       # print(f"{x} {y}")
        if self._cells[x][y].get_xo_value() is None:
            return self._cells[x][y],x,y
        return None, None, None

        
    def _check_win_condition(self,player,x,y):
        check = "o" if player ==1 else "x"

        #chk row
        if ( 
            self._cells[x][0].get_xo_value() == check 
            and self._cells[x][1].get_xo_value() == check 
            and self._cells[x][2].get_xo_value() == check
        ):
            self._cells[x][0].draw_win(self._cells[x][2])
            return True
        #chk col
        if (
            self._cells[0][y].get_xo_value() == check 
            and self._cells[1][y].get_xo_value() == check 
            and self._cells[2][y].get_xo_value() == check
        ):
            self._cells[0][y].draw_win(self._cells[2][y])
            return True
        #chk diag
        if self._cells[1][1].get_xo_value() is not None:
            if (
                self._cells[0][0].get_xo_value() == check 
                and self._cells[1][1].get_xo_value() == check 
                and self._cells[2][2].get_xo_value() == check
            ):
                self._cells[0][0].draw_win(self._cells[2][2])
                return True
            if (
                self._cells[0][2].get_xo_value() == check 
                and self._cells[1][1].get_xo_value() == check 
                and self._cells[2][0].get_xo_value() == check
            ):
                self._cells[0][2].draw_win(self._cells[2][0])
                return True
        return False
  

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

        #print(f"{x1} {y1} , {x2} {y2}")
        #draw board
        self._win.draw_rounded_line(Line(Point(x1,0+(line_width*3)),Point(x1,height-(line_width*3))), line_width,radius)
        self._win.draw_rounded_line(Line(Point(x2,0+(line_width*3)),Point(x2,height-(line_width*3))), line_width,radius)
        self._win.draw_rounded_line(Line(Point(0+(line_width*3),y1),Point(width-(line_width*3),y1)), line_width,radius)
        self._win.draw_rounded_line(Line(Point(0+(line_width*3),y2),Point(width-(line_width*3),y2)), line_width,radius)

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

        self._cells[i][j].draw(cx1,cy1,cx2,cy2)
        self._animate()

    #reset to start over
    def _reset_cells(self):
        self._cells = []
        self._create_board()
        self._create_cells()
        self._animate()
        self.play()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()

    def _load_image(self,filename,x=50,y=50):
        image = Image.open(filename).convert("RGBA")
        image = image.resize((x,y), resample=Image.LANCZOS)
        return ImageTk.PhotoImage(image)
