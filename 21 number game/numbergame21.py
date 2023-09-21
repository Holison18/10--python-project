# This is a simple 21 number game using python programming language.
# This game is played between the play and the computer
# The player can choose to start first or second
import random

# declare variables
target = 21
totalMoves = 5



# declare a function randomSelectPlayer which will randomly select a player when the game begins
def randomSelectPlayer():
    arr = [1,2]
    number = random.choice(arr)
    return arr

# set the computerTotal to 0
computerTotal = 0

# When the computer is selected as the one to make a move, this function is called
def computer(move):
    pass

# set the player1total to 0
player1total = 0

# player1 function is called when player1 is selected randomly
def player1(move):
    pass


def start():
    print(f"\n\t\t\t21 number game")
    print(f"\t\t\t--------------")
    print("Making a choice of who will start first....")
    # randomly select a player
    player = randomSelectPlayer()
    # continue the game until the total moves are reached and total of both players is less than 21
    while True:
        if player == 1:
            print("Player 1's turn")
            player1()
            player = 2
        else:
            computer()
            print("Computer's turn")
            player = 1
        if player1total >= 21 or computerTotal >= 21:
            break


start()
