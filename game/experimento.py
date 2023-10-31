from game.board import Board


def show_board(board):
    column_width = 2

    print('\n' + '  ' * column_width, end='  ')
    for col_index in range(15):
        print(str(col_index).rjust(column_width), end='     ')
    print()

    for row_index, row in enumerate(board.grid):
        print(str(row_index).rjust(column_width) + '|', end=' ')
        for square in row:
            print(str(square).rjust(column_width), end=' ')
        print()

def main():
    board = Board()
    board.place_multipliers()
    show_board(board)

if __name__ == "__main__":
    main()
