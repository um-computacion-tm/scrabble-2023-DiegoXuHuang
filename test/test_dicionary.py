import unittest
from game.dictionary import Dictionary
from game.board import Board
from game.cell import Cell
from game.tile import Tile

class TestDictionary(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.board = Board()
        cls.dictionary = Dictionary()

    def test_dictionary_true(self):
        word = [
            Cell(letter=Tile('C', 1)),
            Cell(letter=Tile('A', 1)),
            Cell(letter=Tile('S', 2)),
            Cell(letter=Tile('A', 1)),
        ]
        file_path = self.dictionary.file_path
        self.assertEqual(self.board.check_word(word, file_path), True)

    def test_dictionary_false(self):
        word = [
            Cell(letter=Tile('C', 1)),
            Cell(letter=Tile('S', 2)),
            Cell(letter=Tile('S', 2)),
            Cell(letter=Tile('A', 1)),
        ]
        file_path = self.dictionary.file_path
        self.assertEqual(self.board.check_word(word, file_path), False)

if __name__ == '__main__':
    unittest.main()
