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
import unittest
from TreeNode import *
class Solution:
    # 3rd visit on 7/21/2020
    # recursive solution
    def tree2str3(self, t):
        if not t: return ''
        left, right = self.tree2str(t.left), self.tree2str(t.right)
        if not left and not right:
            return "{}".format(t.val) # omit both left and right
        elif not right:
            return "{0}({1})".format(t.val, left) # omit right
        else:
            return "{0}({1})({2})".format(t.val, left, right) # no omit       
            
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

# 3rd round solution on 7/2/2019
class Solution2:
    def tree2str(self, root):
        if not root:
            return ''
        
        res = str(root.val)
        left, right = self.tree2str(root.left), self.tree2str(root.right)
        # form a truth table
        if right:
            res += "({})({})".format(left, right)
        elif left:
            res += "({})".format(left)

        return res

obj = Solution()
class Test(unittest.TestCase):

    def test_empty(self):
        root = ListToTree([])
        self.assertEqual(obj.tree2str3(root), '')

    def test_single(self):
        root = ListToTree([1])
        self.assertEqual(obj.tree2str3(root), '1')

    def test_small(self):
        root = ListToTree([1, 2])
        self.assertEqual(obj.tree2str3(root), "1(2)")
        root = ListToTree([1, 2, 3, None, 4])
        self.assertEqual(obj.tree2str3(root), "1(2()(4))(3)")      
        root = ListToTree([1,None,2,None, 3,None,4])
        self.assertEqual(obj.tree2str3(root), "1()(2()(3()(4)))")

if __name__ == '__main__':
    unittest.main(exit=False)