import unittest
from game.scrabble import ScrabbleGame, GameOverException
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

    def test_clean_word_to_use(self):
        game = ScrabbleGame(2)
        word = 'Imaginación'
        self.assertEqual(game.clean_word_to_use(word), 'IMAGINACION')

    def test_show_amount_tiles_bag(self):
        game = ScrabbleGame(2)
        self.assertEqual(game.show_amount_tiles_bag(), 100)

    
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


    def test_validate_word_invalid_placement(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.current_player = scrabble_game.players[0]

        word = "anticonstitucionalidad"
        orientation = "V"
        location = (7, 7)

        assert not scrabble_game.validate_word(word, location, orientation)


    def test_validate_word_NOT_EXIST_in_dictionary(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.current_player = scrabble_game.players[0]

        # Establece una palabra que no está en el diccionario
        word = "xyz"
        orientation = "H"
        location = (7, 7)

        assert not scrabble_game.validate_word(word, location, orientation)
    

    def test_word_playable_horizontally_by_current_player(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.current_player.tiles = [
            Tile('C', 3),
            Tile('A', 1),
            Tile('S', 1),
            Tile('A', 1),
        ]
        word = "Casa"
        orientation = "H"
        location = (7, 7)
        word_validate = scrabble_game.validate_word(word, location, orientation)
        assert word_validate is True


    def test_word_playable_vertically_by_current_player(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.current_player.tiles = [
            Tile('C', 3),
            Tile('A', 1),
            Tile('S', 1),
            Tile('A', 1),
        ]
        word = "Casa"
        orientation = "V"
        location = (7, 7)
        word_validate = scrabble_game.validate_word(word, location, orientation)
        assert word_validate is True


    def test_word_unplayable_without_sufficient_letters(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.current_player.tiles = [
            Tile('C', 3),
            Tile('A', 1),
            Tile('S', 1),
        ]
        word = "Casa"
        orientation = "V"
        location = (7, 7)
        word_validate = scrabble_game.validate_word(word, location, orientation)
        assert not word_validate


    def test_play_word_with_blank_space(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.current_player.tiles = [
            Tile('C', 3),
            Tile('A', 1),
            Tile('S', 1),
            Tile('A', 1),
        ]
        word = "Casa"
        orientation = "V"
        location = (7, 7)
        word_validate = scrabble_game.validate_word(word, location, orientation)
        assert word_validate is True


    def test_full_board(self):
        scrabble_game = ScrabbleGame(players_count=2)

        for i in range(7):
            for j in range(15):
                scrabble_game.board.grid[i][j].letter = Tile("T", 1)

        is_board_full = scrabble_game.is_board_full()
        self.assertFalse(is_board_full)



        

    def test_end_game_raises_exception(self):
        
        game = ScrabbleGame(players_count=2) # con 2 jugadores
        game.bag_tiles.tiles = []  # Vaciar la bolsa de fichas
        game.current_player = game.players[0]

        
        with self.assertRaises(GameOverException):
            game.end_game()

    def test_end_game_raises_exception(self):
        
        game = ScrabbleGame(players_count=3) # con 3 jugadores
        game.bag_tiles.tiles = []  # Vaciar la bolsa de fichas
        game.current_player = game.players[0]

        
        with self.assertRaises(GameOverException):
            game.end_game()


    def test_end_game_raises_exception(self):
        
        game = ScrabbleGame(players_count=4) # con 4 jugadores
        game.bag_tiles.tiles = []  # Vaciar la bolsa de fichas
        game.current_player = game.players[0]

        
        with self.assertRaises(GameOverException):
            game.end_game()


    def test_end_game_when_board_is_full(self):
        scrabble_game = ScrabbleGame(players_count=2)
    
        # Llenar el tablero con letras
        for row in scrabble_game.board.grid:
            for cell in row:
                cell.letter = Tile("T", 1)
    
        with self.assertRaises(GameOverException):
            scrabble_game.end_game()


    def test_end_game_false(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.bag_tiles.tiles = ['A']
        game_finish = scrabble_game.end_game()
        self.assertFalse(game_finish, False) 


    def test_score_board_2(self):
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = "Diego"
        scrabble_game.players[0].score = 30
        scrabble_game.players[1].name = "Facundo"
        scrabble_game.players[1].score = 8

        scoreboard = scrabble_game.end_score()

        self.assertEqual(scoreboard, [("Diego", 30), ("Facundo", 8)])


    def test_score_board_3(self):
        scrabble_game = ScrabbleGame(3)
        scrabble_game.players[0].name = "Diego"
        scrabble_game.players[0].score = 30
        scrabble_game.players[1].name = "Facundo"
        scrabble_game.players[1].score = 8
        scrabble_game.players[2].name = "Florencia"
        scrabble_game.players[2].score = 6

        scoreboard = scrabble_game.end_score()

        self.assertEqual(scoreboard, [("Diego", 30), ("Facundo", 8), ("Florencia", 6)])


    def test_has_wildcard(self):
        scrabble_game = ScrabbleGame(2)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.current_player.tiles = [Tile(" ", 0)]
        self.assertTrue(scrabble_game.has_wildcard())






    '''----------------DDD-------------------- '''





















    



        


if __name__ == '__main__':
    unittest.main()