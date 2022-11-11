# Task 24 - Hack-proof

username = "admin"
password = "password"

if input("Enter username: ") == username and input("Enter password: ") == password:
    with open('tasks/24/secret.txt', 'r') as f:
        for line in f.readlines():
            print(line)