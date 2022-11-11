# Task 24 - Hack-proof

username = "admin"
password = "password"

inputUsername = input("Enter username: ")
inputPassword = input("Enter password: ")

if inputUsername == username and inputPassword == password:
    with open('tasks/24/secret.txt', 'r') as f:
        for line in f.readlines():
            print(line)