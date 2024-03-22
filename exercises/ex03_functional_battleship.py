"""More battleship blahblahblah."""

__author__ = "730672003"
import random

# Emoji time!!
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


def input_guess(grid_size: int, rc: str) -> int:
    """Establish grid size and ask if input is row or column."""
    if rc == "row":
        row_guess: int = int(input("Guess a row: "))
        while row_guess > grid_size or row_guess < 1:
            row_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
        print(row_guess)
        return row_guess
    if rc == "column":
        column_guess: int = int(input("Guess a column: "))
        while column_guess > grid_size or column_guess < 1:
            column_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
        print(column_guess)
        return column_guess
    assert rc == "row" or rc == "column"


def print_grid(grid_size: int, row_guess: int, column_guess: int, correct: bool) -> None:
    """Print the grid."""
    # Hit
    if correct is True:
        result = RED_BOX
        # Msg = "Hit!"
    # Complete miss
    else:
        result = WHITE_BOX
        # Msg = "Miss!"
    rowcounter: int = 1
    while rowcounter <= grid_size:
        rows: str = ""
        columncounter: int = 1
        if row_guess == rowcounter:
            while columncounter <= grid_size:
                if column_guess == columncounter:
                    rows = rows + result
                else:
                    rows = rows + BLUE_BOX
                columncounter = columncounter + 1
        else:
            while columncounter <= grid_size:
                rows = rows + BLUE_BOX
                columncounter = columncounter + 1
        print(rows)
        rowcounter = rowcounter + 1


def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    """If guess is correct."""
    if row_guess == secret_row and column_guess == secret_column:
        print(True)
        return True
    else:
        print(False)
        return False
    

def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Utilize all function."""
    correct = False
    turn_counter = 1
    max_turns = 5  # number of turns
    while turn_counter <= max_turns and not correct:
        print(f"=== Turn {turn_counter}/{max_turns} ===")
        # Use input_guess for row and column, and store the returned values.
        row_guess = input_guess(grid_size, "row")
        column_guess = input_guess(grid_size, "column")
        # Use the values to check if they guessed right.
        correct = correct_guess(secret_row, secret_column, row_guess, column_guess)
        # Use print_grid to display the grid with the current guesses.
        print_grid(grid_size, row_guess, column_guess, correct)
        if correct:
            print(f"Hit! You won in {turn_counter}/{max_turns} turns!")
            break  # This ends the loop if the user has won.
        else:
            print("Miss!")
            if turn_counter == max_turns:
                print(f"X/{max_turns} - Better luck next time!")
        turn_counter += 1


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))