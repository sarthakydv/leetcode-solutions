# @before-stub-for-debug-begin
from python3problem914 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=914 lang=python3
#
# [914] X of a Kind in a Deck of Cards
#

# @lc code=start
import collections


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = dict(collections.Counter(deck))
        max = -1
        for val in count.values():
            if max == -1:
                max = val
                continue
            if max != val:
                return False
        return max > 1


# @lc code=end
