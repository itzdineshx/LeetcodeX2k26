"""
Problem Name   : Plus One
LeetCode ID    : 66
Difficulty     : Easy

Problem Statement:
------------------
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example:
--------
Input:  digits = [1, 2, 3]
Output: [1, 2, 4]

Input:  digits = [9, 9, 9]
Output: [1, 0, 0, 0]
"""

# Optimal Solution
"""
Algorithm:
----------
1. Initialize a carry variable with value 1.
2. Traverse the digits array from right to left.
3. For each digit:
   - Add the carry to the current digit.(Digit[i]+carry)
   - Update the digit to (sum % 10) to keep only the last digit.(10 % 10 = 0)
   - Update the carry to (sum // 10) to handle overflow.
4. After traversal, if a carry still exists, insert 1 at the beginning of the array.
5. Return the updated digits array.
"""

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:

        carry = 1 # carrier if 9 appears

        for i in range(len(digits)-1, -1, -1):
            s = digits[i] + carry # Last Digit + carry
            digits[i] = s % 10 # keeps only the last digit
            carry = s // 10 # carry if overflow occurs

        # carry exist? [1, digits]
        if carry:
            digits = [1] + digits

        return digits

"""
Time Complexity:
----------------
O(n) – traversal of arrays

Space Complexity:
-----------------
O(1) – Updating the current list itself
"""
