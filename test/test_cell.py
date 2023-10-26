import unittest
from game.cell import Cell
from game.models import Tile
from game.tile import Tile


class TestCell(unittest.TestCase):
    
    
    def test_init(self):
        cell = Cell(multiplier=2, multiplier_type='letter')

        self.assertEqual(
            cell.multiplier,
            2,
        )
        self.assertEqual(
            cell.multiplier_type,
            'letter',
        )
        self.assertIsNone(cell.letter)
        self.assertEqual(
            cell.calculate_value(),
            0,
        )

    


    def test_add_letter(self):
        cell = Cell(multiplier=1, multiplier_type='')
        letter = Tile(letter='p', value=3)

        cell.add_letter(letter=letter)

        self.assertEqual(cell.letter, letter)

    def test_cell_value(self):
        cell = Cell(multiplier=2, multiplier_type='letter')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)

        self.assertEqual(
            cell.calculate_value(),
            6,
        )

    def test_cell_multiplier_word(self):
        cell = Cell(multiplier=2, multiplier_type='word')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)

        self.assertEqual(
            cell.calculate_value(),
            3,
        )


    # def test_toggle_cell_active_to_inactive(self):
    #     cell = Cell(multiplier=2, multiplier_type='X', letter=None, active=True)
    #     self.assertTrue(cell.active)
    #     cell.toggle_cell()
    #     self.assertFalse(cell.active)



    # def test_toggle_cell_inactive_to_active(self):
    #     cell = Cell(multiplier=2, multiplier_type='X', letter=None, active=False)
    #     self.assertFalse(cell.active)
    #     cell.toggle_cell()
    #     self.assertTrue(cell.active)



    def test_repr_without_letter(self):
        instance = Cell(letter=None, multiplier=2, multiplier_type='D')
        self.assertEqual(repr(instance), 'Dx2')

    def test_repr_without_letter_and_multiplier_one(self):
        instance = Cell(letter=None, multiplier=1)
        self.assertEqual(repr(instance), '   ')




    


    




  
   



    

    


   
    



if __name__ == '__main__':
    unittest.main()