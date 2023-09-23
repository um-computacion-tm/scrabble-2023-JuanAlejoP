from game.tile import Tile
from game.bag_tiles import BagTiles
from game.player import Player
from game.square import Square
from game.board import Board
from game.bag_tiles import Over100TilesException, UnderZeroTilesException

class ScrabbleGame:
    def __init__(self, players_count: int):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players:list[Player] = []
        self.current_player = None
        for _ in range(players_count):
            self.players.append(Player(bag_tiles=self.bag_tiles))

    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        else:
            index = self.players.index(self.current_player) + 1
            if index >= len(self.players):
                index = 0
            self.current_player = self.players[index]
