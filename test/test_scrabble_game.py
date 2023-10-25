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



    def test_full_board(self):
        scrabble_game = ScrabbleGame(players_count=2)

        for i in range(7):
            for j in range(15):
                scrabble_game.board.grid[i][j].letter = Tile("T", 1)

        is_board_full = scrabble_game.is_board_full()
        self.assertFalse(is_board_full)



    def test_end_game(self):
        scrabble_game = ScrabbleGame(players_count=4)
        scrabble_game.bag_tiles = []  
        self.assertTrue(scrabble_game.end_game())




 

    

        


if __name__ == '__main__':
    unittest.main()