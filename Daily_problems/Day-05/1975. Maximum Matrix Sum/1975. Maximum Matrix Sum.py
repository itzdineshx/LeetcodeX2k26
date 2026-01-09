"""
Problem Name   : Maximum Matrix Sum
LeetCode ID    : 1975
Difficulty     : Medium

Problem Statement:
------------------
maximize the summation of the matrix's elements. Return the maximum sum of the matrix

Example:
--------
Input: matrix = [[1,-1],[-1,1]]
Output: 4
Explanation: We can follow the following steps to reach sum equals 4:
- Multiply the 2 elements in the first row by -1.
- Multiply the 2 elements in the first column by -1.
"""

# Optimal Solution
"""
Algorithm:
----------
1. Initialize the trackers(neg count, total sum, min abs)
2. Track the smallest absolute value, and count the number of negative elements
3. Traverse through each element in the matrix
    - Add the absolute value of val to totalSum
    - If val is negative -> negativeCount ++
    - minAbsVal -> smaller of minAbsVal and abs(val)
4. After traversing the matrix check "-ve" counts:
    - odd: subtract 2 * minAbsVal from totalSum
    - even: Return totalSum
"""

matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
neg_count = 0
totalSum = 0
min_abs = float('inf')
for j in range(len(matrix)): # columns
    for i in range(len(matrix)): # rows
        if matrix[i][j] < 0: 
            neg_count += 1
        abs_val = abs(matrix[i][j])
        totalSum += abs_val
        min_abs = min(min_abs, abs_val)

if negative_count % 2 != 0:
total_sum -= 2 * min_abs_val
print(totalSum)

"""
Time Complexity:
----------------
Time complexity: O(n×m) – iterates through matrix

Space Complexity:
-----------------
Space complexity: O(1) – Size of Matrix
"""
