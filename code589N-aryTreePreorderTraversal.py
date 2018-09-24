"""
589 N-ary Tree Preorder Traversal

Given an n-ary tree, return the preorder traversal of its nodes' values.

 
For example, given a 3-ary tree:

            --------1-------------
         /          |             \
        3           2               4
      /   \
    5       6

Return its preorder traversal as: [1,3,5,6,2,4].
"""
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    # iterative solution
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        if not root:
            return res

        stack = [root]
        while len(stack) > 0:
            node = stack.pop()
            res.append(node.val)
            for child in reversed(node.children):
                stack.append(child)

        return res

    # recursive solution
    def preorder2(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def dfs(root, res):
            if not root:
                return

            res.append(root.val)
            for c in root.children:
                dfs(c, res)

        # main
        res = []
        dfs(root, res)

        return res
