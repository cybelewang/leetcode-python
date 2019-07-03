"""
663 Equal Tree Partition

Given a binary tree with n nodes, your task is to check if it's possible to partition the tree to two trees which have the equal sum of values after removing exactly one edge on the original tree.

Example 1:

Input:     
    5
   / \
  10 10
    /  \
   2   3

Output: True
Explanation: 
    5
   / 
  10
      
Sum: 15

   10
  /  \
 2    3

Sum: 15
 

Example 2:

Input:     
    1
   / \
  2  10
    /  \
   2   20

Output: False
Explanation: You can't split the tree into two trees with equal sum after removing exactly one edge on the tree.
"""
import unittest
from TreeNode import *
class Solution:
    def checkEqualTree(self, root):
        self.zero_count = 0
        def dfs(root, sums):
            if not root:
                return 0
            value = root.val + dfs(root.left, sums) + dfs(root.right, sums)
            if value == 0:
                self.zero_count += 1
            sums.add(value)
            return value

        s = set()
        total = dfs(root, s)
        if total == 0:
            return self.zero_count > 1

        return (total%2 == 0) and (total//2 in s)

obj = Solution()
class Test(unittest.TestCase):
    def test_empty(self):
        root = ListToTree([])
        self.assertFalse(obj.checkEqualTree(root))
    
    def test_single(self):
        root = ListToTree([0])
        self.assertFalse(obj.checkEqualTree(root))

    def test_small(self):
        root = ListToTree([0, 1])
        self.assertFalse(obj.checkEqualTree(root))
        root = ListToTree([0, -1, 1])
        self.assertFalse(obj.checkEqualTree(root))
        root = ListToTree([0, None, 0])
        self.assertTrue(obj.checkEqualTree(root))
        root = ListToTree([5, 10, 10, None, None, 2, 3])
        self.assertTrue(obj.checkEqualTree(root))
        root = ListToTree([1, 2, 10, None, None, 2, 20])
        self.assertFalse(obj.checkEqualTree(root))

if __name__ == '__main__':
    unittest.main(exit=False)