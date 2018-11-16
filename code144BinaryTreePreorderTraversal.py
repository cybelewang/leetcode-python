from TreeNode import *
"""
144 Binary Tree Preorder Traversal

Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# use similar stack method as inorder traversal, but print the left branch nodes before putting them into stack
class Solution(object):
    # Best OJ solution
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if not root:
            return result
        stack = [root]
        while stack:
            node = stack.pop()
            if node is not None:
                result.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return result
    # Accepted, 31% 
    def preorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        res, stack = [], []

        while root is not None:
            res.append(root.val)
            stack.append(root)
            root = root.left

        while len(stack) > 0:
            node = stack.pop()
            if node.right is not None:
                node = node.right
                while node is not None:
                    res.append(node.val)
                    stack.append(node)
                    node = node.left

        return res
    
    # recursive solution
    def _recursive(self, root, res):
        if root is None:
            return
        else:
            res.append(root.val)
            self._recursive(root.left, res)
            self._recursive(root.right, res)

    def _generator(self, root):
        """
        Generator solution
        """
        def G(node):
            if node:
                yield node.val
                yield from G(node.left)
                yield from G(node.right)
        
        return list(G(root))

null = None
test_case =  [1,null,2,3]
root = ListToTree(test_case)
PrintTree(root)

obj = Solution()
res = obj._generator(root)
print(res)