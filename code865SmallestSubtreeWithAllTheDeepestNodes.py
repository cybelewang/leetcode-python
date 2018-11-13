"""
865 Smallest Subtree with all the Deepest Nodes

Given a binary tree rooted at root, the depth of each node is the shortest distance to the root.

A node is deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is that node, plus the set of all descendants of that node.

Return the node with the largest depth such that it contains all the deepest nodes in its subtree.

 

Example 1:

Input: [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation:



We return the node with value 2, colored in yellow in the diagram.
The nodes colored in blue are the deepest nodes of the tree.
The input "[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]" is a serialization of the given tree.
The output "[2, 7, 4]" is a serialization of the subtree rooted at the node with value 2.
Both the input and output have TreeNode type.
 

Note:

The number of nodes in the tree will be between 1 and 500.
The values of each node are unique.
"""
# similar problems: 104 Maximum Depth of Binary Tree; 236 Lowest Common Ancestor of a Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from TreeNode import *
class Solution:
    # my own solution: 1. find all deepest nodes and put in a set. 2. Up-merge these nodes to a common ancestor
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # first get a set of deepest nodes
        self.deepest = set()
        self.maxDepth = -1
        def find(root, depth):
            """
            find the deepest nodes and put them in a set
            """
            if not root:
                return

            if depth >= self.maxDepth:
                if depth > self.maxDepth:
                    self.deepest.clear()
                    self.maxDepth = depth
                self.deepest.add(root)
            
            find(root.left, 1 + depth)
            find(root.right, 1 + depth)
        
        # now find the lowest common ancestor of these nodes
        def merge(root):
            """
            up-merge to find the lowest common ancestor of the deepest nodes
            """
            if not root or len(self.deepest) == 1:
                return

            # if left or right child in deepest nodes, replace them using the parent node
            bFound = False
            if root.left in self.deepest:
                self.deepest.remove(root.left)
                bFound = True
            if root.right in self.deepest:
                self.deepest.remove(root.right)
                bFound = True
            
            if bFound:
                self.deepest.add(root)
            
            merge(root.left)
            merge(root.right)

        # main
        find(root, 0)
        merge(root)

        return self.deepest.pop()

null = None
root = ListToTree([0,3,1,4,null,2,null,null,6,null,5])
PrintTree(root)
result = Solution().subtreeWithAllDeepest(root)
PrintTree(result)