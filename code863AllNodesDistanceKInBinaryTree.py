"""
863 All Nodes Distance K in Binary Tree

We are given a binary tree (with root node root), a target node, and an integer value K.
Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.

Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.

Note:

The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
from TreeNode import *
class Solution:
    # my own solution
    # 1. search the target
    # 2. after finding the target, return the distance from the target, then search K distance child nodes from the target
    # 3. for each parent node (recursively iterate them), if target in left branch, search right branch with reduced distance, or vice versa.
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        res = []
        def find(root, dist, dir):
            """
            BFS looking for child nodes which has "dist" distance from root
            dir: 0 for left branch, 1 for right branch
            """
            if dist < 0:
                return

            if dist == 0:
                res.append(root.val)
                return

            q = deque([root.left if dir == 0 else root.right])
            for _ in range(dist-1):
                n = len(q)
                for _ in range(n):

                    node = q.popleft()
                    if not node:
                        continue
                    q.append(node.left)
                    q.append(node.right)
            
            res.extend(node.val for node in q if node)


        def dfs(root, target):
            """
            look for target node, if target is under the root, return the distance from target, else return -1
            """
            if root is None:
                return -1
            
            if root == target:
                # find the target node, append child nodes with K distance from target
                find(root, K, 0)
                if K > 0:   # if K == 0, we only need to append root node
                    find(root, K, 1)
                return 0

            left = dfs(root.left, target)
            if left != -1:  # left branch has target, so we search on right branch with remaining distance K-1-left
                find(root, K-1-left, 1)
                return 1 + left

            right = dfs(root.right, target)    
            if right != -1: # right branch has target, so we search on left branch with remaining distance K-1-right
                find(root, K-1-right, 0)
                return 1 + right

            return -1
            
        # main
        dfs(root, target)
        
        return res

null = None
root = ListToTree([1])
target = root
K = 3
print(Solution().distanceK(root, target, K))