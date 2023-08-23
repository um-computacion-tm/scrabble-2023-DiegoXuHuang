import random


class Diccionario:
    def __init__(self):
        self.palabras_validas = ["abaco", "tabaco"]


# a  co


class Player:  # Diego
    def __init__(self, puntuacion=10):
        self.tiles_elegidas = []
        self.puntuacion = puntuacion

    # def buscar_letra(self,letra):
    #     for tile in self.tiles_elegidas:
    #         if tile.letter


class Tile:  # A=1
    # representar las letras en el tablero
    def __init__(self, letter, value, jugador: Player = None):
        self.letter = letter
        self.value = value
        if not isinstance(jugador, Player):
            raise ValueError(
                "El parametro jugador debe ser un objeto de la clase jugador"
            )
        self.jugador = jugador
        self.jugador.tiles_elegidas.append(self)


class AdministradorFichas:
    # administra los puntos del jugador
    def __init__(self, tiles: [], jugador: Player = None):
        if not isinstance(jugador, Player):
            raise ValueError(
                "El parametro jugador debe ser un objeto de la clase jugador"
            )
        self.jugador = jugador
        self.tiles = tiles


class BagTiles:
    def __init__(self):
        self.tiles = [
            Tile("A", 1),
            Tile("A", 1),
            Tile("A", 1),
            Tile("A", 1),
            Tile("A", 1),
            Tile("A", 1),
            Tile("A", 1),
            Tile("A", 1),
            Tile("A", 1),
            Tile("A", 1),
            Tile("A", 1),
            Tile("A", 1),
            Tile("E", 1),
            Tile("E", 1),
            Tile("E", 1),
            Tile("E", 1),
            Tile("E", 1),
            Tile("E", 1),
            Tile("E", 1),
            Tile("E", 1),
            Tile("E", 1),
            Tile("E", 1),
            Tile("E", 1),
            Tile("E", 1),
            Tile("O", 1),
            Tile("O", 1),
            Tile("O", 1),
            Tile("O", 1),
            Tile("O", 1),
            Tile("O", 1),
            Tile("O", 1),
            Tile("O", 1),
            Tile("O", 1),
            Tile("I", 1),
            Tile("I", 1),
            Tile("I", 1),
            Tile("I", 1),
            Tile("I", 1),
            Tile("I", 1),
            Tile("S", 1),
            Tile("S", 1),
            Tile("S", 1),
            Tile("S", 1),
            Tile("S", 1),
            Tile("S", 1),
            Tile("N", 1),
            Tile("N", 1),
            Tile("N", 1),
            Tile("N", 1),
            Tile("N", 1),
            Tile("L", 1),
            Tile("L", 1),
            Tile("L", 1),
            Tile("L", 1),
            Tile("R", 1),
            Tile("R", 1),
            Tile("R", 1),
            Tile("R", 1),
            Tile("R", 1),
            Tile("U", 1),
            Tile("U", 1),
            Tile("U", 1),
            Tile("U", 1),
            Tile("U", 1),
            Tile("T", 1),
            Tile("T", 1),
            Tile("T", 1),
            Tile("T", 1),
            Tile("D", 2),
            Tile("D", 2),
            Tile("D", 2),
            Tile("D", 2),
            Tile("D", 2),
            Tile("G", 2),
            Tile("G", 2),
            Tile("C", 3),
            Tile("C", 3),
            Tile("C", 3),
            Tile("C", 3),
            Tile("B", 3),
            Tile("B", 3),
            Tile("M", 3),
            Tile("M", 3),
            Tile("P", 3),
            Tile("P", 3),
            Tile("H", 4),
            Tile("H", 4),
            Tile("F", 4),
            Tile("V", 4),
            Tile("Y", 4),
            Tile("CH", 5),
            Tile("Q", 5),
            Tile("J", 8),
            Tile("LL", 8),
            Tile("Ñ", 8),
            Tile("RR", 8),
            Tile("X", 8),
            Tile("Z", 10),
        ]
        random.shuffle(self.tiles)

    def take(self, count):
        tiles = []
        for _ in range(count):
            tiles.append(self.tiles.pop())
        return tiles

    def put(self, tiles):
        self.tiles.extend(tiles)
