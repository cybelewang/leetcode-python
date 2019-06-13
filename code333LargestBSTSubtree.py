"""
333 Largest BST Subtree
 
Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.

Note:
A subtree must include all of its descendants.
Here's an example:

    10
    / \
   5  15
  / \   \ 
 1   8   7
The Largest BST Subtree in this case is the highlighted one. 
The return value is the subtree's size, which is 3.

Hint:

You can recursively use algorithm similar to 98 Validate Binary Search Tree at each node of the tree, which will result in O(nlogn) time complexity.
Follow up:
Can you figure out ways to solve it with O(n) time complexity?
"""
from TreeNode import *
class Solution:
    # Solution 4 from https://www.cnblogs.com/grandyang/p/5188938.html
    # DFS returns 3 information: min value in current BST, max value in current BST, max count of BST nodes
    def largestBSTSubtree(self, root):
        INT_MAX, INT_MIN = 2**31, -2**31-1
        def dfs(node):
            if not node:
                return (INT_MAX, INT_MIN, 0)
            left, right = dfs(node.left), dfs(node.right)
            if left[1] < node.val < right[0]:
                return (min(node.val, left[0]), max(node.val, right[1]), 1 + left[2] + right[2])    # we cannot return (left[0], right[1], 1 + left[2] + right[2]) because left[0] could be INT_MAX, right[1] could be INT_MIN
            else:
                return (INT_MIN, INT_MAX, max(left[2], right[2]))   # this return pattern will cause parent's left[1] < node.val < right[0] always fail

        # main
        return dfs(root)[2]

    # my own solution, O(N^2)
    # modified from 98 validate BST
    # use DFS to count BST nodes, return -1 if not a BST
    # if current subtree is not BST, modify lower and upper and check left child and right child separately
    def largestBSTSubtree2(self, root):
        INT_MAX, INT_MIN = 2**31, -2**31-1
        self.res = 0

        def countBST(node, lower, upper):
            """
            return -1 if this subtree is not a BST, otherwise return the count of nodes
            """
            if not node:
                return 0
            if lower < node.val < upper:
                left_cnt = countBST(node.left, lower, node.val)
                right_cnt = countBST(node.right, node.val, upper)
                if left_cnt != -1 and right_cnt != -1:
                    cnt = 1 + left_cnt + right_cnt
                    self.res = max(self.res, cnt)
                    return cnt
            
            countBST(node.left, INT_MIN, INT_MAX)
            countBST(node.right, INT_MIN, INT_MAX)

            return -1

        # main
        countBST(root, INT_MIN, INT_MAX)
        return self.res
            
root = ListToTree([10, 5, 15, 1, 8, None, 7])
print(Solution().largestBSTSubtree(root))