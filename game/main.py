from game.scrabble_cli import ScrabbleCli

def main():
    cli = ScrabbleCli(players=0)
    cli.start_game()


if __name__ == '__main__':
    main()   