# Task 62 - R@nd0m P@ssw0rd generator

import random

password = []

length = int(input("Enter length: "))

for i in range(length):
    password.append(chr(random.randint(33, 126)))

print(''.join(password))
