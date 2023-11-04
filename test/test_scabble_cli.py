import unittest
from game.scrabble_cli import *
from unittest.mock import patch
from io import StringIO
from game.tile import Tile


class TestCli(unittest.TestCase):
    
        
    @patch('builtins.input', return_value="3")
    def test_init(self, patchInput):
        cli = ScrabbleCli(patchInput)
        self.assertIsInstance(cli.game, ScrabbleGame)
    
       
    @patch('builtins.input', side_effect=['Diego', 'Facu', 'Mario'])
    def test_scrabble_cli_with_names(self, patchInput):
        scrabble_cli = ScrabbleCli(3)
        scrabble_cli.get_players_name(3)        
        names = ['Diego', 'Facu', 'Mario']
        for i in range(3):
            self.assertEqual(scrabble_cli.game.players[i].name, names[i])
            
    @patch('builtins.print')
    def test_show_score(self, print_patched):
        scrabble_cli = ScrabbleCli(3)
        scrabble_cli.game.current_player = scrabble_cli.game.players[0]
        scrabble_cli.game.current_player.score = 50
        scrabble_cli.show_score()
        

    @patch('builtins.print')
    def test_show_tiles(self, print_patched):
        scrabble_cli = ScrabbleCli(3)
        scrabble_cli.game.current_player = scrabble_cli.game.players[0]
        scrabble_cli.game.current_player.tiles = [ Tile("A",1), Tile("B",2), Tile("C",3), Tile("D",2), Tile("E",1), Tile("F",4), Tile("G",2)]
        scrabble_cli.show_tiles()
        
   

    @patch('builtins.input', return_value='2')
    def test_exchange_tiles(self, input_patched):
        
        scrabble_cli = ScrabbleCli(1)
        scrabble_cli.game.current_player = scrabble_cli.game.players[0]
        scrabble_cli.game.current_player.tiles = [ Tile("A",1), Tile("B",2), Tile("C",3), Tile("D",2), Tile("E",1), Tile("F",4), Tile("G",2),
        ]
        scrabble_cli.exchange_tile()
        
        
    @patch('builtins.input', return_value="H")
    def test_wildcard(self, input_patched):
        scrabble_cli = ScrabbleCli(1)
        scrabble_cli.game.current_player = scrabble_cli.game.players[0]
        scrabble_cli.game.current_player.tiles = [
            Tile(" ",0),
        ]
        scrabble_cli.wildcard()
        self.assertEqual(scrabble_cli.game.current_player.tiles[0].letter, "H")


    @patch('builtins.print')
    @patch('builtins.input', side_effect=["7","1","3"])
    def test_show_menu_show_board(self, patchInput, patchPrint):
        
        scrabble_cli = ScrabbleCli(2)
        scrabble_cli.game.current_player = scrabble_cli.game.players[0]
        scrabble_cli.game.current_player.tiles = [ Tile("C",1), Tile("A",1), Tile("S",1), Tile("A",1),
        ]

        scrabble_cli.show_menu()

        
    @patch('builtins.print')
    @patch('builtins.input', side_effect=["2","1","4"])
    def test_show_menu_exchange_tiles(self, patchInput, patchPrint):
        
        scrabble_cli = ScrabbleCli(2)
        scrabble_cli.game.current_player = scrabble_cli.game.players[0]
        scrabble_cli.game.current_player.tiles = [
            Tile("C",1), Tile("A",1), Tile("S",1), Tile("A",1),
        ]

        scrabble_cli.show_menu()


        
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['A', "9", '3'])
    def test_get_row(self, input_patched, print_patched):
        scrabble_cli = ScrabbleCli(1)
        scrabble_cli.get_row()
        

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['G', "0", '7'])
    def test_get_col(self, input_patched, print_patched):
        scrabble_cli = ScrabbleCli(1)
        scrabble_cli.get_col()
        

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['T', "3", 'V'])
    def test_get_orientation_horizontal(self, input_patched, print_patched):
        scrabble_cli = ScrabbleCli(1)
        scrabble_cli.orientation()
        

    def test_end_current_turn(self):
        scrabble_cli = ScrabbleCli(3)
        with self.assertRaises(FinshiTurnException):
            scrabble_cli.end_current_turn()
        
  
        
       
    @patch('builtins.input', side_effect=["CASA", "3", "7", "H", " "])
    @patch('builtins.print')
    def test_go_back(self, patchInput, patchPrint):
        
        scrabble_cli = ScrabbleCli(2)  
        
        scrabble_cli.game.current_player = scrabble_cli.game.players[0]
        scrabble_cli.game.current_player.tiles = [ Tile("C",1), Tile("A",1), Tile("S",1), Tile("A",1), Tile("M",1), Tile("I",1), Tile("E",1), Tile("N",1), Tile("T",1), Tile("A",1)]
        
        scrabble_cli.input_play_word()  
            
    @patch('builtins.print')
    @patch('builtins.input', side_effect=["0", "hola", "7", "7", "V"])
    def test_show_menuplac_word(self, patchInput, patchPrint):
        
        scrabble_cli = ScrabbleCli(2)
        scrabble_cli.game.current_player = scrabble_cli.game.players[0]
        scrabble_cli.game.current_player.tiles = [ Tile("A",1), Tile("H",1), Tile("O",1), Tile("L",1),
        ]

        scrabble_cli.show_menu()
        

    
        
  
               
if __name__ == '__main__':
    unittest.main()