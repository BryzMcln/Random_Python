import string, sys, os, time
from functools import reduce
from sort import *
from clear import *

def progress_bar():
    clr()
    bar_width = 50
    animation = ["\\", "|", "/", "-",]
    an = ["+", "×"]
    for i in range(1, 101):
        percent = i
        filled_width = int(i / 100 * bar_width)
        bar = '|' * filled_width + '·' * (bar_width - filled_width)
        animation_index = (i % len(animation))
        ai = (i % len(an))
        print(f'LOADING: {an[ai]} [{bar}] {an[ai]} {percent}% {animation[animation_index]}', end='\r')
        time.sleep(0.1)

def again():
    print("==================================")
    ask = input("Do you want to try again (y/n): ")
    print("==================================")
    if ask == "y" or ask == "Y":
        clr()
        string_game()
    elif ask == "n" or ask == "N":
        clr()
        sys.exit()
    else:
        clr()
        print("Invalid Input! Try again.")
        again()


class Text:
    def count_letters(self, string_list):
        vowels = set("aeiou")
        letters = string.ascii_lowercase
        consonants = set(letters) - vowels
        
        num_numbers = num_ave = sum_num = sub_num = res_num = mul_num = quo_num = div_rem = div_num = 0
        num_odd = odd_add = odd_min = odd_ave = 0 
        num_even = eve_add = eve_min = eve_ave = 0 
        eve_mul = eve_div = odd_mul = odd_div = 1
        for s in string_list:    
            # Count numbers and their sum
            if any(c.isdigit() for c in s):
                numbers_list = sorted([int(c) for c in s if c.isdigit()], reverse=True)
                num_numbers += len(numbers_list); sum_num += sum(numbers_list); num_ave = round(sum_num / num_numbers, 2)
                sub_num = reduce(lambda x, y: x-y, numbers_list)
                res_num = reduce(lambda x, y: x*y, numbers_list)
                mul_num = reduce(lambda x, y: x**y, numbers_list)
                div_rem = reduce(lambda x, y: x%y, numbers_list)
                div_num = reduce(lambda x, y: x//y, numbers_list)
                if 0 in numbers_list:
                    quo_num = "N/A"
                else:
                    quo_num = round(reduce(lambda x, y: x/y, numbers_list), 3)
                #Odd and Even Numbers
                odd_list, even_list = [], []
                for n in numbers_list:
                    if n % 2 == 0:
                        num_even += 1; eve_add += n; eve_min -= n; eve_mul *= n; even_list.append(n); eve_ave = round(eve_add / len(even_list), 2); even_list.sort(reverse=True)
                        if 0 in numbers_list:
                            eve_div = "N/A" 
                        else:
                            eve_div /= float(n)
                    else:
                        num_odd += 1; odd_add += n; odd_min -= n; odd_mul *= n; odd_list .append(n); odd_div /= float(n); odd_ave = round(odd_add / len(odd_list), 2); odd_list.sort(reverse=True)
        
        clr()
        print("==================================")
        print(f"You Entered: {s}")
        print(f"Reverse: {s[::-1]}")
        print(f"Id:", id(s))
        print(f"Memory: {sys.getsizeof(s)} bytes & {sys.getsizeof(s) * 8} bits ")
        print(f"Characters: {len(s)}")
        print("==================================")
        
        if sum(1 for word in string_list for letter in word if letter.isalpha() or letter in string.punctuation or letter.isspace()) > 0:
            print(f"Letters: {sum(1 for word in string_list for letter in word if letter.isalpha())}")
            print(f"Uppercase Letters: {sum(1 for c in string_list for s in c if s.isupper())}")
            print(f"Lowercase Letters: {sum(1 for c in string_list for s in c if s.islower())}")
            print(f"Vowels: {sum(1 for c in string_list for s in c if s.lower() in vowels)}")
            print(f"Lowercase Vowels: {sum(1 for c in string_list for s in c if s.islower() and s in vowels)}")
            print(f"Uppercase Vowels: {sum(1 for c in string_list for s in c if s.isupper() and s.lower() in vowels)}")
            print(f"Consonants: {sum(1 for c in string_list for s in c if s.lower() in consonants)}")
            print(f"Lowercase Consonant: {sum(1 for c in string_list for s in c if s.islower() and s in consonants)}")
            print(f"Uppercase Consonant: {sum(1 for c in string_list for s in c if s.isupper() and s.lower() in consonants)}")
            print(f"Symbols: {sum(1 for c in string_list for s in c if s in string.punctuation)}")
            print(f"Spaces: {sum(1 for c in string_list for s in c if s.isspace())}")
        else:
            print("str: None")
        
        if num_numbers > 0:
            print("==================================")
            print(f"Number's List: {numbers_list}")
            print(f"Number/s: {num_numbers}")
            print(f"Average of the Number/s: {num_ave}")
            print(f"(+) Number/s: {sum_num}")
            print(f"(-) Number/s: {sub_num}")
            print(f"(*) Number/s: {res_num}")
            print(f"(/) Number/s: {quo_num}")
            print(f"(%) Number/s: {div_rem}")
            print(f"(//) Number/s: {div_num}")
            sys.set_int_max_str_digits(100000)
            print(f"(**) Number/s: {mul_num}")
            print("==================================")
            print(f"Even's List: {even_list}\nEven number/s: {num_even}\nEven's Average: {eve_ave}\n(+) Even: {eve_add}\n(-) Even: {eve_min}\n(*) Even: {eve_mul}\n(/) Even: {round(eve_div, 3)}")
            print("==================================")
            print(f"Odd's List: {odd_list}\nOdd number/s: {num_odd}\nOdd's Average: {odd_ave}\n(+) Odd: {odd_add}\n(-) Odd: {odd_min}\n(*) Odd: {odd_mul}\n(/) Odd: {round(odd_div, 3)}")
            print("==================================")
            more = input("You want more int calculations (y/n): ")
            if more == "y" or more == "Y":
                print("==================================")
                print(f"Squared num: {sorted([x**2 for x in numbers_list], reverse=False)}")
                print(f"Squared odd: {sorted([x**2 for x in odd_list], reverse=False)}")
                print(f"Squared even: {sorted([x**2 for x in even_list], reverse=False)}")
            else:
                again()
        else:
            print("==================================")
            print("int: None")
        again()

def string_game():
    clr()
    txt = Text()
    string_list = []
    done = False  # flag variable
    while not done:
        s = input("Enter a string (press enter to stop): ")
        if s == "":
            if len(string_list) == 0:  # if no string has been entered
                clr()
                print("!!!Please enter at least one string!!!")
            else:
                done = True  # exit the loop
        else:
            #progress_bar()
            string_list.append(s)
            txt.count_letters(string_list)

if __name__ == "__main__":
    string_game()