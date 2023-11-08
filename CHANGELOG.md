# Changelog

All notable changes to this Scrabble project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.36.0] - 2023-11-08

### Added

#### Board Class:

- Add `BoardException` to handle exceptions in the Board class.

#### Dictionary Class:

- Create a `Dictionary` class.

#### Main Script:

- Add a `clear_terminal` function to clear the terminal (for UNIX-like systems).
- Add the ability to change player names before starting the game.

#### Player Module:

- Create a `PlayerException` to handle exceptions in the Player class.

#### Scrabble Module:

- Add the `validate_word` method to check dictionary and board-related validation.
- Add `ScrabbleException` to handle all exceptions.

### Changed

#### Board Class:

- Modify validation methods for placing a word on the board.
- Change the place_word method to validate the placement and store the placed word.
- Modify the calculate_word_value method to calculate word scores correctly.

#### Main Script:

- Modify import statements.
- Made various modifications in the game menu.

#### Player Module:

- Modify the __init__ constructor to accept player_id.
- Modify the has_letters method to store matched tiles and raise exceptions.
- Change the switch method to handle tile swapping.

#### Scrabble Module:

- Modify the constructor of the ScrabbleGame class.
- Modify the show_board method.
- Modify the play method to correctly validate, place, and score a word.

#### Square Module:

- Modify the __str__ method to display square contents.
- Modify the add_letter method to place letters.
- Modify the calculate_value method to consider square multipliers.

### Removed

#### Dictionary Class:

- Remove an unused exception.

#### Scrabble Module:

- Remove previous exceptions.

## [0.35.0] - 2023-11-06

### Added

#### Tile Class:

- Add the `__str__` method to display the tile's letter and value together.

#### Board Class:

- Add `place_multipliers()` call to ensure the board is initialized with multipliers.

#### Player Class:

- Add a `switch` method to allow players to exchange tiles with the bag.

### Changes

#### ScrabbleGame Class:

- Modify the `__init__` method to accept both the number of players and their names. Player IDs are now correctly assigned.
- Modify `next_turn` method to switch to the next player's turn properly.

#### BagTiles Class:

- Implement a `mix` method to shuffle the tiles.

#### Main Script:

- Now, it displays players' tile racks as formatted text.
- Implement option for exchanging tiles and passing the turn.

### Removed

#### Player Class:

- Removed unused import statements.

## [0.34.0] - 2023-10-31

### Changes

#### Main Script:

- Significant changes in the implementation:
    - Now, at the start of the game, it asks for the number of players and their names.
    - Implement a main loop that allows players to take turns and displays relevant information like tiles and scores.
    - Add a menu with options to place a word, exchange tiles, or end the game.

### Fixes

#### Player Class:

- Fix attribute names in the player's constructor `__init__`.

#### ScrabbleGame Class:

- Fix an error in the `show_board` method.

## [0.33.0] - 2023-10-31

### Added

#### Board Class:

- Implement several new validation methods in the `Board` class:
    - Add `validate_first_turn`: Validates that the first word placed on the board starts from the center.
    - Add `validate_word_crossing`: Verifies that the word doesn't interfere with existing words on the board.
    - Add `validate_next_to_word`: Ensures that the word is placed adjacent to an existing word on the board.

### Changed

#### Board Class:

- Implement several new validation methods in the `Board` class:
    - Modify `validate_word_inside_board`: Checks if the word fits within the board boundaries based on its location and orientation.
    - Modify `validate_word_place_board`: Combines various validation checks to ensure the word placement is valid.

## [0.32.0] - 2023-10-31

### Changed

#### Board Class:

- Modify the `place_word` method. It now generates a list `player_word` that is used for the subsequent calculation of word value. The method has been enhanced to populate the `player_word` list while placing the word on the board.

## [0.31.0] - 2023-10-31

### Added

#### ScrabbleGame Class:

- Add the `place_word` method to place words on the board, populating it with valid words.
- Add a new implementation for the `validate_word` method. The logic is yet to be completed.

### Changed

#### ScrabbleGame Class:

- Rename the `id` attribute to `player_id`.
- Move the `show_board` method from the `experimento` module to the `ScrabbleGame` class.
- Modify the `next_turn` method to improve its functionality.
- Improve the `play` method to work more effectively.

#### Board Class:

- Remove the previous implementation of word validation methods. These are now placeholders for future implementation.

### Removed

- Remove the `show_board` method from `experimento.py `as it has been moved to the `ScrabbleGame` class.
- Remove unused imports and exceptions from `ScrabbleGame`.

## [0.30.0] - 2023-10-31

### Added

#### Board Class:

- Add the `place_multipliers` method to populate the board with word and letter multipliers at their designated positions.

