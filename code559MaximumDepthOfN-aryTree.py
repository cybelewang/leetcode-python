"""

Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

For example, given a 3-ary tree:

            --------1-------------
         /          |             \
        3           2               4
      /   \
    5       6
 
We should return its max depth, which is 3.

Note:

The depth of the tree is at most 1000.
The total number of nodes is at most 5000.
"""
from collections import deque
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    # BFS
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0

        q = deque()
        q.append(root)
        h = 0
        while q:
            length = len(q)
            h += 1
            for _ in range(length):
                node = q.popleft()
                for child in node.children:
                    q.append(child)
        
        return h


