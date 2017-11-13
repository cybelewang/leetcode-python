from TreeNode import *
"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        return self._recursive(root.left, root.right)

    # recursive solution
    def _recursive(self, p, q):
        if not p and not q:
            return True
        
        elif p is not None and q is None:
            return False

        elif p is None and q is not None:
            return False

        else:
            if p.val != q.val:
                return False
            else:
                return self._recursive(p.left, q.right) and self._recursive(p.right, q.left)
    
    # iterative solution, morris traversal method: left branch using the normal morris inorder method, right branch using the reversed morris inorder method
    def _iterative(self, root):
        p, q = root.left, root.right
            

obj = Solution()    
null = None
test_cases = [[1], [1,2,2,3,4,4,3], [1,2,2,null,3,null,3]]
for case in test_cases:
    test_tree = ListToTree(case)
    print(obj.isSymmetric(test_tree))