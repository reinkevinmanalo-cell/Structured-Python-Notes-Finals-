# INTERMEDIATE 1: Largest and Smallest in a List

numbers = [12, 45, 7, 89, 23]

largest = numbers[0]
smallest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

    if number < smallest:
        smallest = number

print("Largest:", largest)
print("Smallest:", smallest)