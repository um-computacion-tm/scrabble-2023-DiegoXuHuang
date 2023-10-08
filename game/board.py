from game.cell import Cell
#from game.dictionary import validate_word


class Board:
    def __init__(self):
        self.grid = [ [ Cell(1, '') for _ in range(15) ] for _ in range(15) ]
        


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

    

    def validate_word_inside_board(self, word, location, orientation):
    # verifica que la palabra este dentro del trablero
        self.orientation = orientation
        self.position_x = location[0]
        self.position_y = location[1] 

        #x, y = location
        len_word = len(word)
        board_size = 15  # Tamaño del tablero 15x15

        if orientation == "H" and self.position_x + len_word <= board_size:
            return True
        elif orientation == "V" and self.position_y + len_word <= board_size:
            return True

        return False
    



    def is_empty(self):
    # verifica que el tablero este vacio
    
        if self.grid[7][7].letter == None:
            self.is_empty = True
        else:
            self.is_empty = False



   



    




   
    
  

    



   

        
        
    









  


 



    


 