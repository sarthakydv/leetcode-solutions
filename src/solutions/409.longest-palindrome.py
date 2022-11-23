#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        dic = {}
        hasExtra = False
        for c in s:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
        for v in dic.values():
            res += v // 2
        res *= 2
        if res < len(s):
            res += 1
        return res


# @lc code=end
