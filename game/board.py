from game.cell import Cell
from game.util import Util

TRIPLE_WORD_SCORE = ((0,0),(7,0),(14,0),(0,7),(14,7),(0,14),(7,14),(14,14))
DOUBLE_WORD_SCORE = ((1,1),(2,2),(3,3),(4,4),(10,10),(11,11),(12,12),(13,13),(1,13),(2,12),(3,11),(4,10),(7,7),(13,1),(12,2),(11,3),(10,4))
TRIPLE_LETTER_SCORE = ((1,5),(1,9),(5,1),(5,5),(5,9),(5,13),(9,1),(9,5),(9,9),(9,13),(13,5),(13,9))
DOUBLE_LETTER_SCORE = ((0,3),(0,11),(2,6),(2,8),(3,0),(3,7),(3,14),(6,2),(6,6),(6,8),(6,12),(7,3),(7,11),(8,2),(8,6),(8,8),(8,12),(11,0),(11,7),(11,14),(12,6),(12,8),(14,3),(14,11))

class NoCenterLetterException(Exception):
    pass

class WordPlacementException(Exception):
    pass

class Board:
    def __init__(self):
        self.grid = [ [ Cell(1, '') for _ in range(15) ] for _ in range(15) ]
        self.add_premium_cells()
        self.is_empty = None
        self.util = Util()


    def set_cell_multiplier(self, coordinate, multiplier_type, multiplier_value):
        cell = self.grid[coordinate[0]][coordinate[1]]
        cell.multiplier_type = multiplier_type
        cell.multiplier = multiplier_value


    def modify_letter(self, letter):
        if self.util.is_word_letters(self.mletter):
            self.mletter = [l for l in self.mletter if l != letter]
        else:
            self.mletter = ''.join(l for l in self.mletter if l != letter)


    def add_premium_cells(self):
        for coordinate in TRIPLE_WORD_SCORE:
            self.set_cell_multiplier(coordinate, "W", 3)
        for coordinate in DOUBLE_WORD_SCORE:
            self.set_cell_multiplier(coordinate, "W", 2)
        for coordinate in TRIPLE_LETTER_SCORE:
            self.set_cell_multiplier(coordinate, "L", 3)
        for coordinate in DOUBLE_LETTER_SCORE:
            self.set_cell_multiplier(coordinate, "L", 2)

    def is_out_of_bounds(self, row, col):
        return not (0 <= row < len(self.grid)) or not (0 <= col < len(self.grid[0]))


    def validate_word_inside_board(self, word, location, orientation):
        word = [letter.upper() for letter in word] if self.util.is_word_list(word) else word.upper()
        self.word = word
        self.orientation = orientation
        self.position_row, self.position_col = location

        if orientation == 'H':
            return len(word) <= 15 - self.position_col
        elif orientation == 'V':
            return len(word) <= 15 - self.position_row
        else:
            return False  


    def update_position(self, orientation):
        if orientation == "H":
            self.position_col += 1
        elif orientation == "V":
            self.position_row += 1

        return self.position_row, self.position_col
    

    def empty(self):
        # Verifica si el tablero está vacío
        self.is_empty = self.grid[7][7].letter is None


    def validate_word_center(self, orientation):
        if (self.position_row, self.position_col) == (7, 7):
            return True
    
        row_offset, col_offset = (0, 1) if orientation == "H" else (1, 0)

        for i in self.word:
            self.position_row += row_offset
            self.position_col += col_offset
            if (self.position_row, self.position_col) == (7, 7):
                return True

        return False
    



    def validate_word_placement_in_occupied_grid(self, orientation):
        row, col = self.position_row, self.position_col

        for letter in self.word:
            if self.is_out_of_bounds(row, col):
                return False

            cell = self.grid[row][col]

            if cell.letter is not None and letter != cell.letter.letter:
                return False

            self.modify_letter(letter)

            row, col = self.update_position(orientation)

        return True



    def show_board(self):
        board_str = "   |  " + "  |  ".join(str(item) for item in range(10)) + "  | " + "  | ".join(str(item) for item in range(10, 15)) + " |"
        board_str += "\n   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n"
        board = list(self.grid)
        for i in range(len(board)):
            if i < 10:
                board[i] = f"{i}  | {' | '.join(map(str, board[i]))} |"
            # if i < 10:
            #     board[i] = str(i) + "  | " + " | ".join(str(item) for item in board[i]) + " |"
            if i >= 10:
                board[i] = str(i) + " | " + " | ".join(str(item) for item in board[i]) + " |"
        board_str += "\n   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|\n".join(board)
        board_str += "\n   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _"
        print(board_str)



    def validate_word_place_board(self, word, location, orientation):
        
        # word = [letter.upper() for letter in word] if self.util.is_word_list(word) else word.upper()
        if self.util.is_word_list(word):
            word = [letter.upper() for letter in word]
        else:
            word = word.upper()

        valid = self.validate_word_inside_board(word, location, orientation)
        self.empty()
        self.mletter = word

        if valid:
            return self.validate_word_center(orientation) if self.is_empty else self.validate_word_placement_in_occupied_grid(orientation)
        return False




        

