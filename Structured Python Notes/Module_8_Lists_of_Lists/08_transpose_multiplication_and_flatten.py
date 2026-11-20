# HARD 2: Transpose, Multiplication Grid, and Flatten a Grid

grid = [
    [1, 2, 3],
    [4, 5, 6]
]

# Transpose
transposed = []

for column in range(len(grid[0])):
    new_row = []

    for row in range(len(grid)):
        new_row.append(grid[row][column])

    transposed.append(new_row)

print("Transposed grid:")
for row in transposed:
    print(row)

# Multiplication Grid
print("\nMultiplication Grid:")

for row in range(1, 4):
    for column in range(1, 4):
        print(row * column, end=" ")
    print()

# Flatten a Grid
flat_list = []

for row in grid:
    for value in row:
        flat_list.append(value)

print("\nFlattened list:", flat_list)