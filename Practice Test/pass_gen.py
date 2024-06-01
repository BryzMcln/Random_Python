from secrets import choice
from string import ascii_letters, digits, punctuation
from typing import Callable

def pass_gen(length: int) -> str:
    return ''.join(choice(ascii_letters + digits + punctuation) for _ in range(length))


def main() -> None:
    try:
        num = int(input("Input how long the password is: "))
        if num <= 0:
            print("Please enter a positive integer.")
        else:
            print(pass_gen(num))
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == '__main__':
    main()
