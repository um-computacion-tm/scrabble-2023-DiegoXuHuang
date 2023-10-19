from game.cell import Cell
from game.tile import Tile



class Board:
    def __init__(self):
        self.grid = [ [ Cell(1, '') for _ in range(15) ] for _ in range(15) ]
        self.add_premium_cells()

    

    def calculate_word_value(self, word):
    #calcular valor de la palabra
        total_value = 0
        word_multiplier = 1

        for cell in word:
            tile = cell.letter
            tile_value = tile.value

            if cell.active:
                if cell.multiplier_type == 'letter':
                    tile_value *= cell.multiplier
                elif cell.multiplier_type == 'word':
                    word_multiplier *= cell.multiplier

            total_value += tile_value

        return total_value * word_multiplier
    
    
    
    def add_premium_cells(self):
        #Agrega todos los cuadrados premium que influyen en la puntuación de la palabra.
        TRIPLE_WORD_SCORE = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
        DOUBLE_WORD_SCORE = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10))
        TRIPLE_LETTER_SCORE = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
        DOUBLE_LETTER_SCORE = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))

        for coordinate in TRIPLE_WORD_SCORE:
            self.grid[coordinate[0]][coordinate[1]] = "TWS"
        for coordinate in TRIPLE_LETTER_SCORE:
            self.grid[coordinate[0]][coordinate[1]] = "TLS"
        for coordinate in DOUBLE_WORD_SCORE:
            self.grid[coordinate[0]][coordinate[1]] = "DWS"
        for coordinate in DOUBLE_LETTER_SCORE:
            self.grid[coordinate[0]][coordinate[1]] = "DLS"

    

    def validate_word_inside_board(self, word, location, orientation):
    # verifica que la palabra este dentro del trablero
        self.orientation = orientation
        self.position_row = location[0]
        self.position_col = location[1]

        #x, y = location
        len_word = len(word)
        board_size = 15  # Tamaño del tablero 15x15

        if orientation == "H" and self.position_row + len_word <= board_size:
            return True
        elif orientation == "V" and self.position_col + len_word <= board_size:
            return True

        return False
    

    
    
    
    def is_empty(self):
        # verifica que el tablero este vacio
        if self.grid[7][7].letter == None:
            self.is_empty = True
        else:
            self.is_empty = False




    #test
    def show_board(board):
        print('\n  |' + ''.join([f' {str(row_index).rjust(2)} ' for row_index in range(15)]))
        for row_index, row in enumerate(board.grid):
            print(
                str(row_index).rjust(2) +
                '| ' +
                ' '.join([repr(cell) for cell in row])
            )



    
    



 





    



    






    
   
    



   



    


  


 



    


 