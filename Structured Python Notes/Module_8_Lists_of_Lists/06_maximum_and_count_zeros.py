# INTERMEDIATE 3: Maximum in a Grid and Count Zeros

grid = [
    [0, 5, 8],
    [21, 0, 14],
    [7, 18, 0]
]

largest = grid[0][0]
zero_count = 0

for row in grid:
    for value in row:
        if value > largest:
            largest = value

        if value == 0:
            zero_count += 1

print("Maximum value:", largest)
print("Number of zeros:", zero_count)