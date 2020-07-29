from TreeNode import *
"""
173 Binary Search Tree Iterator

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
"""
# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class BSTIterator(object):
    
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = deque()
        while root is not None:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0

    def next(self):
        """
        :rtype: int
        """
        cur = self.stack.pop()
        node = cur.right
        while node is not None:
            self.stack.append(node)
            node = node.left
        
        return cur.val

# 2nd visit on 7/16/2020       
class BSTIterator2:

    def __init__(self, root: TreeNode):
        def G(root):
            if root:
                yield from G(root.left)
                yield root
                yield from G(root.right)
        
        self.g = G(root)
        self.next = next(self.g)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        t = self.next.val
        self.next = next(self.g)
        return t

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.next != None

class BSTIterator_MORRIS:
    def __init__(self, root: TreeNode):
        # Morris inorder generator
        def G(root):
            while root:                
                if not root.left:
                    yield root
                    root = root.right
                else:
                    pre = root.left
                    while pre.right != None and pre.right != root:
                        pre = pre.right
                    if pre.right == None:
                        pre.right = root
                        root = root.left
                    if pre.right == root:
                        yield root
                        pre.right = None
                        root = root.right
        
        self.G = G(root)
        self.cur = next(self.G, None)
        

    def next(self) -> int:
        """
        @return the next smallest number
        """
        value = self.cur.val
        self.cur = next(self.G, None)
        return value
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.cur is not None

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

null = None
test_case =  [1,2,3,4,5]
root = ListToTree(test_case)
i, v = BSTIterator(root), []
while i.hasNext(): v.append(i.next())
print(v)