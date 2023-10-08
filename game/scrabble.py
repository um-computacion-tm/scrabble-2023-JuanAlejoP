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

    def play(self, word, location, orientation):
        self.validate_word(word, location, orientation)
        words = self.board.put_words(word, location, orientation)
        total = calculate_word_value(words)
        self.players[self.current_player].score += total
        self.next_turn()

    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        elif self.current_player == self.players[-1]:
            self.current_player = self.players[0]
        else:
            index = self.players.index(self.current_player) + 1
            self.current_player = self.players[index]

#ARREGLAR
    def validate_word(self, word, location, orientation):
        # '''
        # 1- Validar que usuario tiene esas letras
        # 2- Validar que la palabra entra en el tablero
            # esta unida a otra palabra
            # es inicial y pasa por el inicio
        # '''
        # self.board.validate_word_inside_board(word, location, orientation)
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