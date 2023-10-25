from game.board import Board
from game.player import Player
from game.models import BagTiles
from game.dictionary import * 
from game.cell import *


class DictionaryConnectionError(Exception):
    pass
class InvalidWordException(Exception):
    pass
class InvalidPlaceWordException(Exception):
    pass



class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = [Player() for _ in range(players_count)]
        self.current_player = None
        self.turn = 0
        self.board.add_premium_cells()
        self.dictionary = Dictionary('dictionaries/diccionario.txt')

    

        


    # falta test de playing
    def playing(self):
        return True
    
    # falta definir  
    # def play(self, word, location, orientation):
    #     self.validate_word(word, location, orientation)
    #     words = self.board.put_words(word, location, orientation)
    #     total = self.calculate_words_value(words)
    #     self.players[self.current_player].score += total
    #     self.next_turn()
    #     self.dictionary = Dictionary('dictionaries/dictionary.txt')


    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        else:
            index = (self.players.index(self.current_player) + 1) % len(self.players)
            self.current_player = self.players[index]

    #refill lo tengo en el archivo Player,

# 
    #falta definir



    
    def validate_word(self, word, location, orientation):
        # Comprueba si la palabra puede colocarse en el tablero
        if not self.board.validate_word_place_board(word, location, orientation):
            return False
    
        # Comprueba si la palabra está en el diccionario
        if not self.dictionary.has_word(word):
            return False
    
        # me falta validar si el jugador tiene las fichas necesarias para format la palabra/jugar
        # # Comprueba si el jugador tiene las letras necesarias para formar la palabra
        # if not self.current_player.has_letters(self.board.mletter):
        #     return False

        # return True


    # def validate_word(self, word, location, orientation):
    #     if not dict_validate_word(word):
    #         raise InvalidWordException("Su palabra no existe en el diccionario")
    #     if not self.board.validate_word_inside_board(word, location, orientation):
    #         raise InvalidPlaceWordException("Su palabra excede el tablero")
    #     if not self.board.validate_word_place_board(word, location, orientation):
    #         raise InvalidPlaceWordException("Su palabra esta mal puesta en el tablero")
    

  
    def is_board_full(self):
        cell_has_letter = [cell.letter is not None for row in self.board.grid for cell in row]
        return all(cell_has_letter)
    




    # def end_game(self):
    #     if len(self.bag_tiles) == 0:
    #         return True
    #     return False



   
    






    # def validate_word(self, word, location, orientation):
    #     
        #   '''
        #   1- Validar que usuario tiene esas letras
        #   2- Validar que la palabra entra en el tablero
        #   '''
    #     self.board.validate_word_inside_board(word, location, orientation)
    

    #---------------------------
    # def get_words():
    #     '''
    #     Obtener las posibles palabras que se pueden formar, dada una palabra, ubicacion y orientacion 
    #     Preguntar al usuario, por cada una de esas palabras, las que considera reales
    #     '''
    
    # def put_words():
    #     '''
    #     Modifica el estado del tablero con las palabras consideradas como correctas
    #     '''






 
  
  
    

    
