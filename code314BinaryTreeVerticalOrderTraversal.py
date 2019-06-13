"""
314 Binary Tree Vertical Order Traversal

Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its vertical order traversal as:
[
  [9],
  [3,15],
  [20],
  [7]
]
Given binary tree [3,9,20,4,5,2,7],
    _3_
   /   \
  9    20
 / \   / \
4   5 2   7
return its vertical order traversal as:
[
  [4],
  [9],
  [3,5,2],
  [20],
  [7]
]
"""
from TreeNode import *
from collections import defaultdict, deque
class Solution:
    # use a dict to save the elements in the same x coordinate
    # pitfall: the DFS cannot guarantee the correct order (top to down, left to right), so we must use BFS
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: list[list[int]]
        """
        res = []
        if not root:
            return res

        vertical = defaultdict(list)
        q = deque([(0, root)])
        while q:
            length = len(q)
            for _ in range(length):
                x, node = q.popleft()
                vertical[x].append(node.val)
                if node.left:
                    q.append((x-1, node.left))
                if node.right:
                    q.append((x+1, node.right))

        for x in sorted(vertical):
            res.append(vertical[x])
        
        return res

root = ListToTree([3,9,20,None, 5, 2, None, 4, None, None, 7, None, 6, 8])  # expect [[9, 4], [3, 5, 2, 6, 8], [20, 7]]
PrintTree(root)
print(Solution().verticalOrder(root))