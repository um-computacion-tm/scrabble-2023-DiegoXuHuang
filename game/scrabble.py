# from game.board import Board
# from game.player import Player
# from game.models import BagTiles
# from game.dictionary import * 
# from game.cell import *

# class DictionaryConnectionError(Exception):
#     pass
# class InvalidWordException(Exception):
#     pass
# class InvalidPlaceWordException(Exception):
#     pass



# class ScrabbleGame:
#     def __init__(self, players_count):
#         self.board = Board()
#         self.bag_tiles = BagTiles()
#         self.players = []
#         for _ in range(players_count):
#             self.players.append(Player())

#         self.current_player = None
#         self.turn = 0
#         self.board.add_premium_cells()


#     # falta test de playing
#     def playing(self):
#         return True
    
#     # falta definir  
#     def play(self, word, location, orientation):
#         self.validate_word(word, location, orientation)
#         words = self.board.put_words(word, location, orientation)
#         total = self.calculate_words_value(words)
#         self.players[self.current_player].score += total
#         self.next_turn()


    
#     def next_turn(self):
#         if self.current_player is None:
#             self.current_player = self.players[0]
#         else:
#             index = (self.players.index(self.current_player) + 1) % len(self.players)
#             self.current_player = self.players[index]
# # 
#     #falta definir

#     def validate_word(self, word, location, orientation):
#         if not dict_validate_word(word):
#             raise InvalidWordException("Su palabra no existe en el diccionario")
#         if not self.board.validate_word_inside_board(word, location, orientation):
#             raise InvalidPlaceWordException("Su palabra excede el tablero")
#         if not self.board.validate_word_place_board(word, location, orientation):
#             raise InvalidPlaceWordException("Su palabra esta mal puesta en el tablero")

 



#     def end_game(self):
#         if len(self.bag_tiles) == 0:
#             return True
#         return False
    



   
    






#     # def validate_word(self, word, location, orientation):
#     #     
#         #   '''
#         #   1- Validar que usuario tiene esas letras
#         #   2- Validar que la palabra entra en el tablero
#         #   '''
#     #     self.board.validate_word_inside_board(word, location, orientation)
    

#     #---------------------------
#     # def get_words():
#     #     '''
#     #     Obtener las posibles palabras que se pueden formar, dada una palabra, ubicacion y orientacion 
#     #     Preguntar al usuario, por cada una de esas palabras, las que considera reales
#     #     '''
    
#     # def put_words():
#     #     '''
#     #     Modifica el estado del tablero con las palabras consideradas como correctas
#     #     '''


