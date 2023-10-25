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


    def test_player_exchange_first_tile(self):

        player = Player()
        bag = BagTiles()
        player.tiles.extend(bag.take(4))
        original_tile = player.tiles[0]

       
        player.exchange_tile(bag, original_tile)

        # Verificar que la ficha se haya intercambiado correctamente
        self.assertNotEqual(original_tile, player.tiles[0])
        
        
    def test_player_exchange_second_tile(self):
        
        player = Player()
        bag = BagTiles()
        player.tiles.extend(bag.take(3))
        original_tile = player.tiles[1]
        
        # Intercambiar el segundo ficha y comprobar si es diferente
        player.exchange_tile(bag, player.tiles[1])
        exchanged_tile = player.tiles[1]
        
        # Afirmar que los ficha son diferentes
        self.assertNotEqual(original_tile, exchanged_tile)


    def test_remove_tile(self):
        player = Player()
        player.tiles = [
            Tile(letter='C', value=4),
            Tile(letter='A', value=1),
            Tile(letter='S', value=1),
            Tile(letter='A', value=1),
        ]
        player.remove_tile(Tile("A",1))
        self.assertEqual(len(player.tiles),3)
    


if __name__ == '__main__':
    unittest.main()
