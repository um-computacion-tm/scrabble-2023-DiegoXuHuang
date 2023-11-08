from game.scrabble import *
from game.scrabble import ScrabbleGame


class ScrabbleCli:
    def __init__(self, players):
        self.game = ScrabbleGame(players)  
        self.util = Util()


    def start_game(self):
        players = self.players_to_play()
        scrabble_game = ScrabbleCli(players)
        scrabble = ScrabbleGame(players)
        scrabble_game.print_welcome()
        scrabble_game.get_players_name(len(scrabble_game.game.players))
    
        while True:
            try:
                scrabble_game.game.next_turn()
                scrabble_game.game.end_game()
                scrabble_game.show_menu()
            
            except GameOverException:
                scrabble.show_results()
                break



    def players_to_play(self):
        while True:
            try:
                player = int(input("Ingresa el número de jugadores [2-4]: "))
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
    │ 4. Los jugadores alternan turnos        │
    │    para formar palabras en el tablero.  │
    │ 5. Las palabras puede conectarse a      │
    │    otras palabras en el tablero.        │
    │ 6. El juego termina cuando se agotan    │
    │    las fichas o cuando un jugador no    │
    │    puede formar palabras.               │
    │ 7. El ganador es el jugador con la      │
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
    




    def show_menu(self):
        self.game.current_player.refill()

        while True:
            self.display_game_info()

            print("Opciones del Menú:")
            print("╔══════════════════════════════╗")
            print("║  0. Colocar Palabra          ║")
            print("║  1. Reglas                   ║")
            print("║  2. Intercambiar Fichas      ║")
            print("║  3. Pasar Turno              ║")
            print("║  4. Mostrar Tablero          ║")
            print("║  5. Usar comodin             ║")
            print("║  6. Finalizar juego          ║")
            print("╚══════════════════════════════╝")

            option = input("Ingrese un número: ")

            try:
                option = int(option)

                if option == 0:
                    self.input_play_word()
                elif option == 1:
                    self.display_scrabble_rules()
                elif option == 2:
                    self.handle_tile_exchange()
                elif option == 3:
                    self.end_current_turn()
                elif option == 4:
                    print("\n" + "=" * 95)
                    self.game.board.show_board()
                    print("=" * 95 + "\n")
                elif option == 5:
                    self.wildcard()
                elif option == 6:
                    self.game.end_game_directly()
                    break
                else:
                    error_message = "\n"\
                                    "╔══════════════════════════════════════════════╗\n" \
                                    "║  ❌ Número no válido. Por favor, ingrese un  ║\n" \
                                    "║  número válido del menú.                     ║\n" \
                                    "╚══════════════════════════════════════════════╝"
                    raise ValueError(error_message)
            except ValueError as e:
                print(e)
            except FinshiTurnException:
                self.display_turn_end_message()
                break


    def display_game_info(self):

        print("\n")
        self.show_tiles()
        print("\n")

        print("Puntajes:")
        self.show_score()
        print("\n")

    # def handle_play_word(self):
    #     self.input_play_word()


    def handle_tile_exchange(self):
        tile_changes = int(input("Cuantas fichas quieres cambiar? --> "))
        for _ in range(tile_changes):
            self.exchange_tile()
            self.show_tiles()
        self.end_current_turn()

  
    def display_turn_end_message(self):
        separator_line = "=" * 94
        message = " Turno terminado "
        
        print("\n" + separator_line)  
        print(f"|{' '*(45 - len(message)//2)}{message}{' '*(45 - len(message)//2)}|")  
        print(separator_line + "\n") 

        

    def show_tiles(self):
        tiles = self.game.current_player.tiles
        if tiles:
            print("Fichas del jugador:")
            print("╔═════════════╗")
            for i, tile in enumerate(tiles):
                tile_str = "{:2d}. {}".format(i, tile)
                print("║ {:<12}║".format(tile_str))
            print("╚═════════════╝")
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
                index_exchange = int(input(f"Que fichas queres intercambiar? [0-1-2-3-4-5-6] --> "))

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
            print("\n")
            print("╔══════════════════════════╗")
            print("║   ⚠️ No tienes comodín 🃏 ║")
            print("╚══════════════════════════╝")
        else:
            player_tiles = self.game.current_player.tiles
            wildcard_tile = next((tile for tile in player_tiles if tile.value == 0), None)

            if wildcard_tile:
                letter_for_wild = input("Escribi una LETRA que quieras (comodín):").strip().upper()
                wildcard_tile.set_letter(letter_for_wild)



    def get_input_within_range(self, prompt, min_value, max_value):
        while True:
            try:
                value = int(input(prompt))
                if min_value <= value <= max_value:
                    return value
                else:
                    print(f"Entrada no válida. Por favor, ingrese un número entre {min_value} y {max_value}.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número válido.")

    

    def get_location_and_orientation(self):
        def orientation():
            while True:
                orientation = input("Pone una posicion (H/V): ").strip().upper()
                if orientation == "H" or orientation == "V":
                    return orientation
                else:
                    print("Orientación no válida. Por favor, ingresa 'H' para horizontal o 'V' para vertical")

        row = self.get_input_within_range("Ingrese el número de fila [0-14]: ", 0, 14)
        col = self.get_input_within_range("Ingrese el número de columna [0-14]: ", 0, 14)
        orientation = orientation()
        return (row, col), orientation



    def is_valid_play(self, word, location, orientation):
        if not self.game.validate_word(word, location, orientation):
            return False

        if not self.game.validate_and_score_word(word, location, orientation):
            return False

        return True

    def play_word(self, word, location, orientation):
        self.game.place_word_on_board(word, location, orientation)
        self.game.calculator(word, location, orientation)
        self.end_current_turn()
            
    def end_current_turn(self):
        raise FinshiTurnException 

    def input_play_word(self):
        while True:
            try:
                action = input("Escribe una palabra y presiona ENTER, o presiona espacio y ENTER para volver: ")
                if action == " ":
                    break

                word = self.util.split_groups_in_string(action) 
                location, orientation = self.get_location_and_orientation()

                if self.is_valid_play(word, location, orientation):
                    self.play_word(word, location, orientation)
                else:
                    raise InvalidWordException
            except InvalidWordException:
                print("\n")
                print(" ⚠️  ACORDATE QUE SI ESTAS EN EL PRIMER MOVIMIENTO TENES QUE PONERLO EN EL CENTRO ")
                print("-----------------------------------------------------------------------------------")
                print("                    ❌ LA PALABRA QUE INGRESASTE ES INVALIDA ")
                print("\n")

 
    