from TreeNode import *
"""
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        #self._inorder(root, res)
        #build = [root]
        #self._nonrecursive1(build, res)
        res = self._nonrecursive2(root)

        return res
    
    # non-recursive solution 1, has a bug, consider the above example, when build = [2, 3], and pop 3, then 3 will be added again. Dead loop!
    def _nonrecursive1(self, build, res):
        """
        Non-recursive method to traverse tree in order
        :type build: list[TreeNode]
        :type res: list[int]
        :rtype: No
        """
        while len(build) > 0:
            node = build[-1]
            if node.left is not None:
                build.append(node.left)
            else:
                res.append(node.val)
                build.pop()
                if node.right is not None:
                    build.append(node.right)
    
    # Accepted non-recursive solution: First push all left TreeNodes to a stack, then pop them. If the poped node has a right node, then push the right node and its left nodes into the stack again.
    def _nonrecursive2(self, root):
        """
        :type root: TreeNode
        :rtype: No
        """
        build, res = [], []
        while root is not None:
            build.append(root)
            root = root.left

        while len(build) > 0:
            node = build.pop()
            res.append(node.val)
            if node.right is not None:
                node = node.right
                while node is not None:
                    build.append(node)
                    node = node.left
            
        return res

        
    # recursive solution
    def _inorder(self, node, res):
        if not node:
            return
        else:
            if node.left is not None:
                self._inorder(node.left, res)
            res.append(node.val)
            if node.right is not None:
                self._inorder(node.right, res)

null = None
test_case =  [1,null,2,3]
root = ListToTree(test_case)
obj = Solution()
res = obj.inorderTraversal(root)
print(res)