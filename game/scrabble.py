from game.tile import Tile
from game.bag_tiles import BagTiles
from game.player import Player
from game.square import Square
from game.board import Board
from game.bag_tiles import Over100TilesException, UnderZeroTilesException


class InvalidWordException(Exception):
    def __init__(self, message):
        super().__init__(message)

class InvalidPlaceWordException(Exception):
    def __init__(self, message):
        super().__init__(message)

class InvalidWordPlacementException(Exception):
    def __init__(self, message):
        super().__init__(message)

class InvalidTurnException(Exception):
    def __init__(self, message):
        super().__init__(message)

class ScrabbleGame:
    def __init__(self, players_count: int):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players:list[Player] = []
        for index in range(players_count):
            self.players.append(Player(id=index, bag_tiles=self.bag_tiles))
        self.current_player = None

    def play(self, word, location, orientation):
        if self.validate_word(word, location, orientation):
            words = self.board.put_words(word, location, orientation)
            total = self.board.calculate_word_value(words)
            self.current_player.score += total
            self.next_turn()

    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        elif self.current_player == self.players[-1]:
            raise InvalidTurnException("Error al cambiar de turno: el jugador actual es el último de la lista.")
        else:
            index = self.players.index(self.current_player) + 1
            self.current_player = self.players[index]


    # def next_turn(self):
    #     self.current_player = (self.current_player + 1) % len(self.players)

    def validate_word(self, word, location, orientation):
        ...


    # version anterior
    # def validate_word(self, word, location, orientation):
    #     if not Board.dict_validate_word(word):
    #         raise InvalidWordException("Su palabra no existe en el diccionario.")
    #     if not self.board.validate_word_inside_board(word, location, orientation):
    #         raise InvalidPlaceWordException("Su palabra excede el tablero.")
    #     if not self.board.validate_word_place_board(word, location, orientation):
    #         raise InvalidPlaceWordException("Su palabra esta mal puesta en el tablero.")

#     def next_turn(self):
#         if self.current_player is None:
#             self.current_player = self.players[0]
#         elif self.current_player == self.players[-1]:
#             self.current_player = self.players[0]
#         else:
#             index = self.players.index(self.current_player) + 1
#             self.current_player = self.players[index]

# #ARREGLAR
#     def validate_word(self, word, location, orientation):
#         # '''
#         # 1- Validar que usuario tiene esas letras
#         # 2- Validar que la palabra entra en el tablero
#             # esta unida a otra palabra
#             # es inicial y pasa por el inicio
#         # '''
#         # self.board.validate_word_inside_board(word, location, orientation)
#         try:
#             player_tiles = self.current_player.get_tiles()
#             for letter in word:
#                 if letter not in player_tiles:
#                     raise ValueError('El jugador no tiene las letras necesarias para formar la palabra.')
#         except ValueError as e:
#             print(e)
#             return False
#         try:
#             self.board.validate_word_inside_board(word, location, orientation)
#         except ValueError as e:
#             print(e)
#             return False
#         return True

    def get_words(self, word, location, orientation):
        # '''
        # Obtener las posibles palabras que se pueden formar, dada una palabra, ubicacion y orientacion 
        # Preguntar al usuario, por cada una de esas palabras, las que considera reales
        # '''
        possible_words = self.generate_possible_words(word)
        valid_words = []
        for possible_word in possible_words:
            if self.board.is_word_valid(possible_word, location, orientation):
                valid_words.append(possible_word)
        real_words = []
        for valid_word in valid_words:
            user_response = input(f"¿Es '{valid_word}' una palabra real? (Sí/No): ").strip().lower()
            if user_response == 'si':
                real_words.append(valid_word)
        return real_words

    def put_words(self):
        # '''
        # Modifica el estado del tablero con las palabras consideradas como correctas
        # '''
        words_to_put = self.get_words()
        for word, location, orientation in words_to_put:
            if not self.board.is_word_valid(word, location, orientation):
                print(f"La palabra '{word}' no es válida en la ubicación especificada.")
                continue
            self.board.place_word(word, location, orientation)
#ARREGLAR

    def show_board(board):
        print('\n |' + ''.join([f' {str(row_index).rjust(2)} ' for row_index in range(15)]))
        for row_index, row in enumerate(board.grid):
            print(
                str(row_index).rjust(2) +
                '| ' +
                ' '.join([repr(square) for square in row])
            )