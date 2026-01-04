"""
Problem Name   : Score of a String
LeetCode ID    : 3110
Difficulty     : Easy

Example:
--------
Input: s = "hello"
Output: 13
Explanation:

The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111. So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13.

"""

# Optimal Solution
"""
Algorithm:
----------
1. Initialize total score for tracking
2. Traverse through the array
3. Calculate the score = abs(ord(s[i]) - ord(s[i+1]))
4. return the total score of a string
"""

s = "hello"
total_score = 0
for i in range(len(s) - 1):
    total_score += abs(ord(s[i]) - ord(s[i+1]))
print(total_score)

"""
Time Complexity:
O(n) – traversal of characters

Space Complexity:
O(1) – track score
"""