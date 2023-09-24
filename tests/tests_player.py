import unittest
from game.scrabble import BagTiles, Player


class TestPlayer(unittest.TestCase):
    def test_init(self):
        bag_tiles = BagTiles()
        player_1 = Player(bag_tiles)
        self.assertEqual(
            len(player_1.tiles),
            0,
        )


if __name__ == '__main__':
    unittest.main()