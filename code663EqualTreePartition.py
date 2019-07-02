"""
663 Equal Tree Partition

Given a binary tree with n nodes, your task is to check if it's possible to partition the tree to two trees which have the equal sum of values after removing exactly one edge on the original tree.

Example 1:

Input:     
    5
   / \
  10 10
    /  \
   2   3

Output: True
Explanation: 
    5
   / 
  10
      
Sum: 15

   10
  /  \
 2    3

Sum: 15
 

Example 2:

Input:     
    1
   / \
  2  10
    /  \
   2   20

Output: False
Explanation: You can't split the tree into two trees with equal sum after removing exactly one edge on the tree.
"""
class Solution:
    def checkEqualTree(self, root):
        def dfs(root, sums):
            if not root:
                return 0
            value = root.val + dfs(root.left, sums) + dfs(root.right, sums)
            sums.add(value)
            return value

        s = set()
        total = dfs(root, s)
        return (total%2 == 0) and (total//2 in s)