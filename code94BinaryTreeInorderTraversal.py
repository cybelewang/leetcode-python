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
    # OJ best non-recursive solution
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        ret = []
        stack = []
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            node = stack.pop()
            ret.append(node.val)
            root = node.right
        
        return ret

    def inorderTraversal2(self, root):
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
        #res = self._morris(root)

        return res
    
    def _morris(self, root):
        """
        Inorder traversal using Morris method, O(1) space, O(n) complexity
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []

        while root: # Loop until the current TreeNode is empty
            if root.left is None:   # case 1: the left child is empty, just append current node value and then proceed to the right child
                res.append(root.val)
                root = root.right
            else:   # case 2: if the left child is not empty, go and find the previous node that just before the current node "in order"
                pre = root.left
                while pre.right is not None and pre.right != root:  # This is to find the previous node just before the current node
                    pre = pre.right
                if pre.right is None:   # If this previous node's right child is not linked to current node, this means the left branch of current node has not been traversed
                    pre.right = root
                    root = root.left
                if pre.right == root:   # If this previous node's right child is linked to current node, this means the left branch of current node has been traversed, we just need to resume the left branch, print current node and then go to the right branch
                    pre.right = None
                    res.append(root.val)
                    root = root.right
        
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
            self._inorder(node.left, res)
            res.append(node.val)
            self._inorder(node.right, res)

null = None
test_case =  [1,2,3,4,5]
root = ListToTree(test_case)
obj = Solution()
res = obj.inorderTraversal(root)
print(res)