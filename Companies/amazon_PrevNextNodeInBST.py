"""
Prev and Next node of a target node in Binary Search Tree

Find prev and next node of a target value's node in BST
https://www.geeksforgeeks.org/inorder-predecessor-successor-given-key-bst/
"""
import unittest
from TreeNode import *
class Solution:
    def search(self, root, x):
        """
        find a node with value x in BST
        :type root: TreeNode
        :type x: int
        :rtype: TreeNode
        """
        if not root:
            return None
        
        if root.val == x:
            return root
        elif root.val > x:
            return self.search(root.left, x)
        else:
            return self.search(root.right, x)

    def next(self, root, node):
        '''
        find the next node in BST
        '''
        if not node:
            return None

        if node.right:
            # get the minimum node in right subtree
            succ = node.right
            while succ.left:
                succ = succ.left
            return succ
        else:
            # search from root
            succ = None
            while root:
                if root.val > node.val:
                    succ = root
                    root = root.left
                elif root.val < node.val:
                    root = root.right
                else:
                    break
            
            return succ

    def prev(self, root, node):
        '''
        find the prev node in BST
        '''
        if not node:
            return None

        if node.left:
            # get the maximum node in left subtree
            pred = node.left
            while pred.right:
                pred = pred.right
            return pred
        else:
            # search from root
            pred = None
            while root:
                if root.val < node.val:
                    pred = root
                    root = root.right
                elif root.val > node.val:
                    root = root.left
                else:
                    break
            
            return pred

# unit test
root = ListToTree([6,2,7,1,4,None, 9, None, None, 3, 5, 8])
#PrintTree(root)
obj = Solution()

class Test(unittest.TestCase):
    def test_node1(self):
        node = obj.search(root, 1)
        self.assertIsNotNone(node)
        prev = obj.prev(root, node)
        next = obj.next(root, node)
        self.assertIsNone(prev)
        self.assertIsNotNone(next)
        self.assertEqual(next.val, 2)

    def test_node2(self):
        node = obj.search(root, 2)
        self.assertIsNotNone(node)
        prev = obj.prev(root, node)
        next = obj.next(root, node)
        self.assertIsNotNone(prev)
        self.assertEqual(prev.val, 1)
        self.assertIsNotNone(next)
        self.assertEqual(next.val, 3)

    def test_node5(self):
        node = obj.search(root, 5)
        self.assertIsNotNone(node)
        prev = obj.prev(root, node)
        next = obj.next(root, node)
        self.assertIsNotNone(prev)
        self.assertEqual(prev.val, 4)
        self.assertIsNotNone(next)
        self.assertEqual(next.val, 6)

    def test_node6(self):
        node = obj.search(root, 6)
        self.assertIsNotNone(node)
        prev = obj.prev(root, node)
        next = obj.next(root, node)
        self.assertIsNotNone(prev)
        self.assertEqual(prev.val, 5)
        self.assertIsNotNone(next)
        self.assertEqual(next.val, 7)

if __name__ == '__main__':
    unittest.main(exit=False)