#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        start = newInterval[0]
        end = newInterval[1]
        res = []
        i = 0
        while i < len(intervals):
            interval = intervals[i]
            interval_start = interval[0]
            interval_end = interval[1]
            if start > interval_start and end < interval_end:
                i += 1
                continue
            if start < interval_start:
                


# @lc code=end
