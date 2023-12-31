
class Util():

    def __init__(self, board=None):
        self.board = board
    
    def update_coordinates(self, orientation, row, col):
        orientation_updates = {"H": (0, 1), "V": (1, 0)}
        row_update, col_update = orientation_updates.get(orientation, (0, 0))
        return row + row_update, col + col_update
    


    def is_word_list(self, word):
        return isinstance(word, list)
    

    def is_word_letters(self, letters):
        return isinstance(letters, list)
    

    def is_word_set(self, letter_set):
        return isinstance(letter_set, str)
    

    # def is_word_item(self, item):
    #     return isinstance(item, str)



    def split_groups_in_string(self, input_string):
        word = []
        i = 0
        while i < len(input_string):
            if i < len(input_string) - 1 and input_string[i:i+2] in ['ch', 'll', 'rr']:
                word.append(input_string[i:i+2])
                i += 2
            else:
                word.append(input_string[i])
                i += 1
        return word




    def get_word_horizontal(self, row, col):
        word = []
        grid = self.board.grid

        c = col
        while c >= 0 and grid[row][c].has_tile():
            word.insert(0, grid[row][c])
            c -= 1

        c = col + 1

        while c < len(grid[row]) and grid[row][c].has_tile():
            word.append(grid[row][c])
            c += 1

        if len(word) < 2:
            return False
        return word

    


    def get_word_vertical(self, row, col):
        word = []
        grid = self.board.grid
        for r in range(row, -1, -1):
            if grid[r][col].has_tile():
                word.insert(0, grid[r][col])
            else:
                break
        for r in range(row + 1, len(grid)):
            if grid[r][col].has_tile():
                word.append(grid[r][col])
            else:
                break

        if len(word) < 2:
            return False
        return word
    


    def get_word_left(self, row, col):
        word = []
        grid = self.board.grid
        while col >= 0 and grid[row][col-1].has_tile():
            word.insert(0, grid[row][col-1])
            col -= 1
        return word
    
    
    def get_word_right(self, row, col):
        word = []
        grid = self.board.grid
        while col < len(grid[row]) and grid[row][col + 1].has_tile():
            word.append(grid[row][col + 1])
            col += 1
        return word



    



   
    
    

    
    

    
    



    
  
    


