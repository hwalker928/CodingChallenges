# Task 20 - Palindromes

def reverseString(string):
    return string[::-1]

word = input("Enter a word to check: ").lower()
reversedWord = reverseString(word)

if(word == reversedWord):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")