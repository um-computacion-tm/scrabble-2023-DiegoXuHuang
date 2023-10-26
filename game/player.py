
from game.tile import Tile
from game.models import BagTiles

#falta ponerlo
class NoSuficienteFichasException(Exception):
    pass

class Player:
    def __init__(self, score = 0,):
        self.tiles = []
        self.score = score  
        self.name = ""
        self.current_player = None
        
    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

    # def get_tiles(self, bag: BagTiles, amount):
    #     self.tiles += bag.take(amount)

    def show_tiles(self):
        return self.tiles

    def take_tiles(self, bag: BagTiles, amount):
        taken_tiles = bag.take(amount)
        for tile in taken_tiles:
            self.tiles.append(tile)

    def increase_score(self,increase):
        self.score += increase

    def get_score(self):
        return self.score
    
    def refill(self, bag: BagTiles):
        # Calcula la cantidad de fichas que se necesitan para llegar a un total de 7.
        # rellenar las fichas de un jugador para que tengan 7 fichas en su mano
        tiles_needed = 7 - len(self.tiles)
        new_tiles = bag.take(tiles_needed)
        self.tiles.extend(new_tiles)
 

    def has_letters(self, letter_set):
        letter_inventory = {tile.letter: 0 for tile in self.tiles}

        if isinstance(letter_set, str):
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
                print(f"Tile {i.letter} eliminado.")
                break







