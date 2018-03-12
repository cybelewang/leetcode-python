"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def _path(root, build, res):
            build.append(root.val)
            if root.left is None and root.right is None:
                res.append('->'.join(map(str, build)))
            if root.left is not None:                
                _path(root.left, build, res)
            if root.right is not None:
                _path(root.right, build, res)
            build.pop()

        res, build = [], []
        if root is not None:
            _path(root, build, res)

        return res