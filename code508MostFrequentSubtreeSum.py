"""
508 Most Frequent Subtree Sum

Given the root of a tree, you are asked to find the most frequent subtree sum. 
The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). 
So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

Examples 1
Input:

  5
 /  \
2   -3
return [2, -3, 4], since all the values happen only once, return all of them in any order.
Examples 2
Input:

  5
 /  \
2   -5
return [2], since 2 happens twice, however -5 only occur once.
Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# similar problems: 501
from TreeNode import *
from collections import defaultdict
class Solution:
    # my own solution: recursively add all subtree's sum, and use a dict to maintain the count of the subtree sum
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.max = 0
        # post-order traversal
        def dfs(root, mem, res):
            if root is None:
                return 0
            
            root.val += dfs(root.left, mem, res)
            root.val += dfs(root.right, mem, res)

            value = root.val
            mem[value] += 1 # update count

            if mem[value] >= self.max:
                if mem[value] > self.max:
                    res.clear()
                res.append(value)
                self.max = mem[value]

            return value

        # main
        mem, res = defaultdict(int), []
        dfs(root, mem, res)

        return res


root = ListToTree([5, 2, -5])
PrintTree(root)
print(Solution().findFrequentTreeSum(root))