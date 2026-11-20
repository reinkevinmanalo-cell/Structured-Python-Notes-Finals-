# EASY 3: Count the Elements and Average

numbers = [10, 20, 30, 40, 50]

count = 0
total = 0

for number in numbers:
    count += 1
    total += number

average = total / count

print("Number of elements:", count)
print("Average:", average)