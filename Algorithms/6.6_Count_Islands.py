# Given a 2D grid, count the number of connected components (islands).


def count_islands(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def dfs(i, j):
        if 0 <= i:
            if i < rows:
                if 0 <= j:
                    if j < cols:
                        if grid[i][j] == 1:
                            grid[i][j] = 0
                            dfs(i - 1, j)
                            dfs(i + 1, j)
                            dfs(i, j - 1)
                            dfs(i, j + 1)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                dfs(i, j)
                count += 1

    return count


# Test cases
grid = [
    [1, 1, 0, 0, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
]

print(count_islands(grid))
