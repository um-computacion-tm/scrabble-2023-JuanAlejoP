class Player:
    def __init__(self, bag_tiles, player_id):
        self.player_name = None
        self.player_id = player_id
        self.score = 0
        self.tiles = bag_tiles.take(7)
        self.bag_tiles = bag_tiles
        
    def fill(self):
        self.tiles += self.bag_tiles.take(7 - len(self.tiles))

    def has_letters(self, word):
        player_letters = {}
        for tile in self.tiles:
            letter = tile.letter
            player_letters[letter] = player_letters.get(letter, 0) + 1

        try:
            for letter in word:
                if player_letters[letter] > 0:
                    player_letters[letter] -= 1
                else:
                    raise KeyError(f"Falta la letra '{letter}' para formar la palabra '{word}'.")
        except KeyError as e:
            raise KeyError(e)
        
        return True
    
    def switch(self):
        player_tiles = self.tiles
        self.tiles = []
        new_tiles = self.bag_tiles.take(7)
        self.tiles.extend(new_tiles)
        self.bag_tiles.put(player_tiles)
        

    # def switch(self, tiles_to_change):
    #     if tiles_to_change < 1:
    #         print("Debes cambiar al menos una ficha.")
    #         return
    #     if tiles_to_change > len(self.tiles):
    #         print("No tienes suficientes fichas para cambiar esa cantidad.")
    #         return

    #     changes = input("Ingresa las letras de las fichas que deseas cambiar (sin espacios): ").upper()
    #     changes = list(changes)

    #     if len(changes) != tiles_to_change or not all(tile in [t.letter for t in self.tiles] for tile in changes):
    #         print("Selección de fichas inválida.")
    #         return

    #     new_tiles = self.bag_tiles.take(tiles_to_change)
    #     for tile in new_tiles:
    #         self.tiles.remove(tile)

    #     for tile_letter in changes:
    #         self.tiles.append(self.bag_tiles.take(1, tile_letter)[0])

    #     self.bag_tiles.put(new_tiles)