from TreeNode import *
"""
129 Sum Root to Leaf Numbers

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
"""
# similar problems: 112 Path Sum; 113 Path Sum II
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            return self._sum(0, root)

    def _sum(self, carry, root):
        """
        recursively calculate the sum of root-to-leaf numbers
        carry: the carried value from upper levels
        """
        if root.left is None and root.right is None:
            return carry*10 + root.val
        elif root.left is None:
            return self._sum(carry*10 + root.val, root.right)
        elif root.right is None:
            return self._sum(carry*10 + root.val, root.left)
        else:
            return self._sum(carry*10 + root.val, root.right) + self._sum(carry*10 + root.val, root.left)

    # 2nd round solution on 12/20/2018
    def sumNumbers2(self, root):
        self.res = 0
        def helper(preSum, node):
            if not node:
                return
            
            preSum = 10*preSum + node.val
            if not node.left and not node.right:
                self.res += preSum
            else:
                helper(preSum, node.left)
                helper(preSum, node.right)

        # main
        helper(0, root)
        return self.res            

obj = Solution()
null = None
test_case = [1, 2, 5, 6, 3, null, null, 4]
test_tree = ListToTree(test_case)
PrintTree(test_tree)
print(obj.sumNumbers2(test_tree))
