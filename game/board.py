from game.cell import Cell
from game.models import Tile

TRIPLE_WORD_SCORE = ((0, 0), (7, 0), (14, 0), (0, 7), (14, 7), (0, 14), (7, 14), (14, 14))
DOUBLE_WORD_SCORE = ((1, 1), (2, 2), (3, 3), (4, 4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2),
                    (11, 3), (10, 4), (13, 13), (12, 12), (11, 11), (10, 10))
TRIPLE_LETTER_SCORE = (
    (1, 5), (1, 9), (5, 1), (5, 5), (5, 9), (5, 13), (9, 1), (9, 5), (9, 9), (9, 13), (13, 5), (13, 9))
DOUBLE_LETTER_SCORE = (
    (0, 3), (0, 11), (2, 6), (2, 8), (3, 0), (3, 7), (3, 14), (6, 2), (6, 6), (6, 8), (6, 12), (7, 3), (7, 11),
    (8, 2), (8, 6), (8, 8), (8, 12), (11, 0), (11, 7), (11, 14), (12, 6), (12, 8), (14, 3), (14, 11))

class NoCenterLetterException(Exception):
    pass

class Board:
    def __init__(self):
        self.grid = [ [ Cell(1, '') for _ in range(15) ] for _ in range(15) ]
        self.add_premium_cells()
        self.is_empty = None
           
    
    def set_cell_multiplier(self, coordinate, multiplier_type, multiplier_value):
        cell = self.grid[coordinate[0]][coordinate[1]]
        cell.multiplier_type = multiplier_type
        cell.multiplier = multiplier_value

    def add_premium_cells(self):
        for coordinate in TRIPLE_WORD_SCORE:
            self.set_cell_multiplier(coordinate, "word", 3)
        for coordinate in DOUBLE_WORD_SCORE:
            self.set_cell_multiplier(coordinate, "word", 2)
        for coordinate in TRIPLE_LETTER_SCORE:
            self.set_cell_multiplier(coordinate, "letter", 3)
        for coordinate in DOUBLE_LETTER_SCORE:
            self.set_cell_multiplier(coordinate, "letter", 2)



    def validate_word_inside_board(self, word, location, orientation):
        word = [letter.upper() for letter in word] if isinstance(word, list) else word.upper()
        self.word = word
        self.orientation = orientation
        self.position_row, self.position_col = location

        if orientation == 'H':
            return len(word) <= 15 - self.position_col
        elif orientation == 'V':
            return len(word) <= 15 - self.position_row
        else:
            return False  


   
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
    


    def empty(self):
        # Verifica si el tablero está vacío
        self.is_empty = self.grid[7][7].letter is None


    def validate_word_place_board_is_empty(self, orientation):
        if (self.position_row, self.position_col) == (7, 7):
            return True
    
        # Definir el desplazamiento en función de la orientación
        row_offset, col_offset = (0, 1) if orientation == "H" else (1, 0)

        for i in self.word:
            self.position_row += row_offset
            self.position_col += col_offset
            if (self.position_row, self.position_col) == (7, 7):
                return True

        return False
    


    def validate_word_place_board_is_not_empty(self, orientation):
        def update_letters_container(letters, letter):
            if isinstance(letters, list):
                return [l for l in letters if l != letter]
            else:
                return "".join([l for l in letters if l != letter])

        for i in self.word:
            cell = self.grid[self.position_row][self.position_col]

            if cell.letter is not None:
                if i != cell.letter.letter:
                    return False

                self.mletter = update_letters_container(self.mletter, i)

            self.position_row, self.position_col = self.update_position(orientation)

        return True
    
    

    def update_position(self, orientation):
        if orientation == "H":
            self.position_col += 1
        elif orientation == "V":
            self.position_row += 1

        return self.position_row, self.position_col



    def validate_word_place_board(self, word, location, orientation):
        #este método se utiliza para validar si una palabra dada se puede colocar en el tablero en una ubicación y orientación específicas, 
        #teniendo en cuenta si el tablero está vacío o si ya contiene letras en algunas celdas
        
        valid = self.validate_word_inside_board(word, location, orientation)
        self.empty()
        self.mletter = word

        if valid and self.is_empty:
            return self.validate_word_place_board_is_empty(orientation)
        elif valid:
            return self.validate_word_place_board_is_not_empty(orientation)
        return False
    
    


    def show_board(board):
    #toma un tablero y muestra una representación legible de ese tablero en la consola
        print('\n  |' + ''.join([f' {str(row_index).rjust(2)} ' for row_index in range(15)]))
        for row_index, row in enumerate(board.grid):
            print(
                str(row_index).rjust(2) +
                '| ' +
                ' '.join([repr(cell) for cell in row])
            )


   
    


    

    
  




        
    
           
                
        
        




    
    



 





    



    






    
   
    



   



    


  


 



    


 