"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. 
A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""
# similar problems: 100 Same Tree
from TreeNode import *
class Solution:
    # my own solution: use preorder (bug fixed. why inorder doesn't work) string to represent the tree, and check if t is a substring of s
    # bug fixed: consider s = 12 and t = 2, if we use ',' to separate each node, '2' will be considered as substring of '12', so we need to add ',' before the node
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def encode(root, values):
            """
            serialize tree to a string, in order
            """
            if not root:
                values.append(',#')
            else:
                values.append(','+str(root.val))
                encode(root.left, values)                
                encode(root.right, values)
        
        s_values, t_values = [], []
        encode(s, s_values)
        encode(t, t_values)
        #print(''.join(s_values))
        #print(''.join(t_values))

        return ''.join(s_values).count(''.join(t_values)) > 0

    # recursive solution, from https://www.cnblogs.com/grandyang/p/6828687.html
    def isSubtree2(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s is None and t is None:
            return True
        elif s is None or t is None:
            return False

        if s.val == t.val and self.isSubtree2(s.left, t.left) and self.isSubtree2(s.right, t.right):
            return True
        else:
            return self.isSubtree2(s.left, t) or self.isSubtree2(s.right, t)

s = ListToTree([3,4,5,1,2,None,None,0])
t = ListToTree([4,1, 2])
print(Solution().isSubtree(s, t))   # expected: False


s = ListToTree([3,4,5,1,None,2])
#PrintTree(s)
t = ListToTree([3,1, 2])
#PrintTree(t)
print(Solution().isSubtree2(s, t))  # expected: False