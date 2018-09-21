"""
225 Implement Stack using Queues

Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Notes:
You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
"""
from collections import deque
class MyStack:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.master = deque()
        self.helper = deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        while len(self.master) > 0:
            self.helper.append(self.master.popleft())        
        
        self.master.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        x = self.master.pop()
        while len(self.helper) > 1:
            self.master.append(self.helper.popleft())
        self.master, self.helper = self.helper, self.master

        return x

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.master[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.master) == 0
        


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
print(obj.pop())
obj.push(3)
print(obj.top())
print(obj.pop())
print(obj.empty())
print(obj.pop())
print(obj.empty())