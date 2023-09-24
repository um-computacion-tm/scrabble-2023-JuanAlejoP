import unittest
from game.scrabble import Tile


class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)


if __name__ == '__main__':
    unittest.main()