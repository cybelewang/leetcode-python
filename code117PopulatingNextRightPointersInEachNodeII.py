"""
117 Populating Next Right Pointers in Each Node II

Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
"""
# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        parent = root
        dummy = TreeLinkNode(0) # dummy head in child level
        while parent:
            dummy.next = None   # Don't forget to break dummy.next with previous level's head
            p, c = parent, dummy    # parent and child levels' iterators
            while p:
                if p.left is not None:
                    c.next = p.left
                    c = c.next
                if p.right is not None:
                    c.next = p.right
                    c = c.next                
                p = p.next
            parent = dummy.next
                