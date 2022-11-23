#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b, carry, res = list(a), list(b), 0, []

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            res.append(str(carry % 2))
            carry = carry // 2
        return "".join(res)[::-1]


# @lc code=end
