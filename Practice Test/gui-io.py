import tkinter as tk
import sys


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


# Create main window
root = tk.Tk()
root.title("Text Analyzer Example")

# Entry label and widget
entry_label = tk.Label(root, text="Enter a string to analyze:", font=("Arial", 12))
entry_label.pack()

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# Text widget to display analysis
result_text = tk.Text(root, height=15, width=60, font=("Consolas", 10))
result_text.pack(pady=10)


def analyze_text():
    user_input = entry.get()
    analyzer = Text()
    analysis = analyzer.text_analyzer(user_input)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, analysis)


submit_button = tk.Button(root, text="Analyze", command=analyze_text)
submit_button.pack(pady=10)

root.mainloop()
