"""
662 Maximum Width of Binary Tree

Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. 
The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, 
where the null nodes between the end-nodes are also counted into the length calculation.

Example 1:
Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
Example 2:
Input: 

          1
         /  
        3    
       / \       
      5   3     

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
Example 3:
Input: 

          1
         / \
        3   2 
       /        
      5      

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).
Example 4:
Input: 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).


Note: Answer will in the range of 32-bit signed integer.
"""
from TreeNode import *
from collections import deque
class Solution:
    # my own solution using modified BFS (push tree node and its column index into queue)
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        res = 0
        q = deque()
        q.append((root, 1)) # second is the column index counting from 1

        while q:
            res = max(res, q[-1][1] - q[0][1] + 1)
            n = len(q)
            for _ in range(n):
                node, i = q.popleft()
                if node.left:
                    q.append((node.left, 2*i-1))
                if node.right:
                    q.append((node.right, 2*i))

        return res

root = ListToTree([1, 3, 2, 5, None, None, 9, 6, None, None, 7])
PrintTree(root)
print(Solution().widthOfBinaryTree(root))