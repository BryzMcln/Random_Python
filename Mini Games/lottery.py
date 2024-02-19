import random

def lotteries():
    # Generate the winning numbers
    winning_numbers = random.sample(range(1, 51), 6)
    winning_numbers = sorted(winning_numbers)
    
    # Ask the user to guess the numbers
    guess_numbers = []
    for i in range(6):
        while True: 
            guess = int(input(f"Guess the {i+1} number (1-50): ")) #input the number
            if guess < 1 or guess > 50:
                print("Invalid input. Please enter a number between 1 and 50.") #check if the number is valid
            elif guess in guess_numbers:
                print("You already guessed that number. Please enter a different number.") #check if the number is already guessed
            else:
                guess_numbers.append(guess)
                guess_numbers.sort()
                break

    guess_numbers = sorted(guess_numbers)
    # Print the winning numbers and the user's guesses
    print('====================================')
    print(f"The winning numbers are: {winning_numbers}")
    print(f"Your guesses are: {guess_numbers}")   

    # Compute the number of correct guesses
    correct_guesses = set(winning_numbers) & set(guess_numbers)
    num_correct_guesses = len(correct_guesses)

    # Print the number of correct guesses
    print('====================================')
    print(f"You guessed {num_correct_guesses} correct number(s)")

    # Determine the prize based on the number of correct guesses
    print('====================================')
    prizes = {6: "₱5,000,000.00", 5: "₱100,000.00", 4: "₱10,000.00"}
    if num_correct_guesses in prizes:
        print(f"Congratulations, you won {prizes[num_correct_guesses]}!")
    else:
        print("Sorry, you did not win any prize.")

if __name__ == "__main__":
    lotteries()