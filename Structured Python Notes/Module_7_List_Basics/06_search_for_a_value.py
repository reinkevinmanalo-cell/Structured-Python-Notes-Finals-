# INTERMEDIATE 3: Search for a Value

numbers = [10, 20, 30, 40, 50]

target = int(input("Enter a number to search: "))
found = False

for number in numbers:
    if number == target:
        found = True
        break

if found:
    print("Value found!")
else:
    print("Value not found.")