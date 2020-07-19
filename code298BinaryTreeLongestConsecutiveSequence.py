"""
298 Binary Tree Longest Consecutive Sequence

Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

For example,

   1
	\
	 3
	/ \
   2   4
		\
		 5
Longest consecutive sequence path is 3-4-5, so return 3.

   2
	\
	 3
	/
   2
  /
 1
Longest consecutive sequence path is 2-3,not3-2-1, so return 2.
"""
class Solution:
    # DFS solution
    def longestConsecutive(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(root, pLen, pVal):
            if not root: return
            if root.val == pVal + 1:
                pLen += 1                
            else:
                pLen = 1
            self.res = max(self.res, pLen)
            dfs(root.left, pLen, root.val)
            dfs(root.right, pLen, root.val)
        
        dfs(root, 0, -2**31-1)
        return self.res