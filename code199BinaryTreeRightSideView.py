"""
199 Binary Tree Right Side View

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from TreeNode import *

from collections import deque
class Solution:
    # use queue and do BFS
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        queue, res = deque(), []
        queue.append(root)
        while len(queue) > 0:
            res.append(queue[-1].val)
            n = len(queue)            
            for i in range(n):
                node = queue.pop()
                if node.right is not None:
                    queue.appendleft(node.right)
                if node.left is not None:
                    queue.appendleft(node.left)
        
        return res

    def rightSideView_DFS(self, root):
        if not root: return []
        res = []
        def dfs(node, level):
            if level == len(res):
                res.append(node.val)
            if node.right:
                dfs(node.right, level+1)
            if node.left:
                dfs(node.left, level+1)
        
        dfs(root, 0)
        return res

    # has a bug. Consider a tree with only one right leaf and many left subnodes.
    def rightSideView2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        while root:
            res.append(root.val)
            if root.right:
                root = root.right
            else:
                root = root.left
        
        return res

obj = Solution()
test_case = [1, 2, None, 3, 4]
print(obj.rightSideView(ListToTree(test_case)))
print(obj.rightSideView_DFS(ListToTree(test_case)))