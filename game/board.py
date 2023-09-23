from game.square import Square


class Board:
    def __init__(self):
        self.grid = [[Square(1, '') for _ in range(15)] for _ in range(15)]

    @staticmethod
    def calculate_word_value(word: list[Square]) -> int:
        value: int = 0
        multiplier_word = None
        for square in word:
            value = value + square.calculate_value()
            if square.multiplier_type == 'word' and square.active:
                multiplier_word = square.multiplier
        if multiplier_word:
            value = value * multiplier_word
        return value

    def validate_word_inside_board(self, word, location, orientation):
        position_x = location[0]
        position_y = location[1]
        len_word = len(word)
        if orientation == 'H':
            if position_x + len_word > 15:
                return False
            else:
                return True
        else:
            pass 