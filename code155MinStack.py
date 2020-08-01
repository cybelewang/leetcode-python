from collections import deque
"""
155 Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""
# Solution 1: use minEle to save the current minimum, if the new element x < minEle, push (2*x - minEle) and update minEle to x. When poping top element, check if top < min, if so, minEle as (2*minEle - top). if top >= minEle, just pop x as is.
# Solution 2: use two stacks, the extra stack saves the corresponding min element. Time O(1), Space O(n)
class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minEle = 2**31 - 1

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stack:
            self.stack.append(x)
            self.minEle = x
        elif x >= self.minEle:
            self.stack.append(x)
        else: # x < self.minEle
            self.stack.append(2*x-self.minEle)
            self.minEle = x  

    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack) > 0:
            x = self.stack.pop()
            if x < self.minEle:
                self.minEle = 2*self.minEle - x # bug fixed

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
            x = self.stack[-1]
            return max(x, self.minEle)  # bug fixed

    def getMin(self):
        """
        :rtype: int
        """
        return self.minEle

class MinStack2:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = deque()
        self.minEle = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if not self.minEle or self.minEle[-1] > x:
            self.minEle.append(x)
        else:
            self.minEle.append(self.minEle[-1])

    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack) > 0:
            self.stack.pop()
            self.minEle.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.minEle) > 0:
            return self.minEle[-1]
        else:
            return None


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())   #--> Returns -3.
minStack.pop()
print(minStack.top())      #--> Returns 0.
print(minStack.getMin())   #--> Returns -2.

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()