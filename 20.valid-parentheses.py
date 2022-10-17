# @before-stub-for-debug-begin
# @lc code=start

# @before-stub-for-debug-end

#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        pairs = {"(": ")", "{": "}", "[": "]"}
        stk = []
        for curr in s:
            if curr in pairs:
                stk.append(curr)
            elif len(stk) == 0 or pairs[stk.pop()] != curr:
                return False
        return len(stk) == 0


# @lc code=end
