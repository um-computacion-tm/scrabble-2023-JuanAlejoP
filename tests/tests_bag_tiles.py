import unittest
from unittest.mock import patch
from game.scrabble import BagTiles, Over100TilesException, UnderZeroTilesException


class TestBagTiles(unittest.TestCase):
    @patch('random.shuffle')
    def test_bag_tiles(self, patch_shuffle):
        bag = BagTiles()
        self.assertEqual(
            len(bag.tiles),
            100,
        )
        self.assertEqual(
            patch_shuffle.call_count,
            1,
        )
        self.assertEqual(
            patch_shuffle.call_args[0][0],
            bag.tiles,
        )

    def test_take(self):
        bag = BagTiles()
        tiles = bag.take(2)
        self.assertEqual(
            len(bag.tiles),
            98,
        )
        self.assertEqual(
            len(tiles),
            2,
        )

    def test_put(self):
        bag = BagTiles()
        tiles = bag.take(5)
        bag.put(tiles)
        self.assertEqual(
            len(bag.tiles),
            100,
        )

    def test_under_zero_tiles_exception(self):
        bag = BagTiles()
        with self.assertRaises(UnderZeroTilesException):
            bag.take(101)

    def test_over_100_tiles_exception(self):
        bag = BagTiles()
        tiles_to_put = [1] * 101
        with self.assertRaises(Over100TilesException):
            bag.put(tiles_to_put)


if __name__ == '__main__':
    unittest.main()