
class Util():
    
  
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


    def get_word_horizontal(self, row, col):
        word = []
    
        for c in range(col, -1, -1):
            if self.grid[row][c].has_tile():
                word.insert(0, self.grid[row][c])
            else:
                break
        for c in range(col + 1, len(self.grid[row])):
            if self.grid[row][c].has_tile():
                word.append(self.grid[row][c])
            else:
                break

        if len(word) < 2:
            return False
        return word
    

    def get_word_vertical(self, row, col):
        word = []
    
        for r in range(row, -1, -1):
            if self.grid[r][col].has_tile():
                word.insert(0, self.grid[r][col])
            else:
                break
        for r in range(row + 1, len(self.grid)):
            if self.grid[r][col].has_tile():
                word.append(self.grid[r][col])
            else:
                break

        if len(word) < 2:
            return False
        return word
    
    def get_word_left(self, row, col):
        word = []
        while col >= 0 and self.grid[row][col-1].has_tile():
            word.insert(0, self.grid[row][col-1])
            col -= 1
        return word
    

    def get_word_right(self, row, col):
        word = []
        while col < len(self.grid[row]) and self.grid[row][col + 1].has_tile():
            word.append(self.grid[row][col + 1])
            col += 1
        return word
    


  


    



   
    
    

    
    

    
    



    
  
    


