import unicodedata, os
from game.scrabble import ScrabbleGame
from game.square import Square

def clear_terminal():
    os.system('clear')

def main():
    print('\n¡Bienvenido a PyScrabble!')
    def get_player_count():
        while True:
            try:
                player_quantity = int(input('\nIngrese la cantidad de jugadores (1-4): '))
                if 1 <= player_quantity <= 4:
                    return player_quantity
                else:
                    print('Ingrese un número entre 1 y 4.')
            except ValueError:
                print('Ingrese un número válido.')
    
    player_quantity = get_player_count()
    player_names = []

    for i in range(player_quantity):
        player_name = input(f'\nNombre del Jugador {i + 1}: ')
        player_names.append(player_name)

    print('\nLos jugadores son:')
    for i, name in enumerate(player_names):
        print(f'Jugador {i + 1}: {name}')

    while True:
        print('\n¿Son correctos los nombres de los jugadores?: ')
        print('1. Sí')
        print('2. No')
        answer = input('\nElige una opción: ').strip()
        if answer == '1':
            break

        elif answer == '2':
            while True:
                try:
                    player_to_change = int(input('\nIngrese el número del jugador que cambiará de nombre: '))
                    if 1 <= player_to_change <= player_quantity:
                        new_name = input(f'\nIngrese el nuevo nombre del Jugador {player_to_change}: ')
                        player_names[player_to_change - 1] = new_name
                        print(f'El Jugador {player_to_change} ahora es {new_name}.')
                        print('\nLos jugadores son:')
                        for i, name in enumerate(player_names):
                            print(f'Jugador {i + 1}: {name}')
                        break

                    else:
                        print('Número de jugador no válido.')

                except ValueError:
                    print('Ingrese un número válido.')

    scrabble_game = ScrabbleGame(players_count=player_quantity, player_names=player_names)
    # clear_terminal()

    while True:
        current_player = scrabble_game.current_player
        tiles_format = "  ".join([str(tile) for tile in current_player.tiles])
        tiles_format = unicodedata.normalize("NFKD", tiles_format)

        print('\n-------------------------------------------------PyScrabble------------------------------------------------')
        scrabble_game.show_board()
        print('-----------------------------------------------------------------------------------------------------------')
        print(f"\nTurno del Jugador {current_player.player_id}: {current_player.player_name}")
        print(f"Fichas: 「 {tiles_format} 」")
        print(f"Puntaje: {current_player.score}") #『 』
        print('\n¿Qué quieres hacer?')
        print('1. Colocar una palabra')
        print('2. Cambiar fichas')
        print('3. Pasar turno')
        print('4. Terminar el juego')

        option = input('\nElige una opción: ').strip()
        if option == '1':
            word = input('Palabra a colocar: ').upper()
            x = int(input('Ingrese coordenada en x: '))
            y = int(input('Ingrese coordenada en y: '))
            location = x,y
            orientation = input('Ingrese la orientación de la palabra: ')
            scrabble_game.play(word, location, orientation)

        elif option == '2':
            scrabble_game.current_player.switch()
            tiles_format = "  ".join([str(tile) for tile in current_player.tiles])
            tiles_format = unicodedata.normalize("NFKD", tiles_format)
            
            print(f'Tus nuevas fichas son: 「 {tiles_format} 」')
            # tiles_to_change = int(input('Cantidad de fichas a cambiar: '))
            # scrabble_game.player.switch(tiles_to_change)
            # print(f"Has cambiado {len(tiles_to_change)} fichas. Tus nuevas fichas son: 「 {tiles_format} 」")
            scrabble_game.next_turn()

        elif option == '3':
            scrabble_game.next_turn()           

        elif option == '4':
            break

        else:
            print('Opción no válida. Por favor, elige una opción válida.')


if __name__ == '__main__':
    main()