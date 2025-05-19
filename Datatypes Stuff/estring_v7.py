import string, sys, os, time, operator
from functools import reduce
from sort import *
import tkinter as tk
from tkinter import scrolledtext

CUT = "=================================="
results = []

def P(result):
    results.append(result)

def clr():  # clear the screen
    os.system("cls" if os.name == "nt" else "clear")

def again():  # Run again
    P(CUT)
    ask = input("Do you want to try again (y/n): ")
    P(CUT)
    if ask == "y" or ask == "Y":
        clr()
        string_game()
    elif ask == "n" or ask == "N":
        clr()
        sys.exit()
    else:
        clr()
        P("Invalid Input! Try again.")
        again()

class Text:
    def text_analyzer(self, text: str) -> dict:
        P(f"{CUT}TEXT-ANALYZER{CUT}")
        details: dict = {
            "User Entered": text,
            "Split by words": (words := text.split()),
            "Reverse": text[::-1],
            "Words": len(words),
            "Char Words": len("".join(words)),
            "Char Words w/ Spaces": len(text),
            "ID": id(text),
            "Memory": sys.getsizeof(text),
        }

        for key, value in details.items():
            P(f"{key}: {value}")

    def count_letters(self, string_list):
        vowels = set("aeiou")
        letters = string.ascii_lowercase
        consonants = set(letters) - vowels
        if (
            sum(
                1
                for word in string_list
                for letter in word
                if letter.isalpha() or letter in string.punctuation or letter.isspace()
            )
            > 0
        ):
            P(CUT)
            P(f"Letters: {sum(1 for word in string_list for letter in word if letter.isalpha())}")
            P(f"Uppercase Letters: {sum(1 for c in string_list for s in c if s.isupper())}")
            P(f"Lowercase Letters: {sum(1 for c in string_list for s in c if s.islower())}")
            P(CUT)
            P(f"Vowels: {sum(1 for c in string_list for s in c if s.lower() in vowels)}")
            P(f"Lowercase Vowels: {sum(1 for c in string_list for s in c if s.islower() and s in vowels)}")
            P(f"Uppercase Vowels: {sum(1 for c in string_list for s in c if s.isupper() and s.lower() in vowels)}")
            P(CUT)
            P(f"Consonants: {sum(1 for c in string_list for s in c if s.lower() in consonants)}")
            P(f"Lowercase Consonant: {sum(1 for c in string_list for s in c if s.islower() and s in consonants)}")
            P(f"Uppercase Consonant: {sum(1 for c in string_list for s in c if s.isupper() and s.lower() in consonants)}")
            P(CUT)
            P(f"Symbols: {sum(1 for c in string_list for s in c if s in string.punctuation)}")
            P(f"Spaces: {sum(1 for c in string_list for s in c if s.isspace())}")
        else:
            P(CUT)
            return P("String: None")

    def count_numbers(self, string_list):
        num_numbers = num_ave = sum_num = sub_num = res_num = mul_num = quo_num = (
            div_rem
        ) = div_num = 0
        num_odd = odd_add = odd_min = odd_ave = 0
        num_even = eve_add = eve_min = eve_ave = 0
        eve_mul = eve_div = odd_mul = odd_div = 1
        for s in string_list:
            # Count numbers and their sum
            if any(c.isdigit() for c in s):
                numbers_list = sorted([int(c) for c in s if c.isdigit()], reverse=True)
                num_numbers += len(numbers_list)
                sum_num += sum(numbers_list)
                num_ave = round(sum_num / num_numbers, 2)
                sub_num = reduce(lambda x, y: x - y, numbers_list)
                res_num = reduce(lambda x, y: x * y, numbers_list)
                mul_num = reduce(lambda x, y: x**y, numbers_list)
                # Division and Remainder
                if 0 in numbers_list:
                    quo_num, div_rem, div_num = "N/A"
                else:
                    div_num = reduce(lambda x, y: x // y, numbers_list)
                    div_rem = reduce(lambda x, y: x % y, numbers_list)
                    quo_num = round(reduce(lambda x, y: x / y, numbers_list), 3)
                # Odd and Even Numbers
                odd_list, even_list = [], []
                for n in numbers_list:
                    if n % 2 == 0:
                        num_even += 1
                        eve_add += n
                        eve_min -= n
                        eve_mul *= n
                        even_list.append(n)
                        eve_ave = round(eve_add / len(even_list), 2)
                        even_list.sort(reverse=True)
                        if 0 in numbers_list:
                            eve_div = "N/A"
                        else:
                            eve_div /= float(n)
                    else:
                        num_odd += 1
                        odd_add += n
                        odd_min -= n
                        odd_mul *= n
                        odd_list.append(n)
                        odd_div /= float(n)
                        odd_ave = round(odd_add / len(odd_list), 2)
                        odd_list.sort(reverse=True)
            # ALL NUMBERS IN LIST
            if num_numbers > 0:
                P(CUT)
                P(f"Number's List: {numbers_list}")
                P(f"Number/s: {num_numbers}")
                P(f"Average of the Number/s: {num_ave}")
                P(f"(+) Number/s: {sum_num}")
                P(f"(-) Number/s: {sub_num}")
                P(f"(*) Number/s: {res_num}")
                P(f"(/) Number/s: {quo_num}")
                P(f"(%) Number/s: {div_rem}")
                if not len(numbers_list) <= 3:
                    P(CUT)
                    P(f"Bubble Sorted List: {bubble_sort(numbers_list)}")
                    P(f"Insertion Sorted List: {insertion_sort(numbers_list)}")
                    P(f"Selection Sorted List: {selection_sort(numbers_list)}")
                    P(f"Merge Sorted List: {merge_sort(numbers_list)}")
                    P(f"Quick Sorted List: {quick_sort(numbers_list)}")
                    P(f"Radix Sorted List: {radix_sort(numbers_list)}")
                    P(f"Counting Sort List: {counting_sort(numbers_list, 1)}")
                    P(f"Stupid Sorted List: {stupid_sort(numbers_list)}")
                    P(f"Built-in Sorted List: {sorted(numbers_list)}")
                else:
                    P(CUT)
                    P("Number List cannot be sorted.")

                # EVEN LIST
                P(CUT)
                if not len(even_list) <= 0:
                    P(
                        f"Even's List: {even_list}\nEven number/s: {num_even}\nEven's Average: {eve_ave}\n(+) Even: {eve_add}\n(-) Even: {eve_min}\n(*) Even: {eve_mul}\n(/) Even: {round(eve_div, 3) if isinstance(eve_div, (int, float)) else eve_div}"
                    )
                    if not len(even_list) <= 3:
                        P(CUT)
                        P(f"Bubble Sorted List: {bubble_sort(even_list)}")
                        P(f"Insertion Sorted List: {insertion_sort(even_list)}")
                        P(f"Selection Sorted List: {selection_sort(even_list)}")
                        P(f"Merge Sorted List: {merge_sort(even_list)}")
                        P(f"Quick Sorted List: {quick_sort(even_list)}")
                        P(f"Radix Sorted List: {radix_sort(even_list)}")
                        P(f"Counting Sort List: {counting_sort(even_list, 1)}")
                        P(f"Stupid Sorted List: {stupid_sort(even_list)}")
                        P(f"Built-in Sorted List: {sorted(even_list)}")
                    else:
                        P(CUT)
                        P("Even List cannot be sorted.")
                else:
                    P(CUT)
                    P("No even numbers.")
                # ODD LIST
                P(CUT)
                if not len(odd_list) <= 0:
                    P(
                        f"Odd's List: {odd_list}\nOdd number/s: {num_odd}\nOdd's Average: {odd_ave}\n(+) Odd: {odd_add}\n(-) Odd: {odd_min}\n(*) Odd: {odd_mul}\n(/) Odd: {round(odd_div, 3)}"
                    )
                    if not len(odd_list) <= 3:
                        P(CUT)
                        P(f"Bubble Sorted List: {bubble_sort(odd_list)}")
                        P(f"Insertion Sorted List: {insertion_sort(odd_list)}")
                        P(f"Selection Sorted List: {selection_sort(odd_list)}")
                        P(f"Merge Sorted List: {merge_sort(odd_list)}")
                        P(f"Quick Sorted List: {quick_sort(odd_list)}")
                        P(f"Radix Sorted List: {radix_sort(odd_list)}")
                        P(f"Counting Sort List: {counting_sort(odd_list, 1)}")
                        P(f"Stupid Sorted List: {stupid_sort(odd_list)}")
                        P(f"Built-in Sorted List: {sorted(odd_list)}")
                    else:
                        P(CUT)
                        P("Odd List cannot be sorted.")
                else:
                    P(CUT)
                    P("No odd numbers.")
                P(CUT)
                more = input("You want more int calculations (y/n): ")
                if more == "y" or more == "Y":
                    P(CUT)
                    P(
                        f"Squared num: {sorted([x**2 for x in numbers_list], reverse=False)}"
                    )
                    P(
                        f"Squared odd: {sorted([x**2 for x in odd_list], reverse=False)}"
                    )
                    P(
                        f"Squared even: {sorted([x**2 for x in even_list], reverse=False)}"
                    )
                    sys.set_int_max_str_digits(100000)
                    P(f"(//) Number/s: {div_num}")
                    P(f"(**) Number/s: {mul_num}")
            else:
                P(CUT)
                return P("Integer: None")

def string_game() -> None:
    clr()
    txt = Text()
    string_list = []
    done = False  # flag variable
    while not done:
        # progress_bar() #Loading screen
        s = input("Enter a string (press enter to stop): ")
        if s == "":
            if len(string_list) == 0:  # if no string has been entered
                clr()
                print("!!!Please enter at least one string!!!")
            else:
                done = True  # exit the loop
        else:
            string_list.append(s)
            txt.text_analyzer(s)
            txt.count_letters(string_list)
            txt.count_numbers(string_list)
            again()

    window = tk.Tk()
    window.title("String Game Results")
    result = "\n".join(string_list)
    text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=100, height=30)
    text_area.pack(padx=10, pady=10)
    text_area.insert(tk.INSERT, result)
    text_area.configure(state='disabled')  # Make the text area read-only

    window.mainloop()

if __name__ == "__main__":
    string_game()
