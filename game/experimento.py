from game.board import Board
from game.scrabble import ScrabbleGame


def main():
    ScrabbleGame.board = Board()
    ScrabbleGame.board.place_multipliers()
    print('\n-------------------------------------------------PyScrabble------------------------------------------------')
    ScrabbleGame.show_board(ScrabbleGame.board)
    
    

if __name__ == "__main__":
    main()
