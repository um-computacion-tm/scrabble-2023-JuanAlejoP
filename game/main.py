from game.scrabble import ScrabbleGame


def main():
    print("¡Bienvenido!")
    while True:
        try: 
            players_count = int(input('Ingrese cantidad de jugadores: '))
            if players_count <= 1 or players_count > 4:
                raise ValueError
            break
        except ValueError:
            print('Valor inválido')
    scrabble_game = ScrabbleGame(players_count=players_count)
    print('Cantidad de jugadores: ',len(scrabble_game.players))
    scrabble_game.next_turn()
    print(f'Turno del jugador {scrabble_game.current_player.id}')
    word = input('Ingrese palabra: ')
    location_x = input('Ingrese posición X: ')
    location_y = input('Ingrese posición Y: ')
    location = (location_x, location_y)
    orientation = input('Ingrese orientación (V/H)')
    scrabble_game.validate_word(word, location, orientation)


if __name__ == '__main__':
    main()