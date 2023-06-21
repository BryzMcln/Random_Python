import os, sys, random, time

global NUM_DIGITS,  ARITHMETIC_OPERATOR #global variables
ARITHMETIC_OPERATOR = '+' #default operator
NUM_DIGITS = 2 #default number of digits
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def loading():
    bar_width = 50
    animation = ["\\", "|", "/", "-",]
    an = ["+", "×"]
    for i in range(1, 101):
        percent = i
        filled_width = int(i / 100 * bar_width)
        bar = '|' * filled_width + '·' * (bar_width - filled_width)
        animation_index = (i % len(animation))
        ai = (i % len(an))
        print(f'LOADING: {an[ai]} [{bar}] {an[ai]} {percent}% {animation[animation_index]}', end='\r') #print loading bar
        time.sleep(0.1)
    clear_screen()

def title():
    print("""
    =========================
            GUESS GAME
    =========================
            MAIN MENU:
    (1) ARITHMETIC
    (2) RANGE
    (3) OPTIONS
    (4) QUIT
    =========================
    """)

def num_game():
    clear_screen()
    #loading()
    title()
    while True:
        try:
            choice = int(input("    Enter: "))
            if choice == 1:
                arithmetic()
            elif choice == 2:
                ranges()
            elif choice == 3:
                options()
            elif choice == 4:
                quit()
            else:
                raise ValueError('Invalid choice')
        except ValueError as e:
            clear_screen()
            print('Error:', e)
            time.sleep(1)

def arithmetic():
    loading()
    clear_screen()
    score = 0
    while True:
        n1 = random.randint(10**(NUM_DIGITS-1), 10**NUM_DIGITS-1)
        n2 = random.randint(10**(NUM_DIGITS-1), 10**NUM_DIGITS-1)
        print("======================================")
        if ARITHMETIC_OPERATOR == '+':
            result = n1 + n2
            question = f"What is the answer: {n1} + {n2}"
        elif ARITHMETIC_OPERATOR == '-':
            result = n1 - n2
            question = f"What is the answer: {n1} - {n2}"
        elif ARITHMETIC_OPERATOR == '*':
            result = n1 * n2
            question = f"What is the answer: {n1} * {n2}"
        elif ARITHMETIC_OPERATOR == '/':
            result = n1 / n2
            question = f"What is the answer: {n1} / {n2}"
        elif ARITHMETIC_OPERATOR == '%':
            result = n1 % n2
            question = f"What is the answer: {n1} % {n2}"
        elif ARITHMETIC_OPERATOR == '**':
            result = n1 ** n2
            question = f"What is the answer: {n1} ** {n2}"
        print(question)
        ans = input('Enter: ')

        try:
            ans = int(ans)
            if ans == result:
                score += 1
                print("======================================")
                print("Correct!")
            else:
                print("======================================")
                print("Incorrect!")
                print(f"Your score was: {score}")
                again()
                score = 0 # reset score if user chooses to arithmetic again
        except ValueError:
            print("======================================")
            print("Invalid Input!")
            again()
            score = 0 # reset score if user chooses to arithmetic again

def ranges():
    loading()
    clear_screen()
    max = 10 ** NUM_DIGITS - 1
    min = 10 ** (NUM_DIGITS - 1)
    answer = random.randint(min, max)
    ranges = 0
    count = 0
    max_attempts = 20  # maximum number of attempts allowed
        
    print("=========================")
    print("GUESS THE NUMBA!!!")
    print("The numbers between", min, "and", max)

    while ranges != answer and count < max_attempts:
        try:
            ranges = int(input("Enter your ranges: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
            
        count += 1
            
        if ranges < answer:
            print("=========================")
            print(f"Health: {count-max_attempts}")
            print("That's too low. Try again.")
            print("=========================")
        elif ranges > answer:
            print("=========================")
            print(f"Health: {count-max_attempts}")
            print("That's too high. Try again.")
            print("=========================")
        else:
            print("Correct! You guessed my number in", count, "attempts.")
            if count <= 5:
                print("=========================")
                print("Whoa, Excellent!")
            elif count <= 10:
                print("=========================")
                print("Goods, Not bad.")
            else:
                print("=========================")
                print("Fair enough, Better luck Next time.")
        
        if count == max_attempts:
            print("You've reached the maximum number of attempts. The correct answer is:", answer)
            again()
    again()


   
def again(): # function to ask user if they want to arithmetic again
    print("==============================")
    while True:
        ask = input("Wanna play again? (y/n): ")
        if ask == "y" or ask == "Y":
            arithmetic()
        elif ask == "n" or ask == "N":
            num_game()
        else:
            clear_screen()
            print('Invalid Input, try again!')

def options():
    clear_screen()
    print('OPTIONS')
    print('---------------------')
    print('1. SET DIFFICULTY LEVEL') # set difficulty level
    print('2. CHOOSE ARITHMETIC OPERATOR') # choose arithmetic operator
    print('3. BACK TO num_game MENU') # back to num_game menu
    print('---------------------')
    try:
        choice = int(input('Enter your choice: '))
        if choice == 1:
            print('DIFFICULTY LEVELS')
            print('---------------------')
            print('1. EASY (2 digits)') 
            print('2. MEDIUM (3 digits)')
            print('3. HARD (4 digits)')
            print('---------------------')
            try:
                level_choice = int(input('Enter difficulty level: '))
                if level_choice == 1:
                    global NUM_DIGITS
                    NUM_DIGITS = 2
                    print('Difficulty level set to EASY')
                elif level_choice == 2:
                    NUM_DIGITS = 3
                    print('Difficulty level set to MEDIUM')
                elif level_choice == 3:
                    NUM_DIGITS = 4
                    print('Difficulty level set to HARD')
                else:
                    print('Invalid difficulty level')
            except ValueError:
                print('Invalid input')
        elif choice == 2:
            print('ARITHMETIC OPERATORS')
            print('---------------------')
            print('1. +')
            print('2. -')
            print('3. *')
            print('4. /')
            print('5. %')
            print('6. **')
            print('---------------------')
            try:
                operator_choice = int(input('Enter operator number: '))
                if operator_choice == 1:
                    global ARITHMETIC_OPERATOR
                    ARITHMETIC_OPERATOR = '+'
                    print('Operator set to +')
                elif operator_choice == 2:
                    ARITHMETIC_OPERATOR = '-'
                    print('Operator set to -')
                elif operator_choice == 3:
                    ARITHMETIC_OPERATOR = '*'
                    print('Operator set to *')
                elif operator_choice == 4:
                    ARITHMETIC_OPERATOR = '/'
                    print('Operator set to /')
                elif operator_choice == 5:
                    ARITHMETIC_OPERATOR = '%'
                    print('Operator set to %')
                elif operator_choice == 6:
                    ARITHMETIC_OPERATOR = '**'
                    print('Operator set to **')
                else:
                    print('Invalid operator number')
            except ValueError:
                print('Invalid input')
        elif choice == 3:
            return
        else:
            print('Invalid choice')
    except ValueError:
        print('Invalid input')
    input('Press Enter to continue...')
    num_game()


def quit():
    clear_screen()
    print("==============================")
    while True:
        why = input("Are you sure want to leave (y/n): ")
        if why == "y" or why == "Y":
            clear_screen()
            sys.exit()
        elif why == "n" or why == "N":
            clear_screen()
            num_game()
        else:
            clear_screen()
            print('Invalid Input, try again!')

if __name__ == "__num_game__":
    num_game()
