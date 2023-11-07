import unittest
from game.models import BagTiles
from game.tile import Tile
from game.player import Player
from game.scrabble import ScrabbleGame




class TestPlayer(unittest.TestCase):
    def test_init(self):
        player_1 = Player()
        self.assertEqual(
            len(player_1.tiles),
            0,
        )
  

    def test_take_tiles(self):
        player=Player()
        bag = BagTiles()
        player.take_tiles(bag, 7)
        self.assertEqual(len(player.tiles), 7)


    def test_score(self):
        player = Player()
        player.increase_score(5)
        self.assertEqual(player.get_score(), 5)
    


    def test_add_tile(self):
        player = Player()
        player.tiles = [
            Tile('C', 4),
            Tile('A', 1),
            Tile('S', 1),
            Tile('A', 1),
        ]
        player.add_tile(Tile("A",1))
        self.assertEqual(len(player.tiles),5)




    def test_refill_player_tiles(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.current_player.tiles = [
            Tile(letter="H", value=3)  
            ]
        scrabble_game.current_player.refill()
        self.assertEqual(scrabble_game.current_player.tiles[0].letter, "H")
        self.assertEqual(scrabble_game.current_player.tiles[0].value, 3)



    def test_validate_user_has_letters(self):
        bag_tile = BagTiles()
        player = Player()
        bag_tile.tiles = [
            Tile('H',1),
            Tile('O',1),
            Tile('L',1),
            Tile('A',1),
            Tile('C',1),
            Tile('U',1),
            Tile('M',1),
        ]
        tiles = [
            Tile('H', 1),
            Tile('O', 1),
            Tile('L', 1),
            Tile('A', 1),
        ]
        player.tiles = bag_tile.tiles 
        is_valid = player.has_letters(tiles)
        self.assertEqual(is_valid, True)


    def test_validate_fail_when_user_has_not_letters(self):
        bag_tile = BagTiles()
        player = Player()
        bag_tile.tiles = [
            Tile('P',1),
            Tile('O',1),
            Tile('L',1),
            Tile('A',1),
            Tile('C',1),
            Tile('U',1),
            Tile('M',1),
        ]
        tiles = [
            Tile('H', 1),
            Tile('O', 1),
            Tile('L', 1),
            Tile('A', 1),
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
            Tile('C', 4),
            Tile('A', 1),
            Tile('S', 1),
            Tile('A', 1),
        ]
        player.remove_tile(Tile("A",1))
        self.assertEqual(len(player.tiles),3)






if __name__ == '__main__':
    unittest.main()
