"""
958 Check Completeness of a Binary Tree

Given a binary tree, determine if it is a complete binary tree.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example 1:
Input: [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.

Example 2:
Input: [1,2,3,4,5,null,7]
Output: false

Explanation: The node with value 7 isn't as far left as possible.
Note:
The tree will have between 1 and 100 nodes.
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
    def isCompleteTree_2020(self, root: TreeNode) -> bool:
        q = deque([root])
        while q:
            node = q.popleft()
            if not node:
                break
            q.append(node.left)
            q.append(node.right)
        
        return not any(q)
    # https://leetcode.com/problems/check-completeness-of-a-binary-tree/solution/
    # O(N) space
    def isCompleteTree_OJ(self, root):
        nodes = [(root, 1)]
        i = 0
        while i < len(nodes):
            node, v = nodes[i]
            i += 1
            if node:
                nodes.append((node.left, 2*v))
                nodes.append((node.right, 2*v+1))

        return  nodes[-1][1] == len(nodes)
    # correct solution: handle null nodes in BFS, O(logN) space
    # 1. if a null node appears before a non-null node, always return false
    # 2. if null nodes appear at the tail part of a level-order queue, then the next level-order queue must contain only null nodes
    def isCompleteTree(self, root):
        q = deque([root])
        while q:
            n, has_null = len(q), False
            for _ in range(n):
                node = q.popleft()
                if node:
                    if has_null:    # case 1 above
                        return False
                    q.append(node.left)
                    q.append(node.right)
                else:
                    has_null = True
            if has_null:    # case 2 above
                break
        
        return not any(q)   # case 2 above
        
    # wrong for [1, null, 2], we cannot assume that the input binary tree has last level nodes in the most left
    def isCompleteTree_WRONG(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        while node:
            node = node.left
            levels += 1

        q = deque([root])
        for level in range(levels-1):
            for _ in range(n):
                node = q.popleft()
                if node:
                    count += 1
                    q.append(node.left)
                    q.append(node.right)
            
            if count != 2**level:
                return False

        # remove all "None" in right
        while q and not q[-1]:
            q.pop()
        
        return all(q)

        
    # Wrong solution because ignoring some internal levels may not have complete nodes
    def isCompleteTree_WRONG(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = deque([root])
        while q:
            n = len(q)
            has_null = False
            for _ in range(n):
                node = q.popleft()
                if node:
                    if has_null:
                        return False
                    q.append(node.left)
                    q.append(node.right)
                else:
                    has_null = True
        
        return True

null = None
#root = ListToTree([1,2,3,4,5,6,7,8,9,10,11,12,13,null,null,15])    #expect false
root = ListToTree([1, null, 2])
PrintTree(root)
print(Solution().isCompleteTree(root))
