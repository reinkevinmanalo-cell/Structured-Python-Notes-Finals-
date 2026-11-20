# INTERMEDIATE 1: sorted() vs sort()

numbers = [5, 2, 8, 1, 3]

# sorted() creates a new sorted list
new_list = sorted(numbers)

print("Original list:", numbers)
print("New sorted list:", new_list)

# sort() changes the original list
result = numbers.sort()

print("After using sort():", numbers)
print("Return value of sort():", result)