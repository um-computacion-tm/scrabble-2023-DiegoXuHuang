import unittest
from game.tile import Tile  

class TestTile(unittest.TestCase):

    def test_get_value(self):
        tile = Tile("A", 1)
        self.assertEqual(tile.get_value(), 1)
   

    def test_get_letter(self):
        tile = Tile("B", 3)
        self.assertEqual(tile.get_letter(), "B")

    def test_default_player(self):
        tile = Tile("C", 3)
        self.assertIsNone(tile.player)

    def test_custom_player(self):
        player = "Facundo"
        tile = Tile("D", 2, player)
        self.assertEqual(tile.player, player)

    def test_tile_repr(self):
        tile = Tile('A', 1)
        expected_repr = 'A:1'
        self.assertEqual(repr(tile), expected_repr)

    

if __name__ == '__main__':
    unittest.main()



