"""
285 Inorder Successor in BST

Given a binary search tree and a node in it, find the in-order successor of that node in the BST.
The successor of a node p is the node with the smallest key greater than p.val.
 
Example 1:
 
Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.
Example 2:
 
Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.
 
Note:
If the given node has no in-order successor in the tree, return null.
It's guaranteed that the values of the tree are unique.
"""
from TreeNode import *
class Solution:
    def inorderSuccessor(self, root, p):
        res = None
        while root:
            if root.val > p.val:
                res = root
                root = root.left
            else:
                root = root.right
        
        return res

    # BUGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG!
    def inorderSuccessor2(self, root, p):
        # find p 
        parent, cur = None, root
        while cur:
            if cur.val < p.val:
                parent = cur
                cur = cur.right
            elif cur.val > p.val:
                parent = cur
                cur = cur.left
            else:
                break
        
        if not cur: return None # p is not found
        
        # check if p's right child is non empty
        if cur.right:
            cur = cur.right
            while cur.left:
                cur = cur.left
            return cur
        else: # p's right child is empty, check parent node
            # bug here: parent may not be the successor, see test case
            if parent and parent.val > p.val:
                return parent
        
        return None

null = None
root = ListToTree([5,3,6,1,4,null,null,null,2])
PrintTree(root)
res = Solution().inorderSuccessor(root, TreeNode(4))
print(res)