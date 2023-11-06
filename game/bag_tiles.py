import random
from game.tile import Tile


class UnderZeroTilesException(Exception):
    def __init__(self, message):
        super().__init__(message)

class Over100TilesException(Exception):
    def __init__(self, message):
        super().__init__(message)

class BagTiles:
    def __init__(self):
        self.tiles = [
            Tile('A', 1), Tile('A', 1), Tile('A', 1), Tile('A', 1), Tile('A', 1), Tile('A', 1), Tile('A', 1), Tile('A', 1), Tile('A', 1), Tile('A', 1), Tile('A', 1), Tile('A', 1),
            Tile('B', 3), Tile('B', 3),
            Tile('C', 3), Tile('C', 3), Tile('C', 3), Tile('C', 3),
            Tile('CH', 5),
            Tile('D', 2), Tile('D', 2), Tile('D', 2), Tile('D', 2), Tile('D', 2),
            Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1),
            Tile('F', 4),
            Tile('G', 2), Tile('G', 2),
            Tile('H', 4), Tile('H', 4),
            Tile('I', 1), Tile('I', 1), Tile('I', 1), Tile('I', 1), Tile('I', 1), Tile('I', 1),
            Tile('J', 8),
            Tile('L', 1), Tile('L', 1), Tile('L', 1), Tile('L', 1),
            Tile('LL', 8),
            Tile('M', 3), Tile('M', 3),
            Tile('N', 1), Tile('N', 1), Tile('N', 1), Tile('N', 1), Tile('N', 1),
            Tile('Ñ', 8),
            Tile('O', 1), Tile('O', 1), Tile('O', 1), Tile('O', 1), Tile('O', 1), Tile('O', 1), Tile('O', 1), Tile('O', 1), Tile('O', 1),
            Tile('P', 3), Tile('P', 3),
            Tile('Q', 5),
            Tile('R', 1), Tile('R', 1), Tile('R', 1), Tile('R', 1), Tile('R', 1),
            Tile('RR', 8),
            Tile('S', 1), Tile('S', 1), Tile('S', 1), Tile('S', 1), Tile('S', 1), Tile('S', 1),
            Tile('T', 1), Tile('T', 1), Tile('T', 1), Tile('T', 1),
            Tile('U', 1), Tile('U', 1), Tile('U', 1), Tile('U', 1), Tile('U', 1),
            Tile('V', 4),
            Tile('X', 8),
            Tile('Y', 4),
            Tile('Z', 10),
            Tile('*', 0), Tile('*', 0),
        ]
        self.mix()

    def take(self, count, wildcard_value=None):
        tiles = []
        for _ in range(count):
            if not self.tiles:
                raise UnderZeroTilesException('La bolsa de fichas no puede tener menos de 0 fichas.')
            tile = self.tiles.pop()
            if tile.letter == '*' and wildcard_value is not None:
                tile.set_wildcard_value(wildcard_value)
            tiles.append(tile)
        return tiles

    def put(self, tiles):
        if len(self.tiles) + len(tiles) > 100:
            raise Over100TilesException('La bolsa de fichas no puede tener más de 100 fichas.')
        self.tiles.extend(tiles)
        self.mix()

    def mix(self):
        random.shuffle(self.tiles)