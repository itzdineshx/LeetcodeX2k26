## About the Problem

**Problem Name**   : Minimum Operations to Make Array Sum Divisible by K

**LeetCode ID**    : 3512

**Difficulty**     : Easy

## Example
    Input: nums = [3,9,7], k = 5
    Output: 4
    Explanation:
    Perform 4 operations on nums[1] = 9. Now, nums = [3, 5, 7].
    The sum is 15, which is divisible by 5.

## Algorithm
1. Compute the sum of all elements in the array.
2. Find the remainder when the sum is divided by k.

---

## Complexity

Time Complexity:
O(n) – computing the sum of the array

Space Complexity:
O(1) – only constant extra variables are used
