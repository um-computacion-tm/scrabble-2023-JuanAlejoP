from game.board import Board
from game.bag_tiles import BagTiles
from game.player import Player

class InvalidWordException(Exception):
    def __init__(self, message):
        super().__init__(message)

class InvalidPlaceWordException(Exception):
    def __init__(self, message):
        super().__init__(message)

class InvalidWordPlacementException(Exception):
    def __init__(self, message):
        super().__init__(message)


class ScrabbleGame:
    def __init__(self, players_count: int):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players:list[Player] = []
        for index in range(players_count):
            self.players.append(Player(player_id=index, bag_tiles=self.bag_tiles))
        self.current_player = None

    def show_board(board):
        column_width = 2
        print('\n' + '  ' * column_width, end='  ')
        for col_index in range(15):
            print(str(col_index).rjust(column_width), end='     ')
        print()
        for row_index, row in enumerate(board.grid):
            print(str(row_index).rjust(column_width) + '|', end=' ')
            for square in row:
                print(str(square).rjust(column_width), end=' ')
            print()

    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        else:
            self.current_player = (self.current_player + 1) % len(self.players)

    def validate_word(self, word, location, orientation):
        if not Board.dict_validate_word(word):
            raise InvalidWordException("Su palabra no existe en el diccionario.")
        if not self.board.validate_word_inside_board(word, location, orientation):
            raise InvalidPlaceWordException("Su palabra excede el tablero.")
        if not self.board.validate_word_place_board(word, location, orientation):
            raise InvalidPlaceWordException("Su palabra est mal puesta en el tablero.")

    def play(self, word, location, orientation):
        if self.validate_word(word, location, orientation):
            player_word = self.board.place_word(word, location, orientation)
            total = self.board.calculate_word_value(player_word)
            self.current_player.score += total
            self.next_turn()