"""
872 Leaf-Similar Trees

Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 

Note:

Both of the given trees will have between 1 and 100 nodes.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from TreeNode import *
from itertools import zip_longest
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def F(root):
            """
            Generator to generate all leaves in the tree
            Similar to iterative in-order traversal
            """
            stack = []
            node = root
            while node:
                stack.append(node)
                node = node.left
            
            while stack:
                node = stack.pop()
                if node.left is None and node.right is None:
                    yield node
                else:
                    node = node.right
                    while node:
                        stack.append(node)
                        node = node.left

        def G(node):
            """
            Generator to generate all leaves in the tree
            Similar to recursive in-order traversal
            """
            if node:
                yield from G(node.left)
                if not node.left and not node.right:
                    yield node
                yield from G(node.right)            

        #print(list(F(root1)))    
        #print(list(F(root2)))
        #return all(a and b and a.val==b.val for a, b in zip_longest(F(root1), F(root2)))
        print(list(G(root1)))    
        print(list(G(root2)))
        return all(a and b and a.val==b.val for a, b in zip_longest(G(root1), G(root2)))


null = None
root1 = ListToTree([3,5,1,6,2,0,8,null,null,7,4])
PrintTree(root1)
root2 = ListToTree([3,5,1,6,2,0,8,null,null,7])
print(Solution().leafSimilar(root1, root2))