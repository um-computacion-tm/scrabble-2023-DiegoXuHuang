import unittest
from game.scrabble import ScrabbleGame
from game.tile import Tile



class TestScrabbleGame(unittest.TestCase):
    def test_init(self):
        scrabble_game = ScrabbleGame(players_count=3)
        self.assertIsNotNone(scrabble_game.board)
        self.assertEqual(
            len(scrabble_game.players),
            3,
        )
        self.assertIsNotNone(scrabble_game.bag_tiles)

    def test_playing(self):
        game = ScrabbleGame(players_count=2)
        self.assertTrue(game.playing())
    
 
    
    def test_next_turn_when_game_is_starting(self):
        scrabble_game = ScrabbleGame(players_count=3)

        scrabble_game.next_turn()

        assert scrabble_game.current_player == scrabble_game.players[0]


    def test_next_turn_when_player_is_not_the_first(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[0]

        scrabble_game.next_turn()

        assert scrabble_game.current_player == scrabble_game.players[1]

    def test_next_turn_when_player_is_last(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[2]

        scrabble_game.next_turn()

        assert scrabble_game.current_player == scrabble_game.players[0]

#------------------------------

    def test_validate_word_NOT_EXITS_in_dictionary(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.current_player = scrabble_game.players[0]

        # Establece una palabra que no está en el diccionario
        word = "xyz"
        orientation = "H"
        location = (7, 7)

        # Llama a la función para validar la palabra
        word_validate = scrabble_game.validate_word(word, location, orientation)

        # Asegura que la palabra no esté en el diccionario
        assert word_validate is False


    def test_validate_word_invalid_placement(self):
        # check de si la palabra esta fuera del tablero
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.bag_tiles.tiles = [
            Tile(letter='A', value=3),
            Tile(letter='N', value=1),
            Tile(letter='T', value=1),
            Tile(letter='I', value=3),
            Tile(letter='C', value=1),
            Tile(letter='O', value=1),
            Tile(letter='N', value=3),
            Tile(letter='S', value=1),
            Tile(letter='T', value=1),
            Tile(letter='I', value=3),
            Tile(letter='T', value=1),
            Tile(letter='U', value=1),
            Tile(letter='C', value=1),
            Tile(letter='I', value=1),
            Tile(letter='O', value=1),
            Tile(letter='N', value=1),
            Tile(letter='A', value=1),
            Tile(letter='L', value=1),
            Tile(letter='I', value=1),
            Tile(letter='D', value=1),
            Tile(letter='A', value=1),
            Tile(letter='D', value=1),
        ]
        scrabble_game.current_player.tiles.extend(scrabble_game.bag_tiles.take(22))
        word = "anticonstitucionalidad"
        orientation = "V"
        location = (7,7)
        word_validate = scrabble_game.validate_word(word, location, orientation)
        assert word_validate == False
        





#-------------------------------
    def test_full_board(self):
        scrabble_game = ScrabbleGame(players_count=2)

        for i in range(7):
            for j in range(15):
                scrabble_game.board.grid[i][j].letter = Tile("T", 1)

        is_board_full = scrabble_game.is_board_full()
        self.assertFalse(is_board_full)



    # def test_end_game(self):
    #     scrabble_game = ScrabbleGame(players_count=4)
    #     scrabble_game.bag_tiles = []  
    #     self.assertTrue(scrabble_game.end_game())




 

    

        


if __name__ == '__main__':
    unittest.main()