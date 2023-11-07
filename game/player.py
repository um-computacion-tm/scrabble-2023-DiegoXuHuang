
from game.tile import Tile
from game.models import BagTiles
from game.util import Util



class NoSuficienteFichasException(Exception):
    pass

class Player:
    def __init__(self):
        self.tiles = []
        self.score = 0  
        self.name = ""
        self.current_player = self
        self.bag_tiles = BagTiles()
        self.util = Util()
        


    def refill(self):
        max_tiles_to_take = 7 - len(self.tiles)
        if max_tiles_to_take > 0:
            tiles_to_take = self.bag_tiles.take(max_tiles_to_take)
            self.tiles.extend(tiles_to_take)



    def add_tile(self, tile: Tile):
        self.tiles.insert(0, tile)

        

    def take_tiles(self, bag: BagTiles, amount):
        taken_tiles = bag.take(amount)
        for tile in taken_tiles:
            self.tiles.append(tile)

    def increase_score(self,increase):
        self.score += increase

    def get_score(self):
        return self.score


    def has_letters(self, letter_set):
        letter_inventory = {tile.letter: 0 for tile in self.tiles}

        if self.util.is_word_set(str):
            letter_set = letter_set.upper()
       
        elif all(isinstance(item, str) for item in letter_set):
            letter_set = [letter.upper() for letter in letter_set]
        else:
            letter_set = [letter.letter for letter in letter_set]

        for tile in self.tiles:
            letter_inventory[tile.letter] += 1

        for letter in letter_set:
            if letter in letter_inventory and letter_inventory[letter] > 0:
                letter_inventory[letter] -= 1
            else:
                return False

        return True
    
   
        
    def exchange_tile(self, bag: BagTiles, tile_exchange):
        if tile_exchange in self.tiles:
            self.tiles.remove(tile_exchange)
            bag.put([tile_exchange])
            bag.shuffle_bag()
            self.tiles.append(bag.take(1)[0])
    
    
    def remove_tile(self, tile: Tile):
        for i in self.tiles:
            if i.letter == tile.letter:
                self.tiles.remove(i)
                break

    
    
    

    







