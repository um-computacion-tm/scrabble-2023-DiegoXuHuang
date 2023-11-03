import unittest
from game.cell import Cell
from game.models import Tile
from game.tile import Tile
from game.cell import Cell, Tile
from parameterized import parameterized



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

    def test_calculate_value(self):
        cell = Cell(multiplier=2, multiplier_type='L', letter=None, active=True)
        letter = Tile(letter='a', value=1)
        cell.add_letter(letter=letter)

        expected_value = 2
        actual_value = cell.calculate_value()

        self.assertEqual(actual_value, expected_value)

    def test_multiplier_word(self):
        cell = Cell(multiplier=2, multiplier_type='word')
        letter = Tile(letter='a', value=1)
        cell.add_letter(letter=letter)

        expected_value = 1
        actual_value = cell.calculate_value()

        self.assertEqual(actual_value, expected_value)

  
    def test_has_letter(self):
        cell = Cell(multiplier=1, multiplier_type='', letter=None, active=True)
        cell.add_letter(Tile(letter='a', value=1))
        self.assertTrue(cell.has_tile())


    def test_get_tile(self):
        initial_letter = Tile(letter='p', value=3)
        cell = Cell(multiplier=1, multiplier_type='', letter=initial_letter, active=True)
        
        retrieved_letter = cell.get_tile()

        self.assertEqual(retrieved_letter.letter, initial_letter.letter)
        self.assertEqual(retrieved_letter.value, initial_letter.value)


    def test_deactivate_cell(self):
        cell = Cell(multiplier=2, multiplier_type='W', letter=None, active=True)
        cell.deactivate_cell()
        self.assertEqual(cell.active,False)



    @parameterized.expand([
        ("Single Letter", Cell(1, None, Tile("X", 1), True), " X "),
        ("Two Letters", Cell(1, None, Tile("CH", 1), True), "CH "),
        ("No Letter", Cell(1, None, None, True), "   "),
        ("Multiplier", Cell(2, "L", None, True), "Lx2"),
    ])
    def test_repr(self, name, cell, expected):
        self.assertEqual(repr(cell), expected)





  

if __name__ == "__main__":
    unittest.main()




    


    




  
   



    

    


   
    



if __name__ == '__main__':
    unittest.main()