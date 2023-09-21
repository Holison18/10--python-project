import random

# declare variables
target = 21
totalMoves = 5
# initialize player1total and computerTotal to 0
player1Moves = []
computerMoves = []

# declare a function randomSelectPlayer which will randomly select a player when the game begins
def randomSelectPlayer():
    arr = [1, 2]
    number = random.choice(arr)
    return number

# When the computer is selected as the one to make a move, this function is called
def computer():
    print("Computer's turn...")
    move = random.randint(1, 10)
    computerMoves.append(move)  # add the randomly selected move to the computer's total moves


# player1 function is called when player1 is selected randomly
def player1():
    print("Prayer 1's turn")
    print("Select a number between 1 to 10")
    move = int(input(">> "))
    player1Moves.append(move)

def start():
    print(f"\n\t\t\t21 number game")
    print(f"\t\t\t--------------")
    print("Making a choice of who will start first....")
    # randomly select a player
    player = randomSelectPlayer()
    # continue the game until the total moves are reached and total of both players is less than 21
    while True:
        if player == 1:
            movesMade = 0
            # check if player1 has reached the target
            if player1Moves == 21:
                print("Player1 wins")
                break
            elif sum(player1Moves) < 21 and movesMade < totalMoves:  # if player one has not reached the target and still has moves, then he can play
                player1()
                movesMade += 1
                player = 2
            else:
                print("Player1 lost")
                break
        elif player == 2:
            movesMade = 0
            if sum(computerMoves) == 21:
                print("Computer wins")
                break
            elif sum(computerMoves) < 21 and movesMade < totalMoves:
                computer()
                movesMade += 1
                player = 1
            else:
                print("Computer lost")
                break
start()
