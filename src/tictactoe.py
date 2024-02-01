import tkinter as tk
from PIL import Image, ImageTk
from graphics import Line, Point, Window
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
        self._playing = False
        self._num_rows = 3
        self._num_cols = 3
        self._cells = []
        self.turn = 0

        #image load
        self.image_o = self._load_image("./images/o.png",self._cell_size_x,self._cell_size_y)
        self.image_x = self._load_image("./images/x.jpg",self._cell_size_x,self._cell_size_y)
        self.image_x2 = self._load_image("./images/x2.jpg",self._cell_size_x,self._cell_size_y)

        
        #create game board
        self._create_board()
        #create cells here
        #2D array 3 x 3 cells
        self._create_cells()

        # self.clicked_coordinates = tk.StringVar()
        # self._win.__canvas.bind("<Button-1>", self.on_click)

    # def on_click(self, event):
    #     self.clicked_coordinates.set((event.x, event.y))

    def _turn(self, cell, player):
        #self._cells[0][0].move("o",self.image_o)
        if player == 1:
            cell.move("o",self.image_o)
        else:
            cell.move("x",self.image_x)
        self._animate()
        self.turn += 1
        #self._check_win_condition(player,cell)
        #print(self._cells[0][0]._xo)

    def play(self):
        #self._playing = True
        #self._win.wait_variable()
        while self.turn < 9:#and not self._check_win_condition():
            print(self.turn)
            cell = None
            while cell is None:
                input = self._win.wait_input()#check_for_mouse_input()
                cell,x,y = self.get_cell(input)
            if self.turn%2 == 0:
                player = 1
            else:
                player = 2
            print(player)
            self._turn(cell, player)
            if not self._check_win_condition(player,x,y):
                break

        print("No valid turns")

    def check_for_mouse_input(self):
        #input = self._win.wait_input()
        #cell = None
        # cell = self.get_cell(input)
        # if cell is not None:
        #     if self.turn%2 == 0:
        #         player = 1
        #     else:
        #         player = 2
        #     self._turn(cell, player)
        # else:
        #     self.check_for_mouse_input()
        pass

    def get_cell(self, input):
        x = input[0]//self._cell_size_x
        y = input[1]//self._cell_size_y
        print(f"{x} {y}")
        if self._cells[x][y].get_xo_value() is None:
            return self._cells[x][y],x,y
        return None, None, None

        
    def _check_win_condition(self,turn,x,y):
        #check x
        if turn == 1:
            check = "o"
        else:
            check = "x"


        if self._cells[x][0].get_xo_value() == check and self._cells[x][1].get_xo_value() == check and self._cells[x][2].get_xo_value() == check:
            #p1 = 
            #self._win.draw_win(self._cells[x][0],self._cells[x][2])
            print("WIN")
            return False
        if self._cells[0][y].get_xo_value() == check and self._cells[1][y].get_xo_value() == check and self._cells[2][y].get_xo_value() == check:
            print("WIN")
            return False
        if self._cells[1][1].get_xo_value is not None:
            if self._cells[0][0].get_xo_value() == check and self._cells[1][1].get_xo_value() == check and self._cells[2][2].get_xo_value() == check:
                print("WIN")
                return False
            if self._cells[0][2].get_xo_value() == check and self._cells[1][1].get_xo_value() == check and self._cells[2][0].get_xo_value() == check:
                print("WIN")
                return False
        return True
        

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

        print(f"{cx1} {cy1} , {cx2} {cy2}") #DEBUG REMOVE
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
