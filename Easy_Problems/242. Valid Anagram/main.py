"""
Problem Name   : Valid Anagram
LeetCode ID    : 242
Difficulty     : Easy

Problem Statement:
------------------
Find the Anagram of the given two strings

Example:
--------
Example 2:
Input: s = "rat", t = "car"
Output: false
"""

# Optimal Solution
"""
Algorithm:
----------
1. Sort both strings.
2. Compare the sorted strings.
3. If they are equal, return True; otherwise, return False.
"""

s = "anagram"
t = "nagaram"
if sorted(s) == sorted(t): 
    print(True)
else: 
    print(False)

"""
Time Complexity:
----------------
O(n log n) – sorting both strings

Space Complexity:
-----------------
O(n) – extra space used by sorted strings
"""
