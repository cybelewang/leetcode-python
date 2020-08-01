"""
716 Max Stack

Design a max stack that supports push, pop, top, peekMax and popMax.

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.

Example 1:
MaxStack stack = new MaxStack();
stack.push(5); 
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5

Note:
-1e7 <= x <= 1e7
Number of operations won't exceed 10000.
The last four operations won't be called when stack is empty.
"""
# different from 155 min stack because this problem requires popMax()
# two stacks to store elements and max elements separately
class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s1, self.s2 = [], []

    def push(self, x: int) -> None:
        self.s1.append(x)
        if not self.s2:
            self.s2.append(x)
        else:
            self.s2.append(max(self.s2[-1], x))

    def pop(self) -> int:
        self.s2.pop()
        return self.s1.pop()        

    def top(self) -> int:
        return self.s1[-1]

    def peekMax(self) -> int:
        return self.s2[-1]
        
    def popMax(self) -> int:
        mx = self.s2[-1]
        s3 = []
        # keep popping s1 until seeing mx
        while self.s1[-1] != mx:
            s3.append(self.s1.pop())
            self.s2.pop()
        # pop mx from s1 and s2
        self.s1.pop()
        self.s2.pop()
        # push s3 elements back to s1 and s2 using push function
        while s3: self.push(s3.pop())
            
        return mx

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()