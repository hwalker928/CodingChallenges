# Task 18 - Years In a Range

startYear = int(input("Enter starting year: "))
endYear = int(input("Enter ending year: "))

multiple = False
years = 0

for year in range(startYear, endYear):
    for char in str(year):
        count = str(year).count(char)
        if count > 1:
            multiple = True      
    if multiple:
        years += 1
        multiple = False

print(years)