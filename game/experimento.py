from game.board import Board
from game.scrabble import ScrabbleGame


def main():
    ScrabbleGame.board = Board()
    ScrabbleGame.board.place_multipliers()
    ScrabbleGame.show_board(ScrabbleGame.board)

if __name__ == "__main__":
    main()
