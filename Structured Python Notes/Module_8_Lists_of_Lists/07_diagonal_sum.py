# HARD 1: Diagonal Sum

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

total = 0

for index in range(len(grid)):
    total += grid[index][index]

print("Diagonal sum:", total)