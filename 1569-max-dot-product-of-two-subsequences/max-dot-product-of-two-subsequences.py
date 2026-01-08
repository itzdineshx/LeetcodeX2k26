class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [[-float('inf')] * (m+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                curr_prod = nums1[i-1] * nums2[j-1]

                dp[i][j] = max(
                    curr_prod, # Take current pair
                    curr_prod + dp[i-1][j-1], # Take current pair + previous best pairs
                    dp[i-1][j], # Don't take current pair, keeps best prefix of nums1(i)
                    dp[i][j-1] # Don't take current pair, keeps best prefix of nums2(j)
                )
        return dp[n][m]