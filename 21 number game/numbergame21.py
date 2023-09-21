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
    move = random.randint(1,10)
    # add move to the computerTotal
    computerTotal += move
    print(f"Computer selected {move}")
    print(f"Computer total is {computerTotal}")

# player1 function is called when player1 is selected randomly
def player1():
    print("Player 1's turn.....")
    print("Select a number between 1 and 10")
    move = int(input())
    # add move to the player1total
    player1total += move


def start():
    print(f"\n\t\t\t21 number game")
    print(f"\t\t\t--------------")
    print("Making a choice of who will start first....")
    # randomly select a player
    player = randomSelectPlayer()
    if player == 1:
        print("Player 1 will start first")
        player1()
    else:
        print("Computer will start first")
        computer()
