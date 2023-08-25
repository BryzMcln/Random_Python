import random, os
from clear import *
HANDS = {1: 'ROCK', 2: 'PAPER', 3: 'SCISSORS'}
PLAYER_SCORE = 0
COMPUTER_SCORE = 0
clr()
def menu():
    print("=================================")
    print("    ~ ROCK·PAPER·SCISSORS ~")
    print(f"    PLAYER: {PLAYER_SCORE} || COMPUTER: {COMPUTER_SCORE} ")
    print("=================================")
    print(f"1. {HANDS[1]}")
    print(f"2. {HANDS[2]}")
    print(f"3. {HANDS[3]}")
    print("4. CANCEL")
    print("=================================")

def rps():
    global PLAYER_SCORE, COMPUTER_SCORE
    while PLAYER_SCORE < 10 and COMPUTER_SCORE < 10:
        menu()
        choice = input("Enter your choice (1-3 or 4): ")

        if choice == '4':
            leave()
            break

        choice = int(choice)

        if choice not in HANDS.keys():
            clr()
            print("Invalid! Try again.")
            continue

        computer_choice = random.choice(list(HANDS.keys()))
        computer_choice_value = HANDS[computer_choice]
        if choice == computer_choice:
            clr()
            print(f"      {HANDS[choice]} <=(TIE)=> {computer_choice_value}")
        elif (choice == 1 and computer_choice == 3) or (choice == 2 and computer_choice == 1) or (choice == 3 and computer_choice == 2):
            clr()
            PLAYER_SCORE += 1
            print(f"\t{HANDS[choice]} <===> {computer_choice_value}")
        else:
            clr()
            COMPUTER_SCORE += 1
            print(f"\t{HANDS[choice]} <===> {computer_choice_value}")

    if PLAYER_SCORE == 10:
        clr()
        print("VICTORY, YOU WIN!")
        print("You have reached a score of 10.")
    else:
        clr()
        print("GAME OVER. COMPUTER WINS")
        print("Computer reached 10 victories.")
    input('Press ENTER to continue...')

def leave():
    ask = ["Do you want to leave?", "Are you qutting?", "You don't want play?", "Giving up?", "Exit the game?",
           "End this gameplay?", "Done playing?", "Try'na stop now?, Can't play anymore?"]
    random.shuffle(ask)  # Shuffle the list of ask
    ran_ask = random.choice(ask)  # Choose a random from the shuffled list
    while True:
        clr()
        try: 
            print(f"{ran_ask}")
            me = int(input("(1) YES || (2) NO: "))
            if me == 1:
                exit()
            elif me == 2:
                input('Press ENTER to continue...')
                rps()
            else:
                raise ValueError('Invalid! Try again')
        except ValueError as e:
            print("ERROR 404!")
    

if __name__ == "__main__":
    rps()
