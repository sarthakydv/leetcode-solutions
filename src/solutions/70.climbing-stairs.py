#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 1]
        for i in range(n - 1):
            dp.append(dp[i] + dp[i + 1])
        return dp[-1]


# @lc code=end
