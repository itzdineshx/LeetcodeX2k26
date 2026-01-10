"""
Problem Name   : Minimum ASCII Delete Sum for Two Strings
LeetCode ID    : 712
Difficulty     : Medium

Problem Statement:
------------------
Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.

Example:
--------
Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.

"""

"""
Algorithm:
----------
1. Traverse through both strings character by character using Dynamic Programming.
2. Find the CS with the maximum ASCII sum.
3. Keep this subsequence in both strings.
4. Delete all other characters from both strings.
5. Calculate:
    min_sum = asciiSum(s1) + asciiSum(s2) − 2 × asciiSum(MCS)
6. Return min_sum.
"""

# Optimal Solution
s1 = "delete"
s2 = "leet"

m, n = len(s1), len(s2)
dp = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(1, m + 1): # i → s1
    for j in range(1, n + 1): # j → s2
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + ord(s1[i - 1])
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

ascii_sum1 = sum(ord(c) for c in s1)
ascii_sum2 = sum(ord(c) for c in s2)

sum = ascii_sum1 + ascii_sum2 - 2 * dp[m][n]
print(sum)


"""
Time Complexity:
----------------
O(m × n) - DP over both strings

Space Complexity:
-----------------
O(m × n) – DP table storage
"""
