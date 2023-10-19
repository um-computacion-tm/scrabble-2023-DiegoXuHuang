import unittest
from game.models import BagTiles
from game.tile import Tile
from game.player import Player,NoSuficienteFichasException



class TestPlayer(unittest.TestCase):
    def test_init(self):
        player_1 = Player()
        self.assertEqual(
            len(player_1.tiles),
            0,
        )

    def test_set_name(self):
        player = Player()
        player.set_name('Diego')
        self.assertEqual(player.get_name(), 'Diego')

    def test_take_tiles(self):
        player=Player()
        bag = BagTiles()
        player.take_tiles(bag, 7)
        self.assertEqual(len(player.tiles), 7)


    def test_score(self):
        player = Player()
        player.increase_score(5)
        self.assertEqual(player.get_score(), 5)
    

    def test_show_tiles(self):
        player = Player()
        self.assertEqual(player.show_tiles(), player.tiles)


    
    def test_refill(self):
    # la cantidad de fichas en la mano del jugador (player2.tiles) sea igual a 7
        player2 = Player()
        player2.tiles = ['A', 'B']
        bag = BagTiles()
        
        player2.refill(bag)
    
        self.assertEqual(len(player2.tiles), 7)


    def test_validate_user_has_letters(self):
        bag_tile = BagTiles()
        player = Player()
        bag_tile.tiles = [
            Tile(letter='H', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
            Tile(letter='C', value=1),
            Tile(letter='U', value=1),
            Tile(letter='M', value=1),
        ]
        tiles = [
            Tile(letter='H', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
        ]
        player.tiles = bag_tile.tiles 
        is_valid = player.has_letters(tiles)
        self.assertEqual(is_valid, True)


    def test_validate_fail_when_user_has_not_letters(self):
        bag_tile = BagTiles()
        player = Player()
        bag_tile.tiles = [
            Tile(letter='P', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
            Tile(letter='C', value=1),
            Tile(letter='U', value=1),
            Tile(letter='M', value=1),
        ]
        tiles = [
            Tile(letter='H', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
        ]
        player.tiles = bag_tile.tiles
        is_valid = player.has_letters(tiles)
        self.assertEqual(is_valid, False)


    def test_exchange_tiles(self):
        player = Player()
        bag = BagTiles()
        player.get_tiles(bag, 3)
        tile = player.tiles[0]
        exchanged_tiles, new_tiles = player.exchange_tiles(bag, 2)
        
        self.assertNotEqual(tile, player.tiles[0])  # Verificar que la ficha intercambiada no sea igual a la ficha original
        self.assertEqual(len(player.tiles), 3)  # El jugador debería tener 3 fichas después del intercambio

    def test_exchange_not_enough_tiles(self):
        player = Player()
        bag = BagTiles()
        player.get_tiles(bag, 2)
        with self.assertRaises(NoSuficienteFichasException):
            exchanged_tiles, new_tiles = player.exchange_tiles(bag, 3)
        self.assertEqual(len(player.tiles), 2)  # El jugador debería seguir teniendo 2 fichas
    


if __name__ == '__main__':
    unittest.main()
