import unittest
from game.scrabble import Board, Square, Tile


class TestCalculateWordValue(unittest.TestCase):
    def test_simple(self):
        board = Board()
        word = [
            Square(letter=Tile("C", 3)),
            Square(letter=Tile("A", 1)),
            Square(letter=Tile("S", 1)),
            Square(letter=Tile("A", 1))
        ]
        value = board.calculate_word_value(word)
        self.assertEqual(value, 6)

    def test_with_letter_multiplier(self):
        board = Board()
        word = [
            Square(letter=Tile('C', 3)),
            Square(letter=Tile('A', 1)),
            Square(letter=Tile('S', 1), multiplier=2, multiplier_type='letter'),
            Square(letter=Tile('A', 1)),
        ]
        value = board.calculate_word_value(word)
        self.assertEqual(value, 7)

    def test_with_word_multiplier(self):
        board = Board()
        word = [
            Square(letter=Tile('C', 3)),
            Square(letter=Tile('A', 1)),
            Square(letter=Tile('S', 1), multiplier=2, multiplier_type='word'),
            Square(letter=Tile('A', 1)),
        ]
        value = board.calculate_word_value(word)
        self.assertEqual(value, 12)

    def test_with_letter_word_multiplier(self):
        word = [
            Square(
                multiplier=3,
                multiplier_type='letter',
                letter=Tile('C', 3)
            ),
            Square(letter=Tile('A', 1)),
            Square(
                letter=Tile('S', 1),
                multiplier=2,
                multiplier_type='word',
            ),
            Square(letter=Tile('A', 1)),
        ]
        value = Board.calculate_word_value(word)
        self.assertEqual(value, 24)

    # def test_with_letter_word_multiplier_no_active(self):
    #     word = [
    #         Square(
    #             multiplier=3,
    #             multiplier_type='letter',
    #             letter=Tile('C', 3)
    #         ),
    #         Square(letter=Tile('A', 1)),
    #         Square(
    #             letter=Tile('S', 1),
    #             multiplier=2,
    #             multiplier_type='word',
    #         ),
    #         Square(letter=Tile('A', 1)),
    #     ]
    #     value = Board.calculate_word_value(word)
    #     self.assertEqual(value, 12)