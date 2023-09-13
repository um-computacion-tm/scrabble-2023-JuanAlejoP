import unittest
from unittest.mock import patch
from game.scrabble import (
    BagTiles,
    Tile,
    Player,
    Square,
    Board,
    ScrabbleGame,
)


class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)


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


class TestPlayer(unittest.TestCase):
    def test_init(self):
        bag_tiles = BagTiles()
        player_1 = Player(bag_tiles)
        self.assertEqual(
            len(player_1.tiles),
            0,
        )


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


class TestCalculateWordValue(unittest.TestCase):
    def test_simple(self):
        square= Square()
        word = [
            Square(letter=Tile("C", 3)),
            Square(letter=Tile("A", 1)),
            Square(letter=Tile("S", 1)),
            Square(letter=Tile("A", 1))
        ]
        value = square.calculate_word_value(squares=word)
        self.assertEqual(value, 6)

    def test_with_letter_multiplier(self):
        square = Square()
        word = [
            Square(letter=Tile('C', 3)),
            Square(letter=Tile('A', 1)),
            Square(letter=Tile('S', 1), multiplier=2, multiplier_type='letter'),
            Square(letter=Tile('A', 1)),
        ]
        value = square.calculate_word_value(word)
        self.assertEqual(value, 7)

    def test_with_word_multiplier(self):
        square=Square()
        word = [
            Square(letter=Tile('C', 3)),
            Square(letter=Tile('A', 1)),
            Square(letter=Tile('S', 1), multiplier=2, multiplier_type='word'),
            Square(letter=Tile('A', 1)),
        ]
        value = square.calculate_word_value(word)
        self.assertEqual(value, 12)


class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board()
        self.assertEqual(
            len(board.grid),
            15,
        )
        self.assertEqual(
            len(board.grid[0]),
            15,
        )


class TestScrabbleGame(unittest.TestCase):
    def test_init(self):
        scrabble_game = ScrabbleGame(players_count=3)
        self.assertIsNotNone(scrabble_game.board)
        self.assertEqual(
            len(scrabble_game.players),
            3,
        )
        self.assertIsNotNone(scrabble_game.bag_tiles)

    def test_next_turn_when_game_is_starting(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.next_turn()
        assert scrabble_game.current_player == scrabble_game.players[0]

    def test_next_turn_when_player_is_not_the_first(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.next_turn()
        assert scrabble_game.current_player == scrabble_game.players[1]

    def test_next_turn_when_player_is_last(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[2]
        scrabble_game.next_turn()
        assert scrabble_game.current_player == scrabble_game.players[0]

if __name__ == '__main__':
    unittest.main()