#### Temporary Module `experimento.py`:

- Update the `show_board` function to adjust column width and formatting.
- Add a call to the `place_multipliers` method of the `Board` class to display the multipliers on the board.
- The module is used for testing and will be removed once it is no longer needed.

#### Square Class:

- Modifiy the `__str__` method to use Japanese-style quotes (「」) to represent letters and multipliers.

## [0.29.0] - 2023-10-31

### Added

#### Square Class:

- Add a `__str__` method to improve the string representation of a `Square` object.
  - If the square has a letter, it will be displayed as `[<letter>]`.
  - If the square is a word multiplier, it will be displayed as `[<multiplier>W]`.
  - If the square is a letter multiplier, it will be displayed as `[<multiplier>L]`.
  - Empty squares are represented as `『 』`.

#### New Temporary Module `experimento.py`:

- Create a temporary module called `experimento.py` for testing and experimentation purposes with the game board.
- Add the `show_board` function to display the game board for testing.
- In the `main` function, a `Board` instance is created and the `show_board` function is called to display the board.

## [0.28.0] - 2023-10-25

### Added

#### New Module `dictionary.py`:

- Create a new module `dictionary.py` to handle word validation against a dictionary.
- Implement a connection to the dictionary using `pyrae` (PyPI package) and set log level to 'CRITICAL'.
- Add a custom exception class `DictionaryConnectionError` for handling dictionary connection errors.
- Implement the `validate_dictionary` function to check if a word exists in the dictionary, raising a `DictionaryConnectionError` if the word is not found.

### Removed

#### Board Class:

- Remove the placeholder method `dict_validate_word`, as word validation is now handled by the `dictionary.py` module.

## [0.27.0] - 2023-10-24

### Changed

#### Player Class:

- Modify the `has_letters` method to raise a `KeyError` when a player lacks the required letters to form a word. This change allows for a more specific error message that indicates which letter is missing.
- Renamed the `id` attribute to `player_id` for clarity.

#### Board Class:

- Implement a placeholder method `dict_validate_word` to validate the existence of a word within a dictionary. The actual validation logic or API integration is pending.

#### Removed

- Remove `InsufficientLettersError` custom exception:
  - It will later be re-implemented in a better way.

## [0.26.0] - 2023-10-23

### Added

- Add the `InsufficientLettersError` custom exception in the `Player` class:
  - The `has_letters` method now raises this exception when a player has insufficient letters to make a play.

### Changed

#### Player Class:

- Modify the `has_letters` method to raise `InsufficientLettersError` when the player lacks the required letters to make a play.

#### ScrabbleGame Class:

- Update the `validate_word` method in the `ScrabbleGame` class:
  - Add a new check to ensure that the player has the necessary letters to form the word.
  - Add a check to verify that the word passes through the initial location on the board.
  - These additional checks enhance the validation process for word placement.

## [0.25.0] - 2023-10-22

### Added

- Add the `InsufficientLettersError` custom exception:
  - This exception is declared but not fully implemented yet. It will be used for cases where a player has insufficient letters for a specific action.

### Changed

#### Player Class:

- Modify the `has_letters` method in the `Player` class:
  - Reimplemented the `has_letters` method to use a more efficient approach.
  - It now counts the player's letters and checks if the required letters are available.
  - This change improves the method's performance and readability.

### Removed

- Remove the previous implementation of the `has_letters` method which was marked for improvement.

## [0.24.0] - 2023-10-21

### Changed

#### BagTiles Class:

- Modify the tile representation for "CH" and "LL" to "CH" and "LL" respectively, ensuring consistent formatting.

- Update the `take` method to handle wildcards:
  - If a wildcard is drawn from the bag and `wildcard_value` is provided, it sets the wildcard's value accordingly.

#### Tile Class:

- Update the `Tile` class to include a `wildcard_value` attribute, which is set to `None` by default.

- Add the `set_wildcard_value` method to set the `wildcard_value` for a tile if it's a wildcard.

## [0.23.0] - 2023-10-20

### Added

#### ScrabbleGame Class:

- Add the `InvalidTurnException` custom exception:
  - This exception is raised in the `next_turn` method when attempting to switch to the next player's turn, but it doesn't succeed.

### Changed

- Update the `next_turn` method in the `ScrabbleGame` class to raise the `InvalidTurnException` when necessary, providing an informative error message.

- Made minor internal adjustments to support the new features, exceptions, and methods.

## [0.22.0] - 2023-10-11

### Added

#### ScrabbleGame Class:

- Add the `show_board` method to the `ScrabbleGame` class:
  - This method prints the current state of the game board, displaying the grid and squares.

### Changed

- Made minor internal adjustments to support the new `show_board` method.

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