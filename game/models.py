import random
from game.tile import Tile


class BagTiles:
    def __init__(self):
        tile_data = [
            ('A', 1, 12), ('E', 1, 12),
            ('O', 1, 9),
            ('I', 1, 6), ('S', 1, 6),
            ('N', 1, 5), ('R', 1, 5), ('U', 1, 5), ('D', 2, 5),
            ('L', 1, 4), ('T', 1, 4), ('C', 3, 4),
            ('B', 3, 2), ('M', 3, 2), ('P', 3, 2), ('G', 2, 2), ('H', 4, 2),
            (' ', 0, 2), ('F', 4, 1), ('V', 4, 1), ('Y', 4, 1),
            ('CH', 5, 1), ('Q', 5, 1), ('J', 8, 1),
            ('LL', 8, 1), ('Ñ', 8, 1), ('RR', 8, 1), ('X', 8, 1), ('Z', 10, 1)
        ]

        self.tiles = [Tile(letter, value) for letter, value, count in tile_data for _ in range(count)]
        random.shuffle(self.tiles)


    def shuffle_bag(self):
        random.shuffle(self.tiles)

    def take(self, count):
        count = min(count, len(self.tiles))
        taken_tiles = self.tiles[-count:]
        self.tiles = self.tiles[:-count]
        return taken_tiles


    def put(self, tiles):
        self.tiles.extend(tiles)




