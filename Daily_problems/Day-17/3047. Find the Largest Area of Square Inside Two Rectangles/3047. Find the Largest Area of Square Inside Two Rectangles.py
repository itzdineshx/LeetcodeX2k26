"""
Problem Name   : Find the Largest Area of Square Inside Two Rectangles
LeetCode ID    : 3047
Difficulty     : Medium

Problem Statement:
------------------
find the maximum area of a square that can fit inside the intersecting region of at least two rectangles.

Example:
--------
Input: bottomLeft = [[1,1],[2,2],[3,1]], topRight = [[3,3],[4,4],[6,6]]

Output: 1

Explanation:

A square with side length 1 can fit inside either the intersecting region of rectangles 0 and 1 or the intersecting region of rectangles 1 and 2. Hence the maximum area is 1. It can be shown that a square with a greater side length can not fit inside any intersecting region of two rectangles.
"""

"""
Algorithm:
----------
1. For each rectangle pair(s), find overlapping area of them.
2. Then, take the smaller of width or height as the square side.
3. Keep the maximum side found.
4. Return side².
"""

# Optimal Solution
bl = [[1,1],[2,2],[3,1]]
tr = [[3,3],[4,4],[6,6]]
side = 0 # maximum side
n = len(bl)
# Traverse through the rectangle pairs
for i in range(n):
    for j in range(i + 1, n):
        min_x = max(bl[i][0], bl[j][0])
        max_x = min(tr[i][0], tr[j][0])
        min_y = max(bl[i][1], bl[j][1])
        max_y = min(tr[i][1], tr[j][1])

        # Largest Area
        if min_x < max_x and min_y < max_y:
            length = min(max_x - min_x, max_y - min_y)
            side = max(side, length)

print(side * side)

"""
Time Complexity:
----------------
O(n^2) - Nested Loop

Space Complexity:
-----------------
O(n) – Constant
 
"""
