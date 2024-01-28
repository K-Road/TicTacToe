

#Cell knows its position, xo value, and draws itself
class Cell:
    def __init__(self, window):
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = window
        self._xo = None

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        if self._xo is None:
            self._win.draw_rectangle(self._x1, self._y1, self._x2, self._y2, "white")

    def move(self,move,image):
        self.set_xo_value(move)
        self._win.draw_image(self._x1,self._y1,image)
        

    def set_xo_value(self, value):
       # if self._xo is not None:
        self._xo = value

