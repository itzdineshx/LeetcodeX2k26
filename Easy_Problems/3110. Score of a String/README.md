## About the Problem

**Problem Name**   : Score of a String  

**LeetCode ID**    : 3110

**Difficulty**     : Easy

Problem Statement:
------------------
Given a string s, compute its score as the sum of the absolute differences
between the ASCII values of adjacent characters.

## Example
    Input: s = "hello"

    Output: 13

    Explanation:

    The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111. So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13.

## Algorithm
1. Initialize total score for tracking
2. Traverse through the array
3. Calculate the score = abs(ord(s[i]) - ord(s[i+1]))
4. return the total score of a string

---

## Complexity

Time Complexity:
O(n) – traversal of arrays

Space Complexity:
O(n) – extra set is used