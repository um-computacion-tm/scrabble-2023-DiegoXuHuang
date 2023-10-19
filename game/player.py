from game.tile import Tile
from game.models import BagTiles


class NoSuficienteFichasException(Exception):
    pass

class Player:
    def __init__(self, score = 0,):
        self.tiles = []
        self.score = score  
        self.name = ""
      
    
    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    


    def get_tiles(self, bag: BagTiles, amount):
        self.tiles += bag.take(amount)


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
        tiles_needed = 7 - len(self.tiles)
    
        # Llama al método "take" del objeto "bag" para obtener las fichas necesarias.
        new_tiles = bag.take(tiles_needed)
    
        # Extiende la lista "self.tiles" con las nuevas fichas obtenidas.
        self.tiles.extend(new_tiles)



    
    def has_letters(self, tiles=[]):
        # Obtén las letras de las fichas del jugador
        player_letters = [tile.letter for tile in self.tiles]
    
        # Obtén las letras de las fichas que se pasaron como argumento
        word_letters = [tile.letter for tile in tiles]
    
        # Itera sobre las letras necesarias de las fichas que se pasaron como argumento
        for letra in word_letters:
            # Verifica si la letra está en las fichas del jugador
            if letra in player_letters:
                # Si la letra está en las fichas del jugador, quítala de la lista
                # Esto asegura que una ficha no se use más de una vez
                player_letters.remove(letra)
            else:
                # Si la letra no está en las fichas del jugador, la palabra no se puede formar
                return False
    
        # Si se llega a este punto, significa que todas las letras necesarias están disponibles
        return True
    



    def exchange_tiles(self, bag, tiles_to_exchange):
        if len(self.tiles) < tiles_to_exchange:
            raise NoSuficienteFichasException(f"No quedan mas fichas para intercambiar ({len(self.tiles)} < {tiles_to_exchange})")


         # Toma las fichas del jugador que se intercambiarán
        exchanged_tiles = []
        for _ in range(tiles_to_exchange):
            tile = self.tiles.pop(0)
            exchanged_tiles.append(tile)


        # Agrega nuevas fichas al jugador desde la bolsa
        new_tiles = bag.take(tiles_to_exchange)
        self.tiles.extend(new_tiles)

        return exchanged_tiles, new_tiles
    



    

    



    







                
    #nuevo 
    # def validate_letter(self, letter):
    #     if letter in self.tiles:
    #         return True
    #     return False


    #--------

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
