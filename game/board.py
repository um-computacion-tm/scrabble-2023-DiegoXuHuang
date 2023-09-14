from game.cell import Cell


class Board:
    def __init__(self):
        self.grid = [ [ Cell(1, '') for _ in range(15) ] for _ in range(15) ]
        #self.grid = [[None for _ in range(15)] for _ in range(15)]


    def calculate_word_value(self, word):
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


    def validate_word_inside_board(self, word, location, orientation):
        x, y = location
        if orientation == "H":
            if x < 0 or x >= 15 or y < 0 or y + len(word) > 15:
                return False
        elif orientation == "V":
            if x < 0 or x + len(word) > 15 or y < 0 or y >= 15:
                return False
        return True
    

    # def is_empty(self):
        # for row in self.grid:
        #     for tile in row:
        #         if tile != ' ':
        #             return False
        # return True
    
    def is_empty(self):
        
        if self.grid[7][7].letter == None:
            self.is_empty = True
        else:
            self.is_empty = False




    # def validate_word_place_board(self):
    #     pass