"""
Design your implementation of the circular double-ended queue (deque).

Your implementation should support following operations:

MyCircularDeque(k): Constructor, set the size of the deque to be k.
insertFront(): Adds an item at the front of Deque. Return true if the operation is successful.
insertLast(): Adds an item at the rear of Deque. Return true if the operation is successful.
deleteFront(): Deletes an item from the front of Deque. Return true if the operation is successful.
deleteLast(): Deletes an item from the rear of Deque. Return true if the operation is successful.
getFront(): Gets the front item from the Deque. If the deque is empty, return -1.
getRear(): Gets the last item from Deque. If the deque is empty, return -1.
isEmpty(): Checks whether Deque is empty or not. 
isFull(): Checks whether Deque is full or not.
 

Example:

MyCircularDeque circularDeque = new MycircularDeque(3); // set the size to be 3
circularDeque.insertLast(1);			// return true
circularDeque.insertLast(2);			// return true
circularDeque.insertFront(3);			// return true
circularDeque.insertFront(4);			// return false, the queue is full
circularDeque.getRear();  			// return 32
circularDeque.isFull();				// return true
circularDeque.deleteLast();			// return true
circularDeque.insertFront(4);			// return true
circularDeque.getFront();			// return 4
 

Note:

All values will be in the range of [0, 1000].
The number of operations will be in the range of [1, 1000].
Please do not use the built-in Deque library.
"""
# similar problems: 622 Design Circular Queue
# be cautious to case k = 0, k = 1
class MyCircularDeque:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.data = [0]*k
        self.front = 0
        self.length = 0

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if not self.data or self.isFull():
            return False
        
        N = len(self.data)
        self.front = (self.front - 1 + N)%N # bug fixed: need to update self.front first
        self.data[self.front] = value
        self.length += 1

        return True

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if not self.data or self.isFull():
            return False

        N = len(self.data)
        end = (self.front + self.length)%N
        self.data[end] = value
        self.length += 1

        return True        

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False

        N = len(self.data)
        self.front = (self.front + 1 + N)%N
        self.length -= 1

        return True        

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False

        self.length -= 1
        return True        

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.data[self.front]
        

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.data[(self.front + self.length - 1)%len(self.data)]        

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self.length == 0
        

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return self.length == len(self.data)
        
obj = MyCircularDeque(0)
assert(obj.isEmpty()==True)
assert(obj.isFull()==True)
assert(obj.insertFront(1)==False)
assert(obj.insertLast(1)==False)

obj = MyCircularDeque(1)
assert(obj.isEmpty()==True)
assert(obj.isFull()==False)
assert(obj.insertFront(1))
assert(obj.insertLast(2)==False)
assert(obj.isFull())
assert(obj.getRear()==1)
assert(obj.deleteLast())
assert(obj.isEmpty())

obj = MyCircularDeque(3)
assert(obj.insertLast(1)==True)
assert(obj.insertLast(2)==True)
assert(obj.insertFront(3)==True)
assert(obj.insertFront(4)==False)
assert(obj.getRear()==2)
assert(obj.isFull()==True)
assert(obj.deleteLast()==True)
assert(obj.insertFront(4)==True)
assert(obj.getFront()==4)

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()