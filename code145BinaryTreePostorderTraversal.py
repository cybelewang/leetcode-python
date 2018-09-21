from TreeNode import *
"""
145 Binary Tree Postorder Traversal

Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# use preorder traversal method but in root-right-left order, then reverse the result
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        res, stack = [], [root]
        while stack:
            node = stack.pop()
            if node is not None:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        
        res.reverse()
        return res

    # recursive solution
    def _recursive(self, root, res):
        if root is None:
            return
        else:            
            self._recursive(root.left, res)
            self._recursive(root.right, res)
            res.append(root.val)

null = None
test_case =  [1,null,2,3]
root = ListToTree(test_case)
PrintTree(root)

obj = Solution()
res = obj.postorderTraversal(root)
print(res)