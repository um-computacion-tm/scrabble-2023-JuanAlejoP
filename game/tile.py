class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value
        self.wildcard_value = None

    def set_wildcard_value(self, letter):
        self.wildcard_value = letter