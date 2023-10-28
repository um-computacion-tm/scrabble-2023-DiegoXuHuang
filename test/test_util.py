import unittest
from game.util import Util
from game.tile import Tile





class TestUpdateCoordinates(unittest.TestCase):

    

    def test_get_word_left(self):
        board = Util()
        letters = ['C', 'A', 'S', 'A']
        for col, letter in enumerate(letters, start=7):
            board.grid[7][col].add_letter(Tile(letter, 1))
    
        word = board.get_word_left(row=7, col=11)
    
        for i, letter in enumerate(letters):
            self.assertEqual(word[i].get_tile().get_letter(), letter)


    def test_get_word_left(self):
        board = Util()
        letters = ['C', 'A', 'S', 'A']
        for col, letter in enumerate(letters, start=7):
            board.grid[7][col].add_letter(Tile(letter, 1))
    
        word = board.get_word_left(row=7, col=11)
    
        for i, letter in enumerate(letters):
            self.assertEqual(word[i].get_tile().get_letter(), letter)


    def test_get_word_right(self):
        board = Util()
        letters = ['C', 'A', 'M', 'A']
        for col, letter in enumerate(letters, start=7):
            board.grid[7][col].add_letter(Tile(letter, 1))
    
        word = board.get_word_right(row=7, col=6)
    
        for i, letter in enumerate(letters):
            self.assertEqual(word[i].get_tile().get_letter(), letter)


    def test_get_word_horizontal(self):
        board = Util()
        letters = ['C', 'A', 'L', 'M', 'A', 'D', 'O']
        for col, letter in enumerate(letters, start=7):
            board.grid[7][col].add_letter(Tile(letter, 1))
    
        word = board.get_word_horizontal(row=7, col=10)
    
        for i, letter in enumerate(letters):
            self.assertEqual(word[i].get_tile().get_letter(), letter)


    def test_get_word_vertical(self):
        board = Util()
        letters = ['C', 'A', 'L', 'M', 'A', 'D', 'O']
        for row, letter in enumerate(letters, start=7):
            board.grid[row][7].add_letter(Tile(letter, 1))
    
        word = board.get_word_vertical(row=10, col=7)
    
        for i, letter in enumerate(letters):
            self.assertEqual(word[i].get_tile().get_letter(), letter)


    def test_get_word_horizontal_invalid_word(self):
        board = Util()

        board.grid[7][1].add_letter(Tile('M', 1))
        board.grid[7][2].add_letter(Tile('I', 1))
        board.grid[7][3].add_letter(Tile('C', 1))
        board.grid[7][4].add_letter(Tile('R', 1))
        board.grid[7][5].add_letter(Tile('O', 1))
        board.grid[7][6].add_letter(Tile('L', 1))

        result = board.get_word_horizontal(row=7, col=10)
        self.assertFalse(result)

    
    def test_get_word_vertical_empty(self):
  
        board = Util()

        board.grid[1][7].add_letter(Tile('M', 1))
        board.grid[2][7].add_letter(Tile('I', 1))
        board.grid[3][7].add_letter(Tile('C', 1))
        board.grid[4][7].add_letter(Tile('R', 1))
        board.grid[5][7].add_letter(Tile('O', 1))
        board.grid[6][7].add_letter(Tile('L', 1))

        result = board.get_word_vertical(row=10, col=7)
        self.assertFalse(result)


    



if __name__ == '__main__':
    unittest.main()
