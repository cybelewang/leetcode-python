"""
Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from TreeNode import *
from collections import deque
class Solution:
    # DFS, stop searching when the first empty leaf node is seen, best O(lgN), worst O(N)
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        H, node = 0, root   # H is height of tree
        while node is not None:
            node = node.left
            H += 1

        lowest = [0]
        def find1stEmptyLeaf(node, h, H, lowest):
            # this function will recursively count the leaf nodes, and will early return True if the first empty leaf node is seen
            if h == H:
                if node is None:
                    return True
                else:
                    lowest[0] += 1
            else:
                if find1stEmptyLeaf(node.left, h+1, H, lowest) or find1stEmptyLeaf(node.right, h+1, H, lowest):
                    return True

            return False                                 
        
        if find1stEmptyLeaf(root, 1, H, lowest):
            return 2**(H-1) -1 + lowest[0]
        else:
            return 2**H -1

    # BFS, O(N)
    def countNodes2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        queue = deque()
        queue.append(root)
        res = 0
        while len(queue) > 0:
            node = queue.popleft()
            res += 1
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        
        return res

obj = Solution()
test_case = [1, 2, 3, 4, 5, 6, 7]
PrintTree(ListToTree(test_case))
print(obj.countNodes(ListToTree(test_case)))
print(obj.countNodes2(ListToTree(test_case)))