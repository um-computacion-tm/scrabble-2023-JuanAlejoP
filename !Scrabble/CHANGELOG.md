# Changelog

All notable changes to this Scrabble project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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