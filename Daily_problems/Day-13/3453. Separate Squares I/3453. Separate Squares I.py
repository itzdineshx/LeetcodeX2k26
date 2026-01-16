"""
Problem Name   : Separate Squares I
LeetCode ID    : 3453
Difficulty     : Medium

Problem Statement:
------------------
Find the minimum y-coordinate value of a horizontal line such that the total area of the squares above the line equals the total area of the squares below the line.

Example:
--------
Input: squares = [[0,0,1],[2,2,1]]
Output: 1.00000
Any horizontal line between y = 1 and y = 2 will have 1 square unit above it and 1 square unit below it. The lowest option is 1.
"""

"""
Algorithm:
----------
1. Compute the total area of all squares.
2. Set low to the as lower bound of y and high as the upper bound of y.
3. While high - low is greater than y:
    - Take mid = (low + high) / 2 and calc areas
    - If area below ≥ total area -> high = mid
    - Else move low = mid
4. Return low.
"""

# Optimal Solutions

squares = [[0,0,1],[2,2,1]]

total_area = sum(l * l for _, _, l in squares) # Total area of all squares

# Binary search bounds
low = min(y for _, y, _ in squares) # lower bound
high = max(y + l for _, y, l in squares) # upper bound

def area_below(H):
    area = 0.0
    for _, y, l in squares:
        if H <= y:
            continue
        elif H >= y + l:
            area += l * l
        else:
            area += l * (H - y)
    return area

# Binary search for balance point
eps = 1e-6
while high - low > eps:
    mid = (low + high) / 2
    if area_below(mid) >= total_area / 2:
        high = mid
    else:
        low = mid

print(round(low))

"""
Time Complexity:
----------------
O(n log R) - no of squares x area

Space Complexity:
-----------------
Space : O(1) - Constant
"""
