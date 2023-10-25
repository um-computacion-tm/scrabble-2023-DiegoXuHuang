import unittest

from game.models import (
    BagTiles,
    Tile,
)
from game.tile import Tile
from unittest.mock import patch



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





class TestBagTiles(unittest.TestCase):
    @patch("random.shuffle")
    def test_bag_tiles(self, patch_shuffle):
        bag = BagTiles()
        self.assertEqual(
            len(bag.tiles),
            98,
        )
        self.assertEqual(
            patch_shuffle.call_count,
            1,
        )
        self.assertEqual(
            patch_shuffle.call_args[0][0],
            bag.tiles,
        )

    def test_take(self):
        bag = BagTiles()
        tiles = bag.take(2)
        self.assertEqual(
            len(bag.tiles),
            96,
        )
        self.assertEqual(
            len(tiles),
            2,
        )

    def test_put(self):
        bag = BagTiles()
        put_tiles = [Tile("Z", 1), Tile("Y", 1)]
        bag.put(put_tiles)
        self.assertEqual(
            len(bag.tiles),
            100,
        )


if __name__ == "__main__":
    unittest.main()
