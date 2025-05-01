# Minesweeper
## Game Principle

The Minesweeper game consists of a rectangular grid, with all cells initially covered (hidden). A certain number of cells, determined randomly at the start, contain an explosive mine. The goal of the game is to uncover all cells that do not contain a mine as quickly as possible.

The player can interact with the game board in different ways:

- Uncover a cell by left-clicking on it. In this case, if the cell contains a mine, the game is lost. Otherwise, the cell is uncovered;
- Indicate by right-clicking that they think a mine is located on a certain cell. The cell is then marked to avoid an accidental click.

When a cell that does not contain a mine is uncovered, two scenarios arise:

- If the cell is adjacent to at least one mine, an integer between 1 and 8, indicating the total number of mines on the eight neighboring cells, is displayed in the cell. No other cells are uncovered.
- If the cell is not adjacent to any mine, all cells adjacent to this cell must be (recursively!) uncovered.

## Configuration

The program allows the following aspects of the game to be configured:

- number of rows and columns of the grid;
- number of mines present;
- initial opening of a cell (or not);
- window size;
- variants...

## Installation Instructions

To install and configure the game, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/yacine20005/Demineur.git
   cd Demineur
   ```

2. Run the game:
   ```sh
   python main.py
   ```

## Usage Examples

To start a game, run the following command:
```sh
python main.py
```

Basic controls:
- Left-click to uncover a cell.
- Right-click to mark a cell as containing a mine.

## Code Structure

The repository contains the following files:

- `main.py`: The main entry point of the game.
- `affichage.py`: Contains functions to display the game in the terminal and graphically.
- `fltk.py`: A library for creating graphical user interfaces.
- `interne.py`: Contains the internal logic of the game and functions.
- `menu.py`: Contains functions to display and manage the game menu.
- `README.md`: This file, containing the description of the game and instructions.

## Related Resources

- [FLTK Documentation](https://www.fltk.org/documents.php)
- [Python Documentation](https://docs.python.org/3/)
