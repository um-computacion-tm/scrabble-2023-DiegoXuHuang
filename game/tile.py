class Tile:
    def __init__(self, letter:str, value:int, player=None):
        self.letter = letter
        self.value = value
        self.player = player

    def __eq__(self, other):
        if isinstance(other, Tile):
            return self.letter == other.letter and self.value == other.value
        return False
    
    # falta test de __repr__
    def __repr__(self):
        return f"{self.letter}:{self.value}"
        
    def get_letter(self):
        return self.letter
    
    def get_value(self):
        return self.value
    



 
