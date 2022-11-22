#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # O(n) space solution
        # visited = set()
        # while head is not None and head not in visited:
        #     visited.add(head)
        #     head = head.next
        # return head is not None

        # O(1) space solution
        if head is None:
            return False
        slow = head
        fast = head.next
        while fast is not None and slow != fast:
            slow = slow.next
            fast = fast.next
            if fast is not None:
                fast = fast.next
        return slow == fast


# @lc code=end
