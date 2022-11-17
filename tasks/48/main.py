# Task 48 - Reverse it

import string as strModule


def countVowels(string: str):
    vowelsCount = 0
    validVowels = ['a', 'e', 'i', 'o', 'u']

    for i in string:
        if i.lower() in validVowels:
            vowelsCount += 1

    return vowelsCount


def countConsonants(string: str):
    consonantsCount = 0
    letters = strModule.ascii_lowercase
    validVowels = ['a', 'e', 'i', 'o', 'u']

    for i in string:
        if i.lower() in letters and i.lower() not in validVowels:
            consonantsCount += 1

    return consonantsCount


def palindromeCheck(string: str):
    return string.lower()[::-1] == string.lower()


text = input("Enter text: ")
print(f"Reversed: {text[::-1]}")
print(f"Vowels: {countVowels(text)}")
print(f"Consonants: {countConsonants(text)}")
print(f"Palindrome: {palindromeCheck(text)}")