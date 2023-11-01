from game.scrabble import ScrabbleGame
from game.square import Square

def main():
    print('\n¡Bienvenido a PyScrabble!')
    def get_player_count():
        while True:
            try:
                player_quantity = int(input('\nIngrese la cantidad de jugadores (1-4), por favor: '))
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

    while True:
        response = input('\n¿Son correctos los nombres de los jugadores? (Sí/No): ').strip().lower()
        if response == 'si':
            break
        elif response == 'no':
            while True:
                try:
                    player_to_change = int(input('\nIngrese el número del jugador que cambiará de nombre, por favor: '))
                    if 1 <= player_to_change <= player_quantity:
                        new_name = input(f'\nIngrese el nuevo nombre del Jugador {player_to_change}: ')
                        player_names[player_to_change - 1] = new_name
                        break
                    else:
                        print('Número de jugador no válido.')
                except ValueError:
                    print('Ingrese un número válido.')
    print('\nLos jugadores son:')
    for i, name in enumerate(player_names):
        print(f'Jugador {i + 1}: {name}')

    scrabble_game = ScrabbleGame(players_count=player_quantity)
    
    while True:
        print('\n-------------------------------------------------PyScrabble------------------------------------------------')
        for player in scrabble_game.players:
            print(f"Turno del Jugador {player.player_id}: {player.player_name}")
            print(f"Fichas: {player.tiles}")
            print(f"Puntaje: {player.score}") #『 』
            scrabble_game.show_board()
        print('\n-----------------------------------------------------------------------------------------------------------')
        
        print('¿Qué quieres hacer?')
        print('1. Colocar una palabra')
        print('2. Cambiar fichas')
        print('3. Terminar el juego')

        option = input('Elige una opción (1/2/3): ').strip()
            
        if option == '1':
            
            pass
        elif option == '2':
            
            pass
        elif option == '3':
            
            break
        else:
            print('Opción no válida. Por favor, elige una opción válida.')
        

if __name__ == '__main__':
    main()