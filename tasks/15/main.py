# Task 15 - Pangrams

import string
import re

userInput = input("Enter a sentence: ")

successful = True

for letter in string.ascii_lowercase:
    if letter not in re.sub(r'[^a-z]', '', f"{userInput.lower()}\t"):
        print(f"The letter {letter} is not present.")
        successful = False

print(successful)