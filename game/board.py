from game.square import Square


class Board:
    def __init__(self):
        self.grid = [[Square(1, "", "") for _ in range(15)] for _ in range(15)]

    def place_multipliers(self):
        self.grid[0][0] = Square(3, 'word')
        self.grid[0][3] = Square(2, 'letter')
        self.grid[0][7] = Square(3, 'word')
        self.grid[0][11] = Square(2, 'letter')
        self.grid[0][14] = Square(3, 'word')
        self.grid[1][1] = Square(2, 'word')
        self.grid[1][5] = Square(3, 'letter')
        self.grid[1][9] = Square(3, 'letter')
        self.grid[1][13] = Square(2, 'word')
        self.grid[2][2] = Square(2, 'word')
        self.grid[2][6] = Square(2, 'letter')
        self.grid[2][8] = Square(2, 'letter')
        self.grid[2][12] = Square(2, 'word')
        self.grid[3][0] = Square(2, 'letter')
        self.grid[3][3] = Square(2, 'word')
        self.grid[3][7] = Square(2, 'letter')
        self.grid[3][11] = Square(2, 'word')
        self.grid[3][14] = Square(2, 'letter')
        self.grid[4][4] = Square(2, 'word')
        self.grid[4][10] = Square(2, 'word')
        self.grid[5][1] = Square(3, 'letter')
        self.grid[5][5] = Square(3, 'letter')
        self.grid[5][9] = Square(3, 'letter')
        self.grid[5][13] = Square(3, 'letter')
        self.grid[6][2] = Square(2, 'letter')
        self.grid[6][6] = Square(2, 'letter')
        self.grid[6][8] = Square(2, 'letter')
        self.grid[6][12] = Square(2, 'letter')
        self.grid[7][0] = Square(3, 'word')
        self.grid[7][3] = Square(2, 'letter')
        self.grid[7][11] = Square(2, 'letter')
        self.grid[7][14] = Square(3, 'word')
        self.grid[8][2] = Square(2, 'letter')
        self.grid[8][6] = Square(2, 'letter')
        self.grid[8][8] = Square(2, 'letter')
        self.grid[8][12] = Square(2, 'letter')
        self.grid[9][1] = Square(3, 'letter')
        self.grid[9][5] = Square(3, 'letter')
        self.grid[9][9] = Square(3, 'letter')
        self.grid[9][13] = Square(3, 'letter')
        self.grid[10][4] = Square(2, 'word')
        self.grid[10][10] = Square(2, 'word')
        self.grid[11][0] = Square(2, 'letter')
        self.grid[11][3] = Square(2, 'word')
        self.grid[11][7] = Square(2, 'letter')
        self.grid[11][11] = Square(2, 'word')
        self.grid[11][14] = Square(2, 'letter')
        self.grid[12][2] = Square(2, 'word')
        self.grid[12][6] = Square(2, 'letter')
        self.grid[12][8] = Square(2, 'letter')
        self.grid[12][12] = Square(2, 'word')
        self.grid[13][1] = Square(2, 'word')
        self.grid[13][5] = Square(3, 'letter')
        self.grid[13][9] = Square(3, 'letter')
        self.grid[13][13] = Square(2, 'word')
        self.grid[14][0] = Square(3, 'word')
        self.grid[14][3] = Square(2, 'letter')
        self.grid[14][7] = Square(3, 'word')
        self.grid[14][11] = Square(2, 'letter')
        self.grid[14][14] = Square(3, 'word')

    def place_word(self, word, location, orientation):
        x, y = location
        if orientation == 'H':
            for letter in word:
                self.grid[x][y].add_letter(letter)
                y += 1
        else:
            for letter in word:
                self.grid[x][y].add_letter(letter)
                x += 1

    @staticmethod
    def calculate_word_value(word: list[Square]) -> int:
        value: int = 0
        multiplier_word = None
        for square in word:
            value = value + square.calculate_value()
            if square.multiplier_type == "word" and square.active:
                multiplier_word = square.multiplier
        if multiplier_word:
            value = value * multiplier_word
        return value
    
    def validate_word_inside_board(self, word, location, orientation):
        #Falta implementar
        ...

    def validate_word_place_board(self, word, location, orientation):
        #Falta implementar
        ...

    def is_empty(self):
            for row in self.grid:
                for square in row:
                    if square.letter:
                        return False
            return True