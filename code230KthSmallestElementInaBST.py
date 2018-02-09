"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from TreeNode import *
class Solution:
    # Morris in order traversal, O(1) space
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
    # In order traversal, using a stack
    def kthSmallest2(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        while root:
            stack.append(root)
            root = root.left

        while len(stack) > 0:
            node = stack.pop()
            k -= 1

            if k == 0:
                return node.val

            node = node.right
            while node:
                stack.append(node)
                node = node.left

        return None
           
null = None
test_case =  [4, 2, 6, 1, 3, 5, 7]
root = ListToTree(test_case)
obj = Solution()
res = obj.kthSmallest2(root,3)
print(res)