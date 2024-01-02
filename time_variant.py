from timer import set_timer
from datetimer import datetimes
from stop_watchpy import stopwatch
import random, os, time

def clr():
     os.system('cls')

def title():
    print('WELCOME to TIME VARIANT')
    print("========================")
    print("1. Date and Time")
    print("2. Timer")
    print("3. Stop watch")
    print("4. Leaving")
    print("========================")

def timevariant():
    title()
    while True:
        clr()
        try:
            t = int(input("Enter: "))
            if t == 1:
                datetimes()
            elif t == 2:
                set_timer()
            elif t == 3:
                stopwatch()
            else:
                raise ValueError("Unacceptable Input!")
        except ValueError as e:
            print("Something Went Wrong!")

def leave():
    ask = ["Do you want to leave?", "Are you qutting?", "You don't want play?", "Giving up?", "Exit the game?",
           "End this gameplay?", "Done playing?", "Try'na stop now?", "Can't play anymore?", "Wanna take a break?"]
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
                timevariant()
            else:
                raise ValueError('Invalid! Try again')
        except ValueError as e:
            print("ERROR 404!")

if __name__ == "__main__":
    timevariant()