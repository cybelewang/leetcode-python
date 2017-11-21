from TreeNode import *
"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #    recursive solution, first look for the index of the first element of preorder in inorder, 
    #    then dynamically split the preorder and inorder list to left branch and right branch.
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1 : mid + 1], inorder[ : mid])  # left branch, note the index range
        root.right = self.buildTree(preorder[mid + 1: ], inorder[mid + 1 : ]) # right branch, note the index range

        return root
    
    # iterative solution from https://discuss.leetcode.com/topic/10244/my-o-n-19ms-solution-without-recusion-hope-help-you/2
    def buildTree2(self, preorder, inorder):
        stack=[]
        if len(preorder)==0:
            return None
        root=TreeNode(preorder[0])
        stack.append(root)
        index=0
        for i in range(1,len(preorder)+1):
            cur=stack[-1]
            if(stack[-1].val!=inorder[index]):
                cur.left=TreeNode(preorder[i])
                stack.append(cur.left)
            else:
                while(len(stack)!=0 and stack[-1].val==inorder[index]):
                    cur=stack[-1]
                    stack.pop()
                    index+=1
                if(index<len(inorder)):
                    cur.right=TreeNode(preorder[i])
                    stack.append(cur.right)
        return root

obj = Solution()
preorder = [5, 3, 1, 8, 9, 2, 10, 11, 4, 6, 12, 13, 7, 14, 15]
inorder = [8, 1, 9, 3, 10, 2, 11, 5, 12, 6, 13, 4, 14, 7, 15]
res = obj.buildTree2(preorder, inorder)
PrintTree(res)