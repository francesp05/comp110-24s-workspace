"""simple battleship.. leveled up!"""
__author__ = "730672003"

# Emoji time!!
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

# secret ship location
grid_size: int = 4
secret_row: int = 3
secret_column: int = 2

# prompt user to guess a row, store answer as integer ++ prompt user to try again if guess is outside bounds
row1: int = int(input("Guess a row: "))
while row1 > grid_size or row1 < 1:
    row1 = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

# prompt user to guess a column, store answer as integer ++ prompt user to try again if guess is outside bounds
column1: int = int(input("Guess a column: "))
while column1 > grid_size or column1 < 1:
    column1 = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

# create conditional result box using red or white depending on if user hit or miss
# hit
if row1 == secret_row and column1 == secret_column:
    result = RED_BOX
    msg = "Hit!"
# giving the user a hint
elif row1 == secret_row and column1 != secret_column:           
    result = WHITE_BOX
    msg = "Close! Correct row, wrong column."
elif column1 == secret_column and row1 != secret_row:
    result = WHITE_BOX
    msg = "Close! Correct column, wrong row."
# complete miss
else:
    result = WHITE_BOX
    msg = "Miss!"

# printing the grid
rowcounter: int = 1
while rowcounter <= grid_size:
    rows: str = ""
    columncounter: int = 1
    if row1 == rowcounter:
        while columncounter <= grid_size:
            if column1 == columncounter:
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

# Telling the user if it is a hit, miss, or close
print(msg)