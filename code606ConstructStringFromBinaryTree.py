"""
606 Construct String from Binary Tree

You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". 
And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

Example 1:
Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     

Output: "1(2(4))(3)"

Explanation: Originallay it needs to be "1(2(4)())(3()())", 
but you need to omit all the unnecessary empty parenthesis pairs. 
And it will be "1(2(4))(3)".
Example 2:
Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \  
      4 

Output: "1(2()(4))(3)"

Explanation: Almost the same as the first example, 
except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
"""
# follow-up: how to construct tree from string?
from TreeNode import *
class Solution:
    # my 2nd trial
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ''

        s = [self.tree2str(t.left), self.tree2str(t.right)]
        while s and s[-1] == '':
            s.pop()

        res = str(t.val)
        for val in s:
            res += '(' + val + ')'

        return res

    # my 1st trial, awkward
    def tree2str2(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ''

        def preorder(root):
            if not root:
                return '()'

            s = [str(root.val)]
            s.append(preorder(root.left))
            s.append(preorder(root.right))
            while s[-1] == '()':
                s.pop()

            res = s[0]
            for i in range(1, len(s)):
                if s[i] == '()':    # bug fixed: there may be '()' from left subtree, we should not add extra () out of it
                    res += s[i]
                else:
                    res += '(' + s[i] + ')'
            
            return res

        # main
        return preorder(t)

    def str2tree(self, s):
        """
        follow-up: convert string to tree
        """
        if not s:
            return None

        index = s.find('(')
        if index == -1:
            return TreeNode(int(s))
        
        # find the position of ')' which matches the first '('
        unbalanced, i = 0, 0
        for i, c in enumerate(s):
            if c == '(':
                unbalanced += 1
            elif c == ')':
                unbalanced -= 1
                if unbalanced == 0:
                    break

        # create treenode for root, and left subtree string, right subtree string
        root = TreeNode(int(s[:index]))
        left_s = s[index+1:i]
        right_s = s[i+2:-1]

        root.left = self.str2tree(left_s)
        root.right = self.str2tree(right_s)

        return root       


root = ListToTree([1,2,3,None,4])
#root = ListToTree([1,None,2,None, 3,None,4])
PrintTree(root)
s = Solution().tree2str(root)
print(s)
t = Solution().str2tree(s)
PrintTree(t)