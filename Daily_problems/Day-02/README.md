### About the Problem
Problem Name   : N-Repeated Element in Size 2N Array

LeetCode ID    : 961

Difficulty     : Easy

Example :
    Input: nums = [1,2,3,3]
    Output: 3   


### Optimal Solution
Algorithm:
1. Type cast list() to set() and stores in var
2. Traverse the digits in array.
3. If digit in Already in seen? -> Return it
4. Otherwise # New element? -> Add it as seen

### Complexity

### Time Complexity:
----------------
O(n) – traversal of arrays

Space Complexity:
-----------------
O(n) – extra set is used