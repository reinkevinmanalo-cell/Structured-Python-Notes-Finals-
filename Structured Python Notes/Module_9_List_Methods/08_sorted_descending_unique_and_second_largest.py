# HARD 2: Sorted Descending, Count Unique Values, and Second Largest

numbers = [10, 25, 5, 40, 25, 30, 10]

# Sort in descending order
descending = sorted(numbers, reverse=True)

print("Descending order:", descending)

# Get unique values
unique_values = []

for number in numbers:
    if number not in unique_values:
        unique_values.append(number)

print("Unique values:", unique_values)
print("Number of unique values:", len(unique_values))

# Find the second largest unique number
unique_sorted = sorted(unique_values)

if len(unique_sorted) >= 2:
    print("Second largest:", unique_sorted[-2])
else:
    print("No second largest number.")