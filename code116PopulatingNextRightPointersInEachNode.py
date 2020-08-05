"""
116 Populating Next Right Pointers in Each Node

Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL

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

        parent = root   # head in the parent level
        dummy = TreeLinkNode(0) # dummy head in child level to help link children
        while parent.left is not None: # if the left child is None, stop
            p = parent  # iterator in parent level
            child = parent.left # head of the children
            c = dummy   # iterator in children level
            while p:
                c.next = p.left # link left child
                c = c.next
                c.next = p.right    # link right child
                c = c.next

                p = p.next  # advance parent level iterator
            
            parent = child  # assign new parent head
    
    # 8/4/2020
    # only need a sentinel node in child level because parent nodes have been connected
    # on each level, reset child to sentinel node
    def connect(self, root):
        parent = root
        sentinel = Node(0)
        while parent and parent.left:
            p = parent
            c = sentinel
            while p:
                c.next = p.left
                p.left.next = p.right
                c = p.right
                p = p.next
            parent = parent.left
        
        return root