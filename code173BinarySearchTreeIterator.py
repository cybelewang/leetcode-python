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

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

null = None
test_case =  [1,2,3,4,5]
root = ListToTree(test_case)
i, v = BSTIterator(root), []
while i.hasNext(): v.append(i.next())
print(v)