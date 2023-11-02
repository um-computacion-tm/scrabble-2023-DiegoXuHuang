from game.scrabble import ScrabbleGame



class ScrabbleCli:
    def __init__(self, players):
        self.game = ScrabbleGame(players)

    def start_game(self):
        pass  
        
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

    