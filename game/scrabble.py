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
class EndTurnException(Exception):
    pass

class InvalidWordException(Exception):
    pass

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
        index = (self.players.index(self.current_player) + 1)
        if index >= self.players_count:index=0
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
    


    def find_tile_letter(self, letter):
        for tile in self.current_player.tiles:
            if tile.letter == letter:
                return tile
        return None
    


    def update_player_score(self, word_value):
        self.current_player.score += word_value
        self.previus = self.current_player.score - word_value




    def calculator(self, word, location, orientation):
        validity_check = self.validate_word(word, location, orientation)
        
        if not validity_check:
            return  

        word_cell = self.get_word_cells(word, location, orientation)
        
        word_value = self.get_word_score(word_cell)

        self.update_player_score(word_value)

        [cell.deactivate_cell() for cell in word_cell]

    

    def place_word_on_board(self, word, location, orientation):
        row, col = location

        if not self.validate_word(word, location, orientation):
            return

        word = [letter.upper() for letter in word] if self.util.is_word_list(word) else word.upper()

        for letter in word:
            selected_tile = self.find_tile_letter(letter)
            if selected_tile:
                tile_row, tile_col = self.util.update_coordinates(orientation, row, col)
                self.board.grid[row][col].add_letter(selected_tile)
                self.current_player.remove_tile(selected_tile)
                row, col = tile_row, tile_col

    
    def rank_players_high_to_low_score(self):
        self.players.sort(key=attrgetter('score'), reverse=True)
        return [(player.name, player.score) for player in self.players]
    
    
    def show_results(self):
        top_players = self.rank_players_high_to_low_score()

        if top_players:
            print("Puntaje Final:")
            print("+------------------+-------+")
            print("| Jugadores        | Score |")
            print("+------------------+-------+")
            for position, (player, score) in enumerate(top_players, 1):
                print(f"| {player:16} | {score:5} |")
            print("+------------------+-------+")

            print(f"GANADOR: {top_players[0][0]}")
    

    







    



   






  






    
                

        

        
