## About the Problem

**Problem Name**   : Minimum ASCII Delete Sum for Two Strings

**LeetCode ID**    : 712

**Difficulty**     : Medium

## Example
    Input: s1 = "sea", s2 = "eat"
    Output: 231
    Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
    Deleting "t" from "eat" adds 116 to the sum.
    At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.

## Algorithm
1. Traverse through both strings character by character using Dynamic Programming.
2. Find the CS with the maximum ASCII sum.
3. Keep this subsequence in both strings.
4. Delete all other characters from both strings.
5. Calculate:
    min_sum = asciiSum(s1) + asciiSum(s2) − 2 × asciiSum(MCS)
6. Return min_sum.
---

## Working

![working](./Diagram.png)


---

## Complexity

Time Complexity:
O(m × n) - DP over both strings

Space Complexity:
O(m × n) – DP table storage

## Submission

![submission](./submit.png)