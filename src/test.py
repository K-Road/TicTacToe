import unittest
from tictactoe import TicTacToe

class Tests(unittest.TestCase):
    def test_tictactoe(self):
        t1 = TicTacToe(1,1,50,50)
        self.assertEqual(
            len(t1._cells),
            0,
        )

if __name__ == "__main__":
    unittest.main()