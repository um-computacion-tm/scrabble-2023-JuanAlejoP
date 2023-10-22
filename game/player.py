from game.bag_tiles import BagTiles

class InsufficientLettersError(Exception):
    def __init__(self, message):
        super().__init__(message)

class Player:
    def __init__(self, bag_tiles, id):
        self.tiles = bag_tiles.take(7)
        self.bag_tiles = bag_tiles
        self.id = id
        self.score = 0

    def fill(self):
        self.tiles += self.bag_tiles.take(7 - len(self.tiles))

    #prueba de modificación
    def has_letters(self, letters_to_check):
        player_letters = {}
        for tile in self.tiles:
            letter = tile.letter
            player_letters[letter] = player_letters.get(letter, 0) + 1

        for tile in letters_to_check:
            letter = tile.letter
            if letter in player_letters and player_letters[letter] > 0:
                player_letters[letter] -= 1
            else:
                return False

        return True


# #ARREGLAR
#     def has_letters(self, letters_to_check):
#         player_letters = {}
#         for tile in self.tiles:
#             letter = tile.letter
#             if letter in player_letters:
#                 player_letters[letter] += 1
#             else:
#                 player_letters[letter] = 1
#         for tile in letters_to_check:
#             letter = tile.letter
#             if letter in player_letters and player_letters[letter] > 0:
#                 player_letters[letter] -= 1
#             else:
#                 return False
#         return True