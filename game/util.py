from game.board import Board


class Util():

    def __init__(self):
        board = Board()  
        self.grid = board.grid
    

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
    



    
  
    


