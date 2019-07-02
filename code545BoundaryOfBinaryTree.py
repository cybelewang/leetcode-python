"""
545 Boundary of Binary Tree - not submitted
 
Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root. Boundary includes left boundary, leaves, and right boundary in order without duplicate nodes.
Left boundary is defined as the path from root to the left-most node. Right boundary is defined as the path from root to the right-most node. If the root doesn't have left subtree or right subtree, then the root itself is left boundary or right boundary. Note this definition only applies to the input binary tree, and not applies to any subtrees.
The left-most node is defined as a leaf node you could reach when you always firstly travel to the left subtree if exists. If not, travel to the right subtree. Repeat until you reach a leaf node.
The right-most node is also defined by the same way with left and right exchanged.

Example 1

Input:
  1
   \
    2
   / \
  3   4

Ouput:
[1, 3, 4, 2]

Explanation:
The root doesn't have left subtree, so the root itself is left boundary.
The leaves are node 3 and 4.
The right boundary are node 1,2,4. Note the anti-clockwise direction means you should output reversed right boundary.
So order them in anti-clockwise without duplicates and we have [1,3,4,2].
 

Example 2

Input:
    ____1_____
   /          \
  2            3
 / \          / 
4   5        6   
   / \      / \
  7   8    9  10  
       
Ouput:
[1,2,4,7,8,9,10,6,3]

Explanation:
The left boundary are node 1,2,4. (4 is the left-most node according to definition)
The leaves are node 4,7,8,9,10.
The right boundary are node 1,3,6,10. (10 is the right-most node).
So order them in anti-clockwise without duplicate nodes we have [1,2,4,7,8,9,10,6,3].
"""
import unittest
from TreeNode import *
class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: list[int]
        """
        if not root:
            return []
        
        left, right, leaves = [root], [], []

        # save left most nodes
        node = root.left
        while node:
            left.append(node)
            if node.left:
                node = node.left
            elif node.right:
                node = node.right
            else:
                node = None
        
        # save right most nodes
        node = root.right
        while node:
            right.append(node)
            if node.right:
                node = node.right
            elif node.left:
                node = node.left
            else:
                node = None

        # get leaves
        def dfs(node, leaves):
            if node:
                if not node.left and not node.right:
                    if (left and node == left[-1]) or (right and node == right[-1]):
                        pass
                    else:
                        leaves.append(node)
                if node.left:
                    dfs(node.left, leaves)
                if node.right:
                    dfs(node.right, leaves)
        
        dfs(root.left, leaves)
        dfs(root.right, leaves)

        # combine results
        return list(map(lambda node: node.val, left+leaves+right[::-1]))

# unit test
class Test(unittest.TestCase):

    def test_empty(self):
        root = ListToTree([])
        obj = Solution()
        self.assertEqual(obj.boundaryOfBinaryTree(root), [])
    
    def test_SingleNode(self):
        root = ListToTree([1])
        obj = Solution()
        self.assertEqual(obj.boundaryOfBinaryTree(root), [1])
    
    def test_small(self):
        obj = Solution()
        root = ListToTree([1, None, 2, 3, 4])
        self.assertEqual(obj.boundaryOfBinaryTree(root), [1, 3, 4, 2])
        root = ListToTree([1, 2, 3, 4, 5, 6, None, None, None, 7, 8, 9, 10])
        self.assertEqual(obj.boundaryOfBinaryTree(root), [1,2,4,7,8,9,10,6,3])

if __name__ == '__main__':
        unittest.main(exit = False)