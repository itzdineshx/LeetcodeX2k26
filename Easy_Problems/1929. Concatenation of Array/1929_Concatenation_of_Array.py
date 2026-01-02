"""
Problem Name   : Concatenation of Array
LeetCode ID    : 1929
Difficulty     : Easy

Algorithm:
----------
1. Repeat the input list twice using list multiplication.
2. Return the resulting concatenated list.
"""

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2

"""
Time Complexity:
----------------
O(n)

Space Complexity:
-----------------
O(n)
"""