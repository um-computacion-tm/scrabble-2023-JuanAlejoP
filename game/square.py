from game.tile import Tile


class Square:
    def __init__(self, multiplier=1, multiplier_type="", letter=None, active=True):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter = letter
        self.active = active

    def __str__(self):
        if self.letter:
            return f'「{self.letter.letter}」'
        elif self.multiplier_type == 'word':
            return f'「{self.multiplier}W」'
        elif self.multiplier_type == 'letter':
            return f'「{self.multiplier}L」'
        else:
            return '「  」'

    def add_letter(self, letter: Tile):
        self.letter = letter

    def calculate_value(self):
        if self.letter is None:
            return 0
        if self.multiplier_type == 'letter' and self.active:
            return self.letter.value * self.multiplier
        else:
            return self.letter.value