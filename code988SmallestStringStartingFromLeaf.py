"""
988 Smallest String Starting From Leaf

Given the root of a binary tree, each node has a value from 0 to 25 representing the letters 'a' to 'z': a value of 0 represents 'a', a value of 1 represents 'b', and so on.

Find the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

(As a reminder, any shorter prefix of a string is lexicographically smaller: for example, "ab" is lexicographically smaller than "aba".  A leaf of a node is a node that has no children.)

Example 1:
Input: [0,1,2,3,4,3,4]
Output: "dba"

Example 2:
Input: [25,1,3,1,3,0,2]
Output: "adz"

Example 3:
Input: [2,2,1,null,1,0,null,0]
Output: "abc"

Note:

The number of nodes in the given tree will be between 1 and 8500.
Each node in the tree will have a value between 0 and 25.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from TreeNode import *
class Solution:
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        self.smallest = "{" # larger than any string "a-z"
        def dfs(node, build):
            if not node:
                return
            build.append(chr(node.val + ord('a')))
            if not node.left and not node.right:
                # this is a leaf node
                s = ''.join(build[::-1])
                if s < self.smallest:
                    self.smallest = s
            else:            
                dfs(node.left, build)
                dfs(node.right, build)
            build.pop()

        # main
        build = []
        dfs(root, build)

        return self.smallest

root = ListToTree([25,1,3,1,3,0,2])
print(Solution().smallestFromLeaf(root))