# import unittest
# from game.tile import Tile



# class TestTiles(unittest.TestCase):
    
    # def setUp(self):
    #     self.tile_A = Tile('A', 1)
    #     self.tile_Z = Tile('Z', 10)

    # def test_get_letter(self):
        # self.assertEqual(self.tile_A.get_letter(), 'A')
        #self.assertEqual(self.tile.get_letter(), 'Z')

    # def test_get_value(self):
        # self.assertEqual(self.tile_A.get_value(), 1)
        #self.assertEqual(self.tile.get_value(), 10)


    # def test_tile(self):
    #     tile = Tile("A", 1)
    #     self.assertEqual(tile.letter, "A")
    #     self.assertEqual(tile.value, 1)

     
# if __name__ == '__main__':
#     unittest.main()       



import unittest
from game.tile import Tile  # Supongo que la clase Tile está en un archivo llamado 'tile.py'

class TestTile(unittest.TestCase):

    # def test_get_value(self):
    #     tile = Tile("A", 1)
    #     self.assertEqual(tile.get_value(), 1)

    def test_get_letter(self):
        tile = Tile("B", 3)
        self.assertEqual(tile.get_letter(), "B")

    def test_default_player(self):
        tile = Tile("C", 3)
        self.assertIsNone(tile.player)

    def test_custom_player(self):
        player = "John"
        tile = Tile("D", 2, player)
        self.assertEqual(tile.player, player)

if __name__ == '__main__':
    unittest.main()

