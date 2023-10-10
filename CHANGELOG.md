# Changelog

All notable changes to this Scrabble project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.21.0] - 2023-10-10

### Added

#### ScrabbleGame Class:

- Add custom exceptions for word and word placement validation:
  - `InvalidWordException` for invalid words not found in the dictionary.
  - `InvalidPlaceWordException` for invalid word placement on the board.
  - `InvalidWordPlacementException` for incorrectly placed words on the board.

#### Player Class:

- Add a `score` attribute to the `Player` class.

#### Board Class:

- Add a placeholder method `dict_validate_word` to simulate word validation against a dictionary.

### Changed

- Updated the `play` method in the `ScrabbleGame` class to raise custom exceptions when word or placement is invalid, providing informative error messages.

- Updated the `next_turn` method in the `ScrabbleGame` class to correctly cycle through players.

- Made minor internal adjustments to support the new features and custom exceptions.

## [0.20.0] - 2023-10-09

### Added

#### Main Module:

- Add the `get_player_count` function to the main module:
  - This function prompts the user to enter the number of players (1-3) with input validation.
  - It ensures that a valid player count is entered and returns it.

### Changed

- Made minor internal adjustments to the main module to support the `get_player_count` function.

## [0.19.0] - 2023-10-08

### Added

#### ScrabbleGame Class:

- Add the `play` method to the `ScrabbleGame` class:
  - This method coordinates the player's move, validating the word, placing it on the board, calculating the word's value, updating the player's score, and advancing the turn.
  - The `validate_word` method is called to ensure the word is valid before proceeding.

### Changed

- Made minor internal adjustments to support the new `play` method.

## [0.18.0] - 2023-10-07

### Added

#### Board Class:

- Add the `is_empty` method to the `Board` class:
  - This method checks if the game board is empty by inspecting each square on the board.
  - Returns `True` if the board is empty, otherwise `False`.

### Changed

- Made minor internal adjustments to support the new `is_empty` method.

## [0.17.0] - 2023-10-06

### Added

#### Player Class:

- Add the `fill` method to the `Player` class:
  - This method fills the player's tiles up to 7 if they have fewer than 7 tiles in their rack.

#### Board Class:

- Add the `validate_word_place_board` method to the `Board` class:
  - This method combines the existing `validate_word_inside_board` method with additional checks for word placement on the board.
  - Returns `True` if the word can be placed on the board, otherwise `False`.

- Add the `is_empty` method's placeholder to the `Board` class:
  - This method should check if the game board is empty (has no tiles placed on it).

### Changed

- Make minor internal adjustments to support the new methods in both the `Player` and `Board` classes.

## [0.16.0] - 2023-09-27

### Added

- Implement the `has_letters` method in the `Player` class:
  - This method checks if the player has a specific set of letters.
  - It counts the occurrence of each letter in the player's tiles.
  - It then checks if the player has the required letters by comparing with the input set.
  - Returns `True` if the player has the letters, otherwise `False`.

### Changed

- Made minor internal adjustments to support the new `has_letters` method.

## [0.15.0] - 2023-09-26

### Added

- Implement the `put_words` method in the `ScrabbleGame` class:
  - This method retrieves a list of words to be placed on the game board using the `get_words` method.
  - It iterates through the list of words and their respective locations and orientations.
  - For each word, it checks if it's valid on the game board, and if not, it provides a message.
  - Valid words are placed on the game board using the `place_word` method.

### Changed

- Made minor internal adjustments to support the new `put_words` method.

## [0.14.0] - 2023-09-25

### Added

- Implement the `get_words` method in the `ScrabbleGame` class:
  - This method generates possible words based on the input word, location, and orientation.
  - It checks each possible word for validity on the game board.
  - The player is prompted to confirm if each valid word is a real word.
  - Real words are collected and returned as a list.

### Changed

- Made minor internal adjustments to support the new `get_words` method.

## [0.13.0] - 2023-09-24

### Added

- Implement the `validate_word` method in the `ScrabbleGame` class:
  - This method checks if the player has the required letters to form the word and raises a ValueError if not.
  - It also validates if the word can fit on the game board and raises a ValueError if not.
  - The method returns `True` if the word is valid and `False` otherwise.

### Changed

- Made minor internal adjustments to support the new `validate_word` method.

## [0.12.0] - 2023-09-23

### Added

- Add the `validate_word` method to the `ScrabbleGame` class:
  - This method validates that the player has the required letters to form the word.
  - It also checks if the word can fit on the game board.

- Add placeholder methods for `get_words` and `put_words` for future functionality development.

### Changed

- Made minor internal adjustments to support the new `validate_word` method.

## [0.11.0] - 2023-09-22

### Added

- Implement the `main.py` module for player interaction:
  - The game now starts with a welcome message.
  - Players are prompted to enter the number of players with input validation.
  - The game starts with the correct number of players.
  - The current player's turn is displayed.
  - Players can input a word, X and Y coordinates, and orientation.
  - Word input is validated in the game.

## [0.10.0] - 2023-09-13

### Added

- Add `validate_word_inside_board` method to verify word positioning inside the board.

### Changed

- Move `calculate_word_value` method from `Square` module to `Board` module.

## [0.9.0] - 2023-09-12

### Added

- Implement custom exception `Over100TilesException` in `BagTiles` class:
  - Raise this exception when attempting to put tiles exceeding the limit of 100 tiles in the bag.

- Update `BagTiles` class to handle exceptions related to tile putting.

### Changed

- Modify `BagTiles` class to use proper exception handling when putting tiles.

### Improved

- Improve error handling and user feedback when interacting with the tile bag.

## [0.8.0] - 2023-09-12

### Added

- Implement custom exception `UnderZeroTilesException` in `BagTiles` class:
  - Raise this exception when attempting to take tiles from an empty bag.

- Update `BagTiles` class to handle exceptions related to tile taking.

### Changed

- Modify `BagTiles` class to use proper exception handling when taking tiles.

### Improved

- Improve error handling and user feedback when interacting with the tile bag.

## [0.7.0] - 2023-09-12

### Added

- Add `calculate_word_value` method to calculate the value of a word formed by multiple squares.
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