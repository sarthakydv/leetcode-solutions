#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # Using sorting
        # return sorted(s) == sorted(t)

        # Pythonic Way
        # count = [0] * 26
        # for chr1, chr2 in zip(s, t):
        #     count[ord(chr1) - ord("a")] += 1
        #     count[ord(chr2) - ord("a")] -= 1
        # return not any(count)

        # Pythonic way 2
        # return collections.Counter(s) == collections.Counter(t)

        # Pythonic way 3
        # Not required here but is a more general solution
        count = [0] * 27
        for chr1, chr2 in zip_longest(s, t, fillvalue="{"):
            count[ord(chr1) - ord("a")] += 1
            count[ord(chr2) - ord("a")] -= 1
        return not any(count)


# @lc code=end
