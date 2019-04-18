"""
270 Convert BST to Greater Tree -   not submitted

Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
"""
from TreeNode import *
class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(node, pre = 0):
            if not node:
                return pre
            node.val += dfs(node.right, pre)
            return dfs(node.left, node.val)
        
        # main
        dfs(root)
        return root

lt = []
lt = [1]
lt = [1, None, 2]
lt = [1, 2, None, 3, None, 4, None]
lt = [5, 2, 13]
root = ListToTree(lt)
PrintTree(root)
PrintTree(Solution().convertBST(root))