class Tile:
    def __init__(self, letter:str, value:int, player=None):
        self.letter = letter
        self.value = value
        self.player = player