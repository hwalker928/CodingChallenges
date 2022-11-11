# Task 15 - Pangrams

import string

letters = string.ascii_lowercase

userInput = input("Enter a sentence: ")

successful = True
print("\n")

for letter in letters:
    if letter not in userInput.lower():
        print(f"The letter {letter} is not present.")
        successful = False

print(successful)