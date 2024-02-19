import random

while True:
    print("MAIN MENU")
    print("========================")
    print("(1) New Game")
    print("(2) Difficulty")
    print("(3) Quit")
    
    choice = input("Enter: ")
    
    if choice == "3":
        print("Bye!")
        break
    elif choice == "2":
        default = input("Enter difficulty (Easy/Hard): ")
    elif choice == "1":
        if default == "Hard":
            min_num = 1
            max_num = 50
        else:
            min_num = 1
            max_num = 10
        
        answer = random.randint(min_num, max_num)
        guess = 0
        count = 0
        
        print("=========================")
        print("GUESS THE NUMBA!!!")
        print("The numbers between", min_num, "and", max_num)
        
        while guess != answer:
            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            
            count += 1
            
            if guess < answer:
                print("That's too low. Try again.")
                print("=========================")
            elif guess > answer:
                print("That's too high. Try again.")
                print("=========================")
            else:
                print("Correct! You guessed my number in", count, "attempts.")
                if count <= 5:
                    print("Whoa, Excellent!")
                    print("=========================")
                elif count <= 10:
                    print("Goods, Not bad.")
                    print("=========================")
                else:
                    print("Fair enough, Better luck Next time.")
                    print("=========================")
        
        choice = input("Do you want to continue? (y/n): ")
        
        if choice.lower() == "n":
            print("Bye!")
            break
