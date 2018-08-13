"""
Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its elements lies in [L, R] (R >= L). 
You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.

Example 1:
Input: 
    1
   / \
  0   2

  L = 1
  R = 2

Output: 
    1
      \
       2
Example 2:
Input: 
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

Output: 
      3
     / 
   2   
  /
 1
 """
 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# similar problems: 653 Two Sum IV Input is a BST
from TreeNode import *
from collections import deque
class Solution:
    # simple solution from http://www.cnblogs.com/grandyang/p/7583185.html
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return None
        
        if root.val < L:
            root = self.trimBST(root.right, L, R)
        elif root.val > R:
            root = self.trimBST(root.left, L, R)
        else:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)

        return root

    # my own solution using deque
    # first put the outline tree nodes into a deque in order
    # pop all left tree nodes if they < L, then relink the next recursive result as left subtree
    # pop all right tree nodes if they > R, then relink the next recursive result as right subtree
    # finally check the position of original root in the deque and return new root
    # a pitfall is to consider only the left part of outline when checking < L, or only the right part of outline when checking > R
    def trimBST2(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return None

        # contour will hold all outline tree nodes in order. As in above last example, contour will be 0->3->4
        contour = deque()
        contour.append(root)

        left, right = root.left, root.right
        while left:
            contour.appendleft(left)
            left = left.left
        while right:
            contour.append(right)
            right = right.right

        # from left end remove all small tree nodes < L
        while contour and contour[0].val < L:
            contour.popleft()
        if contour: # deque could be empty
            contour[0].left = self.trimBST2(contour[0].left, L, R)   # relink left subtree

        # from right end remove all large tree nodes > R     
        while contour and contour[-1].val > R:
            contour.pop()
        if contour: # deque could be empty
            contour[-1].right = self.trimBST2(contour[-1].right, L, R)   # relink right subtree

        if not contour:
            return None # no tree nodes left
        elif contour[0].val > root.val:
            return contour[0]   # L and R are in right subtree of root
        elif contour[-1].val < root.val:
            return contour[-1]  # L and R are in left subtree of root
        else:
            return root # root is between L and R
        
root = ListToTree([3, 0, 4, None, 2, None, None, 1])
PrintTree(root)
PrintTree(Solution().trimBST(root, 1, 4))