# MineSweeper Game
This Python script implements a console-based MineSweeper game. It allows the player to choose between two modes: closed and open. The closed mode reveals the mine count in adjacent cells upon selection, while the open mode exposes the mine count only when selected.

# How to Use:
# Run the Script:

Execute the Python script in your preferred Python environment.

# Game Initialization:

Enter the size of the game board. It must be at least 10x10.
Choose the game mode (closed/open).
# Gameplay:

In each mode, input the row and column numbers to reveal the content of that cell.
The game continues until either all non-mine cells are revealed (win) or a mine is selected (loss).
# End of Game:

The game will display whether you win or lose.
After completion, you can choose to start a new game or exit the program.
File Description:
mine_sweeper.py: Python script containing the MineSweeper game logic.
README.md: Documentation file explaining the game and its usage.
# Game Rules:
The game board size must be at least 10x10.
Mines are randomly generated and occupy approximately 30% of the total cells.
Players can choose between closed and open modes.
In closed mode, the nearby mine count of a selected cell is shown.
In open mode, the nearby mine count is revealed only upon selecting a cell.
The game continues until all non-mine cells are revealed or a mine is chosen.
# Customization:
Feel free to modify the code to enhance the game further:

Adjust the mine generation ratio (size * size / 10 * 3) to change the number of mines.
Implement additional features or graphical interfaces for a better user experience.
Dependencies:
Python 3.x
# How to Run:
Clone or download the repository.
Open the command line or terminal.
Navigate to the directory containing the script.
Run the script using python mine_sweeper.py.
Follow the on-screen instructions to play the game.
# Author:
Abdullah Dedeoglu 