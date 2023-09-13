# Changelog

All notable changes to this Scrabble project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.7.0] - 2023-09-12

### Added

- Add calculate_word_value method to calculate the value of a word formed by multiple squares.
- Improve attributes for better square management.

### Changed

- Update attribute handling in the Square class for better integration with the game logic.

## [0.6.0] - 2023-09-11

### Added

- Implement player turns in `ScrableGame` class:
  - Add functionality to switch to the next player's turn.

### Changed

- Update `scrabble.py`:
  - Implement player turn logic for the game.
  - Ensure players take turns correctly.
  
- Update `player.py`:
  - Adjust the `Player` class to accept the `bag_tiles` parameter in its constructor.

## [0.5.0] - 2023-08-28

### Added

- Implement `Board` class in `board` module:
  -Represent the game board with a grid of squares.
- Implement `ScrableGame` class in `scrabble`:
  - Initialize a game instance with a game board, bag of tiles, and players.

### Changed

- Update relevant files to import and use `Board` and `ScrabbleGame` classes

## [0.4.0] - 2023-08-28

### Added

- Implement `Square` class in `square` module:
  - Represent individual squares on the game board.
  - Allow squares to hold a letter tile and calculate its value based on multipliers.

### Changed

- Update relevant files to import and use the `Square` class.

## [0.3.0] - 2023-08-28

### Added

- Implement `Player` class in `player` module:
  - Initialize player with an empty set of tiles.

### Changed

- Update `scrabble` to import `Player` class.

## [0.2.0] - 2023-08-28

### Added

- Expand tile bag in `BagTiles` class:
  - Add additional tiles for various letters and values.
  - Include blank tiles as wildcards.
  
### Changed

- Move `models` functionality to separate files:
    - `bag_tiles` to manage tile bag.
    - `scrabble` to handle main game logic.
    - `tile` to define the Tile class.

### Removed

- Remove `models` module: Functionality moved to `bag_tiles`, `scrabble`, and `tile`.

## [0.1.0] - 2023-08-21

### Added

- Create `models` module to contain the core components of the game.
- Implement `Tile` class to represent individual game tiles with letters and values.
- Implement `BagTiles` class to manage the bag of tiles for the game.
- Add methods to `BagTiles` class for taking and putting back tiles.