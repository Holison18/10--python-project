import random

target = 21
totalMoves = 5
player1Moves = []
computerMoves = []

def toggle_player(current_player):
    return 3 - current_player 

def computer():
    print("Computer's turn...")
    move = random.randint(1, min(10, target - sum(computerMoves))) # put a constraint so that computer doesn't exceed the target
    computerMoves.append(move)

def player1():
    print("Player 1's turn")
    print("Select a number between 1 to 10")
    move = int(input(">> "))
    if move < 1 or move > 10:
        print("Invalid input. Please choose a number between 1 and 10.")
    else:
        player1Moves.append(move)

def start():
    print("\n\t\t\t21 number game")
    print("\t\t\t--------------")
    print(f"\n\t\t\tTarget: {target}\n\t\t\tTotal moves: {totalMoves}\n")
    print("\t\t\t1. Player 1\n\t\t\t2. Computer\n")  
    print("\t\t\tWho will start the game?\n")
    print("\t\t\tEnter 1 or 2\n")
    current_player = int(input(">> "))

    while True:
        print(f"Player 1 total moves: {sum(player1Moves)}")
        print(f"Computer total moves: {sum(computerMoves)}")

        if (sum(player1Moves) >= target) or (sum(computerMoves) >= target):
            if sum(player1Moves) > sum(computerMoves):
                print("Player 1 wins")
            else:
                print("Computer wins")
            break

        if current_player == 1:
            movesMade = len(player1Moves)  # Count player1's moves
            if sum(player1Moves) >= target:
                print("Player 1 wins")
                break
            elif movesMade < totalMoves:
                player1()
            else:
                print("Out of moves")
                break
            current_player = toggle_player(current_player)  # Toggle player here
        elif current_player == 2:
            movesMade = len(computerMoves)  # Count computer's moves
            if sum(computerMoves) >= target:
                print("Computer wins")
                break
            elif movesMade < totalMoves:
                computer()
            else:
                print("Out of moves")
                break
            current_player = toggle_player(current_player) # Toggle player here

start()
