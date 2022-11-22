#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def binarySearch(self, nums, target, l, r) -> int:
        if l > r:
            return -1
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binarySearch(nums, target, mid + 1, r)
        elif nums[mid] > target:
            return self.binarySearch(nums, target, l, mid - 1)

    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # Iterative
        # while l <= r:
        #     mid = (l + r) // 2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] < target:
        #         l = mid + 1
        #     else:
        #         r = mid - 1
        # return -1

        # Recursive
        return self.binarySearch(nums, target, l, r)


# @lc code=end
