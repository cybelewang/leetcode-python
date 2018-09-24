"""
655 Print Binary Tree

Print a binary tree in an m*n 2D string array following these rules:

The row number m should be equal to the height of the given binary tree.
The column number n should always be an odd number.
The root node's value (in string format) should be put in the exactly middle of the first row it can be put. 
The column and the row where the root node belongs will separate the rest space into two parts (left-bottom part and right-bottom part). 
You should print the left subtree in the left-bottom part and print the right subtree in the right-bottom part. 
The left-bottom part and the right-bottom part should have the same size. 
Even if one subtree is none while the other is not, you don't need to print anything for the none subtree but still need to leave the space as large as that for the other subtree. 
However, if two subtrees are none, then you don't need to leave space for both of them.
Each unused space should contain an empty string "".
Print the subtrees following the same rules.
Example 1:
Input:
     1
    /
   2
Output:
[["", "1", ""],
 ["2", "", ""]]
Example 2:
Input:
     1
    / \
   2   3
    \
     4
Output:
[["", "", "", "1", "", "", ""],
 ["", "2", "", "", "", "3", ""],
 ["", "", "4", "", "", "", ""]]
Example 3:
Input:
      1
     / \
    2   5
   / 
  3 
 / 
4 
Output:

[["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
 ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
 ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
 ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
Note: The height of binary tree is in the range of [1, 10].
"""
from TreeNode import *
class Solution:
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        # ask corner case root == None
        def count(root, h):
            """
            count height and width with root as the root node of the tree
            width must be an odd number
            """
            if not root:
                return (h, 1)

            if not root.left and not root.right:
                return (h, 1)
            else:
                h1, w1 = count(root.left, h+1)
                h2, w2 = count(root.right, h+1)
                h = max(h1, h2)
                w = 2*max(w1, w2) + 1
                return (h, w)

        def put(root, row, left, right, res):
            """
            root: the root node
            row: the row index
            left: the left boarder of column for the subtree
            right: the right boarder of column for the subtree
            res: the final result
            """
            if root:
                column = res[row]
                mid = (left + right)//2
                column[mid] = str(root.val)
                put(root.left, row+1, left, mid-1, res)
                put(root.right, row+1, mid+1, right, res)
        
        # main
        h, w = count(root, 1)
        res = [['']*w for _ in range(h)]       
        put(root, 0, 0, w-1, res)

        return res

root = ListToTree([1,2])
print(Solution().printTree(root))