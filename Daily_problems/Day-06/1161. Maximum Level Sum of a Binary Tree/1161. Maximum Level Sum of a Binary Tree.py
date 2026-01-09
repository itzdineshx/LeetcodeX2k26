"""
Problem Name   : Maximum Level Sum of a Binary Tree
LeetCode ID    : 1161
Difficulty     : Medium

Problem Statement:
------------------
Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

Example:
--------
Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
    Level 1 sum = 1.
    Level 2 sum = 7 + 0 = 7.
    Level 3 sum = 7 + -8 = -1.
    So we return the level with the maximum sum which is level 2.
"""

# Optimal Solution
"""
Algorithm:
----------
1. Initialize a queue with the root node (BFS).
2. Set current_level = 1, max_sum = -∞, answer = 1.
3. While the queue is not empty:
    - Compute the number of nodes at the current level.
    - Sum the values of all nodes at this level.
    - Add their children to the queue.
    - If the current level sum is greater than max_sum, update max_sum and answer.
    - Increment the level counter.
4. Return answer.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        curr_lvl = 1 # initialize the current level
        maxi = float('-inf')
        ans = 1

        queue = deque([root])

        while queue:
            curr_sum = 0
            lvl_size = len(queue)

            # Iterate all levels
            for _ in range(lvl_size):
                node = queue.popleft()
                curr_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if curr_sum > maxi:
                maxi = curr_sum
                ans = curr_lvl

            curr_lvl += 1
        
        return ans
        

"""
Time Complexity:
----------------
O(n) – queue operation

Space Complexity:
-----------------
O(n) – BFS queue stores the nodes
"""
