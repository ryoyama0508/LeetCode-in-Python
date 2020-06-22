from collections import deque


class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._queue = deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        p = self._queue
        p.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self._queue.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self._queue[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        print(self._queue)
        if len(self._queue) == 0:
            return True
        return False


# Your MyStack object will be instantiated and called as such:

obj = MyStack()
obj.push(2)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()
