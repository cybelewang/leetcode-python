"""
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:
Input: 
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.
Example 2:
Input: 
    2
   / \
  2   2

Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from TreeNode import *
from collections import deque
class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1

        def getLeastMax(root):
            """
            get the least max value for tree with root node
            return the root value if all values are the same
            """
            if not root.left:
                return root.val

            if root.left.val == root.val:
                # we need to go deeper to find more potential results
                left_max = getLeastMax(root.left)
            else:
                # subtree must be larger than root, we don't need to go deeper
                left_max = root.left.val

            if root.right.val == root.val:
                right_max = getLeastMax(root.right)
            else:
                right_max = root.right.val

            if left_max > root.val and right_max > root.val:
                # both left and right > root, take the min one
                return min(left_max, right_max)
            else:
                # either/both left and right == root, take the max one
                return max(left_max, right_max)

        # main
        res = getLeastMax(root)
        if res == root.val:
            return -1
        else:
            return res
        
    # WRONG SOLUTION!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # BFS
    def findSecondMinimumValue_WRONG(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1

        q = deque()
        q.append(root)
        res = 2**31
        while q:
            n = len(q)
            bFound = False
            for _ in range(n):
                node = q.popleft()
                if node.val > root.val:
                    res = min(res, node.val)
                    bFound = True
                if node.left:
                    q.append(node.left)
                    q.append(node.right)

            if bFound:
                return res

        return -1

t = ListToTree([1,1,3,1,1,3,4,3,1,1,1,3,8,4,8,3,3,1,6,2,1])
PrintTree(t)
print(Solution().findSecondMinimumValue(t))