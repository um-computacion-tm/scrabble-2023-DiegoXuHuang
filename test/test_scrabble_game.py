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




   


   




 

    

        


if __name__ == '__main__':
    unittest.main()