# import unittest
# from game.dictionary import Dictionary
# from game.board import Board
# from game.cell import Cell
# from game.tile import Tile

# class TestDictionary(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.board = Board()
#         cls.dictionary = Dictionary()

#     def test_dictionary_true(self):
#         word = [
#             Cell(letter=Tile('C', 1)),
#             Cell(letter=Tile('A', 1)),
#             Cell(letter=Tile('S', 2)),
#             Cell(letter=Tile('A', 1)),
#         ]
#         file_path = self.dictionary.file_path
#         self.assertEqual(self.board.check_word(word, file_path), True)

#     def test_dictionary_false(self):
#         word = [
#             Cell(letter=Tile('C', 1)),
#             Cell(letter=Tile('S', 2)),
#             Cell(letter=Tile('S', 2)),
#             Cell(letter=Tile('A', 1)),
#         ]
#         file_path = self.dictionary.file_path
#         self.assertEqual(self.board.check_word(word, file_path), False)

# if __name__ == '__main__':
#     unittest.main()

import unittest
from unittest.mock import patch
from game.dictionary import (
    validate_word,
    DictionaryConnectionError,
)


class TestDiccionary(unittest.TestCase):
    @patch(
        'pyrae.dle.search_by_word',
        return_value=unittest.mock.MagicMock(
            meta_description='1. interj. U. como salutación familiar.'
        )
    )
    def test_valid(self, search_by_word_patched):
        self.assertTrue(validate_word('hola'))

    @patch(
        'pyrae.dle.search_by_word',
        return_value=unittest.mock.MagicMock(
            meta_description='Versión electrónica 23.6 del «Diccionario de la lengua española», obra lexicográfica académica por excelencia.'
        )
    )
    def test_invalid(self, search_by_word_patched):
        self.assertFalse(validate_word('asd'))

    @patch(
        'pyrae.dle.search_by_word',
        return_value=None
    )
    def test_connection_error(self, search_by_word_patched):
        with self.assertRaises(DictionaryConnectionError):
            validate_word('hola')

if __name__ == '__main__':
    unittest.main()
