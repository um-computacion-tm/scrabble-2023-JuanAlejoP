from game.board import Board, BoardException
from game.dictionary import Dictionary
from game.bag_tiles import BagTiles
from game.player import Player, PlayerException


class ScrabbleException(Exception):
    def __init__(self, message):
        super().__init__(message)

class ScrabbleGame:
    def __init__(self, players_count: int, player_names: list):
        self.dictionary = Dictionary()
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players:list[Player] = []
        for index in range(1, players_count + 1):
            player = Player(player_id=index, bag_tiles=self.bag_tiles)
            player.player_name = player_names[index - 1]
            self.players.append(player)
        self.current_player_index = 0 
        self.current_player = self.players[0]

    def show_board(self):
        column_width = 2
        print('\n' + '  ' * column_width, end='  ')
        for col_index in range(15):
            print(str(col_index).rjust(column_width), end='     ')
        print()
        for row_index, row in enumerate(self.board.grid):
            print(str(row_index).rjust(column_width) + '|', end=' ')
            for square in row:
                print(str(square).rjust(column_width), end=' ')
            print()

    def next_turn(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        self.current_player = self.players[self.current_player_index]

    def validate_word(self, word, location, orientation):
        if not self.dictionary.validate_dictionary(word):
            raise ScrabbleException('LA PALABRA NO EXISTE EN EL DICCIONARIO.')
        if not self.board.validate_word_place_board(word, location, orientation):
            return False
        return True

    def play(self, word, location, orientation):
        try:
            if self.validate_word(word, location, orientation):
                played_word = self.current_player.has_letters(word)
                placed_word = self.board.place_word(played_word, location, orientation)
                total_score = self.board.calculate_word_value(placed_word)
                self.current_player.score += total_score
                self.current_player.fill()
                self.next_turn()
        except (ScrabbleException, BoardException, PlayerException) as e:
            print(f"\nERROR: {e}")