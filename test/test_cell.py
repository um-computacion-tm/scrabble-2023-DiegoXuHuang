import unittest
from game.cell import Cell
from game.models import Tile


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


    def test_toggle_cell_active_to_inactive(self):
        # Crea una celda activa
        cell = Cell(multiplier=2, multiplier_type='X', letter=None, active=True)
        # Asegura que la celda esté activa
        self.assertTrue(cell.active)
        # Cambia la celda a inactiva
        cell.toggle_cell()
        # Asegura que la celda esté inactiva
        self.assertFalse(cell.active)

    def test_toggle_cell_inactive_to_active(self):
        # Crea una celda inactiva
        cell = Cell(multiplier=2, multiplier_type='X', letter=None, active=False)
        # Asegura que la celda esté inactiva
        self.assertFalse(cell.active)
        # Cambia la celda a activa
        cell.toggle_cell()
        # Asegura que la celda esté activa
        self.assertTrue(cell.active)

   



    

    


   
    



if __name__ == '__main__':
    unittest.main()