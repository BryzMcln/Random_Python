import random
import re

# Mapping for text to numbers
numlist = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
    "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
    "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
    "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90
}

# Multipliers
multipliers = {"hundred": 100, "thousand": 1000, "million": 1000000}

# Reverse mapping for numbers to text
numlist_reverse = {v: k for k, v in numlist.items()}

def text_to_number(text):
    words = text.lower().split()
    total = 0
    current = 0

    for word in words:
        if word in numlist:
            current += numlist[word]
        elif word in multipliers:
            current *= multipliers[word]
            if word != "hundred":  # For "thousand" or "million", add to total
                total += current
                current = 0
        elif word == "and":
            continue
        else:
            raise ValueError(f"Unknown word: {word}")

    total += current
    return total

def number_to_text(number):
    if number == 0:
        return "zero"

    parts = []
    if number >= 1000:
        for multiplier, word in [("million", 1000000), ("thousand", 1000)]:
            if number >= multipliers[word]:
                parts.append(number_to_text(number // multipliers[word]))
                parts.append(word)
                number %= multipliers[word]

    if number >= 100:
        parts.append(numlist_reverse[number // 100])
        parts.append("hundred")
        number %= 100

    if number >= 20:
        parts.append(numlist_reverse[(number // 10) * 10])
        number %= 10

    if number > 0:
        parts.append(numlist_reverse[number])

    return " ".join(parts)

# Example usage
input_text = input("Enter a number in words: ")
result = text_to_number(input_text)
print(f"Input: {input_text}\nResult: {result:,}")

# Reverse example
input_number = int(input("Enter a number: "))
result_text = number_to_text(input_number)
print(f"Input: {input_number}\nResult: {result_text}")

def main():
    while True:
        try:
            input_text = input("Enter a number in words (or 'exit' to quit): ")
            if input_text.lower() == 'exit':
                break
            result = text_to_number(input_text)
            print(f"Input: {input_text}\nResult: {result:,}")
        except ValueError as e:
            print(e)

