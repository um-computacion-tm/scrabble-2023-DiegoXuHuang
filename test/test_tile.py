import unittest
from game.tile import Tile  

class TestTile(unittest.TestCase):

    def test_get_value(self):
        self.assertEqual(self.tile_A.get_value(), 1)
        self.assertEqual(self.tile.get_value(), 10)
   

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

