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
        for index in range(players_count):
            self.players.append(Player(id=index, bag_tiles=self.bag_tiles))

        self.current_player = None

    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        elif self.current_player == self.players[-1]:
            self.current_player = self.players[0]
        else:
            index = self.players.index(self.current_player) + 1
            self.current_player = self.players[index]

    def validate_word(self, word, location, orientation):
        try:
            player_tiles = self.current_player.get_tiles()
            for letter in word:
                if letter not in player_tiles:
                    raise ValueError('El jugador no tiene las letras necesarias para formar la palabra.')
        except ValueError as e:
            print(e)
            return False
        try:
            self.board.validate_word_inside_board(word, location, orientation)
        except ValueError as e:
            print(e)
            return False
        return True

    def get_words():
        '''
        Obtener las posibles palabras que se pueden formar, dada una palabra, ubicacion y orientacion 
        Preguntar al usuario, por cada una de esas palabras, las que considera reales
        '''

    def put_words():
        '''
        Modifica el estado del tablero con las palabras consideradas como correctas
        '''