# HARD 2: Running Totals

numbers = [5, 10, 15, 20, 25]

running_total = 0
totals = []

for number in numbers:
    running_total += number
    totals.append(running_total)

print("Original list:", numbers)
print("Running totals:", totals)