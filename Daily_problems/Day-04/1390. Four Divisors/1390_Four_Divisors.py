"""
Problem Name   : Four Divisors
LeetCode ID    : 1390
Difficulty     : Medium

Example:
--------
Input: nums = [21,4,7]
Output: 32
Explanation: 
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.
"""

# Optimal Solution
"""
Algorithm:
----------
1. Traverse through element
2. Find the divisor of them by square root of a number
3. if the divisor is 4 return the sum of divisor
4. otherwise return 0
"""
import math
nums = [21,4,7]
div_sum = 0
for i in nums:
    div_count = 0
    in_sum = 0

    for divisor in range(1, int(math.sqrt(i)) + 1):
        if i % divisor == 0:
            other = i // divisor

            if divisor == other:
                div_count += 1
                in_sum += divisor
            else:
                div_count += 2
                in_sum += divisor + other

            if div_count > 4:
                break

    if div_count == 4:
        div_sum += in_sum

print(div_sum)

"""
Time Complexity:
O(n) – traversal of arrays

Space Complexity:
O(n) – extra set is used
"""
