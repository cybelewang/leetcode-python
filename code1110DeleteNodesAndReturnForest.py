"""
1110 Delete Nodes And Return Forest

Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the result in any order.

Example 1:

Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]

Constraints:

The number of nodes in the given tree is at most 1000.
Each node has a distinct value between 1 and 1000.
to_delete.length <= 1000
to_delete contains distinct values between 1 and 1000.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        self.res = []
        # (1) link root to its children after removing nodes
        # (2) add orphan root to result list
        def helper(root, to_remove, isOrphan):
            # isOrphan is True when there is no parent linking to root
            if not root: return None
            if root.val in to_remove:
                helper(root.left, to_remove, True)
                helper(root.right, to_remove, True)
                return None
            else:
                root.left = helper(root.left, to_remove, False)
                root.right = helper(root.right, to_remove, False)
                if isOrphan:
                    self.res.append(root)
                return root
        
        # initially no parent node of root, so set isOrphan to True
        helper(root, set(to_delete), True)
        return self.res