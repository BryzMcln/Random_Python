import string, sys
from functools import reduce

def count_letters(string_list):
    vowels = set("aeiou")
    letters = string.ascii_lowercase
    consonants = set(letters) - vowels
    numbers = set(string.digits)
    
    num_uppercase = num_lowercase = num_vowels = num_consonants = num_symbols = num_spaces = 0
    up_con = up_vow = lo_con = lo_vow = 0
    num_numbers = sum_num = sub_num = res_num = quo_num = 0
    num_odd = odd_add = odd_min = 0 
    num_even = eve_add = eve_min = 0 
    eve_mul = eve_div = odd_mul = odd_div = 1
    
    for s in string_list:
        num_uppercase += sum(1 for c in s if c.isupper())
        num_lowercase += sum(1 for c in s if c.islower())
        num_vowels += sum(1 for c in s if c.lower() in vowels)
        num_consonants += sum(1 for c in s if c.lower() in consonants)
        num_symbols += sum(1 for c in s if c in string.punctuation)
        num_spaces += sum(1 for c in s if c.isspace())

        up_vow += sum(1 for c in s if c.isupper() and c.lower() in vowels)
        lo_vow += sum(1 for c in s if c.islower() and c in vowels)
        up_con += sum(1 for c in s if c.isupper() and c.lower() in consonants)
        lo_con += sum(1 for c in s if c.islower() and c in consonants)
        
        # Count numbers and their sum
        if any(c.isdigit() for c in s):
            numbers_list = [int(c) for c in s if c.isdigit()]
            num_numbers += len(numbers_list)
            sum_num += sum(numbers_list)
            sub_num = reduce(lambda x, y: x-y, numbers_list)
            res_num = reduce(lambda x, y: x*y, numbers_list)
            if 0 in numbers_list:
                quo_num = "N/A"
            else:
                quo_num = reduce(lambda x, y: x/y, numbers_list)
                quo_num = round(quo_num, 3)

            odd_list, even_list = [], []
            for n in numbers_list:
                if n % 2 == 0:
                    num_even += 1
                    eve_add += n
                    eve_min -= n
                    eve_mul *= n
                    even_list.append(n)
                    if 0 in numbers_list:
                        eve_div = "N/A"
                    else:
                        eve_div /= float(n)
                        eve_div = round(eve_div, 3)
                else:
                    num_odd += 1
                    odd_add += n
                    odd_min -= n
                    odd_mul *= n
                    odd_list .append(n)
                    if 0 in numbers_list:
                        odd_div = "N/A"
                    else:
                        odd_div /= float(n)
                        odd_div = round(odd_div, 3)

    num_letters = num_uppercase + num_lowercase
    num_total = len(s)
    print("==================================")
    print(f"Characters: {num_total}")
    print("==================================")
    print(f"Letters: {num_letters}\nSymbols: {num_symbols}\nSpaces: {num_spaces}\nUppercase Letters: {num_uppercase}\nLowercase Letters: {num_lowercase}")
    print(f"Vowels: {num_vowels}\nLowercase Vowels: {lo_vow}\nUppercase Vowels: {up_vow}")
    print(f"Consonants: {num_consonants}\nLowercase Consonant: {lo_con}\nUppercase Consonant: {up_con}")
    print("==================================")
    if num_numbers > 0:
        print(f"Number's List: {numbers_list}\nNumbers: {num_numbers}\n(+) All number: {sum_num}\n(-) All number: {sub_num}\n(*) All number: {res_num}\n(/) All number: {quo_num}")
        print("==================================")
        print(f"Even's List: {even_list}\nEven numbers: {num_even}\n(+) Even: {eve_add}\n(-) Even: {eve_min}\n(*) Even: {eve_mul}\n(/) Even: {eve_div}")
        print("==================================")
        print(f"Odd's List: {odd_list}\nOdd numbers: {num_odd}\n(+) Odd: {odd_add}\n(-) Odd: {odd_min}\n(*) Odd: {odd_mul}\n(/) Odd: {odd_div}")
        print("==================================")
    ask = input("Do you want to try again (y/n): ")
    if ask == "y" or ask == "Y":
        main()
    else:
        sys.exit()
# Main program
def main():
    string_list = []
    s = input("Enter a string (press enter to stop): ")
    while s != "":
        string_list.append(s)
        s = input("Enter a string (press enter to stop): ")

    count_letters(string_list)
if __name__ == "__main__":
    main()
