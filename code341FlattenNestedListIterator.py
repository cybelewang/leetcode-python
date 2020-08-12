"""
341 Flatten Nested List Iterator

Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

Example 2:
Given the list [1,[4,[6]]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
"""
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

# queue solution
from collections import deque
class NestedIterator(object):
    
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.queue = deque()
        for ni in nestedList:
            self.queue.append(ni)

    def next(self):
        """
        :rtype: int
        """
        ni = self.queue.popleft()
        return ni.getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        while len(self.queue) > 0:
            if self.queue[0].isInteger():
                return True
            else:
                nis = self.queue.popleft()
                self.queue.extendleft(nis.getList()[::-1])
        
        return False

# stack solution
class NestedIterator_Stack:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = nestedList[::-1]
    
    def next(self) -> int:
        return self.stack.pop().getInteger()
    
    def hasNext(self) -> bool:
        while self.stack:
            if self.stack[-1].isInteger():
                return True
            else:
                nl = self.stack.pop()
                self.stack.extend(reversed(nl.getList()))
        return False

# recursive solution
class NestedIterator2(object):

    def extract(self, nestedInteger):
        """
        extract integer from input NestedInteger
        :type nestedInteger: NestedInteger
        :rtype list of integer
        """
        if nestedInteger.isInteger():
            return [nestedInteger.getInteger()]
        
        res = []
        for item in nestedInteger.getList():
            res.extend(self.extract(item))

        return res            

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.data = []
        for item in nestedList:
            self.data.extend(self.extract(item))

        self.index = 0

    def next(self):
        """
        :rtype: int
        """
        return self.data[self.index]
        self.index += 1

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index < len(self.data)

# Generator solution
class NestedIterator_Generator:
    def __init__(self, nestedList: [NestedInteger]):
        def G(list):
            for nl in list:
                if nl.isInteger():
                    yield nl.getInteger()
                else:
                    yield from G(nl.getList())
        self.g = G(nestedList)
        self.cur = next(self.g, None)
    
    def next(self) -> int:
        val = self.cur
        self.cur = next(self.g, None)
        return val
    
    def hasNext(self) -> bool:
        return self.cur != None        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())