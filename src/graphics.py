from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("BASE")
        self.__root.protocol("WM_DELETE_WINDOW",self.close)
        self.__canvas = Canvas(self.__root, bg="grey", width=width,height=height)
        self.__canvas.pack(fill=BOTH,expand=1)
        self.__running = False


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

    def draw_line(self, line, fill_colour="black"):
        line.draw(self.__canvas,fill_colour)

    def set_window_canvas(self,image):
        self.__canvas.create_image(0,0,anchor="nw",image=image)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self,canvas, fill_colour="black"):
        canvas.create_line(self.p1.x,self.p1.y, self.p2.x,self.p2.y, fill=fill_colour, width=3)