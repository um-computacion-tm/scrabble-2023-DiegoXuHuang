from game.tile import Tile
from game.models import Tile
class Cell:
    def __init__(self, multiplier=1, multiplier_type='letter', letter=None, active=True):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter = letter
        self.active = active
        # self.row = row
        # self.col = col

    
    #test
    def has_tile(self):
        return self.letter is not None
    #test
    def get_tile(self):
        return self.letter
   
    # def toggle_cell(self):
    #     self.active = not self.active

    # se 
    def __repr__(self):
        if self.letter is not None:
            return f" {self.letter.letter} "
        else:
            if self.multiplier == 1:
                return "   "
            else:
                return f"{self.multiplier_type}x{self.multiplier}"
        
     
    def calculate_value(self):
        if self.letter is None:
            return 0
        if self.multiplier_type == 'letter':
            return self.letter.value * self.multiplier
        else:
            return self.letter.value
        
    
    def add_letter(self, letter:Tile):
        self.letter = letter

        
    # def show_player(player_index, player):
    #     print(f"player #{player_index}: {player.tile}")


    

