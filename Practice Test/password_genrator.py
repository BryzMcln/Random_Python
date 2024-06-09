from secrets import choice
from string import ascii_letters, digits, punctuation
import os, sys

def pass_gen(length: int) -> str:
    return ''.join(choice(ascii_letters + digits + punctuation) for _ in range(length))
# pass_gen: Callable[[int], str] = lambda x: ''.join(choice(ascii_letters + digits + punctuation) for _ in range(x))


def main() -> None:
    try:
        num = int(input("Input how long the password is: "))
        if num <= 0:
            print("Please enter a positive integer.")
        else:
            print(f"Password: {pass_gen(num)}")
        again()
    except ValueError:
        print("Invalid input. Please enter an integer.")

def again() -> None: #Run again
    print("==================================")
    ask = input("Do you want to try again (y/n): ")
    print("==================================")
    if ask == "y" or ask == "Y":
        main()
    elif ask == "n" or ask == "N":
        sys.exit()
    else:
        print("Invalid Input! Try again.")
        again()

if __name__ == '__main__':
    main()