import unittest
from game.scrabble import ScrabbleGame
from game.tile import Tile
from game.util import Util


class TestScrabbleGame(unittest.TestCase):
    def test_init(self):
        scrabble_game = ScrabbleGame(players_count=3)
        self.assertIsNotNone(scrabble_game.board)
        self.assertEqual(
            len(scrabble_game.players),
            3,
        )
        self.assertIsNotNone(scrabble_game.bag_tiles)

    # def test_playing(self):
    #     game = ScrabbleGame(players_count=2)
    #     self.assertTrue(game.playing())

    def test_clean_word_to_use(self):
        game = ScrabbleGame(2)
        word = 'Imaginación'
        self.assertEqual(game.clean_word_to_use(word), 'IMAGINACION')

    def test_show_amount_tiles_bag(self):
        game = ScrabbleGame(2)
        self.assertEqual(game.show_amount_tiles_bag(), 100)


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


    def test_end_game_false(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.bag_tiles.tiles = ['A']
        game_finish = scrabble_game.end_game()
        self.assertFalse(game_finish, False) 


    


   
    def test_has_wildcard(self):
        scrabble_game = ScrabbleGame(2)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.current_player.tiles = [Tile(" ", 0)]
        self.assertTrue(scrabble_game.has_wildcard())



    def test_calculator_vertical(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.bag_tiles.tiles = [
            Tile('C',3),
            Tile('A',1),
            Tile('S',1),
            Tile('A',1),
            Tile('B',3),
        ]
        scrabble_game.current_player.tiles.extend(scrabble_game.bag_tiles.take(5))
        word = "casa"
        orientation = "V"
        location = (7,7)
        scrabble_game.place_word_on_board(word,location,orientation)
        scrabble_game.calculator(word, location, orientation)


    def test_calculator_horizontal(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.bag_tiles.tiles = [
            Tile('C',3),
            Tile('A',1),
            Tile('S',1),
            Tile('A',1),
            Tile('B',3),
        ]
        scrabble_game.current_player.tiles.extend(scrabble_game.bag_tiles.take(5))
        word = "casa"
        orientation = "H"
        location = (7,7)
        scrabble_game.place_word_on_board(word,location,orientation)
        scrabble_game.calculator(word, location, orientation)


    def test_calculator_score(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.bag_tiles.tiles = [
            Tile('C', 3),
            Tile('A', 1),
            Tile('S', 1),
            Tile('A', 1),
            
        ]
        scrabble_game.current_player.tiles.extend(scrabble_game.bag_tiles.take(4))
        word = "casa"
        orientation = "H"
        location = (7,7)
        scrabble_game.place_word_on_board(word,location,orientation)
        scrabble_game.calculator(word, location, orientation)
        self.assertEqual(scrabble_game.current_player.score, 12)

    
    def test_place_word_on_board_horizontal(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.bag_tiles.tiles = [
            Tile('C', 3),
            Tile('A', 1),
            Tile('S', 1),
            Tile('A', 1),
        ]
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.current_player.tiles.extend(scrabble_game.bag_tiles.take(4))
        word = "casa"
        orientation = "H"
        location = (7, 7)
        scrabble_game.place_word_on_board(word, location, orientation)
        grid = scrabble_game.board.grid
        self.assertEqual(grid[7][7].letter.letter, "C")
        self.assertEqual(grid[7][8].letter.letter, "A")
        self.assertEqual(grid[7][9].letter.letter, "S")
        self.assertEqual(grid[7][10].letter.letter, "A")
        self.assertEqual(scrabble_game.current_player.tiles, [])



    def test_place_word_on_board_vertical(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.bag_tiles.tiles = [
            Tile('C', 3),
            Tile('A', 1),
            Tile('S', 1),
            Tile('A', 1),
        ]
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.current_player.tiles.extend(scrabble_game.bag_tiles.take(4))
        word = "casa"
        orientation = "V"
        location = (7, 7)
        scrabble_game.place_word_on_board(word, location, orientation)
        grid = scrabble_game.board.grid
        self.assertEqual(grid[7][7].letter.letter, "C")
        self.assertEqual(grid[8][7].letter.letter, "A")
        self.assertEqual(grid[9][7].letter.letter, "S")
        self.assertEqual(grid[10][7].letter.letter, "A")
        self.assertEqual(scrabble_game.current_player.tiles, [])



    def test_place_word_on_board_vertical_crossing(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.bag_tiles.tiles = [
            Tile('M', 3),
            Tile('A', 1),
            Tile('L', 1),
            Tile('A', 1),
        ]
        scrabble_game.current_player.tiles.extend(scrabble_game.bag_tiles.take(4))
        word = "mala"
        orientation = "V"
        location = (4,10)
        scrabble_game.board.grid[7][7].add_letter(Tile("C",2))
        scrabble_game.board.grid[7][8].add_letter(Tile("A",1))
        scrabble_game.board.grid[7][9].add_letter(Tile("S",2))
        scrabble_game.board.grid[7][10].add_letter(Tile("A",1))
        scrabble_game.place_word_on_board(word, location, orientation)
        self.assertEqual(scrabble_game.board.grid[4][10].letter.letter, "M") 
        self.assertEqual(scrabble_game.board.grid[5][10].letter.letter, "A") 
        self.assertEqual(scrabble_game.board.grid[6][10].letter.letter, "L") 
        self.assertEqual(scrabble_game.board.grid[7][10].letter.letter, "A")


 # VER COSO SE COLOCA 
    '''
   |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  | 10  | 11  | 12  | 13  | 14 | 
   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
0  | TWS |     |     | DLS |     |     |     | TWS |     |     |     | DLS |     |     | TWS |
   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
1  |     | DWS |     |     |     | TLS |     |     |     | TLS |     |     |     | DWS |     |
   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
2  |     |     | DWS |     |     |     | DLS |     | DLS |     |     |     | DWS |     |     |
   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
3  | DLS |     |     | DWS |     |     |     | DLS |     |     |     | DWS |     |     | DLS |
   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
4  |     |     |     |     | DWS |     |     |     |     |     |  M  |     |     |     |     |
   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
5  |     | TLS |     |     |     | TLS |     |     |     | TLS |  A  |     |     | TLS |     |
   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
6  |     |     | DLS |     |     |     | DLS |     | DLS |     |  L  |     | DLS |     |     |
   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
7  | TWS |     |     | DLS |     |     |     |  C  |  A  |  S  |  A  | DLS |     |     | TWS |
   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
8  |     |     | DLS |     |     |     | DLS |     | DLS |     |     |     | DLS |     |     |
   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
9  |     | TLS |     |     |     | TLS |     |     |     | TLS |     |     |     | TLS |     |
   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
10 |     |     |     |     | DWS |     |     |     |     |     | DWS |     |     |     |     |
   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
11 | DLS |     |     | DWS |     |     |     | DLS |     |     |     | DWS |     |     | DLS |
   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
12 |     |     | DWS |     |     |     | DLS |     | DLS |     |     |     | DWS |     |     |
   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
13 |     | DWS |     |     |     | TLS |     |     |     | TLS |     |     |     | DWS |     |
   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
14 | TWS |     |     | DLS |     |     |     | TWS |     |     |     | DLS |     |     | TWS |
   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


   '''
    
    def test_place_word_on_board_horizontal_with_split_groups_in_string(self):
        scrabble_game = ScrabbleGame(1)
        util = Util(scrabble_game)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.bag_tiles.tiles = [
            Tile('LL',8),
            Tile('A', 1),
            Tile('V', 4),
            Tile('E', 1),
        ]
        scrabble_game.current_player.tiles.extend(scrabble_game.bag_tiles.take(4))
        old_word = "llave"
        orientation = "H"
        location = (7,7)
        word = util.split_groups_in_string(old_word)
        scrabble_game.place_word_on_board(word, location, orientation)

        self.assertEqual(scrabble_game.board.grid[7][7].letter.letter, "LL") 
        self.assertEqual(scrabble_game.board.grid[7][8].letter.letter, "A") 
        self.assertEqual(scrabble_game.board.grid[7][9].letter.letter, "V") 
        self.assertEqual(scrabble_game.board.grid[7][10].letter.letter, "E")



    def test_score_board_2(self):
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = "Diego"
        scrabble_game.players[0].score = 30
        scrabble_game.players[1].name = "Facundo"
        scrabble_game.players[1].score = 8

        scoreboard = scrabble_game.rank_players_high_to_low_score()

        self.assertEqual(scoreboard, [("Diego", 30), ("Facundo", 8)])


    def test_score_board_3(self):
        scrabble_game = ScrabbleGame(3)
        scrabble_game.players[0].name = "Diego"
        scrabble_game.players[0].score = 30
        scrabble_game.players[1].name = "Facundo"
        scrabble_game.players[1].score = 8
        scrabble_game.players[2].name = "Florencia"
        scrabble_game.players[2].score = 6

        scoreboard = scrabble_game.rank_players_high_to_low_score()

        self.assertEqual(scoreboard, [("Diego", 30), ("Facundo", 8), ("Florencia", 6)])


    def test_validate_and_score_word(self):
        scrabble_game = ScrabbleGame(1)
        scrabble_game.board.grid[7][7].add_letter(Tile('G', 1))
        scrabble_game.board.grid[7][8].add_letter(Tile('A', 1)) 
        scrabble_game.board.grid[7][9].add_letter(Tile('T', 1)) 
        scrabble_game.board.grid[7][10].add_letter(Tile('A', 1)) 
        scrabble_game.board.grid[7][7].active = False
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.current_player.tiles = [Tile('C', 1), Tile('A', 1), Tile('S', 1), Tile('A', 1)]
        word = "casa"
        location = (3, 11)
        orientation = "V"
        scrabble_game.place_word_on_board(word, location, orientation)
        scrabble_game.calculator(word, location, orientation)
        scrabble_game.validate_and_score_word(word, location, orientation)
        self.assertEqual(scrabble_game.current_player.score, 8)



if __name__ == '__main__':
    unittest.main()






