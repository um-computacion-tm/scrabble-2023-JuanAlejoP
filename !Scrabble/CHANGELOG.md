# Changelog

All notable changes to this Scrabble project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2023-08-21

### Added

- Create `models` module to contain the core components of the game.
- Implement `Tile` class to represent individual game tiles with letters and values.
- Implement `BagTiles` class to manage the bag of tiles for the game.
- Add methods to `BagTiles` class for taking and putting back tiles.
- Create `test_models` module to contain unit tests.
- Add test cases to ensure proper functioning of tile creation, bag initialization, tile taking, and tile putting.