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

    # 3rd round recursive solution on 2/21/2019
    def kthSmallest3(self, root, k):
        def count(root, k):
            """
            k is remaining
            return tuple(number of nodes in this subtree, result node)
            """
            if not root:
                return (0, None)
            left_cnt, left_res = count(root.left, k)
            if left_res:
                return (k, left_res)
            if left_cnt + 1 == k:
                return (k, root)
            right_cnt, right_res = count(root.right, k - left_cnt - 1)
            if right_res:
                return (left_cnt + right_cnt + 1, right_res)
            else:
                return (left_cnt + right_cnt + 1, None)
        
        # main
        return count(root, k)[1].val
    
    # 4th round recursive solution on 2/21/2019
    def kthSmallest4(self, root, k):
        """
        k is remaining
        use a global variable self.res
        """
        self.res = None
        def count(root, k):
            if not root:
                return 0
            left_cnt = count(root.left, k)
            if left_cnt >= k:
                return k
            elif left_cnt + 1 == k:
                self.res = root
                return k
            else:
                right_cnt = count(root.right, k - left_cnt - 1)
                return left_cnt + right_cnt + 1

        # main
        count(root, k)
        return self.res.val;

null = None
test_case =  [4, 2, 6, 1, 3, 5, 7]
root = ListToTree(test_case)
PrintTree(root)
obj = Solution()
res = obj.kthSmallest4(root,3)
print(res)