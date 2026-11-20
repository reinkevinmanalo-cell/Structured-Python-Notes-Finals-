# INTERMEDIATE 1: Sum of a Grid and Row Sums

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

total = 0

for row in grid:
    row_total = sum(row)
    total += row_total
    print("Row sum:", row_total)

print("Total grid sum:", total)