from game.board import Board
from game.player import Player
from game.models import BagTiles
from game.dictionary import * 
from game.cell import CalculateWordValue
from game.util import Util
from operator import attrgetter
import sys




class InvalidPlaceWordException(Exception):
    pass
class GameOverException(Exception):
    pass
class MissingLettersException(Exception):
    pass

'''---dddd--'''


class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = [Player() for _ in range(players_count)]
        self.current_player = None
        self.turn = 0
        self.util = Util()
        self.board.add_premium_cells()
        self.dictionary = Dictionary('dictionaries/diccionario.txt')


    


    # cli
    def clean_word_to_use(self, word):
        word = self.dictionary.remove_accents(word)
        word = word.strip().upper()
        return word


    def show_amount_tiles_bag(self):
        return len(self.bag_tiles.tiles)


    def playing(self):
        return True
    

    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        else:
            index = (self.players.index(self.current_player) + 1) % len(self.players)
            self.current_player = self.players[index]


    # TESTING
    def validate_word(self, word, location, orientation):
        # Comprueba si la palabra puede colocarse en el tablero
        if not self.board.validate_word_place_board (word, location, orientation):
            # raise InvalidPlaceWordException("La palabra no puede ser colocada en esa posición. Asegúrate de que la ubicación y la orientación sean válidas y de que la palabra se ajuste correctamente en el tablero.")
            return False
    
        # Comprueba si la palabra está en el diccionario
        if not self.dictionary.has_word(word):
            # raise InvalidWordException("Su palabra no existe en el diccionario")
            return False
    
        # Comprueba si el jugador tiene las letras necesarias para formar la palabra
        if not self.current_player.has_letters(self.board.mletter):
            # raise MissingLettersException("No tienes las letras necesarias para formar esta palabra. Verifica tus letras disponibles antes de intentar jugar.")
            return False

        return True
    

    
    def is_board_full(self):
        cell_has_letter = [cell.letter is not None for row in self.board.grid for cell in row]
        return all(cell_has_letter)
    


    def end_game(self):
        if self.is_board_full() or (not self.bag_tiles.tiles and not self.current_player.tiles):
            raise GameOverException
            #self.end_game_directly(message)


    def end_game_directly(self, message="El juego ha sido finalizado"):
        print(message)
        sys.exit(0) 
    
    
    # ending scrore
    # show score
    def end_score(self):
        self.players.sort(key=attrgetter('score'), reverse=True)
        return [(player.name, player.score) for player in self.players]
    

    def has_wildcard(self):
        return any(tile.value == 0 for tile in self.current_player.tiles)
    

    # def check_orientation_valid(self, orientation):
    #     return orientation if orientation in {'H', 'V'} else None


    def get_word_score(self, cells, word_value_calculator = CalculateWordValue()):
        return word_value_calculator.calculate_word(cells)
    


    def get_word_cells(self, word, location, orientation):
        row, col = location
        cells = []

        for letter in word:
            if 0 <= row < len(self.board.grid) and 0 <= col < len(self.board.grid[0]):
                cells.append(self.board.grid[row][col])
                row, col = self.util.update_coordinates(orientation, row, col)
            else:
                cells.append(None)  
                break

        return cells
    


    def update_player_score(self, word_value):
        self.current_player.score += word_value
        self.previus = self.current_player.score - word_value


    











    



   






  






    
                

        

        
