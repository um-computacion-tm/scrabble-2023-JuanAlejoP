import unittest
from game.scrabble import Board, Square, Tile


class TestCalculateWordValue(unittest.TestCase):
    def test_simple(self):
        square = Square()
         
        word = [
            Square(letter=Tile("C", 1)),
            Square(letter=Tile("A", 1)),
            Square(letter=Tile("S", 2)),
            Square(letter=Tile("A", 1))
        ]
        value = square.calculate_word_value(cells=word)
        self.assertEqual(value, 5)

    def test_with_letter_multiplier(self):
        square = Square()
        word = [
            Square(letter=Tile('C', 1)),
            Square(letter=Tile('A', 1)),
            Square(letter=Tile('S', 2), multiplier=2, multiplier_type='letter'),
            Square(letter=Tile('A', 1)),
        ]
        value = square.calculate_word_value(word)
        self.assertEqual(value, 7)

    def test_with_word_multiplier(self):
        square = Square()
        word = [
            Square(letter=Tile('C', 1)),
            Square(letter=Tile('A', 1)),
            Square(letter=Tile('S', 2), multiplier=2, multiplier_type='word'),
            Square(letter=Tile('A', 1)),
        ]
        value = square.calculate_word_value(word)
        self.assertEqual(value, 10)
    
    def test_with_both_multiplier(self):
        square = Square()
        word = [
            Square(letter = Tile("C", 3), multiplier=2, multiplier_type='word'),
            Square(letter = Tile("A", 1), multiplier=3, multiplier_type='letter'),
            Square(letter = Tile("S", 1), multiplier=1, multiplier_type=''),
            Square(letter = Tile("A", 1), multiplier=1, multiplier_type='')
        ]
        value = square.calculate_word_value(cells=word)
        self.assertEqual(
            value, 16
        )

    def test_with_both_multiplier_cell_not_active(self):
        square = Square()
        word = [
            Square(letter = Tile("C", 3), multiplier=2, multiplier_type='word', active=False),
            Square(letter = Tile("A", 1), multiplier=3, multiplier_type='letter', active=False),
            Square(letter = Tile("S", 1), multiplier=1, multiplier_type='', active=False),
            Square(letter = Tile("A", 1), multiplier=1, multiplier_type='', active=False)
        ]
        value = square.calculate_word_value(cells=word)
        self.assertEqual(
            value, 6
        )


if __name__ == '__main__':
     unittest.main()