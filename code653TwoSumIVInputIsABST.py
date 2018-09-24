"""
653 Two Sum IV - Input is a BST

Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
Example 2:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
"""
class Solution:
    # my solution, similar to two-pointer solution for a sorted array
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False

        def pushleft(root, stack):
            # push root and its most left branch nodes into stack
            while root:
                stack.append(root)
                root = root.left

        def pushright(root, stack):
            # push root and its most right branch nodes into stack
            while root:
                stack.append(root)
                root = root.right

        # stacks to hold the most left and most right tree nodes
        left, right = [], []
        pushleft(root, left)
        pushright(root, right)

        # initialize two pointers at the smallest node and largest node
        small, large = left.pop(), right.pop()
        pushleft(small.right, left)
        pushright(large.left, right)

        while small != large:
            sum_ = small.val + large.val
            if sum_ == k:
                return True
            elif sum_ < k:  # move small to larger node
                small = left.pop()
                pushleft(small.right, left)
            else:   # move large to smaller node
                large = right.pop()
                pushright(large.left, right)

        return False
            

    # my recursive solution, O(n) space
    def findTarget2(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        def helper(root, m, k):
            if not root:
                return False
            # left subtree
            left = helper(root.left, m, k)
            # current node
            if k - root.val in m:
                return True                        
            m.add(root.val)
            # right subtree
            right = helper(root.right, m, k)

            return left or right

        return helper(root, set(), k)