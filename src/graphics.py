import tkinter as tk #, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = tk.Tk()
        self.__root.title("BASE")
        self.__root.protocol("WM_DELETE_WINDOW",self.on_window_close)
        self.__canvas = tk.Canvas(self.__root, bg="grey", width=width,height=height)
        self.__canvas.pack(expand=1)
        self.__running = False

        self.clicked_coordinates = tk.StringVar()
        self.__canvas.bind("<Button-1>", self.on_click)

    def wait_input(self):
        self.__root.wait_variable(self.clicked_coordinates)
        clicked_coordinates = eval(self.clicked_coordinates.get())
        print(f"User clicked at do stuff here{clicked_coordinates}")

    
    def on_click(self, event):
        self.clicked_coordinates.set((event.x, event.y))
    def exists(self):
        return self.__root.winfo_exists()

    def on_window_close(self):
        self.__running = False
        #self.__root.destroy()

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("Window closed...")
    
    def close(self):
        self.__running = False

    def draw_line(self, line, line_width=1, fill_colour="black"):
        line.draw(self.__canvas,line_width,fill_colour)

    def draw_rounded_line(self, line, line_width=1, radius=1, fill_colour="black"):
        line.draw_rounded(self.__canvas,line_width,radius,fill_colour)

    def set_window_canvas(self,image):
        self.__canvas.create_image(0,0,anchor="nw",image=image)

    def draw_rectangle(self, x1,y1, x2,y2, bg):
        self.__canvas.create_rectangle(x1,y1,x2,y2, fill=bg, outline="")

    def draw_image(self, x,y,image):
        self.__canvas.create_image(x,y,anchor='nw',image=image)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self,canvas, line_width, fill_colour="black"):
        canvas.create_line(self.p1.x,self.p1.y, self.p2.x,self.p2.y, fill=fill_colour, width=line_width)

    def draw_rounded(self,canvas,line_width,radius,fill_colour="black"):
        canvas.create_line(self.p1.x,self.p1.y, self.p2.x, self.p2.y, fill=fill_colour, width=line_width)

        #draw rounded ends
        canvas.create_oval(self.p1.x-radius,self.p1.y-radius, self.p1.x+radius, self.p1.y+radius, fill=fill_colour, outline="")
        canvas.create_oval(self.p2.x-radius,self.p2.y-radius, self.p2.x+radius, self.p2.y+radius, fill=fill_colour, outline="")
