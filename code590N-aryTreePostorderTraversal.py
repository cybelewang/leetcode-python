"""
590 N-ary Tree Postorder Traversal

Given an n-ary tree, return the postorder traversal of its nodes' values.

 
For example, given a 3-ary tree:

            --------1-------------
         /          |             \
        3           2               4
      /   \
    5       6
 
Return its postorder traversal as: [5,6,3,2,4,1].

 
Note: Recursive solution is trivial, could you do it iteratively?
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
    def postorder(self, root):
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
            for child in node.children:
                stack.append(child)
        
        return res[::-1]

    # recursive solution
    def postorder2(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def dfs(root, res):
            if not root:
                return
            
            res.append(root.val)
            for node in root.children[::-1]:
                dfs(node, res)
        res = []
        dfs(root, res)
        return res[::-1]
