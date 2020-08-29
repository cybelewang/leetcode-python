"""
536 Construct Binary Tree from String

You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

Example:
Input: "4(2(3)(1))(6(5))"
Output: return the tree root node representing the following tree:

       4
     /   \
    2     6
   / \   / 
  3   1 5   
Note:
There will only be '(', ')', '-' and '0' ~ '9' in the input string.
An empty tree is represented by "" instead of "()".
"""
from TreeNode import *
class Solution:
    # stack solution, always push root to stack if seeing '(', and always connect current node to stack top with left-first appraoch
    # lessons learned: parse integer in a separate while loop instead of parsing digits one by one
    def str2tree(self, s: str) -> TreeNode:
        stack, cur = [], None
        i = 0
        while i < len(s):
            if s[i] == '-' or s[i].isdigit():
                # parse the integer and create a TreeNode with this integer
                j = i+1
                while j < len(s) and s[j].isdigit(): j += 1
                cur = TreeNode(int(s[i:j]))
                i = j
                continue
            elif s[i] == '(':
                stack.append(cur)
            elif s[i] == ')':
                # connct current node to parent with left-first approach
                if stack[-1].left is None:
                    stack[-1].left = cur
                else:
                    stack[-1].right = cur
                # update cur to its parent
                cur = stack.pop()
            i += 1
            
        return cur 

    # recursive solution
    def str2tree2(self, s: str) -> TreeNode:
        if not s: return None
        i = 0
        while i < len(s) and s[i] != '(':
            i += 1
        root = TreeNode(int(s[:i]))
        # s[i] == '('
        start, count = i+1, 0
        while i < len(s):
            if s[i] == '(':
                count += 1
            elif s[i] == ')':
                count -= 1
                if count == 0:
                    break
            i += 1

        root.left = self.str2tree(s[start:i])          
        root.right = self.str2tree(s[i+2:-1])
        return root