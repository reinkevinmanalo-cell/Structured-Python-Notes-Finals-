# HARD 1: remove(), pop(), insert(), and extend()

numbers = [10, 20, 30, 40]

# Remove a specific value
numbers.remove(20)
print("After remove():", numbers)

# Remove the last element
removed_value = numbers.pop()
print("Popped value:", removed_value)
print("After pop():", numbers)

# Insert a value at a specific position
numbers.insert(1, 15)
print("After insert():", numbers)

# Add multiple elements
numbers.extend([50, 60])
print("After extend():", numbers)