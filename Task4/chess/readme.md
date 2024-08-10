# Chess Game in Python

## Overview

This project is a Python-based chess game that allows two players to play against each other on the same computer. The game is implemented using the Pygame library and supports basic chess rules, including piece movement, turn-based play, and game over conditions when a king is captured.

## Features

- **Turn-Based Gameplay:** The game alternates turns between the two players, with visual indicators for which player's turn it is.
- **Piece Movement:** All standard chess pieces (pawns, rooks, knights, bishops, queens, kings) are implemented with valid movement logic.
- **Piece Selection:** Players can select and move pieces on the board, with visual indicators for the selected piece.
- **Game Over Condition:** The game ends when one player's king is captured, and a game-over screen is displayed.
- **Exit Button:** Allows players to exit the game at any time by clicking the exit button.


## Usage

1. **Run the Game:**
   - You can start the game by running the main script:
     ```bash
     python game.py
     ```

2. **Gameplay:**
   - The game board will be displayed with all pieces in their initial positions.
   - The game starts with White's turn. Click on a piece to select it, and then click on a valid destination square to move it.
   - The selected piece will be highlighted (red for White, blue for Black).
   - The game alternates turns between White and Black.
   - The game ends when a king is captured, at which point the game-over screen will be displayed.


## Key Functions

### `load_image(file_name, size, small_size)`
Loads and scales the images for the pieces and the board.

### `draw_board(screen)`
Renders the chessboard on the screen.

### `draw_pieces(screen, white_locations, black_locations)`
Draws the chess pieces at their current positions on the board.

### `handle_piece_selection(pos)`
Handles the logic for selecting and moving pieces based on the player's input.

### `check_game_over()`
Determines if the game has ended by checking if a king has been captured.
