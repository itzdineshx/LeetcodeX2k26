"""
Problem Name   : Separate Squares II
LeetCode ID    : 3454
Difficulty     : Hard

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
edges = defaultdict(list); target = 0
for left, down, a in squares:
    edges[down].append((1, left, left+a))
    edges[down+a].append((0, left, left+a))
    
cur_edges = []; got = 0; cache = []
def update_cur_edges(y):
    for add, a, b in edges[y]:
        if add:
            insort_left(cur_edges, (a, b))
        else:
            cur_edges.remove((a, b))

    width = 0; left = 0
    for a, b in cur_edges:
        if a >= left:
            width += (b - a)
            left = b
        elif b > left:
            width += (b - left)
            left = b
        #else skip
    return width                        

for y,nexty in pairwise(sorted(edges)):
    width = update_cur_edges(y)
    got += (nexty - y) * width
    cache.append((nexty, width, got))

target = got/2
for entry in cache:
    if entry[2] >= target:
        return entry[0] - (entry[2] - target) / entry[1]

"""
Time Complexity:
----------------
O(n log R) - no of squares x area

Space Complexity:
-----------------
Space : O(1) - Constant
"""
