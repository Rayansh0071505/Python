# # Rock Paper Scissors   

# Make a two-player Rock-Paper-Scissors game. 
# (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if
#  the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock

def game(a, b):
    if a == "rock" and b == "scissor":
        print("A wins")
    elif a == "scissor" and b == "paper":
        print("A wins")
    elif a == "paper" and b == "rock":
        print("A wins")
    else:
        print("B wins")

A = input("Enter your move A: ").lower()
B = input("Enter your move B: ").lower()
game(A, B)
