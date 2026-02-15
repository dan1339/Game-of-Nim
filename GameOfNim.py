"""
Daniel Rostin
Game of Nim
"""
import random

def fnComputerMove(iStones):
    # Pre: iStones must be an integer greater than 0 - must have remaining stones in the game to take 
    # Post: Returns the number of stones the computer takes
    iStonesToTake = (iStones - 1) % 4
    if iStonesToTake == 0 or iStonesToTake > iStones:
        iStonesToTake = random.randint(1, min(3, iStones))
    print("Computer takes", iStonesToTake, "stone(s).")
    return iStonesToTake

def fnPlayerMove(iStones):
    # Pre: iStones must be an integer greater than 0 - must have remaining stones in the game to take 
    # Post: Returns the number of stones the player takes 
    iStonesToTake = 0
    while iStonesToTake not in range(1, min(3, iStones) + 1):
        iStonesToTake = int(input(f"Your turn! There are {iStones} stones left. Take 1, 2, or 3 stones: "))
        if iStonesToTake not in range(1, min(3, iStones) + 1):
            print("Invalid number of stones. You must take 1, 2, or 3 stones.")
    return iStonesToTake


def fnGame():
    # Pre: None.
    # Post: Manages gameplay until the game ends
    iStones = random.randint(21, 31)
    print(f"There are {iStones} stones to start with.")

    boolPlayerTurn = random.choice([True, False])  # True for player, False for computer

    # Game loop
    while iStones > 0:
        if boolPlayerTurn:
            iStones -= fnPlayerMove(iStones)
            if iStones == 0:
                print("You took the last stone. You lose!")
                break
        else:
            iStones -= fnComputerMove(iStones)
            if iStones == 0:
                print("Computer took the last stone. Computer loses!")
                break

        print(f"{iStones} stone(s) left.")
        boolPlayerTurn = not boolPlayerTurn
fnGame()
