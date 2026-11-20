# HARD 1: Count Even Numbers and Squares of a List

numbers = [2, 5, 8, 11, 14, 17]

even_count = 0
squares = []

for number in numbers:
    if number % 2 == 0:
        even_count += 1

    squares.append(number ** 2)

print("Original numbers:", numbers)
print("Even numbers:", even_count)
print("Squares:", squares)
