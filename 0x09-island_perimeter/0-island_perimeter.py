#!/usr/bin/python3
""" 0. Island Perimeter """

def island_perimeter(grid):
    """
    function that returns the perimeter of the island described in grid
    """
    if not grid or not grid[0]:
        return 0

    perimeter = 0
    rows = len(grid)
    columns = len(grid[0])

    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == 1:
                perimeter += 4

                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
    return perimeter
