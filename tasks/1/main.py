# Task 1 - Factorial Finder

attempts = 0
factor = []
final = 1
count = 1

try:
    n = int(input("Enter a number: "))
except:
    print("Number is not valid.")


while not n == 0 :
    n -= 1
    attempts += 1
    factor.append(attempts)
                
for number in factor:
    final = number * final
            
print(final)
