import random, os
from clear import *

def rps():
    hands = {1: 'rock', 2: 'paper', 3: 'scissors'}
    player_score = 0
    computer_score = 0
    clr()
    while player_score < 10 and computer_score < 10:
        print("=============================")
        print("      ROCK-PAPER-SCISSORS")
        print("=============================")
        print(f"1. {hands[1]}")
        print(f"2. {hands[2]}")
        print(f"3. {hands[3]}")
        print("=============================")

        choice = int(input("Enter your choice (1-3): "))

        if choice not in hands:
            print("Invalid choice. Please select a number from 1 to 3.")
            continue

        computer_choice = random.choice(list(hands.keys()))
        print(f"{hands[choice]} <===> {computer_choice}")


        if choice == computer_choice:
            print("It's a tie! No points awarded.")
        elif (choice == 1 and computer_choice == 3) or (choice == 2 and computer_choice == 1) or (choice == 3 and computer_choice == 2):
            player_score += 1
        else:
            computer_score += 1

        print("Player Score:", player_score)
        print("Computer Score:", computer_score)
        print("=============================")

    if player_score == 10:
        print("Congratulations! You reached 10 victories. You win!")
    else:
        print("Game over. Computer reached 10 victories. Computer wins!")
    input('Press any key to continue...')

if __name__ == "__main__":
    rps()
