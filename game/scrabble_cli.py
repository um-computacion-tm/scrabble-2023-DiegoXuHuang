from game.scrabble import *
from game.scrabble import ScrabbleGame

class ScrabbleCli:
    def __init__(self, players):
        self.game = ScrabbleGame(players)  
        self.util = Util()

    def start_game(self):
        players = self.get_player_count()
        scrabble_game = ScrabbleCli(players)
        scrabble = ScrabbleGame(players)
        scrabble_game.print_welcome()
        scrabble_game.get_players_name(len(scrabble_game.game.players))
    
        while True:
            try:
                scrabble_game.game.next_turn()
                scrabble_game.game.end_game()
                
            
            except GameOverException:
                scrabble.show_results()
                break 
        
    def get_player_count():
        while True:
            try:
                player = int(input("Ingresa el número de jugadores (2-4): "))
                if 2 <= player <= 4:
                    return player
                else:
                    print("Entrada inválida. Por favor, ingresa un número entre 2 y 4.")
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número válido.")

    def get_players_name(self, players):
        player_names = [] 
        for i in range(players):
            name = input(f"Ingrese el nombre del jugador {i+1} --> ")
            player_names.append(name)  


        for i, player_name in enumerate(player_names):
            self.game.players[i].name = player_name



    def display_scrabble_rules(self):
        reglas = """
    ╭─────────────────────────────────────────╮
    │   Reglas del Juego de Scrabble          │
    │                                         │
    │ 1. El juego se juega en un tablero      │
    │    de 15x15 casillas.                   │
    │ 2. Los jugadores deben formar palabras  │
    │    en el tablero utilizando fichas      │
    │    con letras.                          │
    │ 3. Cada letra tiene un valor en         │
    │    puntos, y el objetivo es maximizar   │
    │    la puntuación.                       │
    │ 4. Cada jugador comienza con un         │
    │    conjunto de fichas al azar.          │
    │ 5. Los jugadores alternan turnos        │
    │    para formar palabras en el tablero.  │
    │ 6. Las palabras puede conectarse a      │
    │    otras palabras en el tablero.        │
    │ 7. Los jugadores pueden usar            │
    │    diccionarios o listas de palabras    │
    │    permitidas.                          │
    │ 8. El juego termina cuando se agotan    │
    │    las fichas o cuando un jugador no    │
    │    puede formar palabras.               │
    │ 9. El ganador es el jugador con la      │
    │    puntuación más alta al final del     │
    │    juego.                               │
    │                                         │
    │ ¡Diviértete jugando al Scrabble!        │
    ╰─────────────────────────────────────────╯
        """
        print(reglas)



    def print_welcome(self):
        print("╔═══════════════════════════════════════╗")
        print("║                                       ║")
        print("║    Bienvenido al Juego de Scrabble    ║")
        print("║                                       ║")
        print("╚═══════════════════════════════════════╝")
        print("╔═══════════════════════════════════════╗")
        print("║                                       ║")
        print("║  Instrucciones:                       ║")
        print("║  1. El objetivo del juego es formar   ║")
        print("║     palabras con las fichas que tiene.║")
        print("║  2. Cada ficha tiene un valor en      ║")
        print("║     puntos. Gana el jugador con más   ║")
        print("║     puntos al final.                  ║")
        print("║  3. Puedes intercambiar tus fichas x  ║")
        print("║     no puedes formar una palabra.     ║")
        print("║  4. ¡Diviértete y buena suerte!       ║")
        print("║                                       ║")
        print("╚═══════════════════════════════════════╝")
    
    def show_tiles(self):
        tiles = self.game.current_player.tiles
        if tiles:
            print("Fichas del jugador:")
            print("╔════════════╗")
            for tile in tiles:
                print("║    {}     ║".format(tile))
            print("╚════════════╝")
        else:
            print("El jugador no tiene Fichas.")



    def show_score(self):
        player = self.game.current_player
        score = player.score
        name = player.name

        box_length = max(len(name), 10) + 4
        print("+" + "-" * (box_length - 2) + "+")
        print("|" + name.center(box_length - 2) + "|")
        print("|" + "-" * (box_length - 2) + "|")
        print("|" + "-SCORE- {:^4}".format(score) + "|")
        print("+" + "-" * (box_length - 2) + "+")


    def exchange_tile(self):
        available_indexes = list(range(len(self.game.current_player.tiles)))

        while True:
            try:
                index_exchange = int(input(f"Ingresa el índice de la ficha para intercambiar (0-{len(available_indexes) - 1}) --> "))

                if index_exchange in available_indexes:
                    tile_exchange = self.game.current_player.tiles[index_exchange]
                    self.game.current_player.exchange_tile(self.game.bag_tiles, tile_exchange)
                    print("Ficha intercambiada con éxito.")
                    break
                else:
                    print("Índice no válido. Por favor, elige un índice válido.")
            except ValueError:
                print("Entrada no válida. Ingresa un número válido.")


    def wildcard(self):
        wildcard = self.game.has_wildcard()
        
        if not wildcard:
            return  
        
        player_tiles = self.game.current_player.tiles
        wildcard_tile = next((tile for tile in player_tiles if tile.value == 0), None)
        
        if wildcard_tile:
            self.set_letter_for_wildcard(wildcard_tile)

    def set_letter_for_wildcard(self, tile):
        letter_for_wild = input("Escribi una LETRA que quieras (comodin):").strip().upper()
        tile.set_letter(letter_for_wild)




















