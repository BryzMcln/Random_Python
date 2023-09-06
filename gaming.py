from Dougnut_Bagel_v1 import *
from game import *
from estring_v5 import *
from sort import *
from tictactoe import *
from lottery import *
from clear import *
import time

def show():
    clr()
    print("""
    ==========================
    Choose a game:
    1. Number Game
    2. String Game
    3. Tictactoe Game
    4. Sorting Game
    5. Lottery Game
    6. Spin   
    ==========================
    """)

def main():
    show()
    choose = 1
    var: int = int(input("Pick a number: "))
    func: dict = {0: main, 1: num_game, 2: string_game,3: tictactoe,
                  4: sorting, 5: lotteries, 6: spin}
    final = func.get(var, main)
    final()

"""     while True:
        show()
        try:
            user = int(input("Enter: "))
            if user == 1:
                num_game()
            elif user == 2:
                string_game()
            elif user == 3:
                tictactoe()      
            elif user == 4:
                sorting()
            elif user == 5:
                lotteries()
            elif user == 6:
                spin()
            else:
                raise ValueError('Invalid insertion')
        except ValueError as e:
            print('=================')
            print('Error input:', e)
            print('=================')
            time.sleep(1) """


if __name__ == "__main__":
    main()