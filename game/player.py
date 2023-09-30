class Player:
    def __init__(self, score = 0):
        self.tiles = []
        self.score = score
    #nuevo 
    def validate_letter(self, letter):
        if letter in self.tiles:
            return True
        return False

    # def __init__(self, bag_tiles):
    #     self.tiles = bag_tiles.take(7)
    #     self.bag_tiles = bag_tiles

    # def rellenar(self, bag_tiles):
    #     self.tiles += bag_tiles.take(
    #         7 - len(self.tiles)
    #     )
   
    # def has_letter(self):
    #     pass


# terminar turnos de los jugadores

# turno no deberia superar la cantidad 

# 0
# 1
# 2
# 3
# 4
