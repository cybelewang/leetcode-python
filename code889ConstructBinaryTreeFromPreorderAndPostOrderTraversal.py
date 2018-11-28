"""
889 Construct Binary Tree from Preorder and Postorder Traversal

Return any binary tree that matches the given preorder and postorder traversals.

Values in the traversals pre and post are distinct positive integers.

Example 1:

Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]

Note:

1 <= pre.length == post.length <= 30
pre[] and post[] are both permutations of 1, 2, ..., pre.length.
It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.
"""
# similar problems: 105 Construct Binary Tree from Preorder and Inorder Traversal, 106 Construct Binary Tree from Inorder and Postorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from TreeNode import *
class Solution:
    # trick: pre[0] == post[-1]
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        index = {v:i for i, v in enumerate(post)}
        def helper(a, b, c, d):
            """
            a, b: start and end index of pre
            c, d: start and end index of post
            """
            if a > b or c > d:  # bug fixed: always check the index
                return None

            root = TreeNode(pre[a])
            if a < b:
                i = index[pre[a+1]]
                root.left = helper(a+1, i-c+a+1, c, i)
                root.right = helper(i-c+a+2, b, i+1, d-1)
            
            return root
        
        return helper(0, len(pre)-1, 0, len(post)-1)

#pre, post = [1,2,4,5,3,6,7], [4,5,2,6,7,3,1]
pre, post = [2, 1], [1, 2]
PrintTree(Solution().constructFromPrePost(pre, post))