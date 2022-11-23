#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1

        for num, cnt in dic.items():
            if cnt > len(nums) // 2:
                return num


# @lc code=end
