### About the Problem
Problem Name   : Running Sum of 1D Array

LeetCode ID    : 1480

Difficulty     : Easy

Example :
    Input: nums = [1,2,3,4]
    Output: [1,3,6,10]
    Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].


### Optimal Solution
Algorithm:
1. Initialize the arr
2. Traverse through the list from 1 to n-1
2. add the arr[i] = arr[i] + arr[i-1]
3. Return arr

### Complexity

### Time Complexity:
----------------
O(n) – single traversal

### Space Complexity:
-----------------
O(1) – in-place modification, no extra space