# This is a simple 21 number game using python programming language.
# This game is played between the play and the computer
# The player can choose to start first or second
import random

# declare variables
target = 21
totalMoves = 5
player1total = 0
computerTotal = 0

# declare a function randomSelectPlayer which will randomly select a player when the game begins
def randomSelectPlayer():
    arr = [1,2]
    number = random.choice(arr)
    return arr

# When the computer is selected as the one to make a move, this function is called
def computer():
    print("Computer's turn.....")
    move = random.randint(1,4)
    # add move to the computerTotal
    computerTotal += move
    print(f"Computer selected {move}")
    print(f"Computer total is {computerTotal}")

# player1 function is called when player1 is selected randomly
def player1():
    print("Player 1's turn.....")
    print("Press any key to make a move")
    input()


def start():
    print(f"\n\t\t\t21 number game")
