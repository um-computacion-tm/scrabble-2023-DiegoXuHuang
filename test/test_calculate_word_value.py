import unittest

from game.cell import Cell, CalculateWordValue
from game.tile import Tile
from game.models import *



class TestCalculateWordValue(unittest.TestCase):
    
    def test_simple(self):
        word = [
            Cell(letter=Tile('C', 1)),
            Cell(letter=Tile('A', 1)),
            Cell(letter=Tile('S', 2)),
            Cell(letter=Tile('A', 1)),
        ]
        
        value_calculator = CalculateWordValue()
        value = value_calculator.calculate_word(word)
        self.assertEqual(value, 5)


    def test_with_letter_multiplier(self):
        word = [
            Cell(letter=Tile('C', 1)),
            Cell(letter=Tile('A', 1)),
            Cell(
                letter=Tile('S', 2),
                multiplier=2,
                multiplier_type='letter',
            ),
            Cell(letter=Tile('A', 1)),
        ]
        
        value_calculator = CalculateWordValue()
        value = value_calculator.calculate_word(word)
        self.assertEqual(value, 5)


    def test_with_word_multiplier(self):
        word = [
            Cell(letter=Tile('C', 1)),
            Cell(letter=Tile('A', 1)),
            Cell(
                letter=Tile('S', 2),
                multiplier=2,
                multiplier_type='word',
            ),
            Cell(letter=Tile('A', 1)),
        ]
        
        value_calculator = CalculateWordValue()
        value = value_calculator.calculate_word(word)
        self.assertEqual(value, 5)


    def test_with_letter_word_multiplier(self):
        word = [ 
            Cell(
                multiplier=3,
                multiplier_type='letter',
                letter=Tile('C', 1)
            ),
            Cell(letter=Tile('A', 1)),
            Cell(
                letter=Tile('S', 2),
                multiplier=2,
                multiplier_type='word',
            ),
            Cell(letter=Tile('A', 1)),
        ]
        
        value_calculator = CalculateWordValue()
        value = value_calculator.calculate_word(word)
        self.assertEqual(value, 5)


    def test_with_letter_word_multiplier_no_active(self):
        
        word = [
            Cell(
                multiplier=3,
                multiplier_type='letter',
                letter=Tile('C', 1), 
                active=False
            ),
            Cell(letter=Tile('A', 1)),
            Cell(
                letter=Tile('S', 2),
                multiplier=2,
                multiplier_type='word',
                active=False
            ),
            Cell(letter=Tile('A', 1)),
        ]
        
        value_calculator = CalculateWordValue()
        value = value_calculator.calculate_word(word)
        self.assertEqual(value, 5)



    

if __name__ == '__main__':
    unittest.main()


