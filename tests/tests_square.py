import unittest
from game.scrabble import Square, Tile


class TestSquare(unittest.TestCase):
    def test_init(self):
        square = Square(multiplier=2, multiplier_type='letter')
        self.assertEqual(
            square.multiplier,
            2,
        )
        self.assertEqual(
            square.multiplier_type,
            'letter',
        )
        self.assertIsNone(square.letter)
        self.assertEqual(
            square.calculate_value(),
            0,
        )

    def test_add_letter(self):
        square = Square(multiplier=1, multiplier_type='')
        letter = Tile(letter='p', value=3)
        square.add_letter(letter=letter)
        self.assertEqual(square.letter, letter)

    def test_cell_value(self):
        square = Square(multiplier=2, multiplier_type='letter')
        letter = Tile(letter='p', value=3)
        square.add_letter(letter=letter)
        self.assertEqual(
            square.calculate_value(),
            6,
        )

    def test_cell_multiplier_word(self):
        square = Square(multiplier=2, multiplier_type='word')
        letter = Tile(letter='p', value=3)
        square.add_letter(letter=letter)
        self.assertEqual(
            square.calculate_value(),
            3,
        )


if __name__ == '__main__':
    unittest.main()