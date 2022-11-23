#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Starting at index 0 instead of taking base case (bad approch)
        # maxVal = 0
        # sum = 0
        # for curr in nums:
        #     if sum + curr > 0:
        #         sum += curr
        #     else:
        #         sum = 0
        #     maxVal = max(sum, maxVal)
        # if maxVal == 0:
        #     maxVal = nums[0]
        #     for curr in nums:
        #         maxVal = max(maxVal, curr)
        # return maxVal

        # DP without memo
        # maxVal = nums[0]
        # sum = nums[0]
        # for i in range(1, len(nums)):
        #     if sum < 0:
        #         sum = nums[i]
        #     else:
        #         sum += nums[i]
        #     maxVal = max(sum, maxVal)
        # return maxVal

        # DP with memo
        sum = nums[0]
        maxVal = []
        maxVal.append(sum)
        for i in range(1, len(nums)):
            if sum < 0:
                sum = nums[i]
            else:
                sum += nums[i]
            maxVal.append(max(maxVal[-1], sum))
        # print(maxVal)
        return maxVal[-1]


# @lc code=end
