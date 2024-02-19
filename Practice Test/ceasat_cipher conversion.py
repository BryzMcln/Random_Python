def caesar_cipher(text, shift=13):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord("a") if char.islower() else ord("A")
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result


def replace_characters(text):
    replacements = {
        "i": "1",
        "I": "1",
        "s": "5",
        "S": "5",
        "e": "3",
        "E": "3",
        "o": "0",
        "O": "0",
    }
    for old_char, new_char in replacements.items():
        text = text.replace(old_char, new_char)
    return text


# Get input from the user
user_input = input("Enter a string: ")

# Apply Caesar Cipher
caesar_result = caesar_cipher(user_input)

# Apply character replacements
final_result = replace_characters(caesar_result)

# Display the results
# print("Original String:", user_input)
print("==========================================")
print("Caesar Cipher:", caesar_result)
print("Replacements:", final_result)
