"""
Problem Name   : Build Array from Permutation
LeetCode ID    : 1920
Difficulty     : Easy
Example :
    Input: nums = [0,2,1,5,3,4]
    Output: [0,1,2,4,5,3]
    Explanation: The array ans is built as follows: 
        ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
            = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
            = [0,1,2,4,5,3]
"""

# Optimal Solution
"""
Algorithm:
----------
1. Initialize an empty array ans
2. Traverse the input array nums using index `i`
3. For each index i, compute nums[nums[i]]
4. Append the computed value to `ans`
5. Return the array `ans`
"""

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # Optimal soln: Reduced Space Complexeity
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])  # ans[i] = nums[nums[i]] = nums[i] = val
        return ans
"""
Time Complexity:
----------------
O(n) – single traversal of the array

Space Complexity:
-----------------
O(n) – extra array `ans` is used to store the result
"""
