import unittest
from game.scrabble import Board, Square, Tile


class TestCalculateWordValue(unittest.TestCase):
    def test_simple(self):
        word = [
            Square(letter=Tile('C', 1)),
            Square(letter=Tile('A', 1)),
            Square(letter=Tile('S', 2)),
            Square(letter=Tile('A', 1)),
        ]
        value = Board.calculate_word_value(word)
        self.assertEqual(value, 5)

    def test_with_letter_multiplier(self):
        word = [
            Square(letter=Tile('C', 1)),
            Square(letter=Tile('A', 1)),
            Square(
                letter=Tile('S', 2),
                multiplier=2,
                multiplier_type='letter',
            ),
            Square(letter=Tile('A', 1)),
        ]
        value = Board.calculate_word_value(word)
        self.assertEqual(value, 7)

    def test_with_word_multiplier(self):
        word = [
            Square(letter=Tile('C', 1)),
            Square(letter=Tile('A', 1)),
            Square(
                letter=Tile('S', 2),
                multiplier=2,
                multiplier_type='word',
            ),
            Square(letter=Tile('A', 1)),
        ]
        value = Board.calculate_word_value(word)
        self.assertEqual(value, 10)

    def test_with_letter_word_multiplier(self):
        word = [
            Square(
                multiplier=3,
                multiplier_type='letter',
                letter=Tile('C', 1)
            ),
            Square(letter=Tile('A', 1)),
            Square(
                letter=Tile('S', 2),
                multiplier=2,
                multiplier_type='word',
            ),
            Square(letter=Tile('A', 1)),
        ]
        value = Board.calculate_word_value(word)
        self.assertEqual(value, 14)

    def test_with_letter_word_multiplier_no_active(self):
        word = [
            Square(
                multiplier=3,
                multiplier_type='letter',
                letter=Tile('C', 1),
                active=False
            ),
            Square(letter=Tile('A', 1)),
            Square(
                letter=Tile('S', 2),
                multiplier=2,
                multiplier_type='word',
                active=False
            ),
            Square(letter=Tile('A', 1)),
        ]
        value = Board.calculate_word_value(word)
        self.assertEqual(value, 5)


if __name__ == '__main__':
    unittest.main()