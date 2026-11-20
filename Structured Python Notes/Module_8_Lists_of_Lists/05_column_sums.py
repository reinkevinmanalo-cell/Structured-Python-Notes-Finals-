# INTERMEDIATE 2: Column Sums

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for column in range(len(grid[0])):
    total = 0

    for row in range(len(grid)):
        total += grid[row][column]

    print("Column", column + 1, "sum:", total)