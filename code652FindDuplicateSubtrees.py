"""
652 Find Duplicate Subtrees

Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1:

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
The following are two duplicate subtrees:

      2
     /
    4
and

    4
Therefore, you need to return above trees' root in the form of a list.
"""
from TreeNode import *
# similar problems: 572 Subtree of another Tree
from collections import defaultdict
class Solution:
    # already thought using preorder traversal, and ',' to separate values, but missed the following items:
    # (1) didn't think of '#' for None node
    # (2) didn't understand the problem requirement correctly. For example, if the example has 2 -> 4 -> 5 as one of the resulting subtree, should I return [2] or [2, 4, 5]? It seems the latter one is correct.
    # help from http://www.cnblogs.com/grandyang/p/7500082.html
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        m = defaultdict(int)
        res = []
        self.helper(root, m, res)

        return res

    def helper(self, root, m, res):
        """
        :type root: TreeNode
        :type m: defaultdict(int)
        :type res: list
        :rtype: str
        """
        if not root:
            return '#'
        
        s = str(root.val) + ',' + self.helper(root.left, m, res) + ',' + self.helper(root.right, m, res)
        if m[s] == 1:
            res.append(root)
        m[s] += 1

        return s

list_ = [4, 1, 1, 2, None, 2, None, 3, None, 3]
t = ListToTree(list_)
PrintTree(t)
print(Solution().findDuplicateSubtrees(t))