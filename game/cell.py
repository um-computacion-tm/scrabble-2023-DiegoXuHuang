from game.tile import Tile
from game.models import Tile
from functools import reduce


class CalculateWordValue:
    def calculate_word(self, word):
        word_score = sum(cell.calculate_value() for cell in word)
        product = reduce(lambda x, cell: x * cell.multiplier if cell.multiplier_type == 'W' and cell.active else x, word, 1)
        return word_score * product



class Cell:
    def __init__(self, multiplier=1, multiplier_type='letter', letter=None, active=True):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter = letter
        self.active = active
        #self.util = Util()
        #print(type(letter))

    def __repr__(self):
        if self.letter is not None:
            return self.format_special_letter()
        else:
            if self.multiplier == 1:
                return "   "
            return f"{self.multiplier_type}x{self.multiplier}"



    def add_letter(self, letter:Tile):
        self.letter = letter
   
    def has_tile(self):
        return self.letter is not None
 
    def get_tile(self):
        return self.letter

    def deactivate_cell(self):
        self.active = False
     
    def calculate_value(self):
        if self.letter is None:
            return 0
        return self.letter.value * self.multiplier if self.multiplier_type == 'L' and self.active else self.letter.value


    def format_special_letter(self):
        if self.letter is not None and self.letter.letter in ("CH", "RR", "LL"):
            return f"{self.letter.letter} "
        return f" {self.letter.letter} " if self.letter is not None else ""
    

    
   



            
    







  
    
   
    




 



    


    

