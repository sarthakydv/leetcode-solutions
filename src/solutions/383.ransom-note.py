#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = [0] * 26
        for c in ransomNote:
            idx = ord(c) - ord("a")
            count[idx] -= 1
        for c in magazine:
            idx = ord(c) - ord("a")
            count[idx] += 1
        for extra in count:
            if extra < 0:
                return False
        return True


# @lc code=end
