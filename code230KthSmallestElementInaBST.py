"""
230 Kth Smallest Element in a BST

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

# For follow-up question, we should use a modified BST node with self.leftcount to save the count of left subtree
from TreeNode import *
class Solution:

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

    # 2nd round recursive solution on 2/8/2019, with help from http://www.cnblogs.com/grandyang/p/4620012.html
    def kthSmallest(self, root, k):
        def search(root, remain):
            """
            remain is a list with one element, which is the number of remaining nodes to count
            return the corresponding node's value
            """
            if not root:
                return -1

            val = search(root.left, remain) # search left, and remain[0] will decrease
            # check remain[0] after searching left
            if remain[0] == 0:
                return val
            # decrease remain[0] by counting root
            remain[0] -= 1

            # check remain[0] again after counting root
            if remain[0] == 0:
                return root.val

            # if remain[0] still > 0, search right    
            return search(root.right, remain)
        
        #main
        return search(root, [k])

null = None
test_case =  [4, 2, 6, 1, 3, 5, 7]
root = ListToTree(test_case)
obj = Solution()
res = obj.kthSmallest(root,3)
print(res)