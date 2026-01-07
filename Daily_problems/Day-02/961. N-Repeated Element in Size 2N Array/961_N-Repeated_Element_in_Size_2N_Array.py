"""
Problem Name   : N-Repeated Element in Size 2N Array
LeetCode ID    : 961
Difficulty     : Easy

Example:
--------
Example 1:
    Input: nums = [1,2,3,3]
    Output: 3

Example 2:
    Input: nums = [5,5,1,3,4,2,5]
    Output: 5   
"""

# Optimal Solution
"""
Algorithm:
----------
1. Type cast list() to set() and stores in var
2. Traverse the digits in array.
3. If digit in Already in seen? -> Return it
4. Otherwise # New element? -> Add it as seen
"""

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # Typecastin list() -> set()
        seen = set() # Stores Visited Values
        for i in nums:
            if i in seen:
                return i # Already in seen? -> Return it
            seen.add(i) # New element? -> Add it
        return -1 # Nothing Found? -> Fallback

"""
Time Complexity:
----------------
O(n) – traversal of arrays

Space Complexity:
-----------------
O(n) – extra set is used
"""