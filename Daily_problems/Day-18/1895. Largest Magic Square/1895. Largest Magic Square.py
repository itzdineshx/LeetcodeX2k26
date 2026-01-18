"""
Problem Name   : Largest Magic Square
LeetCode ID    : 1895
Difficulty     : Medium

Problem Statement:
------------------
Given an m x n integer grid, return the size of the largest magic square that can be found within this grid.

Example:
--------
Input: grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
Output: 3
Explanation: The largest magic square has a size of 3.
Every row sum, column sum, and diagonal sum of this magic square is equal to 12.
- Row sums: 5+1+6 = 5+4+3 = 2+7+3 = 12
- Column sums: 5+5+2 = 1+4+7 = 6+3+3 = 12
- Diagonal sums: 5+4+3 = 6+4+2 = 12
"""

"""
Algorithm:
----------
1. Precompute prefix sums for rows, columns, and both diagonals.
2. Try square sizes from largest to smallest.
3. For each position, check:
    - All row sums
    - All column sums
    - Both diagonal sums
4. If all sums are equal -> square size. ow -> 1
"""

# Optimal Solution

grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
m, n = len(grid), len(grid[0]) # matrix

# prefix sums of matrix(rows, columns, diagonals)
row = [[0]*(n+1) for _ in range(m)]
col = [[0]*n for _ in range(m+1)]
diag1 = [[0]*(n+1) for _ in range(m+1)]
diag2 = [[0]*(n+2) for _ in range(m+1)]

for i in range(m):
    for j in range(n):
        row[i][j+1] = row[i][j] + grid[i][j]
        col[i+1][j] = col[i][j] + grid[i][j]
        diag1[i+1][j+1] = diag1[i][j] + grid[i][j]
        diag2[i+1][j] = diag2[i][j+1] + grid[i][j]

def is_magic_sq(r, c, d):
    target = row[r][c+k] - row[r][c]

    # rows
    for i in range(r, r+k):
        if row[i][c+k] - row[i][c] != target:
            return False
    # columns
    for j in range(c, c+k):
        if col[r+k][j] - col[r][j] != target:
            return False
    # diagonals
    if diag1[r+k][c+k] - diag1[r][c] != target:
        return False
    if diag2[r+k][c] - diag2[r][c+k] != target:
        return False

    return True

max_d = min(m, n)
for k in range(max_d, 0, -1):
    for i in range(m - k + 1):
        for j in range(n - k + 1):
            if is_magic_sq(i, j, k):
                print(k)


"""
Time Complexity:
----------------
O(min(m,n) × m × n)

Space Complexity:
-----------------
O(m × n) - prefix sum tables
"""
