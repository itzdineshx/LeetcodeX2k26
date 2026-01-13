"""
Problem Name   : Minimum Time Visiting All Points
LeetCode ID    : 1266
Difficulty     : Easy

Problem Statement:
------------------
Return the minimum time in seconds to visit all the points in the order given by points.

Example:
--------
Input: points = [[1,1],[3,4],[-1,0]]
Output: 7
Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]   
Time from [1,1] to [3,4] = 3 seconds 
Time from [3,4] to [-1,0] = 4 seconds
Total time = 7 seconds
"""

"""
Algorithm:
----------
1. Start from the last point in the list(x1, y1).
2. Repeatedly move to the next point(x2, y2).
3. For each move from (x1, y1) to (x2, y2):
    - The minimum time required is: max(|x2 - x1|, |y2 - y1|)
4. Accumulate and Return the total time.
"""

# Optimal Solutions

points = [[1,1],[3,4],[-1,0]]

# Appraoch 1: modifying points
min_time = 0
x1, y1 = points.pop()
while points:
    x2, y2 = points.pop()
    min_time += max(abs(x2-x1),abs(y2-y1))
    x1, y1 = x2, y2
print(min_time) 

# Appraoch 2: without modifying points
n = len(points)
for i in range(1,n):
    x1, y1 = points[i-1]
    x2, y2 = points[i]
    min_time += max(abs(x2-x1),abs(y2-y1))
print(min_time) 

"""
Time Complexity:
----------------
O(n) - Traversal through points

Space Complexity:
-----------------
Space : O(1) - Constant
"""
