class Player:
    def __init__(self, bag_tiles):
        self.tiles = []
        self.bag_tiles = bag_tiles

    def has_letters(self, letters_to_check):
        player_letters = {}
        for tile in self.tiles:
            letter = tile.letter
            if letter in player_letters:
                player_letters[letter] += 1
            else:
                player_letters[letter] = 1
        for tile in letters_to_check:
            letter = tile.letter
            if letter in player_letters and player_letters[letter] > 0:
                player_letters[letter] -= 1
            else:
                return False
        return True