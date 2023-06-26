# @before-stub-for-debug-begin
from python3problem169 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#


# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
            if count[n] > len(nums) // 2:
                return True
        return False


# @lc code=end
