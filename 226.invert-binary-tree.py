#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Recursive
        # if root:
        #     root.left, root.right = self.invertTree(root.right), self.invertTree(
        #         root.left
        #     )
        #     return root

        # Stack - DFS
        # stk = [root]
        # while stk:
        #     currNode = stk.pop()
        #     if currNode:
        #         currNode.left, currNode.right = currNode.right, currNode.left
        #         stk += currNode.left, currNode.right
        # return root

        # Queue - BFS
        deq = collections.deque([root])
        while deq:
            currNode = deq.popleft()
            if currNode:
                currNode.left, currNode.right = currNode.right, currNode.left
                deq += currNode.left, currNode.right
        return root


# @lc code=end
