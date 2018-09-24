"""
623 Add One Row to Tree

Given the root of a binary tree, then value v and depth d, you need to add a row of nodes with value v at the given depth d. The root node is at depth 1.

The adding rule is: given a positive integer depth d, for each NOT null tree nodes N in depth d-1, create two tree nodes with value v as N's left subtree root and right subtree root. 
And N's original left subtree should be the left subtree of the new left subtree root, its original right subtree should be the right subtree of the new right subtree root. 
If depth d is 1 that means there is no depth d-1 at all, then create a tree node with value v as the new root of the whole original tree, and the original tree is the new root's left subtree.

Example 1:
Input: 
A binary tree as following:
       4
     /   \
    2     6
   / \   / 
  3   1 5   

v = 1

d = 2

Output: 
       4
      / \
     1   1
    /     \
   2       6
  / \     / 
 3   1   5   

Example 2:
Input: 
A binary tree as following:
      4
     /   
    2    
   / \   
  3   1    

v = 1

d = 3

Output: 
      4
     /   
    2
   / \    
  1   1
 /     \  
3       1
Note:
The given d is in range [1, maximum depth of the given tree + 1].
The given binary tree has at least one tree node.
"""
from TreeNode import *
from collections import deque
class Solution:
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node

        # BFS navigate to depth d-1
        q = deque()
        q.append(root)
        for _ in range(d-2):    # we already counted 1 level when appending root to q, so we only need to go (d-2) further levels
            len_ = len(q)
            for _ in range(len_):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        # now q has all parent tree nodes for depth d
        for p in q:
            # insert node and relink original left subtree
            node = TreeNode(v)
            node.left = p.left
            p.left = node
            # insert node and relink original right subtree
            node = TreeNode(v)
            node.right = p.right
            p.right = node
            
        return root

t = ListToTree([4, 2, 6, 3, 1, 5])
PrintTree(t)
PrintTree(Solution().addOneRow(t, 1, 1))