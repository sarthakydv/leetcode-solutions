#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # # Bottom up
    # def isBalanced(self, root: Optional[TreeNode]) -> bool:
    #     def getHeight(root: TreeNode):
    #         # Termination condition
    #         if root is None:
    #             return 0
    #         # Recursion (DFS) and return when first imbalance is found  and Mark imbalance
    #         leftHeight, rightHeight = getHeight(root.left), getHeight(root.right)
    #         if (
    #             leftHeight == -1
    #             or rightHeight == -1
    #             or abs(leftHeight - rightHeight) > 1
    #         ):
    #             return -1
    #         # Propagate current height
    #         return max(leftHeight, rightHeight) + 1

    #     return getHeight(root) > -1

    # Top Down
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(TreeNode: root) -> int:
            # TODO: Find reason for infinite recursion here
            if root is None:
                return 0
            print(root.val)
            return max(height(root.left), height(root.right)) + 1

        def isBalancedHelper(TreeNode: root) -> bool:
            if root is None:
                return True
            # print(root.val)
            leftHeight = height(root.left)
            rightHeight = height(root.right)

            return (
                abs(leftHeight - rightHeight) <= 1
                and isBalancedHelper(root.left)
                and isBalancedHelper(root.right)
            )

        return isBalancedHelper(root)


# @lc code=end
