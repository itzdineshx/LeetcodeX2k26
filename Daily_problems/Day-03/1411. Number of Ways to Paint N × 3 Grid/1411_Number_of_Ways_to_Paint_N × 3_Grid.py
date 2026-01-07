"""
Problem Name   : Number of Ways to Paint N × 3 Grid
LeetCode ID    : 1411
Difficulty     : Hard
Example:
--------
Input:  n = 1
Output: 12

Input:  n = 2
Output: 54
"""

# Optimal DP Solution
"""
Algorithm:
----------
1. Initialize two variables:
    a = 6 → number of valid colorings of type abc
    b = 6 → number of valid colorings of type aba
2. Traverse each row from 2 to n:
    a = 3*a + 2*b
    b = 2*a + 2*b
3. Take modulo 10^9 + 7
4. Return (a + b) % (10^9 + 7)
"""

class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7 # to avoid overflow
        
        # Base case for n = 1
        a, b = 6, 6  # abc-pattern, aba-pattern
        
        # Compute for rows 2 to n
        for _ in range(1, n):
            a, b = (3*a + 2*b) % MOD, (2*a + 2*b) % MOD
        
        return (a + b) % MOD 

"""
Time Complexity:
----------------
O(n) – one pass through rows

Space Complexity:
-----------------
O(1) – constant space
"""
