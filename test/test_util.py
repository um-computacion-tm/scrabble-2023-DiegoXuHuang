import unittest
from game.util import Util

class TestUpdateCoordinates(unittest.TestCase):

    # def __init__(self):
    #     self.current_player = None


    
    def test_update_coordinates_horizontal(self):
        self.coordinates_util = Util()
        row, col = self.coordinates_util.update_coordinates("H", 3, 4)
        self.assertEqual((row, col), (3, 5))
        

    def test_update_coordinates_vertical(self):
        self.coordinates_util = Util()
        row, col = self.coordinates_util.update_coordinates("V", 2, 6)
        self.assertEqual((row, col), (3, 6))


    def test_split_groups_in_string_empty_string(self):
        util = Util()
        string = ""
        word = util.split_groups_in_string(string)
        self.assertEqual(word, [],)


    def test_split_groups_in_string_invalid_word_chars(self):
        util = Util()
        string = "Hech@rro"
        word = util.split_groups_in_string(string)
        self.assertEqual(word, ['H', 'e', 'ch', '@', 'rr', 'o']) #espaniol tmb es valido

    def test_split_groups_in_string_with_spaces(self):
        util = Util()
        string = "Hello World"
        word = util.split_groups_in_string(string)
        self.assertEqual(word, ['H', 'e', 'll', 'o', ' ', 'W', 'o', 'r', 'l', 'd'])#espaniol tmb es valido

    def test_split_groups_in_string_mixed_case(self):
        util = Util()
        string = "HeLLo WoRLD"
        word = util.split_groups_in_string(string)
        self.assertEqual(word, ['H', 'e', 'L', 'L', 'o', ' ', 'W', 'o', 'R', 'L', 'D'])#espaniol tmb es valido


    





if __name__ == '__main__':
    unittest.main()
