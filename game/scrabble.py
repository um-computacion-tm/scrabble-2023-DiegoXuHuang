from game.board import Board
from game.player import Player
from game.models import BagTiles


class ScrabbleGame:
    def __init__(self, players_count: int):
        self.board = Board()
        self.bag_tiles = BagTiles()
        # self.players = list[Player] = []
        #self.next_turn = None
        for _ in range(players_count):
            self.players.append(Player(baf_tiles=self.bag_tiles))

        self.current_player = None

    # def next_turn():
    #     if self.current_player = self.players[0]

    
    
