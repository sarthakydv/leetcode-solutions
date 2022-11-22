#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
from collections import deque


class MyQueue(object):
    def __init__(self):
        self.stk1, self.stk2 = [], []

    def push(self, x: int) -> None:
        self.stk1.append(x)

    def pop(self) -> int:
        self.peek()
        return self.stk2.pop()

    def peek(self) -> int:
        if not self.stk2:
            while self.stk1:
                self.stk2.append(self.stk1.pop())
        return self.stk2[-1]

    def empty(self) -> bool:
        return not (self.stk1 or self.stk2)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end
