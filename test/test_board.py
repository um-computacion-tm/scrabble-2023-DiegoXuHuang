import unittest
from game.board import Board
from game.tile import Tile
import sys
from io import StringIO
from game.util import Util



class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board()
        self.assertEqual(
            len(board.grid),
            15,
        )
        self.assertEqual(
            len(board.grid[0]),
            15,
        )
        
    #check
    def test_word_inside_board_horizontal(self):
        board = Board() 
        word = "Facultad"
        location = (5, 4)
        orientation = "H"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)

        assert word_is_valid == True
    #check
    def test_word_inside_board_vertical(self):
        board = Board()
        word = "Facultad"
        location = (5, 4)
        orientation = "V"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)

        assert word_is_valid == True
    
    def test_word_out_of_board_horizontal(self):
        board = Board()
        word = "Facultad"
        location = (4, 14)
        orientation = "H"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)

        assert word_is_valid == False

    def test_word_out_of_board_vertical(self):
        board = Board()
        word = "Facultad"
        location = (10, 8)
        orientation = "V"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)

        assert word_is_valid == False


    def test_board_is_empty(self):
        board = Board()
        board.empty()
        assert board.is_empty == True

    def test_board_is_not_empty(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1))
        board.empty()
        assert board.is_empty == False



    def test_place_word_empty_board_horizontal_fine(self):
        board = Board()
        word = "Facultad"
        location = (7, 4)
        orientation = "H"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == True

    def test_place_word_empty_board_horizontal_wrong(self):
        board = Board()
        word = "Facultad"
        location = (2, 4)
        orientation = "H"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == False

    def test_place_word_empty_board_vertical_fine(self):
        board = Board()
        word = "Facultad"
        location = (4, 7)
        orientation = "V"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == True

    def test_place_word_empty_board_vertical_wrong(self):
        board = Board()
        word = "Facultad"
        location = (2, 4)
        orientation = "V"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == False

    def test_place_word_not_empty_board_horizontal_fine(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1))
        board.grid[8][7].add_letter(Tile('A', 1)) 
        board.grid[9][7].add_letter(Tile('S', 1)) 
        board.grid[10][7].add_letter(Tile('A', 1)) 
        word = "Facultad"   
        location = (8, 6)
        orientation = "H"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == True

    def test_place_word_not_empty_board_horizontal_not_fine(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1))
        board.grid[8][7].add_letter(Tile('A', 1)) 
        board.grid[9][7].add_letter(Tile('S', 1)) 
        board.grid[10][7].add_letter(Tile('A', 1)) 
        word = "MISA"
        location = (8, 6)
        orientation = "H"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == False

    def test_place_word_not_empty_board_vertical_fine(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1))
        board.grid[7][8].add_letter(Tile('A', 1)) 
        board.grid[7][9].add_letter(Tile('S', 1)) 
        board.grid[7][10].add_letter(Tile('A', 1)) 
        word = "Facultad"
        location = (6, 8)
        orientation = "V"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == True

    def test_place_word_not_empty_board_vertical_not_fine(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1))
        board.grid[7][8].add_letter(Tile('A', 1)) 
        board.grid[7][9].add_letter(Tile('S', 1)) 
        board.grid[7][10].add_letter(Tile('A', 1)) 
        word = "HOLA"
        location = (6, 8)
        orientation = "V"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == False


    def test_show_board(self):
        game_instance = Board()  
        expected_output = """
    |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  | 10  | 11  | 12  | 13  | 14 |
   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
0  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
1  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
2  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
3  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
4  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
5  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
6  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
7  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
8  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
9  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
10 |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
11 |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
12 |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
13 |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
14 |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
"""

        
        captured_output = StringIO()
        sys.stdout = captured_output

        game_instance.show_board()


    
    def test_get_word_left(self):
        board = Board()
        util = Util(board)
        letters = ['C', 'A', 'S', 'A']
        for col, letter in enumerate(letters, start=7):
            board.grid[7][col].add_letter(Tile(letter, 1))
    
        word = util.get_word_left(row=7, col=11)
    
        for i, letter in enumerate(letters):
            self.assertEqual(word[i].get_tile().get_letter(), letter)


    def test_get_word_right(self):
        board = Board()
        util = Util(board)
        letters = ['C', 'A', 'M', 'A']
        for col, letter in enumerate(letters, start=7):
            board.grid[7][col].add_letter(Tile(letter, 1))
    
        word = util.get_word_right(row=7, col=6)
    
        for i, letter in enumerate(letters):
            self.assertEqual(word[i].get_tile().get_letter(), letter)


    def test_get_word_horizontal(self):
        board = Board()
        util = Util(board)
        letters = ['C', 'A', 'L', 'M', 'A', 'D', 'O']
        for col, letter in enumerate(letters, start=7):
            board.grid[7][col].add_letter(Tile(letter, 1))
    
        word = util.get_word_horizontal(row=7, col=10)
    
        for i, letter in enumerate(letters):
            self.assertEqual(word[i].get_tile().get_letter(), letter)


    def test_get_word_vertical(self):
        board = Board()
        util = Util(board)
        letters = ['C', 'A', 'L', 'M', 'A', 'D', 'O']
        for row, letter in enumerate(letters, start=7):
            board.grid[row][7].add_letter(Tile(letter, 1))
    
        word = util.get_word_vertical(row=10, col=7)
    
        for i, letter in enumerate(letters):
            self.assertEqual(word[i].get_tile().get_letter(), letter)


    def test_get_word_horizontal_invalid_word(self):
        board = Board()
        util = Util(board)

        board.grid[7][1].add_letter(Tile('M', 1))
        board.grid[7][2].add_letter(Tile('I', 1))
        board.grid[7][3].add_letter(Tile('C', 1))
        board.grid[7][4].add_letter(Tile('R', 1))
        board.grid[7][5].add_letter(Tile('O', 1))
        board.grid[7][6].add_letter(Tile('L', 1))

        result = util.get_word_horizontal(row=7, col=10)
        self.assertFalse(result)

    
    def test_get_word_vertical_empty(self):
  
        board = Board()
        util = Util(board)

        board.grid[1][7].add_letter(Tile('M', 1))
        board.grid[2][7].add_letter(Tile('I', 1))
        board.grid[3][7].add_letter(Tile('C', 1))
        board.grid[4][7].add_letter(Tile('R', 1))
        board.grid[5][7].add_letter(Tile('O', 1))
        board.grid[6][7].add_letter(Tile('L', 1))

        result = util.get_word_vertical(row=10, col=7)
        self.assertFalse(result)
   

if __name__ == '__main__':
    unittest.main()
