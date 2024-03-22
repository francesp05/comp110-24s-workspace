"""EX01 - Simple Battleship - cute emoji battleship."""

__author__ = "730672003"

# Emoji time!!
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

ocean: str = BLUE_BOX * 4
# print(ocean)

# Player one picks secret boat location
boat_loc1: int = int(input("Pick a secret boat location between 1 and 4: "))
if boat_loc1 > 4:
    print(f"Error! {boat_loc1} too high!")
    exit()
elif boat_loc1 < 1:
    print(f"Error! {boat_loc1} too low!")
    exit()

# Player two picks secret boat location
boat_loc2: int = int(input("Guess a number between 1 and 4: "))
if boat_loc2 > 4:
    print(f"Error! {boat_loc2} too high!")
    exit()
elif boat_loc2 < 1:
    print(f"Error! {boat_loc2} too low!")
    exit()

# Program checks if player two's guess is equal to player one's choice
if boat_loc2 != boat_loc1:
    result: str = WHITE_BOX
    print("Incorrect! You missed the ship.")
elif boat_loc2 == boat_loc1:
    result = RED_BOX
    print("Correct! You hit the ship.")

# emojis for if user 2 chooses 1
if boat_loc2 == 1:
    ocean1: str = result + BLUE_BOX + BLUE_BOX + BLUE_BOX
    print(ocean1)
else:
    ocean 

# emojis for if user 2 chooses 2
if boat_loc2 == 2:
    ocean2: str = BLUE_BOX + result + BLUE_BOX + BLUE_BOX
    print(ocean2)
else:
    ocean 

# emojis for if user 2 chooses 3
if boat_loc2 == 3:
    ocean3: str = BLUE_BOX + BLUE_BOX + result + BLUE_BOX
    print(ocean3)
else:
    ocean 

# emojis for if user 2 chooses 4
if boat_loc2 == 4:
    ocean4: str = BLUE_BOX + BLUE_BOX + BLUE_BOX + result
    print(ocean4)
else:
    ocean 
