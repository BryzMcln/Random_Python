import datetime

class Animal:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = datetime.datetime.strptime(birthday, "%Y-%m-%d").date()
    
    def get_age(self):
        today = datetime.date.today()
        age = today.year - self.birthday.year
        if today.month < self.birthday.month or (today.month and today.day < self.birthday.day):
            age -= 1
        return age

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def main():
    pets = []
    num_dogs = 0
    num_cats = 0
    print ("""
    =================     
    WONDER PETS!!!!
    DOG [1]
    CAT [2]
    BOTH [3]
    =================
    """)

    # Ask the user which pets they want to create
    print("================================================")
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            num_dogs = int(input("How many dogs do you want? "))
            break
        elif choice == 2:
            num_cats = int(input("How many cats do you want? "))
            break
        elif choice == 3:
            num_dogs = int(input("How many dogs do you want? "))
            num_cats = int(input("How many cats do you want? "))
            break
        else:
            print("Invalid input, please try again.")
    
    #Ask the user/owner name
    print("================================================")
    owner = input("Your name: ")
    # Ask the user to input names for each pet
    print("================================================")
    for i in range(num_dogs):
        name = input("Enter name for dog {}: ".format(i+1))
        birthday = input("Enter birthday for dog {} (YYYY-MM-DD): ".format(i+1))
        pets.append(Dog(name))
    print("================================================")
    for i in range(num_cats):
        name = input("Enter name for cat {}: ".format(i+1))
        birthday = input("Enter birthday for cat {} (YYYY-MM-DD): ".format(i+1))
        pets.append(Cat(name))

    # Print out the names and sounds of all pets
    print("================================================")
    print(f"Here are all {owner} pets:")
    for pet in pets:
        print("{} ({}, {} years old)".format(pet.name, pet.speak(), pet.get_age()))

print("================================================")

if __name__ == "__main__":
    while True:
        main()
        choice = input("Do you want to create more pets? (y/n) ")
        if choice.lower() != "y":
            break
