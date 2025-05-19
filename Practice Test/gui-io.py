import tkinter as tk, sys, string
from functools import reduce

class Text:
    def text_analyzer(self, text: str) -> str:
        CUT = "========="
        words = text.split()
        details = {
            "User Entered": text,
            "Split by words": words,
            "Reverse": text[::-1],
            "Words": len(words),
            "Char Words": len("".join(words)),
            "Char Words w/ Spaces": len(text),
            "ID": id(text),
            "Memory": sys.getsizeof(text),
        }
        result = [f"{CUT}TEXT-ANALYZER{CUT}"]
        for key, value in details.items():
            result.append(f"{key}: {value}")
        return "\n".join(result)

    def count_letters(self, string_list):
        vowels = set("aeiou")
        letters = string.ascii_lowercase
        consonants = set(letters) - vowels
        output = []
        CUT = "========="
        if (
            sum(
                1
                for word in string_list
                for letter in word
                if letter.isalpha() or letter in string.punctuation or letter.isspace()
            )
            > 0
        ):
            output.append(CUT)
            output.append(f"Letters: {sum(1 for word in string_list for letter in word if letter.isalpha())}")
            output.append(f"Uppercase Letters: {sum(1 for c in string_list for s in c if s.isupper())}")
            output.append(f"Lowercase Letters: {sum(1 for c in string_list for s in c if s.islower())}")
            output.append(CUT)
            output.append(f"Vowels: {sum(1 for c in string_list for s in c if s.lower() in vowels)}")
            output.append(f"Lowercase Vowels: {sum(1 for c in string_list for s in c if s.islower() and s in vowels)}")
            output.append(f"Uppercase Vowels: {sum(1 for c in string_list for s in c if s.isupper() and s.lower() in vowels)}")
            output.append(CUT)
            output.append(f"Consonants: {sum(1 for c in string_list for s in c if s.lower() in consonants)}")
            output.append(f"Lowercase Consonant: {sum(1 for c in string_list for s in c if s.islower() and s in consonants)}")
            output.append(f"Uppercase Consonant: {sum(1 for c in string_list for s in c if s.isupper() and s.lower() in consonants)}")
            output.append(CUT)
            output.append(f"Symbols: {sum(1 for c in string_list for s in c if s in string.punctuation)}")
            output.append(f"Spaces: {sum(1 for c in string_list for s in c if s.isspace())}")
        else:
            output.append(CUT)
            output.append("String: None")
        return "\n".join(output)

    def count_numbers(self, string_list):
        CUT = "========="
        output = []
        num_numbers = num_ave = sum_num = sub_num = res_num = mul_num = quo_num = div_rem = div_num = 0
        num_odd = odd_add = odd_min = odd_ave = 0
        num_even = eve_add = eve_min = eve_ave = 0
        eve_mul = eve_div = odd_mul = odd_div = 1
        numbers_list = []
        odd_list = []
        even_list = []
        for s in string_list:
            if any(c.isdigit() for c in s):
                numbers_list = sorted([int(c) for c in s if c.isdigit()], reverse=True)
                num_numbers += len(numbers_list)
                sum_num += sum(numbers_list)
                if num_numbers > 0:
                    num_ave = round(sum_num / num_numbers, 2)
                if len(numbers_list) > 0:
                    sub_num = reduce(lambda x, y: x - y, numbers_list)
                    res_num = reduce(lambda x, y: x * y, numbers_list)
                    mul_num = reduce(lambda x, y: x**y, numbers_list)
                    if 0 in numbers_list:
                        quo_num = div_rem = div_num = "N/A"
                    else:
                        div_num = reduce(lambda x, y: x // y, numbers_list)
                        div_rem = reduce(lambda x, y: x % y, numbers_list)
                        quo_num = round(reduce(lambda x, y: x / y, numbers_list), 3)
                    for n in numbers_list:
                        if n % 2 == 0:
                            num_even += 1
                            eve_add += n
                            eve_min -= n
                            eve_mul *= n
                            even_list.append(n)
                            if len(even_list) > 0:
                                eve_ave = round(eve_add / len(even_list), 2)
                                if 0 in numbers_list:
                                    eve_div = "N/A"
                                else:
                                    try:
                                        eve_div = reduce(lambda x, y: x / y, even_list)
                                    except ZeroDivisionError:
                                        eve_div = "N/A"
                        else:
                            num_odd += 1
                            odd_add += n
                            odd_min -= n
                            odd_mul *= n
                            odd_list.append(n)
                            try:
                                odd_div = reduce(lambda x, y: x / y, odd_list)
                            except ZeroDivisionError:
                                odd_div = "N/A"
                            if len(odd_list) > 0:
                                odd_ave = round(odd_add / len(odd_list), 2)
        if num_numbers > 0:
            output.append(CUT)
            output.append(f"Number's List: {numbers_list}")
            output.append(f"Number/s: {num_numbers}")
            output.append(f"Average of the Number/s: {num_ave}")
            output.append(f"(+) Number/s: {sum_num}")
            output.append(f"(-) Number/s: {sub_num}")
            output.append(f"(*) Number/s: {res_num}")
            output.append(f"(/) Number/s: {quo_num}")
            output.append(f"(%) Number/s: {div_rem}")
            output.append(CUT)
            if not len(even_list) <= 0:
                output.append(
                    f"Even's List: {even_list}\nEven number/s: {num_even}\nEven's Average: {eve_ave}\n(+) Even: {eve_add}\n(-) Even: {eve_min}\n(*) Even: {eve_mul}\n(/) Even: {round(eve_div, 3) if isinstance(eve_div, (int, float)) else eve_div}"
                )
            else:
                output.append("No even numbers.")
            output.append(CUT)
            if not len(odd_list) <= 0:
                output.append(
                    f"Odd's List: {odd_list}\nOdd number/s: {num_odd}\nOdd's Average: {odd_ave}\n(+) Odd: {odd_add}\n(-) Odd: {odd_min}\n(*) Odd: {odd_mul}\n(/) Odd: {round(odd_div, 3) if isinstance(odd_div, (int, float)) else odd_div}"
                )
            else:
                output.append("No odd numbers.")
            output.append(CUT)
        else:
            output.append(CUT)
            output.append("Integer: None")
        return "\n".join(output)

# Create main window
root = tk.Tk()
root.title("Text Analyzer Example")

# Entry label and widget
entry_label = tk.Label(root, text="Enter a string to analyze:", font=("Arial", 12))
entry_label.pack()

entry = tk.Entry(root, width=70)
entry.pack(pady=5)

# Text widget to display analysis
result_text = tk.Text(root, height=30, width=100, font=("Consolas", 10))
result_text.pack(pady=10)

def analyze_text():
    user_input = entry.get()
    analyzer = Text()
    analysis = analyzer.text_analyzer(user_input)
    letter_analysis = analyzer.count_letters([user_input])
    number_analysis = analyzer.count_numbers([user_input])
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, analysis + "\n\n" + letter_analysis + "\n\n" + number_analysis)

def clear_all():
    entry.delete(0, tk.END)
    result_text.delete(1.0, tk.END)

submit_button = tk.Button(root, text="Scan", width=20, command=analyze_text)
submit_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear", width=20, command=clear_all)
clear_button.pack(pady=5)

root.mainloop()
