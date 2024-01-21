import unittest
from tictactoe import TicTacToe
from graphics import Window

class Tests(unittest.TestCase):
    def test_tictactoe(self):
        w1 = Window(500,500)
        t1 = TicTacToe(1,1,50,50,w1)
        self.assertEqual(
            len(t1._cells),
            0,
        )

    def test_create_cells(self):
        num_cols = 3
        num_rows = 3
        w1 = Window(500,500)
        t1 = TicTacToe(1,1,50,50,w1)
        self.assertEqual(
            len(t1._cells),
            num_cols,
            )
        self.assertEqual(
            len(t1._cells[0]),
            num_rows,
            )



if __name__ == "__main__":
    unittest.main()