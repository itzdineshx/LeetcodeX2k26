## About the Problem

**Problem Name**   : Valid Anagram

**LeetCode ID**    : 242

**Difficulty**     : Easy

## Example
    Input: s = "rat", t = "car"
    Output: false

## Algorithm
1. Sort both strings.
2. Compare the sorted strings.
3. If they are equal, return True; otherwise, return False.

---

## Complexity

Time Complexity:
O(n log n) – sorting both strings

Space Complexity:
O(n) – extra space used by sorted strings