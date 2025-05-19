import tkinter as tk
import sys
import string

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

# Create main window
root = tk.Tk()
root.title("Text Analyzer Example")

# Entry label and widget
entry_label = tk.Label(root, text="Enter a string to analyze:", font=("Arial", 12))
entry_label.pack()

entry = tk.Entry(root, width=70)
entry.pack(pady=5)

# Text widget to display analysis
result_text = tk.Text(root, height=25, width=100, font=("Consolas", 10))
result_text.pack(pady=10)

def analyze_text():
    user_input = entry.get()
    analyzer = Text()
    analysis = analyzer.text_analyzer(user_input)
    letter_analysis = analyzer.count_letters([user_input])
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, analysis + "\n\n" + letter_analysis)

submit_button = tk.Button(root, text="Scan", width=20, command=analyze_text)
submit_button.pack(pady=10)

root.mainloop()
