"""
Problem Name   : Richest Customer Wealth
LeetCode ID    : 1672
Difficulty     : Easy
Example 1:
    Input: accounts = [[1,2,3],[3,2,1]]
    Output: 6
    Explanation:
    1st customer has wealth = 1 + 2 + 3 = 6
    2nd customer has wealth = 3 + 2 + 1 = 6
    Both customers are considered the richest with a wealth of 6 each, so return 6.
"""

# Optimal Solution
"""
Algorithm:
---------
1. Initialize the max wealth of cusomers
2. Traverse through Customer Accounts
3. Initialize current Wealth
4. Traverse through wealth of Accounts
5. Calculate max value and return it
"""

class Solution:
    def maximumWealth(self, accounts) -> int:
        # Soln 1 - Using In built Functions
        # return max(sum(customer) for customer in accounts)

        # Soln 2 - looping through the array
        max_wealth = 0 # intialzie amount
        for customer_acc in accounts:
            curr_wealth = 0 # currently no amount
            for val in customer_acc:
                curr_wealth += val
            max_wealth = max(max_wealth, curr_wealth)
        return max_wealth

        
"""
Time Complexity:
----------------
O(m × n) – traversal of all customer accounts

Space Complexity:
-----------------
O(1) – constant extra space

"""