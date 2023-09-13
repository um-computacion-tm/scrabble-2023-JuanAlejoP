from game.tile import Tile


class Square:
    def __init__(self, multiplier=1, multiplier_type="", letter=None, active=True):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter = letter
        self.active = active

    def add_letter(self, letter: Tile):
        self.letter = letter

    def calculate_value(self):
        if self.letter is None:
            return 0
        if self.multiplier_type == 'letter' and self.active:
            return self.letter.value * self.multiplier
        else:
            return self.letter.value

    def calculate_word_value(self, squares):
        word_value = 0
        word_multiplier = 1
        squares_used = []

        for square in squares:
            if square not in squares_used:
                square_value = square.calculate_value()
                if square.multiplier_type == 'word' and square.active:
                    word_multiplier *= square.multiplier
                word_value += square_value
                squares_used.append(square)

        return word_value * word_multiplier
