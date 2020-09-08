"""
1214 Two Sum BSTs

Given two binary search trees, return True if and only if there is a node in the first tree and a node in the second tree whose values sum up to a given integer target.

Example 1:
Input: root1 = [2,1,4], root2 = [1,0,3], target = 5
Output: true
Explanation: 2 and 3 sum up to 5.

Example 2:
Input: root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
Output: false

Constraints:
Each tree has at most 5000 nodes.
-10^9 <= target, node.val <= 10^9
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from TreeNode import *
class Solution:
    # similar to finding two numbers in two sorted arrays which sums to a target 
    def twoSumBSTs(self, root1, root2, target):
        def inOrder(root):
            if root:
                yield from inOrder(root.left)
                yield root.val
                yield from inOrder(root.right)
        
        def reversedOrder(root):
            if root:
                yield from reversedOrder(root.right)
                yield root.val
                yield from reversedOrder(root.left)
                
        f, g = inOrder(root1), reversedOrder(root2)
        num1, num2 = next(f, None), next(g, None)
        while num1 is not None and num2 is not None:
            if num1 + num2 == target:
                return True
            elif num1 + num2 > target:
                num2 = next(g, None)
            else:
                num1 = next(f, None)
        
        return False

    # follow-up: what if the two nodes cannot be in the same level?
    # we can modify the generator to return a tuple of (node.val, level)
    # when two nodes' sum to the target, we also need to check if they are on the same level
    def twoSumBSTs2(self, root1, root2, target):
        def inOrder(root, level = 0):
            if root:
                yield from inOrder(root.left, level + 1)
                yield (root.val, level)
                yield from inOrder(root.right, level + 1)
        
        def reversedOrder(root, level = 0):
            if root:
                yield from reversedOrder(root.right, level + 1)
                yield (root.val, level)
                yield from reversedOrder(root.left, level + 1)
                
        f, g = inOrder(root1), reversedOrder(root2)
        node1, node2 = next(f, None), next(g, None)
        while node1 is not None and node2 is not None:
            _sum = node1[0] + node2[0]
            if _sum == target:
                if node1[1] != node2[1]:
                    return True
                else:
                    node1, node2 = next(f, None), next(g, None)
            elif _sum > target:
                node2 = next(g, None)
            elif _sum < target:
                node1 = next(f, None)
        
        return False

root1 = ListToTree([2, 1, 4])
root2 = ListToTree([3, 1, 4])
print(Solution().twoSumBSTs(root1, root2, 5)) # True
print(Solution().twoSumBSTs2(root1, root2, 5)) # False
root1 = ListToTree([2, 1, 3])
root2 = ListToTree([2, 1, 4])
print(Solution().twoSumBSTs(root1, root2, 5)) # True
print(Solution().twoSumBSTs2(root1, root2, 5)) # True