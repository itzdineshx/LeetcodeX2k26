"""
Problem Name   :    
LeetCode ID    : 85
Difficulty     : Hard

Problem Statement:
------------------
Given a binary matrix filled with '0's and '1's, find the largest rectangle
containing only '1's and return its area.

Example:
--------
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
"""

# Optimal Solution
"""
Algorithm:
----------
1. make each row of -> base of a histogram.
2. Maintain an array height where each column stores the number of consecutive '1's above it.
3. For each row:
    - Update the height array.
    - Find the largest rectangle area in the histogram using a stack.
4. Keep updating the maximum area.
5. Return the maximum area.
"""

# Optimal Solution - Histogram Approach
matrix =[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
if not matrix: print(0) # Base Case

rows, cols = len(matrix), len(matrix[0])
height = [0] * (cols + 1) # flushing
max_area = 0

for row in matrix:
    for i in range(cols):
        # Update height based on current row(hist base)
        if row[i] == '1':
            height[i] += 1
        else:
            height[i] = 0
        
    # Largest Rectangle in Hist
    stack = [-1] # pointer
    for i in range(cols + 1):
        while stack[-1] != -1 and height[stack[-1]] >= height[i]:
            l = height[stack.pop()] # length
            b = i - stack[-1] - 1 # breadth
            max_area = max(max_area, l * b) # maximum area of rect -> max(l x b)
        stack.append(i)
print(max_area)

"""
Time Complexity:
----------------
O(N x M) – Traversal x pushed/popped from the stack 

Space Complexity:
-----------------
O(M) – No of Columns
"""