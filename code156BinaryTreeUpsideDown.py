"""
156 Binary Tree Upside Down

Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.
Example:
Input: [1,2,3,4,5]

    1
   / \
  2   3
 / \
4   5

Output: return the root of the binary tree [4,5,2,#,#,3,1]

   4
  / \
 5   2
    / \
   3   1  
Clarification:
Confused what [4,5,2,#,#,3,1] means? Read more below on how binary tree is serialized on OJ.
The serialization of a binary tree follows a level order traversal, where '#' signifies a path terminator where no node exists below.
Here's an example:
   1
  / \
 2   3
    /
   4
    \
     5
The above binary tree is serialized as [1,2,3,#,#,4,#,#,5].
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from TreeNode import *
class Solution:
    # stack solution
    def upsideDownBinaryTree(self, root):
        if not root: return None
        stack = []
        sibling_right = None
        while root:
            stack.append((root, sibling_right)) # push root and its right sibling into stack
            sibling_right = root.right
            root.right = None   # remember to disconnect right node, otherwise will cause bugs
            root = root.left

        root, left = stack.pop()
        root.left = left
        parent = root
        while stack:
            node, left = stack.pop()
            node.left = left
            parent.right = node
            parent = node

        return root

root = ListToTree([1,2,3,4,5])
PrintTree(root)
new_root = Solution().upsideDownBinaryTree(root)
PrintTree(new_root)