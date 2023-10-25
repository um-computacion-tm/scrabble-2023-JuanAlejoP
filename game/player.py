from game.bag_tiles import BagTiles


class Player:
    def __init__(self, bag_tiles, player_id):
        self.tiles = bag_tiles.take(7)
        self.bag_tiles = bag_tiles
        self.player_id = player_id
        self.score = 0

    def fill(self):
        self.tiles += self.bag_tiles.take(7 - len(self.tiles))

    def has_letters(self, word):
        player_letters = {}
        for tile in self.tiles:
            letter = tile.letter
            player_letters[letter] = player_letters.get(letter, 0) + 1

        try:
            for letter in word:
                if player_letters[letter] > 0:
                    player_letters[letter] -= 1
                else:
                    raise KeyError(f"Falta la letra '{letter}' para formar la palabra '{word}'.")
        except KeyError as e:
            raise KeyError(e)
        
        return True