# from game.scrabble import *
# from game.board import *
# from game.player import *

# class ScrabbleCli:
#     def main():
#         player_count = get_player_count()
#         game = ScrabbleGame(player_count)
#         while game.is_playing():
#             show_board(game.get_board())
#             show_player(*game.get_current_player())
#             word, coords, orientation = get_inputs()
#             try:
#                 game.play(word, coords, orientation)
#             except Exception as e:
#                 print(e)


#     def get_player_count():
#         while True:
#             try:
#                 player_count = int(input('cantidad de jugadores (1-4): '))
#                 if player_count <= 4:
#                     break
#             except Exception as e:
#                 print('ingrese un numero por favor')

#         return player_count



