from game.cell import Cell
from game.util import Util
from game.dictionary import Dictionary



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
        self.dict = Dictionary
        
        
        

    def update_position(self, orientation):
        
        orientation_mapping = {
            "H": (0, 1),  
            "V": (1, 0),  
        }

        
        if orientation in orientation_mapping:
            row_change, col_change = orientation_mapping[orientation]
            self.position_row += row_change
            self.position_col += col_change

        return self.position_row, self.position_col



    def is_out_of_bounds(self, row, col):

        if row < 0 or row >= len(self.grid):
            return True
        
        if col < 0 or col >= len(self.grid[0]):
            return True
        
        return False
    

    def transform_word_to_upper(self, word):
        return [letter.upper() for letter in word] if self.util.is_word_list(word) else word.upper()



    def set_cell_multiplier(self, coordinate, multiplier_type, multiplier_value):
        cell = self.grid[coordinate[0]][coordinate[1]]
        cell.multiplier_type = multiplier_type
        cell.multiplier = multiplier_value



    def modify_letter(self, letter):
        if self.util.is_word_letters(self.mletter):
            self.mletter = [l for l in self.mletter if l != letter]
        else:
            modified_mletter = []
            for l in self.mletter:
                if l != letter:
                    modified_mletter.append(l)
            self.mletter = ''.join(modified_mletter)

    
    def check_position(self, word, row, col, orientation):
        if (row, col) == (7, 7):
            return True
        if not word:
            return False
        row_offset, col_offset = (0, 1) if orientation == "H" else (1, 0)
        return self.check_position(word[1:], row + row_offset, col + col_offset, orientation)



    def add_premium_cells(self):
        for coordinate in TRIPLE_WORD_SCORE:
            self.set_cell_multiplier(coordinate, "W", 3)
        for coordinate in DOUBLE_WORD_SCORE:
            self.set_cell_multiplier(coordinate, "W", 2)
        for coordinate in TRIPLE_LETTER_SCORE:
            self.set_cell_multiplier(coordinate, "L", 3)
        for coordinate in DOUBLE_LETTER_SCORE:
            self.set_cell_multiplier(coordinate, "L", 2)

   
    def validate_word_inside_board(self, word, location, orientation):
        word = self.transform_word_to_upper(word)
        
        self.word = word
        self.orientation = orientation
        self.position_row, self.position_col = location

        if orientation == 'H':
            return len(word) <= 15 - self.position_col
        elif orientation == 'V':
            return len(word) <= 15 - self.position_row
        else:
            return False


    def empty(self):
        # Verifica si el tablero está vacío
        self.is_empty = self.grid[7][7].letter is None


    
    def validate_word_center(self, orientation):
        if (self.position_row, self.position_col) == (7, 7):
            return True

        return self.check_position(self.word, self.position_row, self.position_col, orientation)


    def is_adjacent_to_tile(self, row, col):
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue 
                r, c = row + dr, col + dc
                if 0 <= r < 15 and 0 <= c < 15 and self.grid[r][c].letter is not None:
                    return True
        return False


    def validate_word_placement(self, word, location, orientation):
        
        if not self.validate_word_place_board(word, location, orientation):
            return False

        if orientation == 'H':
            for i in range(len(word)):
                if self.is_adjacent_to_tile(self.position_row, self.position_col + i):
                    return True
        elif orientation == 'V':
            for i in range(len(word)):
                if self.is_adjacent_to_tile(self.position_row + i, self.position_col):
                    return True

        return False



    def validate_word_placement_in_occupied_grid(self, orientation):
        row, col = self.position_row, self.position_col
        word_iterator = iter(self.word)

        while True:
            if self.is_out_of_bounds(row, col):
                return False

            cell = self.grid[row][col]
            letter = next(word_iterator, None)

            if letter is None:
                break

            if cell.letter is not None and letter != cell.letter.letter:
                return False

            self.modify_letter(letter)
            row, col = self.update_position(orientation)

        if any(word_iterator):
            return False

        return True




    def show_board(self):
        def colored(text, color):
            colors = {
                'reset': '\033[0m',
                'green': '\033[92m',
                'purple': '\033[94m',
            }
            return f"{colors[color]}{text}{colors['reset']}"

        board_str = "   ║  " + "  ║  ".join(str(item) for item in range(10)) + "  ║ " + "  ║ ".join(str(item) for item in range(10, 15)) + " ║"
        board_str += "\n   ═══════════════════════════════════════════════════════════════════════════════════════════\n"
        board = list(self.grid)
        for i in range(len(board)):
            if i < 10:
                board[i] = f"{i}  ║ {' ║ '.join(map(str, board[i]))} ║"
            if i >= 10:
                board[i] = str(i) + " ║ " + " ║ ".join(str(item) for item in board[i]) + " ║"

        
        for i in range(len(board)):
            if i % 2 == 0:
                board[i] = colored(board[i], 'purple')
            else:
                board[i] = colored(board[i], 'green')

        board_str += "\n   ║═════════════════════════════════════════════════════════════════════════════════════════║\n".join(board)
        board_str += "\n   ═══════════════════════════════════════════════════════════════════════════════════════════"
        print(board_str)



    def validate_word_place_board(self, word, location, orientation):
        
        word = self.transform_word_to_upper(word)
    
        valid = self.validate_word_inside_board(word, location, orientation)
        self.empty()
        self.mletter = word

        if valid:
            return self.validate_word_center(orientation) if self.is_empty else self.validate_word_placement_in_occupied_grid(orientation)
        return False



        

